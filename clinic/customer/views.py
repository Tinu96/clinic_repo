from django.shortcuts import render, redirect
from customer.models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, TemplateView, FormView, DetailView, ListView, UpdateView, RedirectView, View
from customer.forms import *
from customer import forms
from django.contrib import messages
import json
from datetime import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

# from customer.decorators import login_required

# Create your views here.
# path("register", views.RegistrationView.as_view(), name="registration")
def aboutus(request):
    return render(request, "about.html")
def team(request):
    return render(request, "team.html")
def bookingg(request):
    services=Services.objects.all()
    category=Categories.objects.all()
    beauticians=Beautician.objects.all()
    timeslot=Timeslots.objects.all()
    context = {"services":services,"category":category,"beauticians":beauticians,"timeslot":timeslot}
    
    if request.method=="POST":
        nam=request.POST.get('na')
        print(nam)
        phn=request.POST.get('ph')
        service=request.POST.get('servic')
        se=Services.objects.get(name=service)
        print(se)
        dt=request.POST.get("dat")
        dt=request.POST.get('dat')
        tme=request.POST.get('tm')
        te=Timeslots.objects.get(name=tme)
        dotr=request.POST.get('doc')
        obj=ForBooking.objects.create(name=nam,phone=phn,services=se,bookingdate=dt,timeslot=te,docter=dotr)
        obj.save()
        print("sucess")
        return redirect(request,"bookingg")
   
    return render(request, "booking.html",context)    




def service(request):
    services=Services.objects.all()
    category=Categories.objects.all()
    context = {"services":services,"category":category}
    return render(request, "services.html",context)


    





class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, "User created successfully !!!")
        return super().form_valid(form)


