from django.shortcuts import render, redirect
from customer.models import *
from owner.models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, TemplateView, FormView, DetailView, ListView, UpdateView, RedirectView, View, DeleteView
from django.contrib import messages
from owner.forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from customer.decorators import*
from django.contrib.auth.models import User


@method_decorator(signin_required,name="dispatch")
class DashboardView(TemplateView):
    template_name = "indexx.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookings"] = Booking.objects.all()
        context["notification_count"] = Notifications.objects.filter(status="unread").count()
        return context

@method_decorator(signin_required,name="dispatch")
class AdminAccountView(TemplateView):
    template_name = "account-settings.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Services.objects.all()
        context["profile"] = ProfileManage.objects.filter(user=self.request.user)
        print(context)
        return context


#path("slots", views.AddSlots.as_view(), name="add-slot")
#Admin action
#Pending
@method_decorator(signin_required,name="dispatch")
class AddSlots(TemplateView):
    template_name = "add-slots.html"

    def get_context_data(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        all_services = Services.objects.all()
        context["services"] = all_services
        a = Timeslots.objects.all()
        a1 = a[::1]
        p = [i for i in a1 if i != 1]
        context["slots"] = p
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST.get("slot")
        print("Fetched data is ", data)
        return redirect("home")


#Categories
@method_decorator(signin_required,name="dispatch")
class ManageCategoriesView(TemplateView):
    model = Categories
    template_name = "manage-categories.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Categories.objects.all()
        return context

@method_decorator(signin_required,name="dispatch")
class AddCategoriesView(CreateView):
    template_name = "add-categories.html"
    form_class = CategoryAddForm
    success_url = reverse_lazy("manage-categories")

    # def post(self, request, *args, **kwargs):
    #     form = CategoryAddForm(request.POST, request.FILES)
    #     if form.is_valid:
    #         form.save()
    #         messages.success(request, "Category created Successfully")
    #         return redirect("manage-categories")
    #     else:
    #         messages.warning(request, "Category creation failed")
    #         return redirect("manage-categories")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Categories.objects.all()
        return context

    

@method_decorator(signin_required,name="dispatch")
class DetailCategoryView(DetailView):

    
    model = Categories
    template_name = "category-view.html"
    pk_url_kwarg = "cid"
    context_object_name = "category"

@method_decorator(signin_required,name="dispatch")
class DeleteCategoriesView(DeleteView):
    model = Categories
    pk_url_kwarg = "cid"
    success_url = reverse_lazy("manage-categories")
    template_name = "confirm-delete.html"

    def form_valid(self, form):
        messages.success(self.request, "Category deleted successfully")
        return super(DeleteCategoriesView, self).form_valid(form)

@method_decorator(signin_required,name="dispatch")
class UpdateCategoryView(UpdateView):
    model = Categories
    template_name = "update-category.html"
    pk_url_kwarg = "cid"
    success_url = reverse_lazy("manage-categories")
    form_class = UpdateCategoryForm

    def form_valid(self, form):
        messages.success(self.request, "Category  updated successfully")
        return super().form_valid(form)


#Services
@method_decorator(signin_required,name="dispatch")
class ManageServicesView(TemplateView):
    model = Services
    template_name = "manage-services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Services.objects.all()
        return context

@method_decorator(signin_required,name="dispatch")
class AddServicesView(FormView):
    template_name = "add-services.html"
    form_class = ServiceAddForm
    success_url = reverse_lazy("manage-services")

    def post(self, request, *args, **kwargs):
        form = ServiceAddForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, "Service created Successfully")
            return redirect("manage-services")
        else:
            messages.warning(request, "Service creation failed")
            return redirect("manage-services")

@method_decorator(signin_required,name="dispatch")
class ServiceView(DetailView):
    model = Services
    template_name = "service-view.html"
    context_object_name = "service"
    pk_url_kwarg = "sid"

@method_decorator(signin_required,name="dispatch")
class DeleteServicesView(DeleteView):
    model = Services
    pk_url_kwarg = "sid"
    success_url = reverse_lazy("manage-services")
    template_name = "confirm-delete.html"

    def form_valid(self, form):
        messages.success(self.request, "Service deleted successfully")
        return super(DeleteServicesView, self).form_valid(form)

