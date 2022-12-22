from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
  def create_user(self, email, birthDay, password=None):
    """Creates and saves a User with the given email, date ofbirth and password."""
    if not email:
      raise ValueError('User must have an email address')

    user = self.create_user(
      email,
      password=password,
      BirthDay=birthDay,
    )
    user.is_admin = True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser):
  email = models.EmailField(max_length=100, verbose_name='email address', unique=True)
  birthDay = models.DateField()
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  objects = UserManager()
  USERNAME_FIELD = 'email'
  GENDERS = (
    ('m', 'Male'),
    ('f', 'Famele'),
  )
  # identifier = models.CharField(max_length=40, unique=True,)
  name = models.CharField(max_length=30)
  surName = models.CharField(max_length=30)
  password_hash = models.CharField(max_length=100)
  avatarImage = models.ImageField(upload_to='avatars/%Y/%m/%d/', max_length=255, null=True, blank=True)
  created_at = models.DateField(auto_now=True)
  REQUIRED_FIELDS = ['Name', 'SurName', 'BirthDay', 'Email']
  # ChoosenLanguages = models.

  def __str__(self):
    return self.Name
