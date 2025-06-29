import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

FIREBASE_API_KEY = {
  'apiKey': "AIzaSyChnT19XK4uXRVSQOYuPEE0Lcx7DhBc36M",
  'authDomain': "miga-piggy.firebaseapp.com",
  'projectId': "miga-piggy",
  'storageBucket': "miga-piggy.firebasestorage.app",
  'messagingSenderId': "490490243020",
  'appId': "1:490490243020:web:5900463f2d27fba3529f69",
  'measurementId': "G-43JZJWGJL6"
}


@api_view(['POST'])
def firebase_register(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error':'Email and Password required'}, status=400)
    
    url = f'"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyChnT19XK4uXRVSQOYuPEE0Lcx7DhBc36M'
    payload = {'email':email,'password':password,'returnSecureToken':True}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return Response(response.json(),status=200)
    return Response({'error':'Something went wrong with API'},status=400)



@api_view(['POST'])
def firebase_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error':'Email and Password required'},status=400)
    
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyChnT19XK4uXRVSQOYuPEE0Lcx7DhBc36M"
    payload = {'email':email,'password':password,'returnSecureToken':True}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return Response(response.json(),status=200)
    return Response({'error':'Something went wrong with API'},status=400)