@method_decorator(signin_required,name="dispatch")
class UpdateServiceView(UpdateView):
    model = Services
    template_name = "update-service.html"
    pk_url_kwarg = "sid"
    success_url = reverse_lazy("manage-services")
    form_class = UpdateServiceForm

    def form_valid(self, form):
        messages.success(self.request, "Service  updated successfully")
        return super().form_valid(form)
#Add Ons
@method_decorator(signin_required,name="dispatch")
class AddAddonsView(FormView):
    template_name = "add-addons.html"
    form_class = AddonAddForm
    success_url = reverse_lazy("manage-memberships")

    def post(self, request, *args, **kwargs):
        form = AddonAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Addons created Successfully")
            return redirect("manage-addons")
        else:
            messages.warning(request, "Addons creation failed")
            return redirect("manage-addons")
        
@method_decorator(signin_required,name="dispatch")
class ManageAddonsView(TemplateView):
    model = AddOns
    template_name = "manage-addons.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["addons"] = AddOns.objects.all()
        return context
#Memberships
@method_decorator(signin_required,name="dispatch")
class ManageMembershipsView(TemplateView):
    model = Memberships
    template_name = "manage-memberships.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["membership"] = Memberships.objects.all()
        return context

@method_decorator(signin_required,name="dispatch")
class AddMembershipsView(FormView):
    template_name = "add-memberships.html"
    form_class = MembershipAddForm
    success_url = reverse_lazy("manage-memberships")

    def post(self, request, *args, **kwargs):
        form = MembershipAddForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, "Membership created Successfully")
            return redirect("manage-memberships")
        else:
            messages.warning(request, "Membership creation failed")
            return redirect("manage-memberships")

@method_decorator(signin_required,name="dispatch")
class DeleteMembershipView(DeleteView):
    model = Memberships
    pk_url_kwarg = "mid"
    success_url = reverse_lazy("manage-memberships")
    template_name = "confirm-delete.html"

    def form_valid(self, form):
        messages.success(self.request, "Membership deleted successfully")
        return super(DeleteMembershipView, self).form_valid(form)


@method_decorator(signin_required,name="dispatch")
class UpdateMembershipView(UpdateView):
    model = Memberships
    template_name = "update-membership.html"
    pk_url_kwarg = "mid"
    success_url = reverse_lazy("manage-memberships")
    form_class = UpdateMembershipForm

    def form_valid(self, form):
        messages.success(self.request, "Membership  updated successfully")
        return super().form_valid(form)

# @method_decorator(signin_required,name="dispatch")
# class DetailMembershipView(DetailView):
#     model = Memberships
#     template_name = "view-membership.html"
#     id = kwargs.get("mid")
#     print(id)

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['membership'] = Memberships.objects.get(id=id)
#         membership = Memberships.objects.get(id=id)
#         context['mem'] = MyMemberships.objects.filter(membership__name=membership.name)
#         return context

#membershipdetailfunction
def detail_membership(request, id):
    membership = Memberships.objects.get(id=id)
    mem = MyMemberships.objects.filter(membership__name=membership.name)
    return render(request, "view-membership.html", {'membership':membership, 'mem':mem})


#Beauticians
@method_decorator(signin_required,name="dispatch")
class ManageBeauticiansView(TemplateView):
    model = Beautician
    template_name = "manage-beauticians.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beauticians"] = Beautician.objects.all()

        return context

@method_decorator(signin_required,name="dispatch")
class AddBeauticiansView(CreateView):
    template_name = "add-beauticians.html"
    form_class = BeauticianAddForm
    success_url = reverse_lazy("manage-beauticians")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beauticians"] = Beautician.objects.all()

        category = Beautician.objects.filter(
            category__category_name="Manicure")
        print("Category is: ", category)

        return context

    def post(self, request, *args, **kwargs):
        form = BeauticianAddForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Beautician added Successfully")
            return redirect( "manage-beauticians")
        else:
            messages.warning(request, "Beautician creation failed")
            return redirect("manage-beauticians")

@method_decorator(signin_required,name="dispatch")
class DetailBeauticianView(DetailView):
    model = Beautician
    template_name = "beautician-view.html"
    pk_url_kwarg = "bid"
    context_object_name = "beautician"

@method_decorator(signin_required,name="dispatch")
class DeleteBeauticianView(DeleteView):
    model = Beautician
    pk_url_kwarg = "bid"
    success_url = reverse_lazy("manage-beauticians")
    template_name = "confirm-delete.html"

    def form_valid(self, form):
        messages.success(self.request, "Beautician deleted successfully")
        return super(DeleteBeauticianView, self).form_valid(form)

