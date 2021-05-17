from django.conf.urls import url
from . import views
from .views import *

urlpatterns=[
    url('^$',views.index,name = 'index'),
    # url('',indexView.as_view(), name='viewmeals'),
    url(r'^api/meals/$', views.MealList.as_view()),
    url(r'^api/shedule/$', views.ScheduleList.as_view()),
    url(r'^api/booking/$', views.bookingList.as_view()),
] 
