from rest_framework.serializers import ModelSerializer
from .models import *



class ImageModelSerializer(ModelSerializer):
    class Meta :

        model = ImageModel
        fields = "__all__"


class SubscriptionsSerailizer(ModelSerializer):

    class Meta :
        model = Subscription
        fields = "__all__"