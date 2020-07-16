from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions

class TestView(APIView):
    """Test API View"""
    serializer_class = serializers.TestSerializer

    def get(self, request, format=None):
        """Returns a list of API features"""
        # output to show to enduser
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view but is specific to APIs',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Heeyyyy', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a message with our name"""
        serializer = self.serializer_class(data=request.data)
        print(serializer)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})

        return Response(serializer.errors, 
                        status=status.HTTP_400_BAD_REQUEST
                        )

    def put(self, request, pk=None):
        """Handle entire update of an object - replace object with object provided"""
        return Response({'method' : 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method' : 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method' : 'DELETE'})


class TestViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.TestSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message' : 'Hello!', 'a_viewset' : a_viewset})

    def create(self, request):
        """Create a new message - router translates to POST request"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hey {name}!'
            return Response({'message' : message})

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def retrieve(self, request, pk=None):
        """Handle getting an object by it's ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, ) # created as a tuple instead of a single item - which is why we leave a trailing comma
    permission_classes = (permissions.UpdateOwnProfile, ) # every request that is made is passed to UpdateOwnProfile class and runs through 
            # has_object_permission function to see if user has the permission to perform the action he/she is trying to perform
    
