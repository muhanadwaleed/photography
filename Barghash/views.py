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
        list_of_posts = []
        list_of_pic = []
        for s in profile_pic:
            print("****",s)
            v = s.split('.jpg')[0].split('UTC')[0] + 'UTC.txt'
            list_of_posts.append('static/'+v)
            if '_UTC_' in s :
                list_of_pic.append(s.split('.jpg')[0].split('UTC')[0] + 'UTC_1.jpg')
            else :
                list_of_pic.append(s.split('.jpg')[0].split('UTC')[0] + 'UTC.jpg')

        filterd_list_of_pic = set(list_of_pic)
        filterd_list_of_posts = set(list_of_posts)

        for v in filterd_list_of_posts:
            with open(v) as f:
                contents = f.read()
                print('2', contents)

        return render(request, "index.html", {
            'main_image': profile.profile_image.url,
            'instagram_profile_name': instgram_opj.name,
            'profile_pic': sorted(filterd_list_of_pic,reverse=True),
            'profile': profile,
        })


class Collection(View):

    def get(self, request):
        profile = Profile.objects.first()
        return render(request, "collection.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,

        })


class About(View):
    def get(self, request):
        profile = Profile.objects.first()
        about = AboutPage.objects.first()
        return render(request, "about.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,
            'about': about,

        })


class Services(View):
    def get(self, request):
        profile = Profile.objects.first()
        return render(request, "services.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,

        })


class Blog(View):
    def get(self, request):
        profile = Profile.objects.first()
        return render(request, "blog.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,

        })


class Contact(View):
    def get(self, request):
        profile = Profile.objects.first()
        return render(request, "contact.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,

        })


class Test(View):
    def get(self, request):
        profile = Profile.objects.first()
        return render(request, "test.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,

        })