#path("",views.LogInView.as_view(),name="login"),
class LogInView(FormView):
    form_class = LoginForm
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if(request.user.is_superuser):
                    return redirect("dashboard")
                else:
                    msg="Hello " +request.user.username+ "!!!, Welcome to Chiropractic !"
                    messages.success(request,msg)
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect("home")
            else:
                msg="Sorry! Log-in request failed, please check your username and password and try again"
                messages.warning(request,msg)
                return render(request, "login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request,"Successfully logged out!!!")
    return redirect('login')

#path("home", views.HomeView.as_view(), name="home"),

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_services = Services.objects.all().filter(exclusive=True)
        context["services"] = all_services
        # context["recently"] = RecentlyViewed.objects.filter(user=self.request.user)
        context["memberships"] = Memberships.objects.all()
        context["currency"] = Currency.objects.filter(status=True)
        context["banner"] = BannerImage.objects.all()

        return context

class MyAccountView(TemplateView):
    template_name="my-account.html"
    

#path("book/<int:sid>", views.BookView.as_view(), name="book")

class BookView(View):

    # template_name = "book.html"
    template_name = "service-detail.html"
    

    def get(self,request,*args, **kwargs):
        
        id = kwargs.get("sid")
        service=Services.objects.get(id=id)
        name = service.name
        # if RecentlyViewed.objects.filter(name=name):
        #     pass
        # else:
        #     RecentlyViewed.objects.create(name=name, service=service,user=request.user)
        cat=service.category
        category=Services.objects.filter(category=cat).exclude(name=name)
        review = ServiceReview.objects.filter(service=service)
        beautician = Beautician.objects.filter(category=service.category)
        form=forms.Date_Form
        available_slots = Timeslots.objects.all() 
        currency = Currency.objects.filter(status=True)
        slot=service.timeslots.all().exclude(status="pending").exclude(availability=0)
        
        if (request.user.is_authenticated):
            print(request.user)
            wish = Wishlist.objects.filter(service=service,user=request.user)  
            return render(request,self.template_name,{"service":service,"beautician":beautician,"review":review, "category":category, "wish":wish, "currency":currency})
            
        else:
            return render(request,self.template_name,{"service":service,"beautician":beautician,"review":review, "category":category, "currency":currency})    
        
        
        # return render(request,self.template_name)
    @method_decorator(login_required,name="dispatch")
    def post(self,request,*args,**kwargs):
        id = kwargs.get("sid")
        service = Services.objects.get(id=id)
        date=request.POST.get("date")
        slot=request.POST.get("slot")
        beautician=request.POST.get("beautician")
        if slot:
            if beautician:
                booked_slot = Timeslots.objects.filter(time=slot,date=date)[0]
                if (booked_slot.availability) > 0:
                    booked_slot.availability-=1
                    booked_slot.save()
                    if (booked_slot.availability)==0:
                        booked_slot.status="pending"
                        booked_slot.save()
                    booked_beautician=Beautician.objects.filter(name=beautician)[0]
                    Booking.objects.create(services=service,user=request.user,timeslot=booked_slot,beautician=booked_beautician,cost=service.cost)
                    messages.success(request,"Hooray! Booking successful! Please complete the payment!")
                    return redirect('bookings')
                else:
                    booked_slot.status="pending"
                    booked_slot.save()                
            else:
                messages.warning(request,"Please select any beautician to initiate booking!")
                return render(request,self.template_name,{"service":service})
            
        else:
            messages.warning(request,"Please select the date, slot & beautician to initiate booking!")
            return render(request,self.template_name,{"service":service})

def booking_payment(request,*args,**kwargs):
    id=kwargs.get("id")
    booking=Booking.objects.get(id=id)
    total=booking.cost
    return render(request, "payment.html", {"total":total,"id":id})

def payment_complete(request,*args,**kwargs):
    body=json.loads(request.body)
    print('BODY: ',body)
    booking=Booking.objects.get(id=body['bookingId'])
    transaction=body['transaction']
    #print("Transaction information is: ",transaction)#Transaction information is:  {'id': '69E993284Y0011637', 'status': 'COMPLETED', 'amount': {'currency_code': 'USD', 'value': '64.00'}, 'final_capture': True, 'seller_protection': {'status': 'ELIGIBLE', 'dispute_categories': ['ITEM_NOT_RECEIVED', 'UNAUTHORIZED_TRANSACTION']}, 'create_time': '2023-01-18T04:49:06Z', 'update_time': '2023-01-18T04:49:06Z'}
    #print("Transaction id is :",transaction['id'])#Transaction id is : 8S6375187M5451324
    if (transaction['status']) == 'COMPLETED':
        Transaction.objects.create(name=transaction['id'],status=transaction['status'],amount=booking.cost,details=transaction,type="Paypal")
        booking.status="booked"
        booking.save()
        return render(request,"payment-complete.html")
    else:
        messages.warning(request,"Payment failed, please try again after some time!")
        return redirect("bookings")
    
        
    # @method_decorator(login_required,name="dispatch")
    # def post(self, request, *args, **kwargs):
    #     id = kwargs.get("sid")
    #     service = Services.objects.get(id=id)
    #     form=forms.Date_Form(request.POST)
    #     b = Beautician.objects.filter(category=service.category)
    #     currency = Currency.objects.filter(status=True)
    #     user = request.user
    #     timeslot = request.POST.get("slot")
    #     selected_beautician = request.POST.get("beautician")  # Fetch selected beautician
    #     if form.is_valid():
    #         date = form.cleaned_data.get("date")        
        
    #     if (timeslot) and (selected_beautician):
    #         if date:
    #             for i in service.timeslots.filter(date=date):
    #                 if i.time==timeslot:
    #                     if (i.status!="pending") & (i.availability>0):
                            
    #                         booked_slot = Timeslots.objects.filter(time=timeslot,date=date)[0]
    #                         beautician = Beautician.objects.filter(name=selected_beautician)[0]
    #                         booking=Booking.objects.create(services=service,user=user,timeslot=booked_slot,beautician=beautician,cost=service.cost)
    #                         name=booking.id
    #                         service=booking.services
    #                         book_timeslot=booking.timeslot
    #                         book_user=booking.user
    #                         content="User "+str(book_user)+" has booked "+str(service)+"service for "+str(book_timeslot)
    #                         Notifications.objects.create(name=name, content=content)
    #                         i.availability-=1
    #                         i.status="booked"
    #                         i.save()
    #                         m = "Hello " +request.user.username+ "!!!, Your booking request initiated and the order id is:" +str(booking.id) + ".Thank you!"
    #                         messages.success(request, m)
    #                         return redirect("bookings")
                            
    #                     else:
    #                         i.status="pending"
    #                         i.save()
    #                         m = "Hello",request.user.username,","," Sorry! Your booking request failed because the selected timeslot was filled already. Please try after some time "
    #                         messages.success(request, m)
    #                         return redirect("shop")
    #         else:
    #             m="Hello",request.user.username,","," Sorry! You haven't selected a preferred date for booking "
    #             messages.warning(request, m)
    #             return render(request,self.template_name,{"service":service,"beautician":b,"currency":currency})
                    
                
    #     else:
    #         if form:
    #             s=service.timeslots.filter(date=date).exclude(status="pending").exclude(availability=0)
    #             wish = Wishlist.objects.filter(service=service)  
    #             return render(request,self.template_name,{"service":service,"beautician":b,"slot":s,"date":date,"form":form, "wish":wish,"currency":currency})
    #         else:
    #             m='Sorry!',request.user.username,","," Your booking request failed! Please make sure you selected preferred timeslot & beautician , thank you!"
    #             messages.warning(request, m)
    #             return redirect("shop")

#path("mybookings", views.MyBookingView.as_view(), name="bookings")
@method_decorator(login_required,name="dispatch")
class MyBookingView(ListView):
    template_name = "bookings.html"
    model = Booking
    # context_object_name = 'bookings'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["bookings"] = Booking.objects.filter(user=self.request.user)       
        context["currency"] = Currency.objects.filter(status=True)
        return context
    
    # def get_queryset(self):
    #     return Booking.objects.filter(user=self.request.user).exclude(
    #         status="cancelled")

        # def delete_service(self, request, *args, **kwargs):
        #     a = Services.objects.all()
        #     a.delete()
        #
        # print(Booking.objects.filter(user=self.request.user))


#path("mybookings/<int:bid>", views.BookingUpdateView.as_view(), name="update-booking"),
@method_decorator(login_required,name="dispatch")
class BookingUpdateView(UpdateView):
    model = Booking
    template_name = "booking-update.html"
    pk_url_kwarg = "bid"
    success_url = reverse_lazy("bookings")
    form_class = UpdateBookingForm

    def form_valid(self, form):
        messages.success(self.request, "Booking  updated successfully")
        return super().form_valid(form)


#path("mybookings/<int:bid>/cancel", views.cancel_booking, name="cancel-booking"),
@method_decorator(login_required,name="dispatch")
class CancelBookingView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("bid")
        booking = Booking.objects.get(id=id)
        return render(request, "confirm-cancel.html", {"booking": booking})

    def post(self, request, *args, **kwargs):
        id = kwargs.get("bid")
        booking = Booking.objects.get(id=id)
        print(booking)
        booking.status = "cancelled"
        booking.save()
        msg = "Hello User booking cancelled as per your request"
        messages.success(request, msg)
        return redirect('home')


class ShopView(TemplateView):
    template_name = "booking1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Services.objects.filter(status=True)
        context["categories"] = Categories.objects.filter(status=True)
        context["currency"] = Currency.objects.filter(status=True)
        return context
    
    def post(self,request,*args,**kwargs):
        body=request.POST.get("body")
        service=request.POST.get("service")
        provider=request.POST.get("provider")
        print("Service is :",service, "Provider is :", provider,"Body is ",body)
        return redirect('home')
    

    # def post(self, request, *args, **kwargs):
    #     category=request.POST.get("category")
    #     categories=Categories.objects.all()
    #     cata=Services.objects.filter(category__category_name=category)

    #     if cata:
    #         return render(request,"shop.html",{"services":cata,"categories":categories})
    #     elif(category=="All Services"):
    #         return render(request,"shop.html",{"services":Services.objects.all(),"categories":categories})
    #     else:
    #         return render(request,"shop.html",{"services":None,"categories":categories})

class MembershipView(ListView):
    template_name="membership.html"
    model=Memberships
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["memberships"] = Memberships.objects.all()
        context["currency"] = Currency.objects.filter(status=True)
        return context




class BookingView(TemplateView):
    template_name = "booknow.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Services.objects.all()
        context["categories"] = Categories.objects.all()
        return context


    def post(self, request, *args, **kwargs):
        category=request.POST.get("category")
        categories=Categories.objects.all()
        cata=Services.objects.filter(category__category_name=category)
       
        if cata:
            return render(request,"booknow.html",{"services":cata,"categories":categories})
        elif(category=="All Services"):
            return render(request,"booknow.html",{"services":Services.objects.all(),"categories":categories})
        else:
            return render(request,"booknow.html",{"services":None,"categories":categories})

# def booknow(request):
    # categories=Categories.objects.all()
    # services=Services.objects.all()
    # return render(request, "booknow.html",{"categories":categories})
    

def test(request,): 
    timeslots=Timeslots.objects.all()
    services=Services.objects.all()
    return JsonResponse({"timeslots":list(timeslots.values()),"services":list(services.values())})
    
def category_detail(request,*args,**kwargs):
    id=kwargs.get("id")
    services=Services.objects.filter(category=id)
    return JsonResponse({"services":list(services.values())})


def test_ajax(request):
    return render(request,"test.html")
    
def get_category_services(request,*args,**kwargs):
    categories=Categories.objects.all()
    id=kwargs.get("cid")
    category=Categories.objects.get(id=id)
    cata=Services.objects.filter(category=category)
    return render(request, "booknow.html",{"categories":categories,"services":cata})


class PackageView(ListView):
    template_name="package.html"
    model=Package

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["packages"] = Package.objects.all()
        context["currency"] = Currency.objects.filter(status=True)
        return context
    

class GiftCardView(ListView):
    template_name="giftcard.html"
    model=GiftCards

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["giftcards"] = GiftCards.objects.all()
        context["currency"] = Currency.objects.filter(status=True)
        return context


class IntroOffersView(ListView):
    model = IntroOffers
    template_name = "introoffer.html"
    context_object_name = "introoffers"


class BlogsView(ListView):
    model = Blogs
    template_name = "blogs.html"
    context_object_name = "blogs"


class ContactUsView(FormView):
    template_name = "contactus.html"
    form_class = ContactUsForm
    success_url = reverse_lazy("contactus")

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ContactUs.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, "Thank You for Contacting us. Our representative will contact you soon")
        return redirect('contactus')
     

