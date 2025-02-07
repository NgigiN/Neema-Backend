from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MilkProduct, Soda, Booking
from .serializers import MilkSerializer, SodaSerializer, BookingSerializer


class ReserveMilkView(APIView):
    def post(self, request, product_name):
        quantity = request.data.get('quantity')
        if quantity is None or quantity <= 0:
            return Response({"error": "Quantity must be a positive integer"}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(MilkProduct, name=product_name)

        if product.stock < quantity:
            return Response({"error": "Not enough stock"}, status=status.HTTP_400_BAD_REQUEST)

        product.stock -= quantity
        product.save()
        return Response(MilkSerializer(product).data, status=status.HTTP_200_OK)


class ReserveSodaView(APIView):
    def post(self, request, product_name):
        quantity = request.data.get('quantity')
        if quantity is None or quantity <= 0:
            return Response({"error": "Quantity must be a positive integer"}, status=status.HTTP_400_BAD_REQUEST)

        product = get_object_or_404(Soda, name=product_name)

        if product.stock < quantity:
            return Response({"error": "Not enough stock"}, status=status.HTTP_400_BAD_REQUEST)

        product.stock -= quantity
        product.save()
        return Response(SodaSerializer(product).data, status=status.HTTP_200_OK)


class GetMilkPriceView(APIView):
    def get(self, request):
        products = MilkProduct.objects.all()
        serializer = MilkSerializer(products, many=True)
        return Response(serializer.data)


class GetSodaPriceView(APIView):
    def get(self, request):
        products = Soda.objects.all()
        serializer = SodaSerializer(products, many=True)
        return Response(serializer.data)


class BookingView(APIView):
    def post(self, request):
        customer_name = request.data.get('customer_name')
        total_price = request.data.get('total_price')
        # Expecting a list of product details
        products = request.data.get('items')

        if not customer_name or not total_price or not products:
            return Response({"error": "Please provide all required fields"}, status=status.HTTP_400_BAD_REQUEST)

        for product in products:
            product_name = product.get('product_name')
            quantity = product.get('quantity')
            price_per_litre = product.get('price_per_litre')

            if not product_name or not quantity or not price_per_litre:
                return Response({"error": "Each product must have a name, quantity, and price per litre"},
                                status=status.HTTP_400_BAD_REQUEST)

            # Check if the product is a MilkProduct or Soda
            db_product = MilkProduct.objects.filter(
                name__iexact=product_name).first()
            if not db_product:
                db_product = Soda.objects.filter(
                    name__iexact=product_name).first()

            if not db_product:
                return Response({"error": f"Product '{product_name}' not found"}, status=status.HTTP_400_BAD_REQUEST)

            if db_product.stock < quantity:
                return Response({"error": f"Not enough stock for product '{product_name}'"},
                                status=status.HTTP_400_BAD_REQUEST)

            # Deduct the stock
            db_product.stock -= quantity
            db_product.save()

        # Create the booking
        booking = Booking.objects.create(
            customer_name=customer_name,
            total_price=total_price,
            items=products  # Ensure Booking model has a JSONField for products
        )

        return Response({"message": "Booking successful", "booking_id": booking.id}, status=status.HTTP_201_CREATED)


class BookingHistoryView(APIView):
    def get(self, request, name):
        if not name:
            return Response({"error": "Customer name parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        bookings = Booking.objects.filter(
            customer_name=name).order_by('-created_at')
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Admin Views


class RestockMilkView(APIView):
    def post(self, request, product_name):
        quantity = request.data.get('quantity')
        if quantity is None or quantity <= 0:
            return Response({"error": "Quantity must be a positive integer"}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(MilkProduct, name=product_name)

        product.stock += quantity
        product.save()
        return Response(MilkSerializer(product).data, status=status.HTTP_200_OK)


class RestockSodaView(APIView):
    def post(self, request, product_name):
        quantity = request.data.get('quantity')
        if quantity is None or quantity <= 0:
            return Response({"error": "Quantity must be a positive integer"}, status=status.HTTP_400_BAD_REQUEST)

        product = get_object_or_404(Soda, name=product_name)

        product.stock += quantity
        product.save()
        return Response(SodaSerializer(product).data, status=status.HTTP_200_OK)
