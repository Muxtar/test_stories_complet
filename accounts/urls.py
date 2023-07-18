from django.urls import path
from django.contrib.auth.views import (
                                        PasswordResetView,
                                        PasswordResetDoneView, 
                                        PasswordResetConfirmView,
                                        PasswordResetCompleteView
                                        )
from accounts.views import (
                            login, 
                            register, 
                            logout, 
                            profile,
                            change_password,
                            MyPasswordResetView,
                            MyPasswordResetConfirmView

)

urlpatterns = [
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),
    path('profile/', profile, name='profile'),
    path('register/', register, name = 'register'),
    path('change-password', change_password, name = 'change_password'),
    
    path('password_reset/', MyPasswordResetView.as_view(), name='forget_password'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]