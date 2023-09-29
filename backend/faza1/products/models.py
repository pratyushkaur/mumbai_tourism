from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

#  Category.objects.create(name= "Children's chloting")
# Brand.objects.create(name="Hemera")
# Product.objects.create(title="Bomber jacket",description="casual jacket for all weather",price=12.50,discount_percentage=10,rating=5,stock=20,brand=Brand.objects.get(id=2),category=Category.objects.get(id=3))

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=4,decimal_places=2)
    rating = models.DecimalField(max_digits=3,decimal_places=2)
    stock = models.IntegerField()
    brand = models.ForeignKey(Brand,null=True,on_delete=models.SET_NULL,
                                 related_name='prod_brand')
    category = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL,
                                 related_name='prod_cat')
    # thumbnail = models.ImageField()
    # images = models.ImageField()
    slug = models.SlugField(default='',null=False,db_index=True)

    def __str__(self):
        return self.title
    
    # class Meta:
    #     verbose_name = "product"
    #     verbose_name_plural = "products"
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Customer(AbstractUser):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    checked_out = models.BooleanField()
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    products = models.ManyToManyField(Product, through='Incart')
    

class Incart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart','product')
    
    """many to many intermediary table with atrribute amount
    compound primary key"""

class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    review = models.TextField()
    rating = models.PositiveIntegerField(validators=[
        MinValueValidator(1,message="Value must be between 1 and 10"),
        MaxValueValidator(10,message="Value must be between 1 and 10")
        ])
    def __str__(self):
        return self.title
    class Meta:
        unique_together = ('customer','product')
    
class Complaint(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    
    def __str__(self):
        return self.title




 





    

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})