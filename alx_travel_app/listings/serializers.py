
from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.
    """
    owner_username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price', 'city', 'country', 'address', 'owner_username', 'created_at']

class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    """
    listing_title = serializers.CharField(source='listing.title', read_only=True)
    guest_username = serializers.CharField(source='guest.username', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'listing_title', 'guest_username', 'check_in_date', 'check_out_date', 'total_price', 'created_at']
