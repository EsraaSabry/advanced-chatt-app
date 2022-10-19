from django.urls import path

from chatty.chats.consumers import ChatConsumer

# websocket_urlpatterns = [

# ]


websocket_urlpatterns = [path("", ChatConsumer.as_asgi())]
