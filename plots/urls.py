from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'plots'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.test, name='test'),
    #path('', views.choose_data, name='choose_data'),
    path('<int:image_id>/getimage', views.getimage, name='getimage'),
    path('<int:image_id>/inter', views.inter, name='inter'),
    path('<int:image_id>/next_image', views.next_image, name='next_image'),
    path('<int:image_id>/previous_image', views.previous_image, name='previous_image'),
    url(r'^getimage/$', views.getimage, name="getimage"), #, name='getimage'
    url(r'^inter/$', views.inter, name='inter'), #, name='getimage'
    url(r'^test/$', views.test, name='test'), #, name='getimage'
]

