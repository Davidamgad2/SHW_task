from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from . import models


class AuthorSerializer(serializers.ModelSerializer):
    """Serializes Author"""

    class Meta:
        model = models.Author
        fields = ('author','quoteIds')
        


class QuoteSerializer(serializers.ModelSerializer):
    """Serializes Quotes"""

    class Meta:
        model = models.Quote
        fields = ('quote','quoteId')

