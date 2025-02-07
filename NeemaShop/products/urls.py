from webbrowser import get
from django.urls import path
from .views import RestockMilkView, ReserveMilkView, RestockSodaView, ReserveSodaView, GetMilkPriceView, GetSodaPriceView, BookingHistoryView, BookingView


urlpatterns = [
    path('milk/subtract/<str:product_name>/',
         ReserveMilkView.as_view(), name='reserve-milk'),
    path('milk/restock/<str:product_name>/',
         RestockMilkView.as_view(), name='restock-milk'),
    path('soda/subtract/<str:product_name>/',
         ReserveSodaView.as_view(), name='reserve-soda'),
    path('soda/restock/<str:product_name>/',
         RestockSodaView.as_view(), name='restock-soda'),
    path('milk/price/',
         GetMilkPriceView.as_view(), name='get-milk-price'),
    path('soda/price/',
         GetSodaPriceView.as_view(), name='get-soda-price'),
    path('bookings/', BookingView.as_view(), name='make-booking'),
    path('bookings/history/<str:name>',
         BookingHistoryView.as_view(), name='booking-history'),
]
