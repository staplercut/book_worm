from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


#class Profile(models.Model):
#    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    bio = models.TextField(max_length=500, blank=True)
#    location = models.CharField(max_length=30, blank=True)
#    birth_date = models.DateField(null=True, blank=True)


#@receiver(post_save, sender=User)
#def update_user_profile(sender, instance, created, **kwargs):
#   if created:
#        Profile.objects.create(user=instance)
#    instance.profile.save()


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    profile_pic = models.ImageField(
        upload_to='pics/profile_pics/', default='pics/profile_pics/None/blank.png')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()



