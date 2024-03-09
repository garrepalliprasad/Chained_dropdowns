from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('get-mandals/',views.mandals,name='get-mandals'),
    path('get-villages/',views.villages,name='get-villages'),
]