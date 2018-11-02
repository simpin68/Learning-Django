from django.conf.urls import include, url
import HelloDJangoApp.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', HelloDJangoApp.views.index, name='index'),
    url(r'^home$', HelloDJangoApp.views.index, name='home'),
]