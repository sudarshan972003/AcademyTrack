from django.shortcuts import render
from rest_framework.response import Response
from .models import QuoteModel
from .ser import QuoteSerializer
from rest_framework.decorators import api_view

@api_view(["GET","POST"])
def home(request):
    quotes = QuoteModel.objects.all()
    serializer = QuoteSerializer(quotes, many=True)
    return Response(serializer.data)

