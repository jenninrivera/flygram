from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from myapp.models import Profile

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, Profile):
        token = super().get_token(Profile)
        token['username'] = Profile.username
        return token
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'email', 'name', 'username', 'password' )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.is_active = True
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
# class UserSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(required=True)
#     password = serializers.CharField(
#         required=True, write_only=True, style={'input_type': 'password'},
#     )
#     bio = serializers.CharField(
#         required=False,
#         max_length=150)
    
#     def create(self, validated_data):
#         user = Profile.objects.create_user(**validated_data)
#         return user
    
#     class Meta:
#         fields = ('email', 'username', 'name', 'password', 'bio', 'profile_pic', 'private')

