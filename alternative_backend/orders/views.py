from rest_framework import viewsets
from .models import Order, OrderRecord
from .serializers import OrderSerializer, OrderRecordSerializer
from common.auth import BaseAccess
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import order_service



class OrderViewSet(viewsets.ModelViewSet):
	
	serializer_class = OrderSerializer
	queryset = Order.objects.all()
	permission_classes = [BaseAccess]

	def get_serializer_context(self):
		return {"boards": self.request.data.get('boards',[])}


class OrderRecordViewSet(viewsets.ModelViewSet):

	serializer_class = OrderRecordSerializer
	queryset = OrderRecord.objects.all()
	permission_classes = [BaseAccess]


class OrderInfo(APIView):
	permission_classes = [BaseAccess]

	def get(self, request, format=None):
		response = order_service.return_order_info_for_all_companies()
		return Response(response)


class CompanyOrderInfo(APIView):
	permission_classes = [BaseAccess]

	def get(self, request, code, format=None):
		response = order_service.return_order_info(company_code=code)
		return Response(response)