from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from.decorator import *
from . import serializers,models




class AuthorViewSet(viewsets.ModelViewSet):
    """Handling Author requests"""
    serializer_class = serializers.AuthorSerializer
    queryset = models.Author.objects.all()


class QuoteViewSet(viewsets.ModelViewSet):
    """Handling Quote requests"""
    serializer_class = serializers.QuoteSerializer
    queryset = models.Quote.objects.all()

@api_view(['Get'])
@authnticate
def get_random_quote(request):
    """Handling getting random quote"""


    return Response({'message':'hello'},status=status.HTTP_200_OK)



