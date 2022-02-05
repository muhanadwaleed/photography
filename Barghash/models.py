from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(null=True, blank=True, max_length=1500)
    profile_image = models.ImageField()
    home_first_photo = models.ImageField(null=True, blank=True)
    home_second_photo = models.ImageField(null=True, blank=True)
    email = models.CharField(null=True, blank=True, max_length=1500)
    phone_number = models.CharField(null=True, blank=True, max_length=1500)
    location = models.CharField(null=True, blank=True, max_length=1500)
    twitter = models.CharField(null=True, blank=True, max_length=1500)
    facebook = models.CharField(null=True, blank=True, max_length=1500)
    instagram = models.CharField(null=True, blank=True, max_length=1500)
    paragraph = models.TextField(null=True, blank=True, max_length=1500)
    title = models.CharField(null=True, blank=True, max_length=1500)
    jop = models.CharField(null=True, blank=True, max_length=1500)
    footer = models.TextField(null=True, blank=True, max_length=1500)

    def __str__(self):
        return self.name


class Instagram(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    numper_of_posts = models.IntegerField(null=True, blank=True, default=10)

    def __str__(self):
        return self.name


class AboutPage(models.Model):
    image = models.ImageField(null=True, blank=True)
    paragraph = models.TextField(null=True, blank=True, max_length=1500, default="")
    pounds_of_equipment = models.IntegerField(null=True, blank=True, default=10)
    studio_session = models.IntegerField(null=True, blank=True, default=10)
    finished_photosession = models.IntegerField(null=True, blank=True, default=10)
    happy_clients = models.IntegerField(null=True, blank=True, default=10)
    main_title = models.CharField(max_length=300, null=True, blank=True)
    main_paragraph = models.TextField(null=True, blank=True, max_length=30000, default="")


    def __str__(self):
        return "About page"