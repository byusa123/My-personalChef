from django.conf.urls import url
from django.urls import path
from . import views
from .views import *
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.index, name='index'),
    # url('',indexView.as_view(), name='viewmeals'),

    # api start -----------#

    url(r'^api/meals/$', views.MealList.as_view()),
    url(r'^api/shedule/$', views.ScheduleList.as_view()),
    url(r'^api/booking/$', views.bookingList.as_view()),

    # api end ----------------#

    url('^add-meals/$', views.addMeals, name='add_meals'),
    url('^all-meals/$', views.all_meals, name='all_meals'),
    url('^update-meals/$', views.update_meal, name='update_meals'),
    url('^delete-meals/$', views.delete_meal, name='delete_meals'),


    url('^add-schedule/$', views.addSchedule, name='add_schedule'),



    url('^chef_detail/(\d+)$', views.chef_detail, name='chef_detail'),
    url(r'ratings/', include('star_ratings.urls', namespace='ratings')),
    url('^booking/(\d+)$', views.book, name='booking'),
    
    

]
