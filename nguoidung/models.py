import abc
from django.db import models
from django.db.models.fields import DateField
from django_countries.fields import CountryField
from django.db.models.deletion import CASCADE, PROTECT
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

class RoomChat(models.Model):
    RoomID = models.CharField(max_length=4)
    RoomIDAPI = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.RoomID
    
    class meta: 
        verbose_name_plural = 'RoomChats'

class thongtinnguoidung(models.Model):
    tennguoidung = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=69)
    nation = CountryField()
    dateofbirth = models.DateField(default=datetime.date.today)
    email = models.EmailField(null=True)
    GENDER_CHOICES = (
        ('M', 'Nam'),
        ('F', 'Nữ'),
        ('O', 'Khác')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='')
    room = models.ForeignKey(RoomChat, on_delete=PROTECT, default='', null=True)
    
    def cleaned_email(self):
        email = User.clean_fields['email'];
        return email

    def __str__(self):
        return self.name
    
class TinNhan(models.Model):
    # tennguoidung = 
    room = models.CharField(max_length=255)
    messenger = models.CharField(max_length=20, null=True)
    noidung = models.TextField(max_length=10000, null=True)
    