from .models import QuoteModel
from rest_framework import serializers

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteModel
        fields = "__all__"
