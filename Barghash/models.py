import os

from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from my_website.settings import MEDIA_ROOT


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


class Category(models.Model):
    category_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.category_name)

    def countposts(self):
        count = Post.objects.filter(category=self.id).count()
        return count


class Post(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    caption = models.TextField(null=True, blank=True, max_length=1500, default="")
    date = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    video = models.FileField(upload_to='videos_uploaded', null=True, blank=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])

    def __str__(self):
        return str(str(self.title) + ' ' + str(self.date))

    def wordcounter(self):
        if len(self.caption) >= 200:
            return True
        else:
            return False

    def videoUrl(self):
        vid = str(self.image)
        return vid.replace('.jpg', '.mp4')



@receiver(pre_delete, sender=Post)
def post_delete_file(sender, instance=None, **kwargs):
    file_upload_dir = os.path.join(MEDIA_ROOT, instance.video.name)
    if os.path.exists(file_upload_dir):
        os.remove(file_upload_dir)

    # Do something
