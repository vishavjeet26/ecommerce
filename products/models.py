from django.db import models
import os
import random

# Create your models here.

def get_filename_ext(filepath):
	base_name  = os.path.basename(filepath)
	print("----------")
	print(base_name)
	name, ext  = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename  = random.randint(1, 3910209312)
    name, ext     = get_filename_ext(filename)
    final_filename =f'{new_filename}{ext}'
    return f"products/{new_filename}/{final_filename}"

class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)

    def active(self):
        return self.filter(active=True)        

class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()    

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        print("In ProductManager----")
        if qs.count() == 1:
           return qs.first()
        return None                 

class Product(models.Model):
	title        = models.CharField(max_length=120)
	description  = models.TextField()
	price        = models.DecimalField(decimal_places=2, max_digits=10, max_length = 20, default = 39.99)
	#image        = models.FileField(upload_to='product/', null=True, blank=True)
	#image        = models.ImageField(upload_to='product/', null=True, blank=True)
	image        = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	featured     = models.BooleanField(default=False)
	active       = models.BooleanField(default=True)
	objects      = ProductManager()
	def __str__(self):return self.title

