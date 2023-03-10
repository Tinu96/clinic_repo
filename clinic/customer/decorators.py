from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy




def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
            return redirect("home")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

# def login_required(fn):
#     def wrapper(request,*args,**kwargs):
#         if not request.user.is_authenticated:
#             messages.warning(request,"Please login to use the function! ")
#             return redirect("login")
#         else:
#             return fn(request,*args,**kwargs)
#     return wrapper



