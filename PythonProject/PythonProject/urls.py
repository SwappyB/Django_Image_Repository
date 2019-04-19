"""PythonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from home import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^sign_in/',auth_views.LoginView.as_view(template_name='home/sign_in.html'),name='sign_in'),
    url(r'^sign_out/',auth_views.LogoutView.as_view(template_name='home/sign_out.html'),name='sign_out'),
    url(r'^sign_up/',views.sign_up,name='sign_up'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^admin/', admin.site.urls),
]

#urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_DIR)
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
