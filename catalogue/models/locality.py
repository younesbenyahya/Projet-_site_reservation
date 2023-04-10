from django.db import models

# Create your models here.
class Locality(models.Model):
	locality = models.CharField(max_length=60)
	postalcode = models.CharField(max_length=30)
	
	class Meta:
		db_table = "localities"
