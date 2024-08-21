from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password
import uuid
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

from .Enums.userType import UserType

# here i've override django's auth user model 
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    
# creatting one to one mapping with our userprofile
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="userProfile")
    user_guid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )
    user_type = models.IntegerField(choices=UserType.choices(), default=UserType.BUYER)
    wallet_balance = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at' ]  # Corrected the ordering syntax
        


