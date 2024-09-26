from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
import pika


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


def send_message(action, book_data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='book_updates')

    message = {'action': action, 'data': book_data}
    channel.basic_publish(exchange='', routing_key='book_updates', body=json.dumps(message))
    connection.close()


# Create your views here.
def signin(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def registration(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    try:
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
    except:
        return render(request, 'registration_error.html')
    return render(request, 'registered.html')


def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/manage/')
    else:
        return render(request, 'login_failed.html')


@login_required(login_url='/signin/')  # redirect when user is not logged in
def manage(request):
    return render(request, 'manage.html')


def logout_view(request):
    logout(request)
    return redirect('/signin')
