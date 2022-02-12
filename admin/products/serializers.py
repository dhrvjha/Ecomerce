
from rest_framework import serializers
from .models import Products, ProductImages


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

    def save(self, **kwargs):
        self.instance = super().save(**kwargs)
        if "image_url" in self.initial_data:
            image_data = self.initial_data.getlist("image_url")
            for url in image_data:
                ProductImages(product=self.instance, image_url=url).save()
        return self.instance
