from django.shortcuts import render
import instaloader


# Create your views here.
from django.views import View

from Barghash.models import *


class Home(View):


    def get(self, request):
        profile = Profile.objects.first()
        instgram_opj = Instagram.objects.first()
        ig = instaloader.Instaloader()
        dp = instgram_opj.name
        profile_pic = ig.download_profile(dp)
        # with open('barghash.photography/2021-09-16_17-59-53_UTC.txt') as f:
        #     contents = f.read()
        #     print(contents)


        return render(request, "index.html", {
            'main_image': profile.profile_image.url,
            'instagram_profile_name': instgram_opj.name,
            'profile_pic':profile_pic,
        })


class Collection(View):

    def get(self, request):
        profile = Profile.objects.first()
        return render(request, "collection.html", {
            'main_image': profile.profile_image.url
        })


class About(View):
    def get(self, request):
        profile = Profile.objects.first()

        return render(request, "about.html", {
            'main_image': profile.profile_image.url
        })


class Services(View):
    def get(self, request):
        profile = Profile.objects.first()
        return render(request, "services.html", {
            'main_image': profile.profile_image.url
        })


class Blog(View):
    def get(self, request):
        profile = Profile.objects.first()
        return render(request, "blog.html", {
            'main_image': profile.profile_image.url
        })


class Contact(View):
    def get(self, request):
        profile = Profile.objects.first()
        return render(request, "contact.html", {
            'main_image': profile.profile_image.url
        })

class Test(View):
    def get(self, request):
        profile = Profile.objects.first()
        return render(request, "test.html", {
            'main_image': profile.profile_image.url
        })

