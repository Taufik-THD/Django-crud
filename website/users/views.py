from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from django.http import HttpResponse
from django.shortcuts import render
from urllib.parse import urlparse
from django.db import connection

from .forms import usersForm
from .models import users

import psycopg2
import hashlib
import bcrypt
import json
import jwt

# Create your views here.

connection = psycopg2.connect("dbname=myproject user=postgres")
cur = connection.cursor()

@csrf_exempt
def sign_up(request):
    password = request.POST['password']
    hashPwd = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
    user = users.objects.filter(email=request.POST['email'])

    if user.values('email'):
        return HttpResponse('email exists...')
    else:
        form = usersForm(request.POST)
        if form.is_valid():
            password = form.save(commit=False)
            password.password = hashPwd
            password.save()
            return HttpResponse('sign up success...')

@csrf_exempt
def sign_in(request):
    user = users.objects.filter(email=request.POST['email'])
    email = user.values('email')[0]['email']
    if email:
        data = user.values('password')[0]
        hashed = hashlib.sha256(str(request.POST['password']).encode('utf-8')).hexdigest()
        for_token = {
            'id': user.values('id')[0]['id'],
            'email': email
        }

        if hashed == data['password']:
            token = jwt.encode(for_token, 'secret', 'HS256').decode('utf-8')

            return HttpResponse('Sign In success, your token: '+ token)
        else:
            return HttpResponse('Wrong password...')

    else:
        return HttpResponse('Email is not defined...')
