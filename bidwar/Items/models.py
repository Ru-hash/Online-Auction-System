from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Item(models.Model):
	name=models.CharField(max_length=20)
	description=models.TextField()
	owner= models.ForeignKey(User, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(default=timezone.now)
	price = models.IntegerField()
	bidder=models.EmailField(null=True)
	def get_absolute_url(self):
		return reverse('Items:detail', kwargs={'pk': self.pk})

# class Bid(models.Model):
# 	Item=models.ForeignKey(Item,on_delete=models.CASCADE)
# 	bid_price=models.IntegerField()
# 	bidder=models.ForeignKey(User,on_delete=models.CASCADE)
