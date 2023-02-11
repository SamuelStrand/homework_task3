import json

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import update_last_login
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from django_app import models


def list_compr(request: HttpRequest) -> JsonResponse:
    data = [
        {
            'id': x,
            'name': f'Emil {x}',
            'age': x
        }
        for x
        in range(1, 100)]

    with open('temp/logs.txt', 'w') as logs_file:
        json.dump(data, logs_file)

    return JsonResponse(data=data, safe=False)


def login_f(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        context = {}
        return render(request, 'login.html', context=context)
    if request.method == 'POST':
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        if username and password:
            user_obj = authenticate(username=username, password=password)
            if user_obj:
                login(request, user_obj)
                update_last_login(sender=None, user=user_obj)
                return redirect(reverse('django_app:list_comrp', args=()))
            else:
                raise Exception('данные не совпадают')
        else:
            raise Exception('no data')


def logout_f(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect(reverse('django_app:login', args=()))


def post_list(request: HttpRequest) -> HttpResponse:
    posts = models.Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post_list.html', context=context)


def home(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, 'components/base.html', context=context)


def post_detail(request: HttpRequest, pk: int):
    post = models.Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'post_detail.html', context=context)


def post_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        context = {}
        return render(request, 'post_create.html', context=context)
    elif request.method == 'POST':
        print('printed', request.POST)

        title = request.POST.get('title', None)
        description = request.POST.get('description', "")
        models.Post.objects.create(
            user=request.user,
            title=title,
            description=description,
        )

        context = {}
        return redirect(reverse('django_app:post_list', args=()))


def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
    models.Post.objects.get(id=pk).delete()
    return redirect(reverse('django_app:post_list', args=()))
