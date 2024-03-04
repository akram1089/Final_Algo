from django.contrib import admin

# Register your models here.
from.models import User

from.models import ChartData

from.models import Top_Gainer
from.models import Top_Loser
from.models import TradedVolume
from.models import SecurityBan
from.models import StockData
from.models import Stock_Low_Data
from.models import Only_buyers
from.models import Watchlist
from.models import Border_FetchedData
from.models import All_stock_underlying
from.models import VolumeGainer
from.models import MostActiveStock
from.models import MostSpreadStock
from.models import ContactUs
from.models import Customer_feedback
from.models import Subscriber
from.models import ZerodhaAPIConfig
from.models import Note
from.models import my_strategies
from.models import AdminAPIIntegrations
from.models import All_brokers_api_name
from.models import Broker
from.models import PopupContent
from.models import Book
from.models import BookCart
from.models import AdditionTask_main_time
from.models import WhatsAppTemplate
from.models import Wallet

# from.models import StockListing



admin.site.register(Wallet)
admin.site.register(ChartData)


admin.site.register(Top_Gainer)
admin.site.register(Top_Loser)
admin.site.register(TradedVolume)
admin.site.register(SecurityBan)
admin.site.register(StockData)
admin.site.register(Stock_Low_Data)
admin.site.register(Only_buyers)
admin.site.register(Watchlist)
admin.site.register(Border_FetchedData)
admin.site.register(All_stock_underlying)
admin.site.register(VolumeGainer)
admin.site.register(MostActiveStock)
admin.site.register(MostSpreadStock)
admin.site.register(ContactUs)
admin.site.register(Customer_feedback)
admin.site.register(Subscriber)
admin.site.register(ZerodhaAPIConfig)
admin.site.register(Note)
admin.site.register(my_strategies)
admin.site.register(AdminAPIIntegrations)
admin.site.register(All_brokers_api_name)
admin.site.register(Broker)
admin.site.register(PopupContent)
admin.site.register(Book)
admin.site.register(BookCart)
admin.site.register(AdditionTask_main_time)

# admin.site.register(StockListing)




# Register the custom UserAdmin
admin.site.register(User)
admin.site.register(WhatsAppTemplate)



# admin.py

from django.contrib import admin
from .models import CustomPeriodicTask

@admin.register(CustomPeriodicTask)
class CustomPeriodicTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'custom_field', 'user', 'enabled', 'last_run_at')

    # Customize other admin options as needed



from django.contrib import admin
from .models import StrategyScheduleTaskResult

@admin.register(StrategyScheduleTaskResult)
class StrategyScheduleTaskResultAdmin(admin.ModelAdmin):
    list_display = ('strategy_name', 'broker_name', 'user', 'id')  # Customize the fields you want to display in the admin list
    search_fields = ('strategy_name', 'broker_name', 'user__username')  # Add fields for searching in the admin

    # You can customize the admin further if needed
    # For example, adding list_filter, readonly_fields, etc.



from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'blog_category')
    list_filter = ('blog_category',)
    search_fields = ('title', 'author')
    prepopulated_fields = {'description': ('short_description',)}



