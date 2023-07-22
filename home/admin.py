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
# admin.site.register(StockListing)




