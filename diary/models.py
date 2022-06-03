from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

    def __str__(self):
        return self.email

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
    productivity_rating = models.SmallIntegerField()
    happiness_rating = models.SmallIntegerField()
    incidents = models.ManyToManyField(Incident)

    def __str__(self):
        return "%s %s" % self.user.email, self.day
