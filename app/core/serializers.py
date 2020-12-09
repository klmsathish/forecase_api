from django.db.models.fields import SlugField
from rest_framework import serializers
from .models import User,Post,Photo
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import update_last_login



class UserSerializer(serializers.ModelSerializer):
    # serializer for the users objects

    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        # Create a new user with encrypted pwd and return it
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        # Update a user, setting the passwrod correctly and return it
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        return {
            'email': user.email,
            'token': jwt_token
        }
class PostSerializer(serializers.ModelSerializer):
    # postImage = serializers.PrimaryKeyRelatedField( 
    photoImage = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset = Photo.objects.all()
    )
    # )
    class Meta:
        # depth = 1,
        model = Post,
        fields = '__all__'
        # fields = ('postImage', 'postCaption','postDescription','postVideo','postHashTags','postLocation','postDate')
