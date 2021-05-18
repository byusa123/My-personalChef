from django.conf.urls import url
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    url('^$', views.index, name='index'),
    # url('',indexView.as_view(), name='viewmeals'),

    # api start -----------#

    url(r'^api/meals/$', views.MealList.as_view()),
    url(r'^api/shedule/$', views.ScheduleList.as_view()),
    url(r'^api/booking/$', views.bookingList.as_view()),

    # api end ----------------#
    url('^add-meals/$', views.addMeals, name='add_meals'),

]