class AboutUs(TemplateView):
    template_name = "aboutus.html"


class SpaEti(TemplateView):
    template_name = "spa-etiquette.html"

#Profile
@login_required
def profile(request, *args, **kwargs):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        image = request.FILES.get('image')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phoneNumber')
        address = request.POST.get('address')
        state = request.POST.get('state')
        zipCode = request.POST.get('zipCode')
        country = request.POST.get('country')
        language = request.POST.get('language')
        profile = ProfileManage.objects.create(first_name=firstName, last_name=lastName,image=image, email=email, user=request.user, address=address, contactno=phoneNumber, language=language, country=country, state=state, zip_code=zipCode)
        profile.save()
        messages.success(request, "Profile created successfully")
        return redirect('profile-manager')
    return render(request,"profile-manager.html" )

@login_required
def profiledetail(request):
    profile = ProfileManage.objects.filter(user=request.user).values()
    return render(request, "view-profile.html", {'profile':profile})


@method_decorator(login_required,name="dispatch")
class ProfileUpdate(UpdateView):
    model = ProfileManage
    template_name = "update-profile.html"
    pk_url_kwarg = "pid"
    success_url = reverse_lazy("profile-manager")

    


    def get_queryset(self):
        return ProfileManage.objects.filter(user=self.request.user)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = ProfileManage.objects.filter(user=self.request.user)
        return context
    # def post(self, request, *args, **kwargs):
    #     form = ProfileForm(request.POST)
    #     if form.is_valid:
    #         form.save()
    #         messages.success(request, "Profile created successfully")
    #         return redirect("customer:my-account")
    #     else:
    #         messages.warning(request, "Error occured while creating")
    #         return redirect("customer:my-account")




