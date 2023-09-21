from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.db import models
class User(AbstractUser):
    username=None
    full_name=models.CharField( max_length=50,null=True,blank=True)
    email=models.EmailField( max_length=254,unique=True)
    Mobile_number=models.CharField( max_length=50,null=True,blank=True)
    Phone_code=models.CharField( max_length=50,null=True,blank=True)
    password=models.CharField( max_length=500,null=True,blank=True)
    confirm_password=models.CharField( max_length=50,null=True,blank=True)
    Country=models.CharField( max_length=50,null=True,blank=True)
    State=models.CharField( max_length=50,null=True,blank=True)
    forget_password_token = models.CharField(max_length=100,null=True)
    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]







class ChartData(models.Model):
    data_json = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at)



class Top_Gainer(models.Model):
 top_gainers = models.TextField()

class Top_Loser(models.Model):
 top_losers = models.TextField()



class TradedVolume(models.Model):
    trade_volume = models.TextField()
    def __str__(self):
        return self.trade_volume




class Traded_Volume(models.Model):
    symbol = models.CharField(max_length=50)
    trade_volume = models.CharField(max_length=50)

    def __str__(self):
        return self.symbol


class SecurityBan(models.Model):
    symbol_name = models.CharField(max_length=255)
    current_percent = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.symbol_name
class Entrance(models.Model):
    Entrance_symbol_name = models.CharField(max_length=255)
    Entrance_precent = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Entrance_symbol_name

from django.db import models

# class StockListing(models.Model):
#     sme_records = models.TextField()
#     equity_records = models.TextField()

#     def __str__(self):
#         return f"Stock Listing {self.pk}"


from django.db import models

class StockData(models.Model):
    api_response = models.TextField()

    def __str__(self):
        return str(self.pk)
from django.db import models

class Stock_Low_Data(models.Model):
    api_response_low = models.TextField()

    def __str__(self):
        return str(self.pk)
    
class Only_buyers(models.Model):
    api_response_buyers = models.TextField()

    def __str__(self):
        return str(self.pk)



# models.py

from django.db import models



class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol_name = models.CharField(max_length=100)
    prev_high = models.CharField(max_length=100)
    today_low = models.CharField(max_length=100)
    today_high = models.CharField(max_length=100)
    change_value = models.CharField(max_length=100)
    change_percent = models.CharField(max_length=100)
    prev_close = models.CharField(max_length=100)
    today_volume = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.full_name} - {self.symbol_name}"


from django.db import models

class Border_FetchedData(models.Model):
    data = models.TextField()



from django.db import models

class All_stock_underlying(models.Model):
    data = models.TextField()


from django.db import models

class VolumeGainer(models.Model):
    data_json = models.TextField()


from django.db import models

class MostActiveStock(models.Model):
    data_json = models.TextField()

    def __str__(self):
        return f"Most Active Stock (ID: {self.id})"



from django.db import models

class MostSpreadStock(models.Model):
    data_json = models.TextField()


class ContactUs(models.Model):
    Contact_first_name = models.CharField(max_length=100)
    Contact_last_name = models.CharField(max_length=100)
    Contact_email = models.CharField(max_length=100)
    Contact_phone_number = models.CharField(max_length=100)
    Contact_messages = models.TextField(max_length=300)

    def __str__(self):  # Use double underscores here
        return self.Contact_first_name



class Customer_feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ui_exp = models.CharField( max_length=50)
    helpful_exp = models.CharField(max_length=50,)
    rating_scale = models.CharField(max_length=50)
    suggestion = models.TextField(max_length=300)
    frnd_recommend = models.BooleanField(default=True)
    def _str_(self):
        return self.user.username