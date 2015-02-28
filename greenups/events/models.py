from django.db import models

from markupfield.fields import MarkupField

# Create your models here.

from django.db import models

class Event(models.Model):
    name = models.CharField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    details = MarkupField()
    wrapup = MarkupField()
    venue = models.ForeignKey(Venue)
    image = models.ImageField(upload_to='events')
    meetup = models.URLField()
    facebook = models.URLField()
    eventbrite = models.URLField()



class Venue(models.Model):
    name = models.CharField()
    address = models.ForeignKey(Address)

class Address(models.Model):
    street = models.TextField()
    city = models.TextField()
    province = models.TextField()
    code = models.TextField()

class Speaker(models.Model):
    name = models.CharField()
    title  = models.CharField()
    url = models.URLField()
    image = models.ImageField(upload_to='speakers')
    about = MarkupField()
    event = models.ForeignKey(Event, related_name='speakers')







