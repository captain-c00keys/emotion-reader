"""emotionreader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from emotionreader.views import HomeView, AboutView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^face_verification/', include('emotion_authentication.urls')),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/', AboutView.as_view(), name='about'),
    url(r'^profile/', include('emotion_profile.urls')),
    url(r'^journal/', include('emotion_journal.urls')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^emotions/', include('emotion_emotions.urls'))
]

if settings.DEBUG:  # pragma: nocover
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
