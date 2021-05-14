from django.conf.urls import url
from . import views

urlpatterns=[
    # url('^$',views.index,name = 'index'),
    url(r'^api/meals/$', views.MealList.as_view()),
    url(r'^api/shedule/$', views.ScheduleList.as_view()),
    url(r'^api/booking/$', views.bookingList.as_view()),
]