from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
   def create_user(self, email, phone=None, score=None, password=None):
       if not email:
           raise ValueError('Users must have an email address')

       user = self.model(
           email=self.normalize_email(email),
       )

       user.set_password(password)
       user.save(using=self._db)
       return user

   def create_superuser(self, email, password, phone=None, score=None):
       user = self.create_user(email,
           password=password,
       )
       user.is_admin = True
       user.save(using=self._db)
       return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    score = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'score']

    def get_full_name(self):
       """The user is identified by their email address"""
       return self.email

    def get_short_name(self):
       """The user is identified by their email address"""
       return self.email

    def __str__(self):              # __unicode__ on Python 2
       return "ID: {} EMAIL: {}".format(self.id, self.email)

    def has_perm(self, perm, obj=None):
       """Does the user have a specific permission?"""
       # Simplest possible answer: Yes, always
       return True

    def has_module_perms(self, app_label):
       """Does the user have permissions to view the app `app_label`?"""
       # Simplest possible answer: Yes, always
       return True

    @property
    def is_staff(self):
       """Is the user a member of staff?"""
       return self.is_admin
