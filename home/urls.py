from django.urls import path, include
from . import views
app_name = "home"


urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path('api/v1/', include('home.api.v1.urls'), name='api-index')
]
