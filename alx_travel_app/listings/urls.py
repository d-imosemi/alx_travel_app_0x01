from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet

# Initialize DRF router
router = DefaultRouter()

# Register endpoints with router
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')

# Export router URLs
urlpatterns = router.urls
