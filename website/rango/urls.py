from django.conf.urls import patterns , url
from rango import views

urlpatterns = pattern('',
                      url(r'^$', view.index, name = 'index'),
                      url(r'^about/$',view.about, name = 'about'
                      
                      )
