from rest_framework.serializers import ModelSerializer


class SerializerAddOn:

    @classmethod
    def only(cls, *args):

        class InnerClass(ModelSerializer):

            class Meta:
                model = cls.Meta.model
                fields = args

        return InnerClass

    @classmethod
    def exclude(cls, *args):

        class InnerClass(ModelSerializer):

            class Meta:
                model = cls.Meta.model
                exclude = args

        return InnerClass
