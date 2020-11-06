"""Main views of the app."""
#Django
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

#Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Rest Utils
from rest_framework.views import APIView
from rest_framework import generics

#Serializers
from api.serializers import DataSerializer, RowSerializer

#Forms
from api.forms import CSVUploadForm

#Filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
#Models
from api.models import Dataset, Row

"""------------------Functions---------------------"""

def create_data(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST,request.FILES)
        if form.is_valid():
            Dataset.objects.create(upload = request.FILES['csv_file'])
            messages.success(request, 'CSV uploaded successfully')            

    return render(request, 'upload_csv.html')


class data_list(generics.ListAPIView):
    """List the datasets loaded"""
    model = Dataset
    serializer_class = DataSerializer
    def get_queryset(self):
        return Dataset.objects.all()


class all_data(APIView):
    #List all Datasets or create a new one
    def get(self,request, format=None):
        dataset = Dataset.objects.all()
        serializer = DataSerializer(dataset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class row_list(generics.ListAPIView):
    """List the rows in the database"""
    model = Row
    serializer_class = RowSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('client_name','dataset__id')
    
    def get_queryset(self):
        return Row.objects.all()