@method_decorator(signin_required,name="dispatch")
class UpdateBeauticianView(UpdateView):
    model = Beautician
    template_name = "update-beautician.html"
    pk_url_kwarg = "bid"
    success_url = reverse_lazy("manage-beauticians")
    form_class = UpdateBeauticianForm

    def form_valid(self, form):
        messages.success(self.request, "Beautician  updated successfully")
        return super().form_valid(form)




#Timeslots
@method_decorator(signin_required,name="dispatch")
class ManageTimeslotsView(TemplateView):
    model = Timeslots
    template_name = "manage-timeslots.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timeslots"] = Timeslots.objects.all()
        return context

@method_decorator(signin_required,name="dispatch")
class AddTimeslotsView(CreateView):
    template_name = "add-timeslots.html"
    form_class = SlotAddForm
    success_url = reverse_lazy("manage-timeslots")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timeslots"] = Timeslots.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        #form = SlotAddForm(request.POST)
        start = request.POST.get('start')
        end = request.POST.get('end')
        date = request.POST.get('date')
        availability = request.POST.get('availability')
        status = request.POST.get('status')
        timeslot = (str(start) + ' - ' + str(end))
        Timeslots.objects.create(start_time=start, end_time=end, time=timeslot, status=status, date=date, availability=availability)
        messages.success(request, "Timeslot created Successfully")
        return redirect("manage-timeslots")


        # if form.is_valid:
        #     form.save()
        #     messages.success(request, "Timeslot created Successfully")
        #     return redirect("manage-timeslots")
        # else:
        #     messages.warning(request, "Timeslot creation failed")
        #     return redirect("manage-timeslots")


@method_decorator(signin_required,name="dispatch")
class DeleteTimeslotsView(DeleteView):
    model = Timeslots
    pk_url_kwarg = "tid"
    success_url = reverse_lazy("manage-timeslots")
    template_name = "confirm-delete.html"

    def form_valid(self, form):
        messages.success(self.request, "Timeslot deleted successfully")
        return super(DeleteTimeslotsView, self).form_valid(form)

@method_decorator(signin_required,name="dispatch")
class UpdateTimeslotView(UpdateView):
    model = Timeslots
    template_name = "update-timeslot.html"
    pk_url_kwarg = "tid"
    success_url = reverse_lazy("manage-timeslots")
    form_class = UpdateTimeslotForm

    def form_valid(self, form):
        messages.success(self.request, "Timeslot  updated successfully")
        return super().form_valid(form)

#Packages
@method_decorator(signin_required,name="dispatch")
class ManagePackagesView(TemplateView):
    model = Package
    template_name = "manage-packages.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["packages"] = Package.objects.all()
        return context

@method_decorator(signin_required,name="dispatch")
class AddPackagesView(FormView):
    template_name = "add-packages.html"
    form_class = PackageAddForm
    success_url = reverse_lazy("manage-packages")

    def post(self, request, *args, **kwargs):
        form = PackageAddForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, "Package created Successfully")
            return redirect("manage-packages")
        else:
            messages.warning(request, "Package creation failed")
            return redirect("manage-packages")

# @method_decorator(signin_required,name="dispatch")
# class DetailPackageView(DetailView):
#     model = Package
#     template_name = "view-package.html"
#     pk_url_kwarg = "pid"
#     context_object_name = "package"

def detail_package(request, id):
    package = Package.objects.get(id=id)
    pack = MyPackages.objects.filter(package__name=package.name)
    return render(request, "view-package.html", {'package':package, 'pack':pack})



@method_decorator(signin_required,name="dispatch")
class DeletePackageView(DeleteView):
    model = Package
    pk_url_kwarg = "pid"
    success_url = reverse_lazy("manage-packages")
    template_name = "confirm-delete.html"

    def form_valid(self, form):
        messages.success(self.request, "Package deleted successfully")
        return super(DeletePackageView, self).form_valid(form)

@method_decorator(signin_required,name="dispatch")
class UpdatePackageView(UpdateView):
    model = Package
    template_name = "update-package.html"
    pk_url_kwarg = "pid"
    success_url = reverse_lazy("manage-packages")
    form_class = UpdatePackageForm

    def form_valid(self, form):
        messages.success(self.request, "Package updated successfully")
        return super().form_valid(form)


