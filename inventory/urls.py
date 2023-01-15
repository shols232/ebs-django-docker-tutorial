from django.urls import path
from .views import InventoryItemView


urlpatterns = [
    path('inventory-item', InventoryItemView.as_view())
]