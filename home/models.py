from django.utils import timezone  # Import 'timezone' from 'django.utils'

from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=150, null=True , blank=True)


    full_name=models.CharField( max_length=50,null=True,blank=True)
    email=models.EmailField( max_length=254,blank=True)
    Mobile_number=models.CharField( max_length=50,unique=True)
    Phone_code=models.CharField( max_length=50,null=True,blank=True)
    password=models.CharField( max_length=500,null=True,blank=True)
    confirm_password=models.CharField( max_length=50,null=True,blank=True)
    Country=models.CharField( max_length=50,null=True,blank=True)
    State=models.CharField( max_length=50,null=True,blank=True)
    forget_password_token = models.CharField(max_length=100,null=True)
    terms_of_service = models.BooleanField(default=False)
    secret_key = models.CharField(max_length=50, blank=True, null=True)
    ip_address_user = models.CharField(max_length=50, blank=True, null=True)  # Add this field


    objects=UserManager()
    USERNAME_FIELD='Mobile_number'
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
    advance_totp_security = models.BooleanField(default=False)  # New field

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
        return f'{self.user} - Product {self.book.id} - Quantity {self.quantity}'



# models.py
from django.db import models


class AdditionTask_main_time(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    result = models.IntegerField(blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, default='active', max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    schedule_time = models.DateTimeField()  # New field for schedule time

    def __str__(self):
        return f"{self.user}: {self.number1} + {self.number2} = {self.result} ({self.status})"




# models.py

from django.db import models

from django_celery_beat.models import PeriodicTask

class CustomPeriodicTask(PeriodicTask):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Add your custom fields here
    custom_field = models.CharField(max_length=255)
    
    # Override any methods if needed

    def save(self, *args, **kwargs):
        # Add custom logic before saving
        super().save(*args, **kwargs)
        # Add custom logic after saving

    def __str__(self):
        return f"{self.name} - {self.custom_field} - User: {self.user.username}"





class StrategyScheduleTaskResult(models.Model):
    strategy_name = models.CharField(max_length=255)
    broker_name = models.CharField(max_length=255)
    broker_profile = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_data = models.JSONField()
    result_data = models.JSONField()
    scheduled_time = models.DateTimeField(default=timezone.now)  # Set default value to current time


    def __str__(self):
        return f"{self.strategy_name} - {self.broker_name} - {self.user}"





class Blog(models.Model):
    FEATURED = 'featured'
    NEWEST = 'newest'
    PLATFORM_UPDATES = 'platform_updates'
    RESEARCH_INSIGHTS = 'research_insights'
    COMPANY_NEWS = 'company_news'

    CATEGORY_CHOICES = [
        (FEATURED, 'Featured'),
        (NEWEST, 'Newest'),
        (PLATFORM_UPDATES, 'Platform Updates'),
        (RESEARCH_INSIGHTS, 'Research Insights'),
        (COMPANY_NEWS, 'Company News'),
    ]

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    short_description = models.TextField()
    description = models.TextField()
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    blog_category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title
    







class WhatsAppTemplate(models.Model):
    title = models.CharField(max_length=255) 
    text = models.TextField()  
    url = models.URLField(max_length=200) 
    image = models.ImageField(upload_to='uploads/')  
    
    def __str__(self):
        return self.title




class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Wallet of {self.user.get_full_name()}'
    








class UserLoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=100)
    action = models.CharField(max_length=10)
    browser = models.CharField(max_length=100)  # Add browser field
    browser_version = models.CharField(max_length=100) 
    origin = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.user.username} - {self.login_time}"

class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, unique=True)
