from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import datetime
from owner.models import *
# from djangodoo.models import OdooModel class Partner(OdooModel):
#     _odoo_model = "res.partner"




# Create your models here.

class BannerImage(models.Model):
    image1 = models.ImageField(upload_to="images/",null=True)
    image2 = models.ImageField(upload_to="images/",null=True)
    image3 = models.ImageField(upload_to="images/",null=True)

class Currency(models.Model):
    currency_type = models.CharField(max_length=20)
    status = models.BooleanField(null=True)

    def __str__(self):
        return self.currency_type

class Categories(models.Model):
    category_name = models.CharField(max_length=140, unique=True)
    description=models.CharField(max_length=200,null=True)
    status=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    image=models.ImageField(upload_to="images/",null=True)

    def __str__(self):
        return self.category_name

class Beautician(models.Model):
    name=models.CharField(max_length=150)
    options=(
        ("male","male"),
        ("female","female"),

    )
    gender=models.CharField(max_length=150,choices=options)
    tenure=models.PositiveIntegerField(default=1)
    category=models.ManyToManyField(Categories,blank=True)
    options=(
        ("available","available"),
        ("unavailable","unavailable")
    )
    status=models.CharField(max_length=150,choices=options,default="available")

    def __str__(self):
        return self.name

class Timeslots(models.Model):
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    time=models.CharField(max_length=30, null=True)
    options=(
        ("available","available"),
        ("pending","pending"),
        ("booked","booked")
    )
    status=models.CharField(max_length=30,choices=options,default="available")
    date=models.DateField(null=True,blank=True)
    availability=models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.time

class Services(models.Model):
    name=models.CharField(max_length=200)
    exclusive = models.BooleanField(default=False)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images/",null=True)
    duration=models.DurationField(null=True, blank=True)
    cost=models.PositiveIntegerField()
    striked_off_cost = models.PositiveIntegerField(default=99)
    description=models.CharField(max_length=250,null=True,blank=True)
    detailed_description = models.TextField(null=True, blank=True)
    detailed_information = models.TextField(null=True, blank=True)
    beautician=models.ManyToManyField(Beautician)
    status=models.BooleanField(default=True)
    rating=models.FloatField(default=5)
    rating_count = models.PositiveIntegerField(default=1)
    timeslots=models.ManyToManyField(Timeslots)


    def __str__(self):
        return self.name

class AddOns(models.Model):
    name=models.CharField(max_length=200,null=True)
    cost=models.PositiveIntegerField(null=True)
    category=models.ManyToManyField(Categories)
    datetime=models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=500,null=True)
    image=models.ImageField(upload_to="images/",null=True)
    duration=models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.name

class Booking(models.Model):

    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(null=True,auto_now_add=True)
    timeslot = models.ForeignKey(Timeslots,on_delete=models.CASCADE,null=True)
    beautician=models.ForeignKey(Beautician,on_delete=models.CASCADE)
    cost=models.PositiveIntegerField()
    options = (
                ("booked","booked"),
                ("payment-pending","payment-pending"),
                ("booking-confirmed", "booking-confirmed"),
                ("cancelled","cancelled"),
                ("completed", "completed"),

            )
    status=models.CharField(max_length=200, choices=options, default="payment-pending")
# for chiropractic booking model
class ForBooking(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=10)
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    bookingdate = models.DateTimeField(null=True,auto_now_add=True)
    timeslot = models.ForeignKey(Timeslots,on_delete=models.CASCADE,null=True)
    docter=models.ForeignKey(Beautician,on_delete=models.CASCADE)

    def __str__(self):
        return self.name    
   
class GiftCards(models.Model):
    name = models.CharField(max_length=300)
    validity = models.PositiveIntegerField()
    desc = models.CharField(max_length=300)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    img = models.ImageField(upload_to="images/",null=True)
    options = (
        ("available", "available"),
        ("booked", "booked"),
        ("not available", "not available")
    )
    status = models.CharField(max_length=200, choices=options, default="available")

    def __str__(self):
        return self.name

class Notifications(models.Model):
    name = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    options = (
        ("unread", "unread"),
        ("viewed", "viewed"),
    )
    status = models.CharField(max_length=200, choices=options, default="unread")

    def __str__(self):
        return self.name

class IntroOffers(models.Model):
    name = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)
    off = models.PositiveIntegerField()
    image = models.ImageField(upload_to="images/",null=True)
    validity = models.PositiveIntegerField()
    options = (
        ("available", "available"),
        ("unavailable", "unavailble"),
        ("expired", "expired"),
        ("redeemed", "redeemed")
    )
    status = models.CharField(max_length=300, choices=options)

    def __str__(self):
        return self.name

class Blogs(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.name

class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name

class ProfileManage(models.Model):
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=300, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    email = models.EmailField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=250, null=True)
    contactno = models.PositiveIntegerField(null=True)
    language = models.CharField(max_length=300, null=True)
    country = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=250, null=True)
    zip_code = models.PositiveIntegerField(null=True)

