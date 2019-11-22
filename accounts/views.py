from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic

from accounts.models import Teacher, Student, User
from accounts.forms import StudentForm, TeacherForm


class UserCreationView(generic.CreateView):
    """Create accounts using generic view."""

    template_name = 'accounts/register.html'
    model = User
    fields = (
        'first_name', 'last_name', 'email', 'username', 'password', 'profile_picture', 
        'birth_date', 'age', 'gender', 'phone', 'address', 'city', 'state',
        'country', 'zip_code', 'joining_date', 'leaving_date', 'is_student', 'is_staff', 'is_superuser'
    )
    student_success_url = reverse_lazy('accounts:student')
    teacher_success_url = reverse_lazy('accounts:teacher')

    def form_valid(self, form):
        user = User.objects.create_user(**form.cleaned_data)
        if user.is_student is True: return redirect(self.student_success_url)
        else: return redirect(self.teacher_success_url)
        

    def test_func(self):
        """
        is testing as super accounts

        :return: self.request.accounts.is_superuser
        """
        return self.request.user.is_superuser


class StudentCreationView(generic.CreateView):
    """Create student using generic view."""

    template_name = 'accounts/student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('accounts:student_list')
    
    def form_valid(self, form):
        Student.objects.create(**form.cleaned_data)
        messages.success(self.request, 'Successfully Added student')
        return redirect(self.success_url)
        

class TeacherCreationView(generic.CreateView):
    """Create teacher using generic view."""

    template_name = 'accounts/teacher.html'
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('accounts:teacher_list')

    def form_valid(self, form):
        poped_subject = form.cleaned_data.pop('subject')
        print(poped_subject)
        teacher = Teacher.objects.create(**form.cleaned_data)
        for subject in poped_subject:
            teacher.subject.add(subject)
        messages.success(self.request, 'Successfully Added Teacher')
        return redirect(self.success_url)


class StudentList(generic.ListView):
    """
    StudentList is using to the list Student using ListView

    """
    model = Student
    template_name = 'accounts/student_list.html'
    context_object_name = 'students'


class TeacherList(generic.ListView):
    """
    TeacherList is using to the list Teacher using ListView

    """
    model = Teacher
    template_name = 'accounts/teacher_list.html'
    context_object_name = 'teachers_profile'


class StudentDetail(generic.DetailView):
    """
    StudentDetail is using to display the student profile

    """
    model = Student
    template_name = 'accounts/student_detail.html'
    context_object_name = 'student_profile'


class TeacherDetail(generic.DetailView):
    """
    TeacherDetail is using to display the teacher profile

    """
    model = Teacher
    template_name = 'accounts/teacher_profile.html'
    context_object_name = 'teacher_profile'


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    Using UpdateView to update the user details

    """
    model = User
    fields = ('first_name', 'last_name', 'username', 'email', 'password', 'is_superuser', 'is_staff')
    template_name = 'login/user_update.html'
    success_url = reverse_lazy('login:home')

    def test_func(self):
        """
        This test function is using to user is superuser

        :return: self.request.user.is_superuser
        """
        return self.request.user.is_superuser


class StudentDeleteView(generic.DeleteView):
    """
    Delete user from the user list

    """
    model = Student
    template_name = 'accounts/test_delete.html'
    success_url = reverse_lazy('login:student_list')


class TeacherDeleteView(generic.DeleteView):
    """
    Delete user from the user list

    """
    model = Teacher
    template_name = 'accounts/test_delete.html'
    success_url = reverse_lazy('login:student_list')
