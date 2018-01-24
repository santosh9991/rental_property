from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class HomeOwnerAccount(models.Model):
	# owner_id = models.IntegerField(auto)
	name = models.CharField(max_length=100)#,default=None)
	contact_number = models.CharField(max_length=100)
	# home_owner_id = models.IntegerField(primary_key=True)
    # property_details = models.ForeignKey(PropertyDetails,
    # 	related_name='property',on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class PropertyDetails(models.Model):
    RESERVATION_STATUS = (
		('Available','AVAILABLE'),
		('Booked','BOOKED'))
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)#, default=None)
    street_name = models.CharField(max_length=100,default='')
    city = models.CharField(max_length=100)

    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    owner = models.ForeignKey(HomeOwnerAccount,
    	related_name='property_details',on_delete=models.CASCADE)
    reservation_status = models.CharField(
    	choices=RESERVATION_STATUS,default='Available',
    	max_length=100)
    # contact_number = models.CharField(max_length=100)
    # user_id = models.IntegerField()
    class Meta:
       unique_together = (('created', 'city','state','zip_code'),)
    def __str__(self):
    	return self.title

class RenterAccoount(models.Model):
    full_name = models.CharField(max_length=100)#,default=None)
    contact_number = models.CharField(max_length=100)
    def __str__(self):
	    return self.full_name
class HouseReservation(models.Model):
	availability = models.BooleanField(default=True)
	start_date = models.DateTimeField(auto_now_add=True)
	end_date = models.DateTimeField(auto_now_add=True)
class PropertyAllocation(models.Model):
	home_owner = models.ForeignKey(HomeOwnerAccount)#,required=True)#,related_name='id')

class UserInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    # customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    creation_ts = models.DateTimeField()
    created_by_id = models.IntegerField(blank=True, null=True)
    last_modification_ts = models.DateTimeField()
    last_modified_by_id = models.IntegerField(blank=True, null=True)
    is_active = models.TextField(blank=True, null=True)  # This field type is a guess.
    #is_enabled = models.TextField()  # This field type is a guess.
    #is_superuser = models.TextField()  # This field type is a guess.
    #is_staff = models.TextField()  # This field type is a guess.
    #date_joined = models.CharField(max_length=45, blank=True, null=True)
    def is_authenticated(self):
        return True
    # class Meta:
    #     managed = False
    #     db_table = 'user_info'