class Memberships(models.Model):
    name = models.CharField(max_length=150)
    validity = models.PositiveIntegerField()
    price = models.PositiveIntegerField(null=True)
    desc = models.CharField(max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to="images/",null=True,blank=True)
    status=models.BooleanField(default=True,null=True)


    def __str__(self):
        return self.name

class Wishlist(models.Model):
    service= models.ForeignKey(Services,on_delete=models.CASCADE)
    options = (
        ("Wishlisted", "Wishlisted"),
        ("Removed", "Removed")
        
    )
    status = models.CharField(max_length=300, choices=options, default="Wishlisted")
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)


#MyMemberships
class MyMemberships(models.Model):

    membership = models.ForeignKey(Memberships, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
    options = (
                ("booked","booked"),
                ("expired", "expired")
            
            )
    status=models.CharField(max_length=200, choices=options, default="booked")

class Package(models.Model):
    name = models.CharField(max_length=150,unique=True)
    price = models.PositiveIntegerField(null=True)
    desc = models.CharField(max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to="images/",null=True)
    status=models.BooleanField(default=True,null=True)
    timeslot=models.ForeignKey(Timeslots,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
#Mypackages
class MyPackages(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    options = (
        ("booked", "booked"),
        ("expired", "expired")
    )
    status = models.CharField(max_length=200, choices=options, default="booked")
    
#MyGiftcards
class MyGiftcards(models.Model):
    giftcard = models.ForeignKey(GiftCards, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    options = (
        ("booked", "booked"),
        ("expired", "expired")
    )
    status = models.CharField(max_length=200, choices=options, default="booked")


class Transaction(models.Model):
    name=models.CharField(max_length=120)
    # options=(
    #     ("Paid", "Paid"),
    #     ("In Process", "In Process"),
    #     ("Pending", "Pending"),
    #     ("Failed", "Failed")
    # )
    status=models.CharField(max_length=300)
    amount=models.PositiveIntegerField()
    details=models.CharField(max_length=500)
    type=models.CharField(max_length=120)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ServiceReview(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    review = models.TextField()
    options = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),

    )

    service = models.ForeignKey(Services, on_delete=models.CASCADE)


class Cart(models.Model):
    giftcard = models.ForeignKey(GiftCards, on_delete=models.CASCADE, null=True)
    membership = models.ForeignKey(Memberships, on_delete=models.CASCADE, null=True)
    introoffer = models.ForeignKey(IntroOffers, on_delete=models.CASCADE, null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    status=models.CharField(max_length=20,default="in-cart")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class ServiceCart(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=True,blank=True)
    timeslot = models.ForeignKey(Timeslots, on_delete=models.CASCADE, null=True,blank=True)
    addons=models.ForeignKey(AddOns,on_delete=models.CASCADE,null=True,blank=True)
    beautician=models.ForeignKey(Beautician,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    cost=models.PositiveIntegerField(null=True,blank=True)
    time=models.CharField(max_length=50,null=True,blank=True)
    beautician=models.CharField(max_length=50,null=True,blank=True)
    options = (
        ("in-cart", "in-cart"),
        ("booked", "booked"),
        ("removed", "removed")
    )
    status=models.CharField(max_length=20,default="in-cart",choices=options)

class ServiceOrder(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(default=1)
    date_time = models.DateTimeField(null=True,auto_now_add=True)
    cost=models.PositiveIntegerField(null=True)
    options = (
                ("order-placed","order-placed"),
                ("order-confirmed", "order-confirmed"),
                ("in-progress","in-progress"),
                ("awaiting-user","awaiting-user"),
                ("cancelled","cancelled"),
                ("rejected","rejected"),
                ("delivered","delivered"),
                ("refunded", "refunded"),
                ("completed", "completed"),

            )
    status=models.CharField(max_length=200, choices=options, default="order-placed")
    cart=models.ManyToManyField(ServiceCart)
class MyIntroOffers(models.Model):
    intro = models.ForeignKey(IntroOffers, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    options = (
        ("booked", "booked"),
        ("expired", "expired")
    )
    status = models.CharField(max_length=200, choices=options, default="booked")


class RecentlyViewed(models.Model):
    name = models.CharField(max_length=300,unique=True, null=True)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Subscription(models.Model):
    name = models.CharField(max_length=20)
    email =  models.EmailField(max_length=50, null=True)

    def __str__(self):
        return self.name

#careerOpeninigsmodel

class CareerOpenings(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/")
    desc = models.TextField()

    def __str__(self):
        return self.name



class PersonalDetails(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    position = models.CharField( max_length=25)
    company_awareness = models.CharField(max_length=100,blank=True, null=True)
    ever_applied = models.CharField(max_length=10, blank=True, null=True)
    ever_applied_yes = models.CharField(max_length=100, blank=True, null=True)
    applied_date = models.DateField( blank=True, null=True)
    ever_employed = models.CharField( max_length=300, blank=True, null=True)
    ever_employed_yes = models.CharField(max_length=100, blank=True, null=True)
    employed_date = models.DateField( blank=True, null=True)
    age = models.CharField( max_length=300,blank=True, null=True)



class EductaionDetails(models.Model):
    school = models.CharField(max_length=50,blank=True, null=True)
    shool_compl_year = models.DateField(blank=True, null=True)
    college = models.CharField(max_length=50,blank=True, null=True)
    college_compl_year = models.DateField(blank=True, null=True)
    college_course = models.CharField(max_length=50,blank=True, null=True)
    university = models.CharField(max_length=50,blank=True, null=True)
    cosmet_school = models.CharField(max_length=50,blank=True, null=True)
    cosmet_compl_year = models.DateField(blank=True, null=True)
    cosmet_course = models.CharField(max_length=50,blank=True, null=True)
    massage_school = models.CharField(max_length=50,blank=True, null=True)
    massage_compl_year = models.DateField(blank=True, null=True)
    massage_course = models.CharField(max_length=50,blank=True, null=True)
    other_school = models.CharField(max_length=50,blank=True, null=True)
    other_compl_year = models.DateField(blank=True, null=True)
    other_course = models.CharField(max_length=50,blank=True, null=True)
    special_training = models.CharField(max_length=50,blank=True, null=True)


class ExperienceDetails(models.Model):
    exp_company = models.CharField(max_length=50,blank=True, null=True)
    exp_phone = models.CharField(max_length=25,blank=True, null=True)
    exp_address = models.CharField(max_length=100,blank=True, null=True)
    exp_from = models.DateField(blank=True, null=True)
    exp_to = models.DateField(blank=True, null=True)
    exp_supervisor = models.CharField(max_length=50, blank=True, null=True)
    exp_rate = models.CharField(max_length=30, blank=True, null=True)
    exp_job = models.CharField(max_length=30, blank=True, null=True)
    exp_reason_leave = models.CharField(max_length=50, blank=True, null=True)
    contact_personal_employer = models.CharField( max_length=10, blank=True, null=True)
    currently_employed = models.CharField( max_length=10, blank=True, null=True)


class ExtraDetails(models.Model):
    law_status = models.CharField( max_length=10,blank=True, null=True)
    drive_license = models.CharField( max_length=10,blank=True, null=True)
    drive_license_exp = models.DateField(blank=True, null=True)
    transportation = models.CharField(max_length=10,blank=True, null=True)
    current_salary = models.CharField(max_length=20,blank=True, null=True)
    need_salary = models.CharField(max_length=10,blank=True, null=True)
    want_salary = models.CharField(max_length=10,blank=True, null=True)
    cuurent_work_hours = models.CharField(max_length=20,blank=True, null=True)
    likely_work_hours = models.CharField(max_length=20,blank=True, null=True)
    client_count = models.CharField(max_length=20,blank=True, null=True)
    strengths = models.CharField(max_length=100,blank=True, null=True)
    areas_improve = models.CharField(max_length=50,blank=True, null=True)
    contr_to_comp = models.CharField(max_length=50,blank=True, null=True)
    contr_subs = models.CharField( max_length=50,blank=True, null=True)
    convicted = models.CharField( max_length=10,blank=True, null=True)
    mon_hrs = models.CharField(max_length=10,blank=True, null=True)
    tue_hrs = models.CharField(max_length=10,blank=True, null=True)
    wed_hrs = models.CharField(max_length=10,blank=True, null=True)
    thu_hrs = models.CharField(max_length=10,blank=True, null=True)
    fri_hrs = models.CharField(max_length=10,blank=True, null=True)
    sat_hrs = models.CharField(max_length=10,blank=True, null=True)
    sun_hrs = models.CharField(max_length=10,blank=True, null=True)


class IndustryExperience(models.Model):
    ind_exp = models.CharField(max_length=30,blank=True, null=True)
    ind_bg = models.CharField(max_length=30,blank=True, null=True)
    ind_offer = models.CharField(max_length=30,blank=True, null=True)
    ind_expect = models.CharField(max_length=30,blank=True, null=True)
    ind_goals = models.CharField(max_length=30,blank=True, null=True)
    ind_goal_plan = models.CharField(max_length=30,blank=True, null=True)
    ind_where_see = models.CharField(max_length=50,blank=True, null=True)
    ind_exp_years = models.CharField(max_length=30,blank=True, null=True)
    ind_pr_job_exp = models.CharField(max_length=50,blank=True, null=True)
    ind_pr_job_leave = models.CharField(max_length=50,blank=True, null=True)
    ind_crazy = models.CharField(max_length=50,blank=True, null=True)
    ind_how_spa = models.CharField(max_length=50,blank=True, null=True)
    ind_how_no_spa = models.CharField(max_length=50,blank=True, null=True)
    reference = models.CharField(max_length=50,blank=True, null=True)
    resume = models.FileField(upload_to="uploads/", max_length=50)










    











    
     
















      





    






    






