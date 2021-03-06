from django.db import models
from django.utils import timezone
import string, random
# import random

# id genarator
def id_genarator(length=11, var= string.digits):
        return ''.join(random.choice(var) for _ in range(length))

# date limit genarator
def limit_day():
    var = timezone.now() + timezone.timedelta(days=3)
    return var
def next_day():
    num = 0
    while num < 22:
        var = timezone.now() + timezone.timedelta(days=num)
        if var != timezone.now() + timezone.timedelta(days=22):
            num += 1
            return num
        elif var == timezone.now() + timezone.timedelta(days=22):
            return 100

    
# client package information
class User_Package_Detail(models.Model):
    choice = {
        ('active', 'active'),
        ('pending', 'pending'),
        ('delayed', 'delayed'),
        ('waiting comfirmation', 'waiting comfirmation'),
    }
    order_id = models.CharField(unique=True ,blank=True, null=True, max_length=11, default=id_genarator)
    order_time = models.DateTimeField(default=timezone.now)

    order_image = models.ImageField(upload_to='image', default='image/homepage.svg')
    reciver_name = models.CharField(max_length=50)
    content = models.CharField(max_length=100, default='iphone12(black), louis vuttion designer bag, sealed 700 x 700 envelop')

    quantity = models.CharField(max_length=20, default='1')
    weight = models.CharField(max_length=20, default='30g')
    
    status = models.CharField(max_length=21, choices=choice ,default=3)
    message = models.CharField(max_length=500, default='This Parcel Is On Transit To Manilla, Phillipines.')

    def __str__(self) -> str:
        return self.reciver_name