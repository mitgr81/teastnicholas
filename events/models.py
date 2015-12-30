import datetime

from django.conf import settings
from django.contrib.gis.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

from django_localflavor_us.models import USStateField


class Notes(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)


class UsLocation(models.Model):
    label = models.CharField(max_length=200, default="New location")
    address_1 = models.CharField(_("address"), max_length=128)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    room = models.CharField(_('room'), max_length=50, blank=True)

    city = models.CharField(_("city"), max_length=64, default="Tea")
    state = USStateField(_("state"), default="SD")
    zip_code = models.CharField(_("zip code"), max_length=5, default="57064")

    def __str__(self):
        return self.label


class Event(models.Model):
    title = models.CharField(max_length=200)
    announce_date = models.DateTimeField('date announced', auto_now_add=True)
    start_date = models.DateTimeField('start datetime', null=True)
    end_date = models.DateTimeField('end datetime', null=True)
    location = models.ForeignKey(UsLocation, null=True, blank=True)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    notes = models.ForeignKey(Notes, null=True, blank=True)

    def __str__(self):
        return self.title

    def is_coming_soon(self):
            return self.start_date >= timezone.now() - datetime.timedelta(days=1)
