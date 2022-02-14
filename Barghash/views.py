from django.shortcuts import render
import instaloader
import re
import random

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
            # print("****",s)
            v = s.split('.jpg')[0].split('UTC')[0] + 'UTC.txt'
            list_of_posts.append('static/' + v)
            if '_UTC_' in s:
                list_of_pic.append(s.split('.jpg')[0].split('UTC')[0] + 'UTC_1.jpg')
            else:
                list_of_pic.append(s.split('.jpg')[0].split('UTC')[0] + 'UTC.jpg')

        filterd_list_of_pic = set(list_of_pic)
        filterd_list_of_posts = set(list_of_posts)

        for p in filterd_list_of_pic:

            date = re.split('/*_U', p)[0].split('/')[1].split('_')
            new_date = date[0] + ' ' + date[1].replace('-', ':') + '+00:00'

            if Post.objects.filter(date=new_date).count() == 0:
                category = Category.objects.get_or_create(category_name='Instagram')
                post = Post.objects.get_or_create(date=new_date)

                post[0].title = 'From Instagram'
                post[0].date = new_date
                post[0].image = p
                post[0].category = category[0]
                with open('static/' + p.split('UTC')[0] + 'UTC.txt') as f:
                    post[0].caption = f.read()

                post[0].save()
            else:
                print("noooooooooooo")

        return render(request, "index.html", {
            'main_image': profile.profile_image.url,
            'instagram_profile_name': instgram_opj.name,
            'profile_pic': sorted(filterd_list_of_pic, reverse=True),
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
        posts = Post.objects.all().order_by('-date')
        items = list(posts)
        categories = Category.objects.all()

        return render(request, "blog.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,
            'posts': posts,
            'Suggested_Articles': random.sample(items, 3),
            'categories': categories,

        })


class CategoryBlog(View):
    def get(self, request, category):
        profile = Profile.objects.first()
        posts = Post.objects.all().order_by('-date')
        items = list(posts)
        categories = Category.objects.all()
        category_obj = Category.objects.get(category_name=category)
        categored_posts = Post.objects.filter(category=category_obj).order_by('-date')

        return render(request, "blog.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,
            'posts': categored_posts,
            'Suggested_Articles': random.sample(items, 3),
            'categories': categories,

        })


class BlogPost(View):
    def get(self, request):
        profile = Profile.objects.first()
        return render(request, "single.html", {
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
