from django.db import models

class Bucket(models.Model):
	item=models.TextField(blank=False, unique=True)
	target_age=models.IntegerField()
	added_date=models.DateTimeField(auto_now_add=True)
	status=models.CharField(max_length=255,blank=False)
	country=models.CharField(max_length=255)
	def __str__(self):
		return self.item

