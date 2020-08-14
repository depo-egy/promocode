from .models import Promo_code
from .serializers import Promo_Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib import messages
import logging

@api_view(['GET'])
def promo_code_redeem_all(request) :
    """
    Return all of the promocodes generated.
    """
    queryset = Promo_code.objects.all()
    data = Promo_Serializer(queryset ,  many=True).data
    return Response({'data' : data})



@api_view(['GET'])
def promo_code(request , code_redeem) :
    """
    Args:-
     code_redeem: is the value of the code a user wants to redeem.
    
    Returns:
     The data of the specific code_redeem.
    """
    redeem = Promo_code.objects.get(code = code_redeem)
    data = Promo_Serializer(redeem).data
    return Response({'data' : data})

def messages():
    if promo_code.response.status_code == 200:
        messages.success(response , "Succeded Retreival")

logger = logging.getLogger(__name__)
def log_request(request):
    logger.debug()