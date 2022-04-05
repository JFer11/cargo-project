from django.db import models

# Create your models here.

class Job(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Plane(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    A330 = 'A330-A'
    PLANES = (
        (A330, 'A330-Airbus'),
    )
    model = models.CharField(max_length=10, choices=PLANES)


class Containers(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    model = models.CharField(max_length=10)
