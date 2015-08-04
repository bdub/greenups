# Create your models here.

from django.db import models
from django.utils.translation import ugettext as _
from django_countries.fields import CountryField

from localflavor.au.models import AUStateField , AUPostCodeField, AUPhoneNumberField

from markupfield.fields import MarkupField
from embed_video.fields import EmbedVideoField

from model_utils.fields import StatusField
from model_utils.models import TimeStampedModel
from model_utils import Choices

from author.decorators import with_author

@with_author
class Event(TimeStampedModel):
    STATUS = Choices('draft', 'published')
    name = models.CharField(max_length=256)
    status = StatusField()
    pub_date = models.DateTimeField("Publish at")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    entry_price = models.CharField(max_length=256, blank=True)
    venue = models.ForeignKey('Venue')
    details = MarkupField(default_markup_type='markdown')
    wrapup = MarkupField(default_markup_type='markdown', blank=True)
    image = models.ImageField(upload_to='events')
    meetup = models.URLField(help_text="http://www.meetup.com/GreenUps-Sydney-Green-Drinks/events/XXXXXXXX/", blank=True)
    facebook = models.URLField(help_text="https://www.facebook.com/events/XXXXXXX/", blank=True)
    eventbrite = models.URLField(help_text="https://www.eventbrite.com.au/e/XXXXX", blank=True)


    def __unicode__(self):
        return self.name

class Speaker(models.Model):
    name = models.CharField(max_length=256)
    title = models.CharField(max_length=256, blank=True)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='speakers', blank=True)
    about = MarkupField(default_markup_type='markdown', blank=True)
    event = models.ForeignKey(Event, related_name='speakers')
    class Meta:
        order_with_respect_to = 'event'

    def __unicode__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=256)
    address = models.ForeignKey('Address')
    url = models.URLField()
    capacity = models.IntegerField(blank=True)
    contact = models.ManyToManyField('Contact', through='Operator')

    def __unicode__(self):
        return self.name

class Operator(models.Model):
    contact = models.ForeignKey('Contact')
    venue = models.ForeignKey('Venue')

class Address(models.Model):
    address_1 = models.CharField(_("address"), max_length=128)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64, default="Sydney")
    state = AUStateField(_("state"), default="NSW")
    code = AUPostCodeField(_("postcode"), default="2000")
    country = CountryField(default="AU")

    def attrs(self):
        # a generator to return the list of model field names and values.
        # it skips over the first field (because it's the hidden index field)
        for field in self._meta.fields[1:]:
            yield field.name, getattr(self, field.name)

    def __unicode__(self):
        # string rendering that returns the iterated list of values in the model.
        line = u""
        for a in self.attrs():
            line = line + str(a[1]) + " "
        return line


class Contact(models.Model):
    name = models.CharField(max_length=256)
    role = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    phone = AUPhoneNumberField(blank=True)

    def attrs(self):
        # a generator to return the list of model field names and values.
        # it skips over the first field (because it's the hidden index field)
        for field in self._meta.fields[1:]:
            yield field.name, getattr(self, field.name)

    def __unicode__(self):
        # string rendering that returns the iterated list of values in the model.
        line = u""
        for a in self.attrs():
            line = line + str(a[1]) + " "
        return line

class Video(models.Model):
    title = models.CharField(max_length=256)
    video = EmbedVideoField()  # same like models.URLField()
    event = models.ForeignKey(Event, blank=True)

    def __unicode__(self):
        return self.title


