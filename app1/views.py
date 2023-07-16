from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from app1.models import Invoice, InvoiceDetail
from app1.serializers import InvoiceSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