class ProfileUpdate(UpdateView):
    model = ProfileManage
    template_name = "update-profile.html"
    pk_url_kwarg = "pid"
    success_url = reverse_lazy("profile-manager")
    form_class = ProfileUpdateForm

    def form_valid(self, form):
        messages.success(self.request, "Profile updated successfully")
        return super().form_valid(form)

@login_required
def wishlist(request,*args,**kwargs):
    id=kwargs.get("sid")
    service=Services.objects.get(id=id)
    wish=Wishlist.objects.filter(user=request.user)
    if wish:
        for wis in wish:
            if (wis.service.name==service.name):
                msg="Service already added in wishlists."
                messages.warning(request,"Service already added in wishlists.")
                return redirect("shop")
        Wishlist.objects.create(service=service,user=request.user,)
        msg="Service added to wishlists."
        messages.success(request,msg)
        return redirect("shop")

    else:
        Wishlist.objects.create(service=service,user=request.user)
        msg="Service added to wishlists."
        messages.success(request,msg)
        return redirect("shop")
    
    


#MyMemberships


# class MyMemView(View):
#     form_class = MyMemForm
#     # template_name = "book.html"
#     template_name = "membership-detail.html"
    
@login_required
def BuyMembership(request, *args, **kwargs):
    id = kwargs.get("mid")
    membership = Memberships.objects.get(id=id)
    print(membership, "membership is")
    user = request.user
    print ("useris", user)
        # timeslot = request.POST.get("slot")
        # date = request.POST.get("date")
        # selected_beautician = request.POST.get(
        #     "beauty")  # Fetch selected beautician

        # if (timeslot) and (selected_beautician):
    MyMemberships.objects.create(membership=membership,
                                             user=user
                                            )
    print("success")                                    
    messages.success(request, "Membership bought successfully")
    return redirect("memberships")
    # return render(request, "membership-detail.html",{'membership':membership})                                    
           
@method_decorator(login_required,name="dispatch")
class MyMembershipView(ListView):
    template_name = "my-memberships.html"
    model = MyMemberships
    # context_object_name = 'memberships'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["memberships"] = MyMemberships.objects.filter(user=self.request.user)
        context["currency"] = Currency.objects.filter(status=True)
        return context


    # def get_queryset(self):
    #     return MyMemberships.objects.filter(user=self.request.user)



#mypackages
@login_required
def BuyPackages(request, *args, **kwargs):
    id = kwargs.get("pid")
    package = Package.objects.get(id=id)
    user = request.user
    MyPackages.objects.create(package=package, user=user)
    messages.success(request, "Package bought successfully")
    return redirect("packages")
    # return render(request, "package-detail.html", {'package':package})

@method_decorator(login_required,name="dispatch")
class MyPackageView(ListView):
    model = MyPackages
    template_name = "my-packages.html"


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["packages"] = MyPackages.objects.filter(user=self.request.user)
        context["currency"] = Currency.objects.filter(status=True)
        return context



#giftcards
@login_required
def BuyGiftCards(request, *args, **kwargs):
    id = kwargs.get("gid")
    giftcard =GiftCards.objects.get(id=id)
    user = request.user
    MyGiftcards.objects.create(giftcard=giftcard, user=user)
    messages.success(request, "Giftcards bought successfully")
    return redirect("giftcards")
    # return render(request, "giftcard-detail.html", {"giftcard":giftcard})

