from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserModel
from .serializer import UserSerializer

# Create your views here.


class UserView(APIView):

    def get(self, request):
        users = UserModel.objects.all()
        serializer = UserSerializer(users, many=True, only=('name', 'age'))
        return Response(serializer.data)
