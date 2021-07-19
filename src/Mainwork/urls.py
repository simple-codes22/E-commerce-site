from django.urls import path
from .views import main, dashboard, register, login, support

app_name = 'users'

urlpatterns = [
    path('', main),
    path('dash/<int:id>/<str:user_name>/', dashboard, name="dash"),
    path('new/', register, name="new"),
    path('login/', login, name="login"),
    path('support/', support, name="support")
]