@method_decorator(login_required,name="dispatch")
class MyGiftCardsView(ListView):
    model = MyGiftcards
    template_name = "my-giftcards.html"
   


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["giftcards"] = MyGiftcards.objects.filter(user=self.request.user)
        context["currency"] = Currency.objects.filter(status=True)
        return context
    # def get_queryset(self):
    #     return MyGiftcards.objects.filter(user=self.request.user)



##membershipupdate
@login_required
def membership_status_change(request, id):
    membership = MyMemberships.objects.filter(user=request.user, id=id)
    for mem in membership:
        if mem.status == "booked":
            mem.status = "expired"  
            mem.save()
    msg="Hello " + str(request.user) + ", Membership cancelled as per your request"
    messages.warning(request,msg)
    return redirect("my-memberships")

#mypackageupdate
@login_required
def package_status_change(request, id):
    package = MyPackages.objects.filter(user=request.user, id=id)
    for pack in package:
        if pack.status == "booked":
            pack.status = "expired"
            pack.save()
    msg = "Hello " + str(request.user) + ", Package cancelled as per your request"
    messages.success(request, msg)
    return redirect("my-packages")

#mygiftcardupdate
@login_required
def giftcard_status_change(request, id):
    giftcard = MyGiftcards.objects.filter(user=request.user, id=id)
    for gift in giftcard:
        if gift.status == "booked":
            gift.status = "expired"
            gift.save()
    msg = "Hello " + str(request.user) + ", GiftCard cancelled as per your request"
    messages.success(request, msg)
    return redirect("my-giftcards")

@login_required
def booking_status_change(request, id):
    booking = Booking.objects.filter(user=request.user, id=id)
    for book in booking:
        if book.status == "booked":
            book.status = "cancelled"
            book.save()
    msg = "Hello " + str(request.user) + ", Booking cancelled as per your request"
    messages.success(request, msg)
    return redirect("bookings")

@login_required
def service_review(request, id):
    service = Services.objects.get(id=id)
    if request.method == 'POST':
        review = request.POST.get('review')
        new_rating = request.POST.get('rating')
        s = int(service.rating)
        service.rating=new_rating
        count = service.rating_count
        new_count = count
        new_count += 1
        rate = s + int(new_rating)
        avg = int(rate) / int((new_count))
        service.rating = float(avg)
        service.save()
        service.rating_count = new_count
        service.save()
        obj = ServiceReview.objects.create(user_name=request.user, review=review, service=service)
        obj.save()
        messages.success(request, "Thank you " +str(request.user)+ " for submitting your review!!")
        return redirect("shop")
    return render(request, "service-review-form.html")


#passwordchange
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


#wishlist
@method_decorator(login_required,name="dispatch")
class WishlistView(TemplateView):
    template_name = "wishlist.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Wishlist.objects.filter(user=self.request.user)
        context["currency"] = Currency.objects.filter(status=True)


        return context


#wishlist_status_change
# def Wishlist_status(request, id):
#     wishlist = Wishlist.objects.filter(user=request.user, id=id)
#     for wish in wishlist:
#         if wish.status == "Wishlisted":
#             wish.status = "Removed"
#             wish.save()
#     msg = "Hello " + str(request.user)+ ", your item has been removed from wishlist"
#     messages.success(request, msg)
#     return redirect("wishlist")
@login_required
def delete_wishlist(request, id):
    wishlist = Wishlist.objects.get(id=id)
    wishlist.delete()
    return redirect("wishlist")

@login_required
def cart_giftcard(request, id):
    giftcard = GiftCards.objects.get(id=id)
    Cart.objects.create(giftcard=giftcard, user=request.user, membership=None)
    messages.success(request, "Item added to cart successfully!!")
    return redirect("giftcards")

@login_required
def cart_items(request):
    cart = Cart.objects.filter(user=request.user)
    subtotal = 0
    total = 10
    giftprice = 0
    memprice = 0
    introprice = 0
    packprice = 0
    if cart:
        for car in cart:
            if car.giftcard:
                giftprice += car.giftcard.price
            elif car.membership:
                memprice += car.membership.price  
            elif car.introoffer:
                introprice += car.introoffer.off  
            else:
                packprice += car.package.price
        subtotal += (giftprice+memprice+introprice+packprice)
        total += (giftprice+memprice+introprice+packprice)  
    currency = Currency.objects.filter(status=True)   
    return render(request, "cart1.html", {"cart":cart, "subtotal":subtotal, "total":total, "currency":currency})

