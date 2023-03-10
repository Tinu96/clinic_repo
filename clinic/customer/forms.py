from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from customer.models import *
from datetime import date
from django.contrib.admin.widgets import AdminDateWidget
from datetime import date

# from datetimewidget.widgets import DateTimeWidget

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {

            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),

        }



class UpdateBookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=["timeslot", "beautician"]

class CancelBookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=["status"]



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']




# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = ProfileManage
#         fields = ["name", "address", "contactno"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileManage
        fields = ['first_name','last_name', 'email', 'address', 'contactno', 'language', 'country', 'state', 'zip_code']
        widgets = {

            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "contactno": forms.TextInput(attrs={"class": "form-control"}),
            "language": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "state": forms.TextInput(attrs={"class": "form-control"}),
            "zip_code": forms.TextInput(attrs={"class": "form-control"}),


        }


class MyMemForm(forms.ModelForm):
    class Meta:
        model = MyMemberships
        fields = "__all__"

class DateInput(forms.DateInput):
    input_type='date'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = date.today()
        self.attrs.setdefault('min', today)

class Date_Form(forms.Form):
    date=forms.DateField(widget=DateInput)




class DateJob(forms.DateInput):
    input_type='date'


class Date_Career(forms.Form):
    date=forms.DateField(widget=DateJob)


# class Date_Form(forms.ModelForm):

#     class Meta:
#         model=Timeslots
#         fields=['date']
#         widgets={
#             "date":AdminDateWidget(attrs={'type': 'date'}),}


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = "__all__"