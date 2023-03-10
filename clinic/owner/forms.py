from django import forms
from django.forms import ModelForm
from customer.models import *
from owner.models import *

class DateInput(forms.DateInput):
    input_type='date'


# class TimeInput(forms.TimeInput):
#     input_type='time'

class SlotAddForm(forms.ModelForm):
    class Meta:
        model=Timeslots
        fields='__all__'
        widgets={
            "date":DateInput,
            # "start_time":forms.TimeField,
            # "end_time":forms.TimeField
        }
        
        
class UpdateTimeslotForm(forms.ModelForm):
    class Meta:
        model=Timeslots
        fields= '__all__'
        

class CategoryAddForm(forms.ModelForm):
    class Meta:
        model=Categories
        fields=["category_name","description","status","image"]

class ServiceAddForm(forms.ModelForm):
    class Meta:
        model= Services
        fields = ['name', 'exclusive', 'category', 'image', 'duration', 'cost', 'striked_off_cost', 'description', 'detailed_description', 'detailed_information', 'beautician', 'status', 'timeslots']

class MembershipAddForm(forms.ModelForm):
    class Meta:
        model= Memberships
        fields ='__all__'

class BeauticianAddForm(forms.ModelForm):
    class Meta:
        model= Beautician
        fields ='__all__'


class UpdateServiceForm(forms.ModelForm):
    class Meta:
        model=Services
        fields = ['name', 'exclusive', 'category', 'image', 'duration', 'cost', 'striked_off_cost', 'description', 'detailed_description', 'detailed_information', 'beautician', 'status', 'timeslots']




class UpdateMembershipForm(forms.ModelForm):
    class Meta:
        model=Memberships
        fields=["name", "validity", "price","desc", "image", "status"]


class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model=Categories
        fields= '__all__'


class UpdateBeauticianForm(forms.ModelForm):
    class Meta:
        model=Beautician
        fields= '__all__'

class PackageAddForm(forms.ModelForm):
    class Meta:
        model= Package
        fields ='__all__'


class UpdatePackageForm(forms.ModelForm):
    class Meta:
        model=Package
        fields= '__all__'


class GiftCardAddForm(forms.ModelForm):
    class Meta:
        model= GiftCards
        fields ='__all__'


class UpdateGiftCardForm(forms.ModelForm):
    class Meta:
        model=GiftCards
        fields= '__all__'


class IntroOfferAddForm(forms.ModelForm):
    class Meta:
        model= IntroOffers
        fields ='__all__'


class UpdateIntroOfferForm(forms.ModelForm):
    class Meta:
        model=IntroOffers
        fields= '__all__'


class BlogsAddForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = "__all__"


class UpdateBlogsForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields= '__all__'


class TransactionsAddForm(forms.ModelForm):
    class Meta:
        model= Transaction
        fields ='__all__'

class EditPassword(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']


class CareerAddForm(forms.ModelForm):
    class Meta:
        model= CareerOpenings
        fields ='__all__'


class UpdateBannerForm(forms.ModelForm):
    class Meta:
        model=BannerImage
        fields= '__all__'
        
        
class AddonAddForm(forms.ModelForm):
    class Meta:
        model= AddOns
        exclude=['datetime','duration']