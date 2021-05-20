from django.conf.urls import url
from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.index, name='index'),
    # url('',indexView.as_view(), name='viewmeals'),

    # api start -----------#

    url(r'^api/meals/$', views.MealList.as_view()),
    url(r'^api/shedule/$', views.ScheduleList.as_view()),
    url(r'^api/booking/$', views.bookingList.as_view()),
<<<<<<< HEAD
] 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
=======

    # api end ----------------#
    url('^add-meals/$', views.addMeals, name='add_meals'),

]
>>>>>>> 298866470486bbf3d48eff9109e045a9d2c2d5be
