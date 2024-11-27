from django.shortcuts import render
from django.http import  JsonResponse

import json

def home(request):
    data = {
        'message': 'Welcome to the homepage',
        'status': 'sucess'
    }

    return JsonResponse(data)

