from django.urls import path

from accounts.views import login, registration

urlpatterns = [
    path('registration/' ,registration ),
    path('login/', login)
]