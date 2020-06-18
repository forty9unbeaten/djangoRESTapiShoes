from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField
from shoes import models


class ShoeSerializer(HyperlinkedModelSerializer):
    manufacturer = StringRelatedField()
    color = StringRelatedField()
    shoe_type = StringRelatedField()

    class Meta:
        model = models.Shoe
        fields = [
            'size',
            'brand_name',
            'material',
            'fasten_type',
            'manufacturer',
            'color',
            'shoe_type'
        ]


class ShoeTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.ShoeType
        fields = '__all__'


class ShoeColorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.ShoeColor
        fields = '__all__'


class ManufacturerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = '__all__'
