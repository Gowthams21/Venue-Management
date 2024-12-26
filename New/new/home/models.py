from django.db import models
from django.conf import settings
from django.utils import timezone

class Query(models.Model):  # Make sure this matches what you import
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=30)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    VENUE_CHOICES = [
        ('audi', 'Auditorium'),
        ('seminar', 'Seminar Hall'),
        ('conference', 'Conference Hall'),
        ('lab', 'Computer Labs'),
        ('classroom', 'Class Rooms'),
    ]
    REFRESHMENT_CHOICES = [
        ('no', 'No'),
        ('yes', 'Yes'),
    ]
    CHILLER_CHOICES = [
        ('no', 'No'),
        ('yes', 'Yes'),
    ]

    date = models.DateField()
    time = models.TimeField()
    organizer = models.CharField(max_length=100)
    reason = models.CharField(max_length=255)
    venue = models.CharField(max_length=50, choices=VENUE_CHOICES)
    subvenue = models.CharField(max_length=100, blank=True, null=True)  # since subvenues might depend on venues
    refreshments = models.CharField(max_length=3, choices=REFRESHMENT_CHOICES)
    chiller = models.CharField(max_length=3, choices=CHILLER_CHOICES)
    approved= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} - {self.subvenue} ({self.organizer})"

# Optional model for Subvenues to enhance dynamic loading
class Subvenue(models.Model):
    venue = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='subvenues')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

