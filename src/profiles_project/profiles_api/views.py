from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class HelloApiView(APIView):
    """
        Test APIView
    """

    def get(self, request, format=None):
        """Resturns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Similar to traditional django view',
            'is mapped manually to URLs',
            'gives you the max power',
        ]

        return Response({ 'message': 'Hello', 'an_apiview': an_apiview })
