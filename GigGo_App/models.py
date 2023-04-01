from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class NewUser(AbstractUser):
    GENDER = [
        ('1', 'Male'),
        ('2', 'Female'),
    ]
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True)
    dob = models.DateField(null=True)
    phone_number = models.CharField(max_length=12, null=True)
    nin = models.PositiveBigIntegerField(null=True)
    email = models.EmailField(null=True)
    weburl = models.URLField(max_length=40, null=True)
    address = models.CharField(max_length=40, null=True)
    status = models.BooleanField(null=True)
    
    def __str__(self):
        return self.username
    

class Category(models.Model):
    CATEGORIES = [
        ('dayworkers', 'Day Workers'),
        ('streetvendors', 'Computer/IT'),
        ('cleaning/laundry', 'Cleaning/Laundry'),
        ('homeappliancerepair', 'Home Appliance Repair'),
        ('machineryrepair', 'Machinery Repair'),
    ]
    name = models.CharField(max_length=20, choices=CATEGORIES)
    slug = models.SlugField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Job(models.Model):
    LOCATION = [
        ('masaki', 'Masaki'),
        ('kinondoni', 'Kinondoni'),
        ('ubungo', 'Ubungo'),
        ('temeke', 'Temeke'),

    ]
    STATUS = [
        ('open', 'Open'),
        ('acquired', 'Acquired'),
        ('inprogress', 'In Progress'),
        ('Reviewing', 'Reviewing'),
        ('complete', 'Complete'),
    ]
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=False)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='gig_images/%Y/%m/%d', blank=True)
    location = models.CharField(choices=LOCATION, max_length=20, null=True)
    date = models.DateField(auto_now=True)
    price = models.FloatField(max_length=25, null=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("feed:gigdetail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['user']
        verbose_name = "Gig"
        verbose_name_plural = "Gigs"
        index_together = (('id', 'slug'),)
