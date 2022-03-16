import sys
import os

from django.db.models import Q
from django.shortcuts import render, redirect
import instaloader
import re
import random

from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views import View

from Barghash.models import *
import time


def current_milli_time():
    return round(time.time() * 1000)


class Home(View):

    def get(self, request):
        before = current_milli_time()
        profile = Profile.objects.first()
        instgram_opj = Instagram.objects.first()

        ig = instaloader.Instaloader()
        dp = instgram_opj.name
        profile_pic = ig.download_profile(dp)
        list_of_pic = []

        for s in profile_pic:
            if os.path.exists('static/' + s.replace('.jpg', '.webp')):
                if '.jpg' in s:
                    corrected_name = s.replace('.jpg', '.webp')
                    print('corrected_name', corrected_name)
                    if '_UTC_' in corrected_name:
                        list_of_pic.append(corrected_name.split('.webp')[0].split('UTC')[0] + 'UTC_1.webp')
                    else:
                        list_of_pic.append(corrected_name.split('.webp')[0].split('UTC')[0] + 'UTC.webp')
            else:
                v = s.split('.jpg')[0].split('UTC')[0] + 'UTC.txt'
                if '_UTC_' in s:
                    list_of_pic.append(s.split('.jpg')[0].split('UTC')[0] + 'UTC_1.jpg')
                else:
                    list_of_pic.append(s.split('.jpg')[0].split('UTC')[0] + 'UTC.jpg')

        filterd_list_of_pic = set(list_of_pic)
        print('filterd_list_of_pic',filterd_list_of_pic)

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
        return render(request, "index.html", {
            'main_image': profile.profile_image.url,
            'instagram_profile_name': instgram_opj.name,
            'profile_pic': sorted(filterd_list_of_pic, reverse=True),
            'profile': profile,
        })


class Collection(View):

    def get(self, request):
        profile = Profile.objects.first()
        images = GallaryImage.objects.all()
        return render(request, "collection.html", {
            'main_image': profile.profile_image.url,
            'profile': profile,
            'images': images,

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


class Archive(LoginRequiredMixin, APIView):
    def get(self, request):
        archive = request.GET.get('archived', None)
        id = request.GET.get('id', None)
        post = Post.objects.get(id=id)
        post.archive = archive
        post.save()


class DeletePost(LoginRequiredMixin, APIView):
    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)
            post.delete()
            success = 'success'
            return Response({'success': success})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(u'error in available labs GET METHOD, at line {line}: {error}, file: {file}, type: {type}'.format(
                line=exc_tb.tb_lineno,
                error=e, file=fname,
                type=exc_type))
            Log.objects.create(
                body=u'in available labs GET METHOD, at line {line}: {error}, file: {file}, type: {type}'.format(
                    line=exc_tb.tb_lineno,
                    error=e, file=fname,
                    type=exc_type))
            return Response({'error': str(e)})


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
        messages = Messages.objects.all().order_by('-date')
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
