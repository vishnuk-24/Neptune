from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, TemplateView, PasswordResetView, PasswordResetDoneView,\
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView

from accounts import views

app_name = 'accounts'

urlpatterns = [

    path('home/', TemplateView.as_view(template_name='base.html'), name='home'),

    path('create/', views.UserCreationView.as_view(), name='usercreation'),

    path('users/', views.UserListView.as_view(), name='user_list'),

    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),

    path('user_update/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),

    path('user_delete/<int:pk>/', views.UserDeleteView.as_view(), name='delete_user'),

    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('password-reset/', PasswordResetView.as_view(
        template_name='accounts/password-reset.html',
        email_template_name='accounts/password_reset_email.html',
        success_url=reverse_lazy('accounts:password_reset_done')), name='password_reset'
        ),

    path('reset-done/', PasswordResetDoneView.as_view(
        template_name='accounts/password-reset-done.html'),
        name='password_reset_done'
        ),

    path('reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='accounts/password-reset-confirm.html',
        success_url=reverse_lazy('accounts:password_reset_complete')), name='password_confirm'
        ),

    path('reset-complete/', PasswordResetCompleteView.as_view(
        template_name='accounts/password-reset-complete.html'),
        name='password_reset_complete'
        ),

    path('password-change/', PasswordChangeView.as_view(
        template_name='accounts/password_change_form.html',
        success_url=reverse_lazy('accounts:password_change_done')), name='password_change'
        ),

    path('password-change/done/', PasswordChangeDoneView.as_view(
        template_name='accounts/password-reset-complete.html'),
        name='password_change_done'
        ),
]
