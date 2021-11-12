from .models import Product, Category, Shop, Shop_category, DeliveryPerson
import factory
import factory.fuzzy
from faker.providers.python import Provider
from django.template.defaultfilters import slugify
import datetime
import pytz 

class ShopCategoryFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyChoice([x[0] for x in Shop_category.SHOP_CATEGORY_CHOICES])
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    class Meta:
        model = Shop_category

class CategoryFactory(factory.django.DjangoModelFactory):
    name_of_category  = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name_of_category))
    class Meta:
        model = Category


class ShopFactory(factory.django.DjangoModelFactory):
    public_key = factory.fuzzy.FuzzyText(length=100)
    secret_key = factory.fuzzy.FuzzyText(length=100)
    encription_key = factory.fuzzy.FuzzyText(length=100)
    image = factory.django.ImageField()
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    location = factory.fuzzy.FuzzyText()
    momo_number = factory.fuzzy.FuzzyText()


    class Meta:
        model = Shop


class ProductFactory(factory.django.DjangoModelFactory):
    

    image = factory.django.ImageField()
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    price = factory.fuzzy.FuzzyFloat(0.0)
    available = factory.Faker('pybool')
    created = factory.fuzzy.FuzzyDateTime(datetime.datetime(2008, 1, 1, tzinfo=pytz.utc))
    updated = factory.fuzzy.FuzzyDateTime(datetime.datetime(2008, 1, 1, tzinfo=pytz.utc))
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    

    class Meta:
        model = Product 

class DeliveryPersonFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    gender = factory.fuzzy.FuzzyChoice([x[0] for x in DeliveryPerson.GENDER_CHOICE])
    studentId = factory.django.ImageField()
    profilePic = factory.django.ImageField()
    momo_number = factory.fuzzy.FuzzyText()
    phone_number = factory.fuzzy.FuzzyText()
    hall_of_affiliation = factory.fuzzy.FuzzyChoice([x[0] for x in DeliveryPerson.HALL_AFFILIATION_CHOICE])
    residential_Address = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    class Meta:
        model = DeliveryPerson