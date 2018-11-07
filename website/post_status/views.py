from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

from .forms import statusForm
from .models import status

import jsonpickle
import psycopg2
import hashlib
import json
import jwt

# Create your views here.

connection = psycopg2.connect("dbname=myproject user=postgres")
cur = connection.cursor()

@csrf_exempt
def timeline(request):
    timeline_lists = []

    cur.execute('SELECT message, email FROM post_status_status CROSS JOIN users_users')

    for message in cur.fetchall():
        status = {}
        status['message'] = message[0]
        status['email'] = message[1]

        timeline_lists.append(status)

    return HttpResponse(jsonpickle.encode(timeline_lists, unpicklable=False))

@csrf_exempt
def post(request):
    headers = request.META.get('HTTP_TOKEN')

    try:
        decode = jwt.decode(headers, 'secret', algorithms=['HS256'])

        cur.execute("INSERT INTO post_status_status (message, user_id) VALUES ('%s', %d)" % (str(request.POST['message']), int(decode['id'])))
        connection.commit()

        return HttpResponse('Status posted...')

    except:

        return HttpResponse('Please sign in first to get token...')


@csrf_exempt
def edit_status(request, id):
    headers = request.META.get('HTTP_TOKEN')

    try:
        decode = jwt.decode(headers, 'secret', algorithms=['HS256'])

        cur.execute("UPDATE post_status_status SET message = '%s' WHERE id=%d and user_id = %d"
                    % (request.POST['message'], id, int(decode['id'])))

        connection.commit()

        return HttpResponse('success update data...')

    except:

        return HttpResponse('data is not valid...')

@csrf_exempt
def remove(request, id):
    headers = request.META.get('HTTP_TOKEN')

    try:
        decode = jwt.decode(headers, 'secret', algorithms=['HS256'])

        status.objects.get(id=id).delete()

        return HttpResponse('status deleted...')

    except:

        return HttpResponse('data is not valid...')

@csrf_exempt
def add_comment(request, id):
    headers = request.META.get('HTTP_TOKEN')
    try:
        decode = jwt.decode(headers, 'secret', algorithms=['HS256'])

        cur.execute("INSERT INTO post_status_comments (comment, user_id, status_id) VALUES('%s', %d, %d)" % (request.POST['comment'], int(decode['id']), id))

        connection.commit()

        return HttpResponse('success add your comment...')

    except:

        return HttpResponse('failed to add comment...')
