from django.shortcuts import render
from customer.models import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from customer.urls import *
from django.views.generic import CreateView,TemplateView
from django.views import View
import stripe
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key=settings.STRIPE_SECRET_KEY 
class CheckoutView(TemplateView):
    template_name='checkout.html'
    def get_context_data(self, **kwargs):
        product=Product.objects.get(name="Men Typography Round Neck White T-Shirt")
        context = super().get_context_data(**kwargs)
        context["STRIPE_PUBLIC_KEY"] = settings.STRIPE_PUBLISHABLE_KEY
        context["product"]=product
        return context
class SuccessView(TemplateView):
    template_name='success.html' 

class CancelView(TemplateView):
    template_name='cancel.html'   

class CreateCheckoutSessionView(View):

    def post(self,request,*args,**kwargs):
        YOUR_DOMAIN="http://127.0.0.1:8000"
        cart = ServiceCart.objects.filter(user=request.user,status="in-cart")
        subtotal=0
        total=10
        products=''
        user_id=request.user.id

        for c in cart:
            subtotal+=c.cost
            total+=c.cost
            name=c.service.name
            products+=name
            products+=','

        grand_total=total*100
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                   'price_data':{
                    'currency':'usd',
                    'unit_amount':grand_total,
                    'product_data':{
                        'name':products
                    },
                   },
                   'quantity':1,
                },
            ],
            metadata={
           'user':user_id

            },
            mode='payment',
            success_url=YOUR_DOMAIN+'/payments' + '/success/',
            cancel_url=YOUR_DOMAIN +'/payments' +  '/cancel/',
        )
        return JsonResponse({
            'id':checkout_session.id
        })



@csrf_exempt
def stripe_webhook(request):
  payload = request.body

  # For now, you only need to print out the webhook payload so you can see
  # the structure.
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, 'whsec_fd8cff64bd1cf0dde619025e9731b468eb9b02dbebfc02a38159ea88b3832404'
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
    # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
    session = stripe.checkout.Session.retrieve(
      event['data']['object']['id'],
      expand=['line_items'],
    )

    line_items = session.line_items
    # Fulfill the purchase...
    user_id=session['metadata']['user']
    user=User.objects.get(id=user_id)
    cart=ServiceCart.objects.filter(user=user,status="in-cart")
    tax=10
    for c in cart:
      # total+=(c.product.cost*c.quantity)
      # seller=c.service.user
      order=ServiceOrder.objects.filter(user=user,status="order-placed")
      if order:
        order=ServiceOrder.objects.get(user=user,status="order-placed")
        cur_cost=(order.cost)+(c.cost)
        order.cart.add(c)
        order.cost=cur_cost
        order.save()
        c.status="booked"
        c.save()
      else:
         new=ServiceOrder.objects.create(user=user)
         new.cart.add(c)
         c.status="booked"
         c.save()
         new.cost=(c.cost)+tax
         new.save()
    # new_order.cost=total
    # new_order.save()
    print("Order creation successfull")
  # Passed signature verification
  return HttpResponse(status=200)