@login_required
def service_cart(request):
    cart=ServiceCart.objects.filter(user=request.user,status="in-cart")
    currency=Currency.objects.filter(status=True)[0]
    STRIPE_KEY=settings.STRIPE_PUBLISHABLE_KEY
    total=0
    if cart:
        for c in cart:
            total+=c.cost
    return render(request,'service-cart.html',{'cart':cart,'currency':currency,'subtotal':total,'total':(total+10),"STRIPE_PUBLIC_KEY":STRIPE_KEY})

@login_required
def remove_service_cart(request,id):
    ServiceCart.objects.get(id=id).delete()
    return redirect('service-cart')

@login_required
def my_orders(request):
    orders = ServiceOrder.objects.filter(user=request.user)  
    currency=Currency.objects.filter(status=True)[0]
    return render(request, "service-orders.html", {"orders":orders,'currency':currency})

@login_required
def delete_cart_item(request, id):
    cart_item = Cart.objects.get(id=id)
    cart_item.delete()
    return redirect("cart-items")

@login_required
def cart_membership(request, id):
    membership = Memberships.objects.get(id=id)
    Cart.objects.create(membership=membership, user=request.user, giftcard=None)
    messages.success(request, "Item added to cart successfully!!")
    return redirect("memberships")


@login_required
def BuyIntroOffers(request, id):
    intro =IntroOffers.objects.get(id=id)
    user = request.user
    MyIntroOffers.objects.create(intro=intro, user=user)
    messages.success(request, "Intro Offer bought successfully")
    return redirect( "introoffers")


@login_required
def cart_introoffer(request, id):
    introoffer = IntroOffers.objects.get(id=id)
    cart_intro = Cart.objects.filter(user=request.user)
    Cart.objects.create(introoffer=introoffer, user=request.user)
    messages.success(request, "Item added to cart successfully!!")
    return redirect("introoffers")



@login_required
def cart_package(request, id):
    package = Package.objects.get(id=id)
    Cart.objects.create(package=package, user=request.user)
    messages.success(request, "Item added to cart successfully!!")
    return redirect("packages")

def first_visit(request):
    return render(request, "firstvisit.html")


def mani_pedi(request):
    services =  Services.objects.filter(category__category_name="MANI/PEDI")
    intro = IntroOffers.objects.all()
    return render(request, "mani-pedi.html", {"services":services, "intro":intro})


def manicure(request):
    services =  Services.objects.filter(category__category_name="MANICURE")
    intro = IntroOffers.objects.all()
    return render(request, "manicure.html", {"services":services, "intro":intro})


def pedicure(request):
    services =  Services.objects.filter(category__category_name="PEDICURE")
    intro = IntroOffers.objects.all()
    return render(request, "pedicure.html", {"services":services, "intro":intro})


def hair_removal(request):
    services =  Services.objects.filter(category__category_name="HAIR REMOVAL WAXING")
    intro = IntroOffers.objects.all()
    return render(request, "hair-removal.html", {"services":services, "intro":intro})


def add_ons(request):
    services =  Services.objects.filter(category__category_name="ADD-ONS")
    intro = IntroOffers.objects.all()
    return render(request, "add-ons.html", {"services":services, "intro":intro})


def massage(request):
    services =  Services.objects.filter(category__category_name="MASSAGE")
    intro = IntroOffers.objects.all()
    return render(request, "massage.html", {"services":services, "intro":intro})


def eye(request):
    services =  Services.objects.filter(category__category_name="EYE LASH EXTENSIONS")
    intro = IntroOffers.objects.all()
    return render(request, "eye.html", {"services":services, "intro":intro})


def facials(request):
    services =  Services.objects.filter(category__category_name="FACIALS")
    intro = IntroOffers.objects.all()
    return render(request, "facials.html", {"services":services, "intro":intro})

@login_required
def payment(request):
    cart = Cart.objects.filter(user=request.user)
    subtotal = 0
    total = 10
    giftprice = 0
    memprice = 0
    introprice = 0
    packprice = 0
    if cart:
        for car in cart:
            if car.giftcard:
                giftprice += car.giftcard.price
            elif car.membership:
                memprice += car.membership.price  
            elif car.introoffer:
                introprice += car.introoffer.off  
            else:
                packprice += car.package.price
        subtotal += (giftprice+memprice+introprice+packprice)
        total += (giftprice+memprice+introprice+packprice)
    return render(request, "payment-cart.html", {"total":total,"cart":cart})

