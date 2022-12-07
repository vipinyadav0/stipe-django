from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
import stripe
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8989'

@csrf_exempt
def create_checkout_session(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
        
        'price': "price_1M94ihSD7rISbdVtTgbwr9CO",

        'quantity': 1,
        }],
        mode='payment',
        success_url=YOUR_DOMAIN + '/success/',
        cancel_url=YOUR_DOMAIN + '/cancel/',
        )
    print(session)

    return JsonResponse({'id': session.id})

def home(request):
    return render(request,'checkout.html')

#success view
def success(request):
    return render(request,'success.html')

#cancel view
def cancel(request):
    return render(request,'cancel.html')