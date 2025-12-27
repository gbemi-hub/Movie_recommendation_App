from rest_framework import serializers
from . models import User
from rest_framework .authtoken.models import Token



class Registration(serializers.ModelSerializers):
    password = serializers.Charfield(write_only = True)

    class Meta:
        model = User
        fields=["id","username","email" 'password"]

    def create(self, validated_data):
            user = User.objects.create_user(
                 username = validated_data["username"],
                 email = validated_data["email"],
                 password = validated_data["password"],
            )
       Token.objects.create = (user=user)

       return user

class Login(serializers.ModelSerializers):
    usename = serializers.Charfield()
    password = password = serializers.Charfield(write_only = True)

    def validate(self, data):
        user = authenticate(**data)
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return user


   