from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom_User(AbstractUser):
    
    fathers_name = models.CharField(max_length=100, null=True)
    mothers_name = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(max_length=30, null=True)
    address = models.TextField(max_length=150, null=True)

class NID_Model(models.Model):

    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, null=True)
    nid_number= models.PositiveIntegerField(null=True)
    profile_pic = models.ImageField(upload_to='Media/Profile_Pic/NID', null=True)
    
class Passport_Model(models.Model):
    
    user = models.OneToOneField(NID_Model, on_delete=models.CASCADE, null=True)
    passport_number = models.PositiveIntegerField(null=True)
    profile_pic = models.ImageField(upload_to='Media/Profile_Pic/Passport', null=True)