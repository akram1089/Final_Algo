from django.urls import path,re_path

from .consumers import NumberGenerator

# from .consumers import ZerodhaAPIConsumer,BrokerDetailsConsumer


ws_urlpatterns = [
    path(r'ws/', NumberGenerator.as_asgi(), name='number-generator'),
    # path(r"ws/zerodha/", ZerodhaAPIConsumer.as_asgi()),
    # re_path(r'ws/broker-details/$', BrokerDetailsConsumer.as_asgi()),

]
