from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from.decorator import *
from django.contrib.auth.decorators import user_passes_test
# Create your views here.


class AuthorViewSet(viewsets.ModelViewSet):
    """Handling Author requests"""
    pass

class QuoteViewSet(viewsets.ModelViewSet):
    """Handling Quote requests"""
    pass

@api_view(['Get'])
@authnticate
def get_random_quote(request):
    """Handling getting random quote"""

    
    return Response({'message':'hello'},status=status.HTTP_200_OK)



