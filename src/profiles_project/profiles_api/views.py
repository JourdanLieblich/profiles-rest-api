from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken


from . import serializers
from . import models
from . import permissions

# Create your views here.

class LogInViewSet(viewsets.ViewSet):
    """Returns an authtoken"""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Obtain the ObtainAuthToken APIView to validate and create a token"""
        return ObtainAuthToken().post(request)

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating reading and updating profiles"""

    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')

class HelloApiView(APIView):
    """
        Test APIView
    """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Resturns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Similar to traditional django view',
            'is mapped manually to URLs',
            'gives you the max power',
        ]

        return Response({ 'message': 'Hello', 'an_apiview': an_apiview })

    def post(self, request):
        """Create a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}!'.format(name)

            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object"""

        return Response({'message': 'put'})

    def patch(self, request, pk=None):
        """Handles patch reques, only updates the required fields"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Handles the deletion of a db object"""

        return Response({'method': 'delete'})



class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions list create update partial update destroy',
            'automatically maps to urls useing routers',
            'more functionality from less code',
        ]
        return Response({'message': a_viewset})

    def create(self, request):
        """ Creates an object """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'eat shit and die {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ retrieves a specified object based on db id"""
        return Response({'message': 'HTTP GET'})

    def update(self, request, pk=None):
        """ updates a specified object """
        return Response({'message': 'HTTP PUT'})

    def partial_update(self, request, pk=None):
        """ updates only specified parameters of an object """
        return Response({'message': 'HTTP PATCH'})

    def destroy(self, request, pk=None):
        """ deletes a specified object"""
        return Response({'message': 'HTTP DELETE'})
