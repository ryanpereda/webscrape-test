from rest_framework import serializers

from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )

    class Meta:
        model = Quote
        fields = [
            "id",
            "text",
            "author",
            "tags",
            "scraped_at",
        ]