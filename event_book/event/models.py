from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import format_html

# Create your models here.
class event(models.Model):
    
    Event_Category_CHOICES = [
        ('trek', 'Trek'),
        ('comedy', 'Comedy'),
        ('music', 'Music'),
        ('adventure', 'Adventure'),
        ('art', 'Art'),
        ('dance', 'Dance'),
        ('game', 'Games'),
        ('food','Food Fest'),
        ('other','Other')
    ]
    
    name = models.CharField(max_length=80)
    image = models.ImageField()
    category = models.CharField(choices=Event_Category_CHOICES,max_length=10)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField() 
    description = models.TextField()
    price = models.FloatField(max_length=10)
    seats = models.PositiveIntegerField(validators=[MaxValueValidator(999)])
    booked_seats = models.PositiveIntegerField(validators=[MaxValueValidator(999)])
    
    class Meta:
        verbose_name = "event"
        verbose_name_plural = "events"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})
    
    def image_tag(self):
        return format_html('<a href="{0}"><img src="{0}" width="250px" height="150px"></a>'.format(self.image.url))
    image_tag.allow_tags = True
    image_tag.short_description = 'Image'

class booking(models.Model):

    event = models.name = models.ForeignKey('event', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    mobile = PhoneNumberField()
    email = models.EmailField()

    class Meta:
        verbose_name = "booking"
        verbose_name_plural = "bookings"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("booking_detail", kwargs={"pk": self.pk})
