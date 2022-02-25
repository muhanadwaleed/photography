from django.db.models import Q
from django.shortcuts import render
import instaloader
import re
import random
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin

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
        services = Service.objects.all()
        profile = Profile.objects.first()
        return render(request, "services.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,
            'services': services,

        })


class Blog(View):
    def get(self, request):
        profile = Profile.objects.first()
        if request.user.is_authenticated:
          posts = Post.objects.all().order_by('-date')
        else:
          posts = Post.objects.filter(archive=False).order_by('-date')
        items = list(posts)
        categories = Category.objects.all()
        text = '0'

        return render(request, "blog.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,
            'posts': posts,
            'Suggested_Articles': random.sample(items, 3),
            'categories': categories,
            'search_text': text,

        })


class CategoryBlog(View):
    def get(self, request, category):
        profile = Profile.objects.first()
        if request.user.is_authenticated:
            posts = Post.objects.all().order_by('-date')
        else:
            posts = Post.objects.filter(archive=False).order_by('-date')
        items = list(posts)
        categories = Category.objects.all()
        category_obj = Category.objects.get(category_name=category)
        categored_posts = Post.objects.filter(category=category_obj, archive=False).order_by('-date')
        text = '0'

        return render(request, "blog.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,
            'posts': categored_posts,
            'Suggested_Articles': random.sample(items, 3),
            'categories': categories,
            'search_text': text,

        })


class SearchResults(View):

    def get(self, request):
        search_text = self.request.GET.get('q')
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        profile = Profile.objects.first()
        if request.user.is_authenticated:
            object_list = Post.objects.filter(
                Q(title__icontains=search_text) | Q(caption__icontains=search_text) | Q(
                    category__category_name__icontains=search_text)
            ).order_by('-date')
        else:
            object_list = Post.objects.filter(
                Q(title__icontains=search_text) | Q(caption__icontains=search_text) | Q(
                    category__category_name__icontains=search_text), archive=False
            ).order_by('-date')

        if date_from and date_to:
            object_list = object_list.filter(date__range=[date_from, date_to])
        elif date_from:
            object_list = object_list.filter(date__gte=date_from)
        elif date_to:
            object_list = object_list.filter(date__lte=date_to)



        posts = Post.objects.filter(archive=False).order_by('-date')
        items = list(posts)
        categories = Category.objects.all()
        text = '0'
        if object_list.count() == 0:
            text = search_text

        return render(request, "blog.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,
            'posts': object_list,
            'Suggested_Articles': random.sample(items, 3),
            'categories': categories,
            'search_text': text,

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
        contact_details = ContactUs.objects.first()
        return render(request, "contact.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,
            'contact_details': contact_details,

        })


class Message(APIView):
    def get(self, request):
        name = request.GET.get('Name', None)
        contact_way = request.GET.get('PhoneOrEmail', None)
        subject = request.GET.get('Subject', None)
        message_text = request.GET.get('Message', None)
        message = Messages.objects.create(name=name, contact_way=contact_way, subject=subject, message=message_text)
        profile = Profile.objects.first()
        contact_details = ContactUs.objects.first()
        return render(request, "contact.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,
            'contact_details': contact_details,
        })


class Archive(LoginRequiredMixin,APIView):
    def get(self, request):
        print(request.GET)
        archive = request.GET.get('archived', None)
        id = request.GET.get('id', None)
        post = Post.objects.get(id=id)
        print('befor', post.archive)
        post.archive = archive
        post.save()
        print('after', post.archive)


class Test(View):
    def get(self, request):
        profile = Profile.objects.first()
        return render(request, "test.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,

        })


class MessageRead(LoginRequiredMixin, View):
    def get(self, request):
        profile = Profile.objects.first()
        messages = Messages.objects.all()
        return render(request, "messages.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,
            'messages': messages,

        })


class PostAdmin(LoginRequiredMixin, View):
    def get(self, request):
        profile = Profile.objects.first()
        posts = Post.objects.all().order_by('-date')
        items = list(posts)
        categories = Category.objects.all()
        text = '0'

        return render(request, "post-admin.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,
            'posts': posts,
            'Suggested_Articles': random.sample(items, 3),
            'categories': categories,
            'search_text': text,

        })

