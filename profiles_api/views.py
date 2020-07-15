from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    """Test API View"""

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

