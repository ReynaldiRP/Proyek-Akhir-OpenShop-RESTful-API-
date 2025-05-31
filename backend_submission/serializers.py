from rest_framework import serializers
from rest_framework.reverse import reverse
from product_app.models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()

    """
    Serializer for the Product model.
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'shop', 'location', 'sku', 'description', 'price', 'discount',
                  'category', 'stock', 'is_available', 'is_delete', 'picture', '_links']

    def get__links(self, obj):
        """
        Returns the links for the Product item.
        """
        request = self.context.get('request')
        return [
            {
                "rel": "self",
                "href": reverse('product-list', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('product-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('product-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('product-detail', kwargs={'pk': obj.pk}, request=request),
                "action": "DELETE",
                "types": ["application/json"]
            }
        ]