def payment_cart_complete(request,*args,**kwargs):
    body=json.loads(request.body)
    print('BODY: ',body)
    cart=Cart.objects.filter(user=request.user)
    card=0
    membership=0
    package=0
    for c in cart:
        if c.giftcard:
            card=c.giftcard
        if c.membership:
            membership=c.membership
        if c.package:
            package=c.package
        if c.introoffer:
            introoffer=c.introoffer
    print(card,membership,package)


    transaction=body['transaction']
    return redirect("home")
    #print("Transaction information is: ",transaction)#Transaction information is:  {'id': '69E993284Y0011637', 'status': 'COMPLETED', 'amount': {'currency_code': 'USD', 'value': '64.00'}, 'final_capture': True, 'seller_protection': {'status': 'ELIGIBLE', 'dispute_categories': ['ITEM_NOT_RECEIVED', 'UNAUTHORIZED_TRANSACTION']}, 'create_time': '2023-01-18T04:49:06Z', 'update_time': '2023-01-18T04:49:06Z'}
    #print("Transaction id is :",transaction['id'])#Transaction id is : 8S6375187M5451324
    # if (transaction['status']) == 'COMPLETED':
    #     Transaction.objects.create(name=transaction['id'],status=transaction['status'],amount=booking.cost,details=transaction,type="Paypal")
    #     booking.status="booked"
    #     booking.save()
    #     return render(request,"payment-complete.html")
    # else:
    #     messages.warning(request,"Payment failed, please try again after some time!")
    #     return redirect("bookings")

@login_required
def membership_payment(request, id):
    membership = Memberships.objects.get(id=id)
    total = membership.price
    return render(request, "payment.html", {"total":total})


@login_required
def package_payment(request, id):
    package = Package.objects.get(id=id)
    total = package.price
    return render(request, "payment.html", {"total":total})



@login_required
def giftcard_payment(request, id):
    giftcard = GiftCards.objects.get(id=id)
    total = giftcard.price
    return render(request, "payment.html", {"total":total})


def subscription(request):
    if request.method == 'POST':
        if request.POST.get('name') == '':
            messages.success(request, "Please provide your name")
            return redirect('/')
        elif request.POST.get('email') == '':
            messages.success(request, "Please provide your email")
            return redirect('/')
        email = request.POST.get('email')
        print(email)
        name = request.POST.get('name')
        Subscription.objects.create(name=name, email=email)
        messages.success(request, "Thank you for subscribing !!")
        return redirect('/')
            
        
       







@login_required
def book_details(request, id):
    service = Booking.objects.get(id=id)
    currency = Currency.objects.filter(status=True)
    return render(request, "book-details.html", {"service":service, "currency":currency})


@login_required
def book_review(request, id):
    service = Services.objects.get(id=id)
    if request.method == 'POST':
        review = request.POST.get('review')
        new_rating = request.POST.get('rating')
        s = int(service.rating)
        service.rating=new_rating
        count = service.rating_count
        new_count = count
        new_count += 1
        rate = s + int(new_rating)
        avg = int(rate) / int((new_count))
        service.rating = float(avg)
        service.save()
        service.rating_count = new_count
        service.save()
        obj = ServiceReview.objects.create(user_name=request.user, review=review, service=service)
        obj.save()
        messages.success(request, "Thank you " +str(request.user)+ " for submitting your review!!")
        return redirect("bookings")
    return render(request, "booking-review.html")



def careers(request):
    careers = CareerOpenings.objects.all()
    return render(request, "careers.html", {"careers":careers})


