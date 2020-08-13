from django.urls import path
from . import views
from . import api

#from rest_framework.authtoken.views import obtain_auth_token
app_name = 'promocode'
urlpatterns = [
    path('promocode',views.promocode , name='some_view'),
    path('promocode/<int:benefit>',views.promo_code_coda , name='redeem_view'),
    path('api/promocode',api.promo_code_redeem_all , name='promo_code_redeem'),
    path('api/promocode/<str:code_redeem>',api.promo_code , name='promo_code_redeem'),
    
]


#path('api/promocode/<int:id>',api.promo_code , name='promo_code_redeem'),