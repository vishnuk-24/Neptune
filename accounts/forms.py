"""Django form for model."""

from django import forms
from django.db.models import Q

from accounts.models import Student, Teacher, User


class StudentForm(forms.ModelForm):
    """Restrict one to one user model drop down list."""

    class Meta:
        model = Student
        fields = ('user', 'standard', 'division', 'rollnumber', 'admission_number', 'register_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(Q(teacher__isnull=True) & Q(student__isnull=True))


class TeacherForm(forms.ModelForm):
    """Restrict one to one user model drop down list."""

    class Meta:
        model = Teacher
        fields = ('user', 'qualification', 'total_experience', 'subject', 'remarks')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(Q(teacher__isnull=True) & Q(student__isnull=True))


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password', 'profile_picture',
            'birth_date', 'age', 'gender', 'phone', 'address', 'city', 'state',
            'country', 'zip_code', 'joining_date', 'leaving_date', 'is_student', 'is_staff', 'is_superuser'
        )


# class ProductCreateView(LoginRequiredMixin, CreateView):
#     model = Product
#     template_name = 'brand/product-create.html'
#     fields = '__all__'

#     def get_form(self, form_class=None):
#         form = super().get_form(form_class=None)
#         form.fields['project'].queryset = form.fields['project'].queryset.filter(owner_id=self.request.user.id)
#         return form
