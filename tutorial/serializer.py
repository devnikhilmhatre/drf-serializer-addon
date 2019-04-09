from rest_framework.serializers import ModelSerializer

from .models import UserModel
from utils.extension import SerializerAddOn


class UserSerializer(SerializerAddOn, ModelSerializer):

    class Meta:
        model = UserModel
        fields = '__all__'
