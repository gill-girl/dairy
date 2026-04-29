from django.db import models
from django.urls import reverse
# Create your models here.C
class Category(models.Model):
    name=models.CharField(max_length=250)
    slug=models.SlugField(unique=True)
    class Meta:
        verbose_name_plural='categories'




    def __str__(self):
        return self.name
    


class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    description=models.TextField(max_length=150)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    available=models.BooleanField(default=True)
    image=models.ImageField(upload_to='photo',null=True,blank=True)

    def __str__(self):
        return self.name
 #We use get_absolute_url() to generate the correct URL for an object in a clean, reusable, and maintainable way.   

    def get_absolute_url(self):
        return reverse('menus:menu_id',kwargs={'id':self.id,'slug':self.slug})
    

     