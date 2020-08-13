from rest_framework import serializers
from .models import Promo_code

class Promo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Promo_code
        #fields = ('start_date', 'end_date', 'freq_of_use' )
        fields = '__all__' 

    