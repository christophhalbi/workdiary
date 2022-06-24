from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ModelForm, TextInput, HiddenInput

class Repo(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Techstack(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class IncidentTag(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Incident(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    meltdown_rating = models.SmallIntegerField()
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    repos = models.ManyToManyField(Repo)
    techstack = models.ManyToManyField(Techstack)
    tags = models.ManyToManyField(IncidentTag)

    def __str__(self):
        return self.name

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField()
    productivity_rating = models.SmallIntegerField(
        default=10,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    happiness_rating = models.SmallIntegerField(
        default=10,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    incidents = models.ManyToManyField(Incident)

    def __str__(self):
        return "%s" % self.day

    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={'pk': self.pk})

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['day', 'productivity_rating', 'happiness_rating']
        widgets = {
            'day': HiddenInput(attrs={'value': date.today()}),
            'productivity_rating': TextInput(attrs={'type': 'range', 'step': 1, 'min': 1, 'max': 10}),
            'happiness_rating': TextInput(attrs={'type': 'range', 'step': 1, 'min': 1, 'max': 10})
        }