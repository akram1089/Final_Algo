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

# from.models import StockListing



admin.site.register(User)
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

# admin.site.register(StockListing)




