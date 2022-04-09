from django.urls import path
from admin import views
urlpatterns = [
    path('registercounter', views.registercounter, name='registercounter'),
    path('registermeter', views.registermeter, name='registermeter'),
    path('editcounter',views.editcounter,name='editcounter'),
    path('counter',views.displaycounter,name='counter'),
    path('reader',views.reader,name='reader'),
    path('customer',views.customer,name='customer'),
    path('admain',views.admain,name='admain')
    
]
