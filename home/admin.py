from django.contrib import admin

# Register your models here.
from.models import User
from.models import Broker
from.models import UserLoginHistory
from.models import UserSession
admin.site.register(User)
admin.site.register(Broker)
admin.site.register(UserLoginHistory)
admin.site.register(UserSession)


from .models import Site
from .models import WebhookResponse

admin.site.register(Site)
admin.site.register(WebhookResponse)