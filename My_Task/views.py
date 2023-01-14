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
    QuoteId=models.Author.objects.values("quoteIds").order_by('?').first()['quoteIds']
    Author=models.Author.objects.values("author").filter(quoteIds=QuoteId)[0]['author']
    _quote=models.Quote.objects.values("quote").filter(quoteId=QuoteId)[0]['quote']
    return Response({'quoteId':QuoteId,'author':Author,'quote':_quote},status=status.HTTP_200_OK)



