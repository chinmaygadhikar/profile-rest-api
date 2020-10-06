from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Return a list of APIView features"""

        an_apiview = [
            "User http methods as function (get,post, patch, put, delete)",
            "Is similat to a traditional Django View",
            "Gives you the most control over you application logic",
            "Is mapped manuallu to URLs"
        ]

        return Response({"Message": "Hello", "an_apiview": an_apiview})
