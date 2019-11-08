from django.urls import path

from .views import Account


urlpatterns = [
    path(r"", Account.as_view(), name="index"),
]
