from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Site(models.Model):
	Office = models.CharField(max_length=200)
	def __str__(self):
            return self.Office

class Team(models.Model):
	member_id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=200)
	Office = models.ForeignKey(Site, on_delete=models.CASCADE)
	def __str__(self):
            return self.Name



class Listing(models.Model):
	list_id = models.AutoField(primary_key=True)
	address = models.CharField(max_length=200)
	date_listed = models.DateTimeField('Date Listed')
	date_exchanged = models.DateTimeField('Date Exchanged',null=True, blank=True)
	date_fallthrough = models.DateTimeField('Date Fallen Through',null=True, blank=True)
	team_member = models.ForeignKey(Team, on_delete=models.CASCADE)
	list_price = models.IntegerField(default=0)
	sale_price = models.IntegerField(default=0)
	commission = models.IntegerField()
	def __str__(self):
            return self.address