#Giftcards
@method_decorator(signin_required,name="dispatch")
class ManageGiftCardsView(TemplateView):
    model = GiftCards
    template_name = "manage-giftcards.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["giftcards"] = GiftCards.objects.all()
        return context

@method_decorator(signin_required,name="dispatch")
class AddGiftCardsView(FormView):
    template_name = "add-giftcards.html"
    form_class = GiftCardAddForm
    success_url = reverse_lazy("manage-giftcards")

    def post(self, request, *args, **kwargs):
        form = GiftCardAddForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, "GiftCard created Successfully")
            return redirect("manage-giftcards")
        else:
            messages.warning(request, "GiftCard creation failed")
            return redirect("manage-giftcards")

# @method_decorator(signin_required,name="dispatch")
# class DetailGiftCardView(DetailView):
#     model = GiftCards
#     template_name = "view-giftcard.html"
#     pk_url_kwarg = "gid"
#     context_object_name = "giftcard"


#giftcard_detailfunction
def detail_giftcard(request, id):
    giftcard = GiftCards.objects.get(id=id)
    gift = MyGiftcards.objects.filter(giftcard__name=giftcard.name)
    return render(request, "view-giftcard.html", {'giftcard':giftcard, 'gift':gift})



@method_decorator(signin_required,name="dispatch")
class UpdateGiftCardView(UpdateView):
    model = GiftCards
    template_name = "update-giftcard.html"
    pk_url_kwarg = "gid"
    success_url = reverse_lazy("manage-giftcards")
    form_class = UpdateGiftCardForm

    def form_valid(self, form):
        messages.success(self.request, "GiftCards  updated successfully")
        return super().form_valid(form)

@method_decorator(signin_required,name="dispatch")
class DeleteGiftCardView(DeleteView):
    model = GiftCards
    template_name = "confirm-delete.html"
    pk_url_kwarg = "gid"
    success_url = reverse_lazy("manage-giftcards")

    def form_valid(self, form):
        messages.success(self.request, "GiftCard deleted successfully")
        return super(DeleteGiftCardView, self).form_valid(form)



#IntroOffers
@method_decorator(signin_required,name="dispatch")
class ManageIntroOffersView(TemplateView):
    model = IntroOffers
    template_name = "manage-introoffers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["introoffers"] = IntroOffers.objects.all()
        return context


@method_decorator(login_required,name="dispatch")
class AddIntroOffersView(FormView):
    template_name = "add-introoffer.html"
    form_class = IntroOfferAddForm
    success_url = reverse_lazy("manage-introoffers")

    def post(self, request, *args, **kwargs):
        form = IntroOfferAddForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, "IntroOffer created Successfully")
            return redirect("manage-introoffers")
        else:
            messages.warning(request, "IntroOffer creation failed")
            return redirect("manage-introoffers")


@method_decorator(login_required,name="dispatch")
class DetailIntroOfferView(DetailView):
    model = IntroOffers
    template_name = "view-introoffer.html"
    pk_url_kwarg = "iid"
    context_object_name = "introoffer"


@method_decorator(login_required,name="dispatch")
class UpdateIntroOfferView(UpdateView):
    model = IntroOffers
    template_name = "update-introoffer.html"
    pk_url_kwarg = "iid"
    success_url = reverse_lazy("manage-introoffers")
    form_class = UpdateIntroOfferForm

    def form_valid(self, form):
        messages.success(self.request, "Intro offer  updated successfully")
        return super().form_valid(form)


@method_decorator(login_required,name="dispatch")
class DeleteIntroOfferView(DeleteView):
    model = IntroOffers
    template_name = "confirm-delete.html"
    pk_url_kwarg = "iid"
    success_url = reverse_lazy("manage-introoffers")
    success_message = "Intro offers deleted"

    def form_valid(self, form):
        messages.success(self.request, "IntroOffer deleted successfully")
        return super(DeleteIntroOfferView, self).form_valid(form)
    


#Blogs
@method_decorator(login_required,name="dispatch")
class ManageBlogsView(TemplateView):
    model = Blogs
    template_name = "manage-blogs.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = Blogs.objects.all()
        return context

@method_decorator(login_required,name="dispatch")
class AddBlogsView(FormView):
    template_name = "add-blogs.html"
    form_class = BlogsAddForm
    success_url = reverse_lazy("manage-blogs")

    def post(self, request, *args, **kwargs):
        form = BlogsAddForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, "Blog created successfully")
            return redirect("manage-blogs")
        else:
            messages.warning(request, "Blog creation failed")
            return redirect("manage-blogs")

