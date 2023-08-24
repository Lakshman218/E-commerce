from django.db import models
from Guest.models import tbl_UserReg
from Seller.models import tbl_Slrproduct
# Create your models here.
class Booking(models.Model):
    user=models.ForeignKey(tbl_UserReg,on_delete=models.CASCADE)
    booking_status=models.IntegerField(default=0)
    payment_status=models.IntegerField(default=0)
    booking_date=models.DateField(auto_now_add=True)

class Cart(models.Model):
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE)
    product=models.ForeignKey(tbl_Slrproduct,on_delete=models.CASCADE)
    cart_qty=models.IntegerField(default=1)