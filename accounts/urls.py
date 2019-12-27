from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, TemplateView, PasswordResetView, PasswordResetDoneView,\
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView

from accounts import views

app_name = 'accounts'

urlpatterns = [

    path('home/', TemplateView.as_view(template_name='base.html'), name='home'),
    path('user_register/', views.UserCreationView.as_view(), name='registration'),
    path('student_register/', views.StudentCreationView.as_view(), name='student'),
    path('teacher_register/', views.TeacherCreationView.as_view(), name='teacher'),

    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('student/', views.StudentList.as_view(), name='student_list'),
    path('teacher/', views.TeacherList.as_view(), name='teacher_list'),

    path('student_detail/<int:pk>/', views.StudentDetail.as_view(), name='student_detail'),
    path('teacher_detail/<int:pk>/', views.TeacherDetail.as_view(), name='teacher_detail'),

    path('student_update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
    path('teacher_update/<int:pk>/', views.TeacherUpdateView.as_view(), name='teacher_update'),

    path('student_new_update/<int:pk>/', views.StudentUpdateNewView.as_view(), name='student_new_update'),

    path('student_delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('teacher_delete/<int:pk>/', views.TeacherDeleteView.as_view(), name='teacher_delete')

]
