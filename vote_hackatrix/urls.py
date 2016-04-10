"""vote_hackatrix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from ideas import views
from ideas.views import CustomObtainAuthToken, GetId
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/authenticate/', CustomObtainAuthToken.as_view()),
    url(r'^api/token-auth/$', obtain_jwt_token),
    url(r'^api/token-auth/get_id/$', GetId.as_view()),
    url(r'^api/token-auth/refresh/$', refresh_jwt_token),
    url(r'api/ideas/$',  views.idea_list, name='idea_list'),
    url(r'api/results/$', views.results, name='results'),
    url(r'api/idea/(?P<pk>\d+)/$', views.idea, name='idea'),
    url(r'api/idea/(?P<pk>\d+)/vote/$', views.vote, name='vote'),
    url(r'api/docs/', include('rest_framework_swagger.urls')),
]
