from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from.decorator import *
from . import serializers,models

import pandas as pd
import xlsxwriter

counter=0
data={}

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
    
    global counter
    global data 
    if counter ==100:
        date=get_current_time()
        sheet=pd.DataFrame({'Quote ID':data.keys(),'Count':data.values()})
        writer=pd.ExcelWriter(f'quotes_api_report_{date}.xlsx', engine='xlsxwriter')
        sheet.to_excel(writer, sheet_name='Quotes Report',index=False)        
        writer.close()
        counter=0
        data.clear()

    
    counter+=1
    
    QuoteId=models.Author.objects.values("quoteIds").order_by('?').first()['quoteIds']
    Author=models.Author.objects.values("author").filter(quoteIds=QuoteId)[0]['author']
    _quote=models.Quote.objects.values("quote").filter(quoteId=QuoteId)[0]['quote']

    if str(QuoteId) not in data:
        data[f'{QuoteId}']=1
    else:
        data[f'{QuoteId}']+=1
        

    return Response({'quoteId':QuoteId,'author':Author,'quote':_quote,"counter":data},status=status.HTTP_200_OK)


def get_current_time():
    """Handling getting the time to save the file with"""
    import datetime
    Current_Time = datetime.datetime.now()
    Adjustedtime = Current_Time.strftime("%Y_%m_%d_%H_%M_%S")
    return str(Adjustedtime)




