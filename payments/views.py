import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

# API for creating charge
class CreateCharge(APIView):
    def post(self, request):     

        # The input parameters are amount and email of the customer   
        amount = request.data.get('amount', None)
        email = request.data.get('email', None)


        # Authenticating the stripe account
        stripe.api_key = settings.STRIPE_SECRET_KEY  

        if amount==None:
            return Response({"Please give a valid amount"}, status=status.HTTP_400_BAD_REQUEST)
        
        if email==None:
            return Response({"Please give a valid email address"}, status=status.HTTP_400_BAD_REQUEST)

        # Creating customer based on the email given
        customer = stripe.Customer.create(email=email)
     
             
        # Creating payment method for attaching it to customer
        card = stripe.PaymentMethod.create(
            type="card",
            card={
                "number": "378282246310005", # This particular card does not require 3D authentication
                "exp_month": 1,
                "exp_year": 2023,
                "cvc": "314",
            },
            )

        # Attaching the Payment Method to the customer created in above block of code
        cus_method = stripe.PaymentMethod.attach(
                card.id,
                customer=customer,
                )
       
       # Creating the Payment
        charge = stripe.PaymentIntent.create(
            payment_method_types=['card'],
            amount=int(amount)*100,
            currency='inr',
            confirm = True,
            payment_method = card,                       
            customer = customer           
            )  

        return Response(charge, status=status.HTTP_200_OK)

class CreateUncaptureCharge(APIView):
    def post(self, request):        
        # The input parameters are amount and email of the customer   
        amount = request.data.get('amount', None)
        email = request.data.get('email', None)

        # Authenticating the stripe account
        stripe.api_key = settings.STRIPE_SECRET_KEY  

        if amount==None:
            return Response({"Please give a valid amount"}, status=status.HTTP_400_BAD_REQUEST)
        
        if email==None:
            return Response({"Please give a valid email address"}, status=status.HTTP_400_BAD_REQUEST)

        # Creating customer based on the email given
        customer = stripe.Customer.create(email=email)
     
             
        # Creating payment method for attaching it to customer
        card = stripe.PaymentMethod.create(
            type="card",
            card={
                "number": "378282246310005", # This particular card does not require 3D authentication
                "exp_month": 1,
                "exp_year": 2023,
                "cvc": "314",
            },
            )

        # Attaching the Payment Method to the customer created in above block of code
        cus_method = stripe.PaymentMethod.attach(
                card.id,
                customer=customer,
                )
       
       # Creating the Payment, with capture_method set to manual it will create uncapture payment
        charge = stripe.PaymentIntent.create(
            payment_method_types=['card'],
            amount=int(amount)*100,
            currency='inr',
            confirm = True,
            payment_method = card,                       
            customer = customer, 
            capture_method = 'manual'         
            )  
        return Response(charge, status=status.HTTP_200_OK)

class CaptureCharge(APIView):
    def post(self, request):   
        # The input parameters charge ID for an uncaptured charge 
        charge = request.data.get('charge', None)

        # Authenticating the stripe account
        stripe.api_key = settings.STRIPE_SECRET_KEY 
      
        # Capturing the uncaptured payment
        capture =stripe.PaymentIntent.capture(charge)         

        return Response(capture, status=status.HTTP_200_OK)
class CreateRefund(APIView):
    def post(self, request):     
        # The input parameters charge ID for a captured charge    
        charge = request.data.get('charge', None)

        # Authenticating the stripe account
        stripe.api_key = settings.STRIPE_SECRET_KEY   
        
        # Initiating the refund of a sucessful payment
        refund = stripe.Refund.create(
        charge=charge,
        )    

        return Response(refund, status=status.HTTP_200_OK)

class GetCharges(APIView):
    def get(self, request):   

        # Authenticating the stripe account
        stripe.api_key = settings.STRIPE_SECRET_KEY 

        # Generating the list of charges that has been created yet
        charge_list = stripe.Charge.list()

        return Response(charge_list, status=status.HTTP_200_OK)