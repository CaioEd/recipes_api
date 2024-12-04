from django.shortcuts import render
from django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

from .models import Recipe
from .serializers import RecipeSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

import json


def home(request):
    data = {
        'message': 'Welcome to the homepage',
        'status': 'sucess'
    }

    return JsonResponse(data)


def list_recipes(request):
    recipes = Recipe.objects.all()
    recipes_list = list(recipes.values())
    return JsonResponse(recipes_list, safe=False)


@api_view(['GET'])
def getRecipeByID(request, id):
    try:
        recipe = Recipe.objects.get(id=id)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    except Recipe.DoesNotExist:
        return Response('This recipe does not exist')
    
    
@api_view(['POST'])
def createRecipe(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

