from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

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

