from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated 




from . import serializers
from . import models
from . import permissions

class UserprofileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserprofileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,) 
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)



class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manaully to URLs',

        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """"Create a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)  

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, requeat, pk=None):
        """Handels updating an object."""
        return Response({'method':'put'})
    
    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in request. """

        return Response({'method': 'patch'})
    
    def delete(self, request, pk=None):
        """Patch request, only updates fields provided in request. """

        return Response({'method': 'delete'})
    
class HelloViewset(viewsets.ViewSet):
    """Test API ViewSet."""
    
    serializer_class = serializers.HelloSerializer

    def list(self, request):

        """Return a hello message. """

        a_viewset = [

            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code. '

        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create a new hello message."""
        serializer = serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        """Handles getting an object"""

        return Response({'http_method': 'Get'})
        


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().as_view()(request=request._request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
   #Handels creating, reading and updating profile feed items

    authemtication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        #Sets the user profile to the logged in user

        serializer.save(user_profile=self.request.user)























# Create your views here.
