from django.shortcuts import render
from django.http import HttpResponse
from .models import Promo_code
# Create your views here.



def promocode(request):
    queryset = Promo_code.objects.all()[0].benefit
    return HttpResponse(queryset)



def promo_code_coda( request ,code_redeem) :
    redeem = Promo_code.objects.get(benefit =code_redeem)
    return HttpResponse(redeem)

   