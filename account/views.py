from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class Account(APIView):

    def get(self, request):
        serializer = UserSerializer()
        return Response(serializer.data)

    def post(self, request, format="json"):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                ret_data = serializer.data
                ret_data["token"] = token.key
                return Response(ret_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    """
    User login
    """

    def get(self, request):
        """
        See if session is valid
        """
        # return render(request, "login.html", {"form": LoginForm()})

    def post(self, request):
        """
        Create session
        """
        pass

    def delete(self, request):
        """
        End session
        """
        pass


class AccountSummary(APIView):
    """
    User summary/home page
    """

    def get(self, request):
        # return render(request, "login.html", {"form": LoginForm()})
        return "OK"

    def post(self, request):
        pass
