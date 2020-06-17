from rest_framework.serializers import ModelSerializer, StringRelatedField
from shoes import models


class ShoeSerializer(ModelSerializer):

    class Meta:
        model = models.Shoe
        fields = '__all__'


class ShoeTypeSerializer(ModelSerializer):
    class Meta:
        model = models.ShoeType
        fields = '__all__'


class ShoeColorSerializer(ModelSerializer):
    class Meta:
        model = models.ShoeColor
        fields = '__all__'


class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = '__all__'
