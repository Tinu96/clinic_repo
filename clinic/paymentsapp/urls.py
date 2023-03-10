from django.urls import path
from . import views

urlpatterns = [
    path('checkout',views.CheckoutView.as_view()),
    path('create-checkout-session/',views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('success/',views.SuccessView.as_view(), name='success'),
    path('cancel/',views.CancelView.as_view(), name='cancel'),
    path('webhooks/stripe/',views.stripe_webhook,name='stripe-webhook'),
]
