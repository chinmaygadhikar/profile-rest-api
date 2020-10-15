from rest_framework import serializers

from profiles_api import models

class HelloSerializers(serializers.Serializer):
    """ Serializers a name field for testing our APOView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password' : {                              # making password as only input while creating profile
                'write_only' : True,                    # here are the arguments
                'style' : {                             # here is the style of the password
                    'input_type' : 'password'           # here the input type is considered
                }
            }
        }

    def create(self, validated_data) :
        """ create and return a new user"""

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