class CareerForm(FormView):
    form_class = Date_Form
    template_name = "job-detail.html"

    def post(self, request, *args, **kwargs):
        form = forms.Date_Form(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get("date")  
            print(date)
        first_name = request.POST.get('first_name')
        print(first_name)
        last_name = request.POST.get('last_name')
        #date = form.cleaned_ata.get('date')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')
        email  = request.POST.get('email')
        position = request.POST.get('position')
        company_awareness = request.POST.get('company_awareness')
        ever_applied = request.POST.get('ever_applied')
        ever_applied_yes = request.POST.get('ever_applied_yes')
        applied_date = request.POST.get('applied_date')
        ever_employed = request.POST.get('ever_employed')
        ever_employed_yes = request.POST.get('ever_employed_yes')
        employed_date = request.POST.get('employed_date')
        school = request.POST.get('school')
        shool_compl_year = request.POST.get('shool_compl_year')
        college = request.POST.get('college')
        college_compl_year = request.POST.get('college_compl_year')
        college_course = request.POST.get('college_course')
        university = request.POST.get('university')
        cosmet_school = request.POST.get('cosmet_school')
        cosmet_compl_year = request.POST.get('cosmet_compl_year')
        cosmet_course = request.POST.get('cosmet_course')
        massage_school = request.POST.get('massage_school')
        massage_compl_year = request.POST.get('massage_compl_year')
        massage_course = request.POST.get('massage_course')
        other_school = request.POST.get('other_school')
        other_compl_year = request.POST.get('other_compl_year')
        other_course = request.POST.get('other_course')
        special_training = request.POST.get('special_training')
        exp_company = request.POST.get('exp_company')
        exp_phone = request.POST.get('exp_phone')
        exp_address = request.POST.get('exp_address')
        exp_from = request.POST.get('exp_from')
        exp_to = request.POST.get('exp_to')
        exp_supervisor = request.POST.get('exp_supervisor')
        exp_rate = request.POST.get('exp_rate')
        exp_job = request.POST.get('exp_job')
        exp_reason_leave = request.POST.get('exp_reason_leave')
        age = request.POST.get('age')
        contact_personal_employer = request.POST.get('contact_personal_employer')
        currently_employed = request.POST.get('currently_employed')
        law_status = request.POST.get('law_status')
        drive_license = request.POST.get('drive_license')
        drive_license_exp = request.POST.get('drive_license_exp')
        transportation = request.POST.get('transportation')
        current_salary = request.POST.get('current_salary')
        need_salary = request.POST.get('need_salary')
        want_salary = request.POST.get('want_salary')
        cuurent_work_hours = request.POST.get('cuurent_work_hours')
        likely_work_hours = request.POST.get('likely_work_hours')
        client_count = request.POST.get('client_count')
        strengths = request.POST.get('strengths')
        areas_improve = request.POST.get('areas_improve')
        contr_to_comp = request.POST.get('contr_to_comp')
        contr_subs = request.POST.get('contr_subs')
        convicted = request.POST.get('convicted')
        mon_hrs = request.POST.get('mon_hrs')
        tue_hrs = request.POST.get('tue_hrs')
        wed_hrs = request.POST.get('wed_hrs')
        thu_hrs = request.POST.get('thu_hrs')
        fri_hrs = request.POST.get('fri_hrs')
        sat_hrs = request.POST.get('sat_hrs')
        sun_hrs = request.POST.get('sun_hrs')
        ind_exp = request.POST.get('ind_exp')
        ind_bg = request.POST.get('ind_bg')
        ind_offer = request.POST.get('ind_offer')
        ind_expect = request.POST.get('ind_expect')
        ind_goals = request.POST.get('ind_goals')
        ind_goal_plan = request.POST.get('ind_goal_plan')
        ind_where_see = request.POST.get('ind_where_see')
        ind_exp_years = request.POST.get('ind_exp_years')
        ind_pr_job_exp = request.POST.get('ind_pr_job_exp')
        ind_pr_job_leave = request.POST.get('ind_pr_job_leave')
        ind_crazy = request.POST.get('ind_crazy')
        ind_how_spa = request.POST.get('ind_how_spa')
        ind_how_no_spa = request.POST.get('ind_how_no_spa')
        reference = request.POST.get('reference')
        resume = request.POST.get('resume')
        PersonalDetails.objects.create(first_name=first_name, last_name=last_name, date=date, address=address, city=city, state=state, country=country, zip_code=zip_code, phone=phone, email=email, position=position, company_awareness=company_awareness, ever_applied=ever_applied, ever_applied_yes=ever_applied_yes, applied_date=applied_date, ever_employed=ever_employed, ever_employed_yes=ever_employed_yes,  employed_date=employed_date,age=age)
        #EductaionDetails.objects.create(school=school, shool_compl_year=shool_compl_year, college=college, college_compl_year=college_compl_year, college_course=college_course, university=university, cosmet_school=cosmet_school,cosmet_compl_year=cosmet_compl_year,  cosmet_course=cosmet_course, massage_school=massage_school, massage_compl_year=massage_compl_year, massage_course=massage_course, other_school=other_school, other_compl_year=other_compl_year, other_course=other_course, special_training=special_training)
        #ExperienceDetails.objects.create(exp_company=exp_company, exp_phone=exp_phone, exp_address=exp_address, exp_from=exp_from, exp_to=exp_to, exp_supervisor=exp_supervisor,exp_rate=exp_rate, exp_job=exp_job, exp_reason_leave=exp_reason_leave,contact_personal_employer=contact_personal_employer ,currently_employed=currently_employed)
        #ExtraDetails.objects.create(law_status=law_status,drive_license=drive_license, drive_license_exp=drive_license_exp,transportation=transportation, current_salary=current_salary,need_salary=need_salary,want_salary=want_salary,cuurent_work_hours=cuurent_work_hours,likely_work_hours=likely_work_hours,client_count=client_count,strengths=strengths,areas_improve=areas_improve,contr_to_comp=contr_to_comp,contr_subs=contr_subs,convicted=convicted,mon_hrs=mon_hrs,tue_hrs=tue_hrs,wed_hrs=wed_hrs,thu_hrs=thu_hrs,fri_hrs=fri_hrs,sat_hrs=sat_hrs,sun_hrs=sun_hrs)
        #IndustryExperience.objects.create(ind_exp=ind_exp,ind_bg=ind_bg,ind_offer=ind_offer,ind_expect=ind_expect,ind_goals=ind_goals,ind_goal_plan=ind_goal_plan,ind_where_see=ind_where_see,ind_exp_years=ind_exp_years,ind_pr_job_exp=ind_pr_job_exp,ind_pr_job_leave=ind_pr_job_leave,ind_crazy=ind_crazy,ind_how_spa=ind_how_spa,ind_how_no_spa=ind_how_no_spa,reference=reference,resume=resume)
        return redirect("career-form")

  

  