@method_decorator(login_required,name="dispatch")
class DetailBlogsView(DetailView):
    model = Blogs
    template_name = "view-blog.html"
    pk_url_kwarg = "bid"
    context_object_name = "blog"



@method_decorator(login_required,name="dispatch")
class UpdateBlogsView(UpdateView):
    model = Blogs
    template_name = "update-blog.html"
    pk_url_kwarg = "bid"
    success_url = reverse_lazy("manage-blogs")
    form_class = UpdateBlogsForm

    def form_valid(self, form):
        messages.success(self.request, "Blog updated successfully")
        return super().form_valid(form)

@method_decorator(login_required,name="dispatch")
class DeleteBlogsView(DeleteView):
    model = Blogs
    template_name = "confirm-delete.html"
    pk_url_kwarg = "bid"
    success_url = reverse_lazy("manage-blogs")

    def form_valid(self, form):
        messages.success(self.request, "Blog deleted successfully")
        return super(DeleteBlogsView, self).form_valid(form)
    


#Transactions
@method_decorator(login_required,name="dispatch")
class ManageTransactionsView(TemplateView):
    model = Transaction
    template_name = "manage-transactions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["transactions"] = Transaction.objects.all()
        return context
        

@method_decorator(login_required,name="dispatch")
class AddTransactionsView(FormView):
    template_name = "add-transactions.html"
    form_class = TransactionsAddForm
    success_url = reverse_lazy("manage-transactions")

    def post(self, request, *args, **kwargs):
        form = TransactionsAddForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Transaction created successfully")
            return redirect("manage-transactions")
        else:
            messages.warning(request, "Transaction creation failed")
            return redirect("manage-transactions")


#ContactUs

class ManageContactUs(TemplateView):
    model = ContactUs
    template_name = "manage-contactus.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contactus"] = ContactUs.objects.all()
        return context



class DetailContactUsView(DetailView):
    model = ContactUs
    template_name = "view-contactus.html"
    pk_url_kwarg = "cid"
    context_object_name = "contactus"


def detail_timeslot(request, id):
    timeslot = Timeslots.objects.get(id=id)
    booking = Booking.objects.filter(timeslot=timeslot)
    # package = MyPackages.objects.filter(package__timeslot=timeslot)
    return render(request, "view-timeslot.html", {"booking":booking})


class ManageUsers(TemplateView):
    model = User
    template_name = "manage-users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        return context


@method_decorator(signin_required,name="dispatch")
class EditPassword(UpdateView):
    model = User
    form_class = EditPassword
    template_name = "edit-password.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("manage-users")

    def form_valid(self, form):
        messages.success(self.request, "Password  Changed successfully")
        return super().form_valid(form)


def notifications(request):
    notifications = Notifications.objects.all()
    return render(request, "notifications.html", {"notifications":notifications})


def view_notification(request, id):
    notification = Notifications.objects.get(id=id)
    if notification.status == "unread":
            notification.status = "viewed"
            notification.save()
    else:
        pass
    return render(request, "view-notifications.html", {"notification":notification})


#Careers
@method_decorator(signin_required,name="dispatch")
class ManageCareersView(TemplateView):
    model = CareerOpenings
    template_name = "manage-careers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["careers"] = CareerOpenings.objects.all()
        return context


@method_decorator(signin_required,name="dispatch")
class AddCareersView(FormView):
    template_name = "add-careers.html"
    form_class = CareerAddForm
    success_url = reverse_lazy("manage-careers")

    def post(self, request, *args, **kwargs):
        form = CareerAddForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, "Career created Successfully")
            return redirect("manage-careers")
        else:
            messages.warning(request, "Career creation failed")
            return redirect("manage-careers")


def manage_bookings(request):
    bookings =Booking.objects.all().order_by('booking_date')
    return render(request, "manage-bookings.html", {"bookings":bookings})

def ManageBanner(request):
    banner = BannerImage.objects.get(id=1)
    context = {"banner":banner}
    return render(request, "manage-banner.html", context)



class UpdateBanner(UpdateView):
    model = BannerImage
    template_name = "update-banner.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("manage-banner")
    form_class = UpdateBannerForm

    def form_valid(self, form):
        messages.success(self.request, "Banner updated successfully")
        return super().form_valid(form)
    
#Booking Calendar
class BookingCalendar(TemplateView):
    template_name="calendar1.html"






    