from django.db import models


class Support(models.Model):

    email = models.EmailField(max_length=255, unique=True, blank=False)
    name = models.CharField(max_length=15)
    short_description = models.CharField(max_length=50, blank=False)
    detailed_description = models.TextField(max_length=1000)

    def __str__(self):
        return self.email
