'''
cardcollectordb URL Configuration
'''
from django.contrib import admin
from django.urls import include, path

from account.views import SignUp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls'), name='account'),
    path('signup', SignUp.as_view(), name='signup'),
]
