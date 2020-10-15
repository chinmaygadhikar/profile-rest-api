from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers
from profiles_api import models

class HelloApiView(APIView):
    """Test API view"""

    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """Return a list of APIView features"""

        an_apiview = [
            "User http methods as function (get,post, patch, put, delete)",
            "Is similat to a traditional Django View",
            "Gives you the most control over you application logic",
            "Is mapped manuallu to URLs"
        ]

        return Response({"Message": "Hello", "an_apiview": an_apiview})

    def post(self, request):
        """ Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'Message': message})
        else:
            return Response(
                       serializer.errors,
                       status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle to update an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle t partial update of an object"""
        return Response({'method':'Patch'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':"DELETE"})



class HelloViewSets(viewsets.ViewSet):
    """Test api view set"""

    serializer_class = serializers.HelloSerializers

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            "User Actions(list, create, retrive, update, partial_update)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code"
        ]

        return Response({"Message": "Hello", "a_viewset": a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'Message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self, request,pk=None):
        """handle getting an object by its ID"""
        return Response({'Http_method':'GET'})

    def update(self, request,pk=None):
        """handle update an object """
        return Response({'Http_method':'PUT'})

    def partial_update(self, request,pk=None):
        """handle updating part of an object"""
        return Response({'Http_method':'PATCH'})

    def destroy(self, request,pk=None):
        """handle removing an object"""
        return Response({'Http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    
