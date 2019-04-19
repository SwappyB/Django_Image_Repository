from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^sign_in/',views.sign_in,name='sign_in'),
    url(r'^sign_up/',views.sign_up,name='sign_up'),
    url(r'^profile/',views.profile,name='profile'),
]
