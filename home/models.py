from django.utils import timezone  # Import 'timezone' from 'django.utils'

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
    def __str__(self):  
        return f"{self.user.email}"
    




class Subscriber(models.Model):
    email = models.EmailField(max_length=254)
    subscribed_at = models.DateTimeField()

from django.db import models




class ZerodhaAPIConfig(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app_name = models.CharField(max_length=100)
    api_key = models.TextField()  # Change from CharField to TextField
    secret_key = models.TextField()  # Change from CharField to TextField
    brokers = models.TextField(default='zerodha')  # Set default value to 'zerodha'
    access_token = models.TextField()  # Change from CharField to TextField
    api_added_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user}"


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
    


class my_strategies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    strategy_name = models.CharField(max_length=100)
    strategy_notes = models.CharField(max_length=256)
    trading_positions = models.TextField()
    def __str__(self):
        return self.strategy_name




from django.db import models

class AdminAPIIntegrations(models.Model):
    broker_name = models.CharField(max_length=100)
    app_name = models.CharField(max_length=100)
    api_key = models.TextField()  # Changed to TextField
    api_secret_key = models.TextField()  # Changed to TextField
    access_token = models.TextField()  # Changed to TextField
    api_added_at = models.DateTimeField()
    active_api = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.broker_name} - {self.app_name}"




class All_brokers_api_name(models.Model):
    broker_name=models.CharField(max_length=50)






class Broker(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    broker_name = models.CharField(max_length=255)
    trading_platform = models.CharField(max_length=255)
    logging_id = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    totp_key = models.CharField(max_length=255)
    fa_pin = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=15)
    api_key = models.CharField(max_length=255)
    api_secret = models.CharField(max_length=255)
    app_name = models.CharField(max_length=255)
    enctoken=models.TextField()
    active_api = models.BooleanField(default=False)
    added_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"{self.broker_name} - {self.user} - {self.app_name}"
    








class PopupContent(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='popup_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
            return self.title



from django.utils import timezone

class Book(models.Model):
    TRADING = 'Trading'
    OPTION_TRADING = 'Option Trading'
    INVESTMENT = 'Investment'
    TECHNICAL_ANALYSIS = 'Technical Analysis'

    CATEGORY_CHOICES = [
        (TRADING, 'Trading'),
        (OPTION_TRADING, 'Option Trading'),
        (INVESTMENT, 'Investment'),
        (TECHNICAL_ANALYSIS, 'Technical Analysis'),
    ]

    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Hindi', 'Hindi'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='book_images/', blank=True)  # Set your desired upload path
    page = models.IntegerField()
    read_sample = models.CharField(max_length=8000)
    book_category = models.CharField(
        max_length=255,
        choices=CATEGORY_CHOICES,
        default=TRADING,  # Set the default category if needed
    )
    language = models.CharField(
        max_length=255,
        choices=LANGUAGE_CHOICES,
        default='English',  # Set the default language if needed
    )
    author = models.CharField(max_length=255, default='') 
    publish_date = models.DateField(null=True, blank=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  
    updated_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title







class BookCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE) # Adjust this based on your product ID field type
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user.username} - Product {self.book.id} - Quantity {self.quantity}'
