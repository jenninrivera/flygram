import datetime
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from .serializers import MyTokenObtainPairSerializer, UserSerializer, UserLoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Profile
import jwt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def check_user_authentication( request):
    print('checking auth!')
    print(request.user.username)
    if request.user.is_authenticated:
        return Response({'detail': 'Success'}, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated.')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated.')
        
        user = Profile.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        
        return Response(serializer.data)


class ProfileCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class LoginView(APIView):
    print()
    def post(self, request):
        print("whooo")
        username = request.data['username']
        password = request.data['password']

        user = Profile.objects.filter(username=username).first()
        print(f"User: {user}")
        print(f"User Authentication Attribution: {user.is_authenticated}")

        if user is None:
            raise AuthenticationFailed('Username not found.')
        if not user.check_password(password):
            raise AuthenticationFailed('Password invalid')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        """
        Seemingly, `user.is_authenticated` cannot be manually set after it's 
        programmatically set from the creation of `user` up above. 

        So instead, we'll create a JWT Token and return the response ONLY IF 
        the user is successfully authenticated (returns True). If not (returns
        False), then we'll return an error code.
        """
        # user.is_authenticated = True
        if user.is_authenticated is True:
            res = Response()
            res.set_cookie(key='jwt', value=token, httponly=True)
            res.data = {'jwt': token}
            print(f"Resultant Data (JWT): {res.data}")
            return res
        else:
            return "whoops", 401
    

class LogoutView(APIView):
    def post(self, request):
        res = Response()
        res.delete_cookie('jwt')
        res.data = {'message': 'success'}
        return res



'''
A logout class contructed to essentially logout with a refresh token given from frontend
'''
# class BlacklistTokenUpdateView(APIView):

#     def post(self, request):
        
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
