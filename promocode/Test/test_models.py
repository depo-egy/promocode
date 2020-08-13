from django.test import TestCase
from promocode import models.Promo_code , models.Transactions
import datetime
# Create your tests here.


class Promo_code_test(TestCase):
    code_test = Promo_code.generate_code()
    day_test = Promo_code.code_is_not_expire()
    benefit_test = Promo_code.generate_benefit()
    quantity_test = Promo_code.generate_code_quantity()
    not_expire = Promo_code.code_is_not_expire()
    def promo_test = Promo_code.objects.create(desc="any desc", benefit= benefit_test , quantity = quantity_test , code = code_test,
    start_date = datetime.now() , end_date = day_test , is_active = True , freq_of_use = 1)
   
    def test_check(self):
        self.assertTrue(Promo_code.is_active)
        self.assertEqual(Promo_code.start_date , datetime.now())
        self.assertIsNotNone(Promo_code.code )
        self.assertIsNotNone(Promo_code.code )
        self.assertTrue(day_test , end_date)



