import os

from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django_resized import ResizedImageField
import PIL.Image

# Create your models here.
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from sorl.thumbnail import default
from sorl.thumbnail.images import ImageFile

from my_website.settings import MEDIA_ROOT



# from faicon.fields import FAIconField

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
    color = ColorField(default='#CCB78F')

    def __str__(self):
        return self.name


class Instagram(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    numper_of_posts = models.IntegerField(null=True, blank=True, default=10, validators=[
        MaxValueValidator(11),
        MinValueValidator(0)
    ])

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
    main_paragraph = RichTextField(null=True, blank=True,default="")

    def __str__(self):
        return "About page"


class Category(models.Model):
    category_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.category_name)

    def countposts(self):
        count = Post.objects.filter(category=self.id).count()
        return count


class ContactUs(models.Model):
    address = models.CharField(max_length=1500, null=True, blank=True)
    phone = models.CharField(max_length=300, null=True, blank=True)
    email = models.CharField(max_length=300, null=True, blank=True)
    website = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str('Contact Us')


class Messages(models.Model):
    messages_number = models.AutoField(primary_key=True)
    date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    name = models.CharField(max_length=1500, null=True, blank=True)
    contact_way = models.CharField(max_length=300, null=True, blank=True)
    subject = models.CharField(max_length=1500, null=True, blank=True)
    message = models.TextField(max_length=50000, null=True, blank=True)

    def __str__(self):
        return str('message ( ' + str(self.messages_number) + ' ) From :' + str(self.name) + ' send in : ' + str(
            self.date.date()))


class Post(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    caption = models.TextField(null=True, blank=True, max_length=1500, default="")
    date = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    archive = models.BooleanField(null=True, blank=True, default=False)
    from_instagram = models.BooleanField(null=True, blank=True, default=False)
    video = models.FileField(upload_to='videos_uploaded', null=True, blank=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])

    def __str__(self):
        return str('Title: ' + str(self.title) + ' |  Date: ' + str(self.date.date())) + ' |  Category: ' + str(
            self.category.category_name)

    def wordcounter(self):
        if len(self.caption) >= 200:
            return True
        else:
            return False

    def pic(self):
        pic = str(self.image)

        if os.path.exists('static/' + pic.replace('.jpg', '.webp')):
            return pic.replace('.jpg', '.webp')
        else:
            return False

    def videoUrl(self):
        vid = str(self.image)
        if os.path.exists('static/' + vid.replace('.jpg', '.mp4')):
            return vid.replace('.jpg', '.mp4')
        else:
            return False


@receiver(pre_delete, sender=Post)
def post_delete_file(sender, instance=None, **kwargs):
    if instance.video:
        file_upload_dir = os.path.join(MEDIA_ROOT, instance.video.name)
        if os.path.exists(file_upload_dir):
            os.remove(file_upload_dir)


class Service(models.Model):
    icon_image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.title)

class Log(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    body = models.TextField(null=True)

    def __str__(self):
        return self.body


class GallaryImage(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_thump = ResizedImageField(size=[500, 300], blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='categoryesee')
    categoryes = models.ManyToManyField(Category, blank=True, null=True)
    title = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.title

    def pic(self):
        pic = str(self.image)

        if os.path.exists('static/' + pic.replace('.jpg', '.webp')):
            return pic.replace('.jpg', '.webp')
        else:
            return False

    def picsize(self):
        image_file = default.kvstore.get_or_set(ImageFile(self.image))

        final_width = int(image_file.size[0] / 10)
        final_height = int(image_file.size[1] / 10)

        if final_width < 300 or final_height < 300:
            final_width = int(final_width * 1.3)
            final_height = int(final_height * 1.3)
        size = [final_width, final_height]
        return size

    def save(self, *args, **kwargs):
        try:
            if self.image and self.id:
                self.image_thump = self.image

                super(GallaryImage, self).save()
                image = PIL.Image.open(self.image_thump)
                size2 = self.picsize()
                size = (size2[0], size2[1])
                image = image.resize(size, PIL.Image.ANTIALIAS)
                image.save(self.image_thump.path.replace('.', str(size2[0]) + '_' + str(size2[1]) + '.'))
                self.image_thump = self.image_thump.name.replace('.', str(size2[0]) + '_' + str(size2[1]) + '.')
        except:
            pass
        super().save(*args, **kwargs)


@receiver(pre_delete, sender=GallaryImage)
def post_delete_file(sender, instance=None, **kwargs):
    if instance.image:
        file_upload_dir = os.path.join(MEDIA_ROOT, instance.image.name)
        if os.path.exists(file_upload_dir):
            os.remove(file_upload_dir)
    if instance.image_thump:
        file_upload_dir = os.path.join(MEDIA_ROOT, instance.image_thump.name)
        if os.path.exists(file_upload_dir):
            os.remove(file_upload_dir)
