from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse 
from django.conf import settings


# Create your models here.

class Shop_category(models.Model):
    COSMETICS = 'CS'
    PHARMACY = 'PH'
    ELECTRONICS = 'ELC'
    OTHER = 'OT'

    SHOP_CATEGORY_CHOICES = [
        (COSMETICS,'Cosmetics'),
        (PHARMACY, 'Pharmacy'),
        (ELECTRONICS, 'Electronics'),
        (OTHER, 'other')
    ]
    name = models.CharField(max_length=11, choices=SHOP_CATEGORY_CHOICES, default=OTHER,)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

class Category(models.Model):
    name_of_category = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name_of_category')
    
    def __str__(self):
        return self.name_of_category

        

class Shop(models.Model):
    public_key = models.CharField(max_length=100, default='')
    secret_key = models.CharField(max_length=100, default='')
    encription_key = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='images/', blank=True)
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(max_length=300)
    location = models.CharField(max_length=20)
    category = models.ForeignKey(Shop_category, on_delete=models.CASCADE)
    momo_number = models.CharField(max_length=10)
    

    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField(upload_to = 'images/', blank=True)
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description= models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default='')

    def __str__(self):
        return self.name
    

class DeliveryPerson(models.Model):
    OPOKU_WARE = "0P"
    AUTONOMY = "AU"
    ATWIMA = "AT"
    MALE ="M"
    FEMALE = "F"

    GENDER_CHOICE=[
        (MALE, "Male"),
        (FEMALE, "Female")
    ]

    HALL_AFFILIATION_CHOICE=[
        (OPOKU_WARE,"Opoku ware"),
        (AUTONOMY,"Autonomy"),
        (ATWIMA, "Atwima")
    ] 

    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, null=False, blank=False)
    email = models.EmailField()
    studentId = models.ImageField(upload_to='images/')
    profilePic = models.ImageField(upload_to='images/')
    momo_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    hall_of_affiliation = models.CharField(max_length=20, choices=HALL_AFFILIATION_CHOICE, null= False, blank=False)
    residential_Address = models.CharField(max_length=300)


    def __str__(self):
        return self.name
    

    

    
