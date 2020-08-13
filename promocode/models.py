from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator
from random import randint
from string import ascii_uppercase
import uuid

# Create your models here.

TRANS_CHOICES = (
    ('CR' , 'RECRNTLY ADDED'),
    ('PE' , 'Pending'),
    ('PR' , 'Processing'),
    ('FL' , 'Failed')
)

PAYMENT_METHODS = (
    ('CR' , 'Credit Card'),
    ('CA' , 'Cash'),
    ('EW' , 'EWallet')
)



class Promo_code(models.Model):
   # id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
   # title = models.CharField(max_length=50)
    desc = models.CharField(max_length=200 , null = True)
    benefit = models.PositiveIntegerField( verbose_name=("Benefit in Cents"), null =True ,validators = [MinValueValidator(10) , MaxValueValidator(50)])
    quantity = models.PositiveIntegerField(validators = [MinValueValidator(1) , MaxValueValidator(5)], null =True)
    code = models.CharField(verbose_name = ("Code") , max_length=5, unique = True , default="")
    start_date = models.DateTimeField( default = timezone.now)
    end_date = models.DateTimeField(default = timezone.now)
    is_active = models.BooleanField(default = False)
    freq_of_use = models.PositiveIntegerField(verbose_name=("No. of time used") , default = 1)

    
    def generate_code():
        letters = string.ascii_uppercase
        code= ''.join(random.choice(letters) for i in range(5))
        return code
    
    
    def generate_code_benefit():
        benefit = randint(10,50)
        return benefit
    
    def generate_code_quantity():
        quantity = randint(3,5)
        return quantity

    def code_is_not_expire():
        now = datetime.now()
        return now < end_date

    
    


class Client(models.Model): 
    client_id = models.OneToOneField(User, verbose_name=("Client ID"),default = "", on_delete=models.CASCADE)
    username = models.CharField(max_length = 50)
    email =models.EmailField(max_length = 254) 
    


class Transactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Created_ts = models.DateTimeField( default = timezone.now)
    Promo_code_id = models.ForeignKey(Promo_code, on_delete=models.CASCADE , null = True)
    Amount = models.IntegerField(verbose_name=("Amount in Cents"),default = 0 , validators = [MinValueValidator(60)])
    client_id = models.ForeignKey(Client,default="", on_delete=models.CASCADE)
    state = models.CharField(choices=TRANS_CHOICES, max_length=2)
    payment_method = models.CharField(choices=PAYMENT_METHODS, max_length=2)
    #timestamp =  models.IntegerField()
    

    @property
    def Billed_amount():
        return Transaction.Amount - Promo_code.benefit 


class Promo_history(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_id = models.ForeignKey(Client,default="", on_delete=models.CASCADE)
    Promo_code_id = models.ForeignKey(Promo_code,default="", on_delete=models.CASCADE)
    Transaction_id  = models.ForeignKey(Transactions,default="", on_delete=models.CASCADE)
    client_freq_use = models.PositiveIntegerField(default = 0)
