from django.urls import path,include
from account.views import UserApi,Login
from chat.views import ShowMessages

urlpatterns = [
    path('userapi/',UserApi.as_view()),
    path('login/',Login.as_view()),
    path('ShowMessages/<str:reciever>/',ShowMessages.as_view())
]