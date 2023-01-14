from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status



def authnticate(function=None,redirect_url='quote/random'):
    """Handling Authntication for predefined token Bearer SHEBAK@2022"""
    def decrator(view_func):
        def _wrapped_view(request,*args,**kwargs):
            x=request.headers['Authorization']
            token = str(x).split(" ")
            if token[0].lower()!="bearer" or token[1].lower()!="shebak@2022":
                return Response({'message':'You are not authorized to use this API!'},status=status.HTTP_403_FORBIDDEN)

            return view_func(function,*args,**kwargs)
        return _wrapped_view
    
    if function:
        return decrator(function)
    
    return decrator


