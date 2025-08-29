from rest_framework import serializers
from django.contrib.auth.models import User


# serializer for user signup (probably will tweak later for profile stuff)
class UserSerializer(serializers.ModelSerializer):
    # making password write-only so it doesn’t leak out in responses
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # not sure if I actually need email here, but keeping it for now
        fields = ["id", "username", "email", "password"]

    # overriding create so we hash the password properly
    def create(self, validated_data):
        # grabbing fields explicitly instead of unpacking for clarity
        uname = validated_data.get("username")
        mail = validated_data.get("email", "")
        pwd = validated_data["password"]

        # NOTE: using create_user ensures password is hashed
        user = User.objects.create_user(
            username=uname,
            email=mail,
            password=pwd
        )

        # might need to send welcome email here later... (not yet)
        return user

   

