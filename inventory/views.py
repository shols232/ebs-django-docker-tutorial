from random import randint

from django.utils.crypto import get_random_string

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import InventoryItem


class InventoryItemView(APIView):

    def get(self, request):
        """
        Retrieve InventoryItems.
        """
        inventory = [
            {'name': item.name, 'quantity': item.quantity}
            for item in InventoryItem.objects.all()
        ]

        return Response(inventory, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create InventoryItem from provided data, using defaults if data is not provided.
        """
        item = InventoryItem.objects.create(
            name=request.data.get('name', get_random_string(8)),
            quantity=request.data.get('quantity', randint(0, 50))
        )

        return Response(
            {'name': item.name, 'quantity': item.quantity}, 
            status=status.HTTP_201_CREATED
        )

