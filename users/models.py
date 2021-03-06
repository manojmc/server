from django.db import models
from django.contrib.auth.models import User
#from device.models import DeviceProfile

     
"""
Class UserProfile

@date 05/10/2012
@author TKI
"""
class UserProfile(models.Model):
  user           = models.ForeignKey(User, unique=True)
#  user = models.OneToOneField(User)
#  devprofile     = models.ForeignKey(DeviceProfile, blank=True, null=True)
  ub_id          = models.CharField(max_length=30, blank=True, null=True)   
  activation_key = models.CharField(max_length=40)
  key_expires    = models.DateTimeField()
