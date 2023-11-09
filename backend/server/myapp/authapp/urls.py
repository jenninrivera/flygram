from django.urls import path
from .views import ProfileCreate, check_user_authentication, LoginView, UserView, LogoutView


urlpatterns = [
    path('register', ProfileCreate.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    #path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist'),
    path('api/check-auth/', check_user_authentication, name='check_user_authentication'),
]