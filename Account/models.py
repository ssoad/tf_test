from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None):

        if not email:
            raise ValueError('Email should not be empty')
        if not first_name:
            raise ValueError('First Name should not be empty')
        if not password:
            raise ValueError('Password should not be empty')

        user = self.model(
            email=self.normalize_email(email=email),
            first_name=first_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password=None):
        user = self.create_user(email=email, first_name=first_name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, verbose_name='Email', unique=True, blank=False)
    first_name = models.CharField(verbose_name='First Name', max_length=100)
    last_name = models.CharField(verbose_name='Last Name', max_length=100)
    phone_number = PhoneNumberField(verbose_name="Phone Number")
    country = CountryField(verbose_name="Country", max_length=50)
    profile_pic = models.ImageField(upload_to='users/', default='users/default.jpg')
    birth_date = models.DateField(verbose_name='Birth Date', blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    gender_options = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    gender = models.CharField(verbose_name='Choose Gender', choices=gender_options, default='Male', max_length=20)

    is_staff = models.BooleanField(verbose_name='Staff Status', default=False, help_text='Designate if the user has '
                                                                                         'staff status')
    is_active = models.BooleanField(verbose_name='Active Status', default=True, help_text='Designate if the user has '
                                                                                          'active status')
    is_superuser = models.BooleanField(verbose_name='Superuser Status', default=False, help_text='Designate if the '
                                                                                                 'user has superuser '
                                                                                                 'status')
    is_bcs = models.BooleanField(verbose_name='Business Status', default=False, help_text='Designate if the user is '
                                                                                          'associated with a business')
    newsletter = models.BooleanField(verbose_name='Newsletter', default=False, help_text='Receive Email About Update '
                                                                                         'and Notifications')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', ]

    objects = UserManager()

    def __str__(self):
        return self.first_name
