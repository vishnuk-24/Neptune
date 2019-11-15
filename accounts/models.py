"""Model for account users."""

from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import BaseModel

MALE = 'male'
FEMALE = 'female'
NOT_SPECIFIED = 'not specified'
GENDER_CHOICES = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (NOT_SPECIFIED, 'Not Specified'),
)

ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10
ELEVEN = 11
TWELVE = 12

SATANDARD_CHOICE = (
    (ONE, 1),
    (TWO, 2),
    (THREE, 3),
    (FOUR, 4),
    (FIVE, 5),
    (SIX, 6),
    (SEVEN, 7),
    (EIGHT, 8),
    (NINE, 9),
    (TEN, 10),
    (ELEVEN, 11),
    (TWELVE, 12),
)

A = 'a'
B = 'b'
C = 'c'
D = 'd'
E = 'd'
F = 'f'
G = 'g'
H = 'h'

DIVISION_CHOICE = (
    (A, 'a'),
    (B, 'b'),
    (C, 'c'),
    (D, 'd'),
    (E, 'd'),
    (F, 'f'),
    (G, 'g'),
    (H, 'h'),
)

ONGOING = 'ongoing'
COMPLETED = 'completed'
DROPPED = 'dropped'
STATUS_CHOICES = (
    (ONGOING, 'Ongoing'),
    (COMPLETED, 'Completed'),
    (DROPPED, 'Dropped'),
)

DIPLOMA = 'diploma'
GRADUATE = 'graduate'
POSTGRADUATE = 'postgraduate'
DOCTOR_OF_PHILOSOPHY = 'doctor-of-philosophy'
POSTDOCTORAL_RESEARCHER = 'postdoctoral-researcher'
OTHER = 'other'
COURSE_TYPE_CHOICES = (
    (DIPLOMA, 'Diploma'),
    (GRADUATE, 'Graduate'),
    (POSTGRADUATE, 'Postgraduate'),
    (DOCTOR_OF_PHILOSOPHY, 'Doctor of Philosophy'),
    (POSTDOCTORAL_RESEARCHER, 'Postdoctoral researcher'),
    (OTHER, 'Other')
)


class User(AbstractUser):
    """Create users using AbstractUser."""

    profile_picture = models.ImageField(
        blank=True, null=True, upload_to='accounts/user/profile-picture')
    birth_date = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(
        max_length=32, default=NOT_SPECIFIED, choices=GENDER_CHOICES)

    phone = models.CharField(max_length=20, blank=True, default='')
    address = models.TextField(blank=True, default='')
    city = models.CharField(blank=True, default='', max_length=128)
    state = models.CharField(blank=True, default='', max_length=128)
    country = models.CharField(blank=True, default='', max_length=128)
    zip_code = models.CharField(blank=True, default='', max_length=12)

    is_student = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.username


class Student(BaseModel):
    """Creating student model."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='student')
    standard = models.IntegerField(choices=SATANDARD_CHOICE)
    division = models.CharField(max_length=32, choices=DIVISION_CHOICE)
    rollnumber = models.IntegerField(blank=True, null=True)
    admission_number = models.IntegerField(blank=True, null=True)
    register_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Specification(BaseModel):
    name = models.CharField(blank=True, default='', max_length=200)

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    """Creating teacher model."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='teacher'
    )
    course_type = models.CharField(
        max_length=64, default=OTHER, choices=COURSE_TYPE_CHOICES
    )
    status = models.CharField(
        max_length=32, default=COMPLETED, choices=STATUS_CHOICES
    )
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    score_percentage = models.DecimalField(
        max_digits=8, blank=True, decimal_places=5, default=0
    )
    total_experience = models.PositiveIntegerField(
        blank=True, null=True, db_index=True
    )
    specification = models.ManyToManyField(Specification, blank=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
