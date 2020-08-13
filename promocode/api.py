from .models import Promo_code
from .serializers import Promo_Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging

@api_view(['GET'])
def promo_code_redeem_all(request , code) :
    queryset = Promo_code.objects.all()
    data = Promo_Serializer(queryset ,  many=True).data
    return Response({'data' : data})



@api_view(['GET'])
def promo_code(request , code_redeem) :
    redeem = Promo_code.objects.get(code = code_redeem)
    data = Promo_Serializer(redeem).data
    return Response({'data' : data})



logger = logging.getLogger(__name__)
def log_request(request):
    logger.debug()