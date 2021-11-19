from django.db import models


# Create your models here.
class Profile(models.Model):
    profile_image = models.ImageField()

    def __str__(self):
        return 'profile'


class Instagram(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    numper_of_posts = models.IntegerField(null=True, blank=True, default=10)
    def __str__(self):
        return self.name
