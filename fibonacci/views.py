from rest_framework.response import Response
from rest_framework.views import APIView

from .functions import fibonacci

class FibonacciValueByIndex(APIView):
    def get(self, request, index):
        return Response(fibonacci(index))
