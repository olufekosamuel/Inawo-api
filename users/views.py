from rest_framework_jwt.settings import api_settings
from rest_framework import permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
# Get the JWT settings, add these lines after the import/from lines
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


"""
Registration endpoint, to register a new user on the platform 
"""
@api_view(['POST'])
@csrf_exempt
@permission_classes((permissions.AllowAny, ))
def Registration(request):
    fullname = request.data.get("fullname", "")
    password = request.data.get("password", "")
    email = request.data.get("email", "")
    

    if not fullname or not password or not email:
        return Response(
            {'message': "fullname, email, passwords and location are required to register",'error':True,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        user = CustomUser.objects.get(email=email)
        return Response(
            {'message': "Email has been taken already",'error':True,'status':status.HTTP_401_UNAUTHORIZED},status=status.HTTP_401_UNAUTHORIZED
        )
    except CustomUser.DoesNotExist:
        pass

  
    firstname = fullname.split()[0]
    lastname = fullname.split()[1] if len(fullname.split()) > 1 else fullname.split()[0]

    new_user = CustomUser(email=email)
    new_user.set_password(password)
    new_user.first_name = firstname
    new_user.last_name = lastname
    new_user.save()


    data = {
        'id': new_user.id,
        'full name': fullname,
        'email': new_user.email,
    }

    return Response({'message': 'Your account  has been created successfully','error':False,'status':status.HTTP_201_CREATED,'data':data,})


"""
Get user info endpoint, to get informations about an authenticated user
"""
@api_view(['GET'])
@csrf_exempt
@permission_classes((permissions.IsAuthenticated, ))
def GetUserInfo(request):
    user = CustomUser.objects.get(email=request.user.email)
    data = {
        'id': user.id,
        'firstname': user.first_name,
        'lastname': user.last_name,
        'email': user.email,
    }
    return Response({'message': 'success','error':False,'status':status.HTTP_200_OK,'data':data,})


"""
Update a user information
"""
@api_view(['POST'])
@csrf_exempt
@permission_classes((permissions.IsAuthenticated, ))
def EditUser(request):
    if request.method == "POST":
        user = request.user
        firstname =  request.data.get("firstName")
        lastname =  request.data.get("lastName")
        email = request.data.get("email")
        updated_at = datetime.datetime.now()

        if not firstname and not lastname and not email:
            return Response({
                "message":"fullname, password and email is required to register a user",
                'error':True,
                'status':status.HTTP_400_BAD_REQUEST}
            )

        try:
            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            user.updated_at = updated_at
            user.save(update_fields=["first_name","last_name","email","updated_at"])
            print(user)
            return JsonResponse({'message': 'Infomation updated successfully','error':False,'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)
        except  CustomUser.DoesNotExist:
            return JsonResponse({'message': 'User does not exist','error':True,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)


"""
Login endpoint, to authenticate a user and provide a jwt for the user
"""
class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)
    queryset = CustomUser.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        
        if not email or not password:
            return Response(
                {'message': "email and password are required to login",'error':True,'status':status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST
            )
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
           
            if serializer.is_valid():
                data = {
                'id': user.id,
                'firstname': user.first_name,
                'lastname': user.last_name,
                'email': user.email,
                'token': serializer.data['token'],
                }
                return JsonResponse({'message': 'logged in','error':False,'status':status.HTTP_200_OK,'data':data,})
        return Response({'message': 'Wrong credentials','error':True,'status':status.HTTP_401_UNAUTHORIZED})