
from django.urls import path
from shope.views import index,detail,checkout,confirmation

urlpatterns = [
    path('',index, name='home'),
    path('<int:myId>',detail,name='detail'),
    path('checkout',checkout, name='checkout'),
    path('confirmation',confirmation, name='confirmation'),
]