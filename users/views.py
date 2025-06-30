import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

firebase_config = settings.FIREBASE_CONFIG
signup_url = settings.FIREBASE_SIGNUP_URL
signin_url = settings.FIREBASE_SIGNIN_URL

@api_view(['POST'])
def firebase_register(request):
    email = request.data.get('email')
    password = request.data.get('password')
    name = request.data.get('name')

    if not email or not password:
        return Response({'error':'Email and Password required'}, status=status.HTTP_401_UNAUTHORIZED)
    
    url = signup_url
    payload = {'email':email,'password':password,'displayName':name,'returnSecureToken':True}
    response = requests.post(url, json=payload)

    if response.status_code == status.HTTP_200_OK:
        return Response(response.json(),status=status.HTTP_200_OK)
    return Response({'error':'Something went wrong with API'},status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def firebase_login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    

    if not email or not password:
        return Response({'error':'Email and Password required'},status=status.HTTP_401_UNAUTHORIZED)
       
    url =  signin_url 
    payload = {'email':email,'password':password,'returnSecureToken':True}
    response = requests.post(url, json=payload)

    if response.status_code == status.HTTP_200_OK:
        return Response(response.json(),status=status.HTTP_200_OK)
    return Response({'error':'Something went wrong with API'},status=status.HTTP_404_NOT_FOUND)
