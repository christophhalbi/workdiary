from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import DateInput, ModelForm, TextInput, HiddenInput, ValidationError

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
    created_at = models.DateField()
    meltdown_rating = models.SmallIntegerField(
        default=5,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    repos = models.ManyToManyField(Repo)
    techstack = models.ManyToManyField(Techstack)
    tags = models.ManyToManyField(IncidentTag)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('incident-detail', kwargs={'pk': self.pk})

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField()
    description = models.TextField(null=True, blank=True)
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
    incidents = models.ManyToManyField(Incident, blank=True)

    class Meta:
        constraints = [
           models.UniqueConstraint(fields=['user', 'day'], name='unique_entry_day')
        ]

    def __str__(self):
        return "%s" % self.day

    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={'pk': self.pk})

class EntryForm(ModelForm):
    def clean_day(self):
        user = self.cleaned_data['user']
        day  = self.cleaned_data['day']

        duplicates = Entry.objects.filter(
            user=user,
            day=day
        )

        if duplicates.exists():
            raise ValidationError('Entry already exists')

        return day

    class Meta:
        model = Entry
        fields = ['user', 'day', 'description', 'productivity_rating', 'happiness_rating', 'incidents']
        widgets = {
            'user': HiddenInput(),
            'day': DateInput(attrs={'value': date.today(), 'type': 'date'}),
            'productivity_rating': TextInput(attrs={'type': 'range', 'step': 1, 'min': 1, 'max': 10}),
            'happiness_rating': TextInput(attrs={'type': 'range', 'step': 1, 'min': 1, 'max': 10})
        }

class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = ['created_by', 'created_at', 'name', 'description', 'meltdown_rating', 'repos', 'techstack', 'tags']
        widgets = {
            'created_by': HiddenInput(),
            'created_at': DateInput(attrs={'value': date.today(), 'type': 'date'}),
            'meltdown_rating': TextInput(attrs={'type': 'range', 'step': 1, 'min': 1, 'max': 10}),
        }