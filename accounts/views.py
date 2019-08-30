from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic

from accounts.models import Teacher, User


class UserCreationView(generic.CreateView):
    """Create accounts using generic view."""

    template_name = 'accounts/register.html'
    model = User
    fields = (
        'username', 'first_name', 'last_name', 'email',
        'password', 'profile_picture', 'birth_date',
        'age', 'gender', 'phone','address', 'city', 'state',
        'country', 'zip_code', 'is_student', 'is_teacher'
    )
    success_url = reverse_lazy('accounts:home')

    def form_valid(self, form):
        User.objects.create_user(**form.cleaned_data)
        return redirect(self.success_url)

    def test_func(self):
        """
        is testing as super accounts

        :return: self.request.accounts.is_superuser
        """
        return self.request.user.is_superuser


class UserDetailView(generic.DetailView):
    """
    UserDetailView is gives detail of user using DetailView.
    """
    model = User
    template_name = 'accounts/user_detail.html'
    context_object_name = 'user_profile'


class UserListView(generic.ListView):
    """
    UserListView is using to the list users using ListView.

    """
    model = User
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                     generic.UpdateView):
    """
    Using UpdateView to update the user details

    """
    model = User
    fields = (
        'first_name', 'last_name', 'username', 'email',
        'password', 'is_superuser', 'is_staff'
    )
    template_name = 'accounts/user_update.html'
    success_url = reverse_lazy('accounts:home')

    def test_func(self):
        """
        This test function is using to user is superuser

        :return: self.request.user.is_superuser
        """
        return self.request.user.is_superuser


class UserDeleteView(generic.DeleteView):
    """
    Delete user from the user list.
    """
    model = User
    template_name = 'accounts/user_delete.html'
    success_url = reverse_lazy('accounts:user_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
