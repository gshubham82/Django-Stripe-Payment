from django.urls import path
from .views import *

urlpatterns = [
    
    # API for creating charge
    path('api/create_charge/', CreateCharge.as_view(), name='CreateCharge'), 

    # API for creating uncaptured charge
    path('api/create_uncapture_charge/', CreateUncaptureCharge.as_view(), name='CreateUncaptureCharge'),

    # API for capturing the uncaptured charge
    path('api/capture_charge/', CaptureCharge.as_view(), name='CaptureCharge'),

    # API for creating refund of a successful charge
    path('api/create_refund/', CreateRefund.as_view(), name='CreateRefund'),

    # API get list of charges
    path('api/get_charges/', GetCharges.as_view(), name='GetCharges')
]
