#Test library
from django.test import TestCase, Client

#Django REST
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

#Django REST Framework testing
from rest_framework.test import APIClient

#File testing
from unittest import mock

#Validators library
from api.validators import read_csv_data

#Models
from api.models import Dataset, Row

#Serializers
from api.serializers import DataSerializer, RowSerializer

#Utilities
from django.core.files import File
from django.urls import reverse

#Views
from api.views import data_list

"""Initialize APIClient app"""
client = Client()
class ParseCSVTest(TestCase):
    """CSV Headers unit testing"""
    def setUp(self):
        self.data = 'backend_test.csv'

    def test_csv_read_data_headers(self):
        self.assertEqual(read_csv_data(self.data)[0], 
        ['latitude', 'longitude','client_id', 'client_name'])

class DatasetTestCase(TestCase):
    """Dataset uploading unit testing module"""

    def test_save_upload(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test'
        file_model = Dataset(upload=file_mock)
        self.assertEqual(file_model.upload.name, file_mock.name)

class GetAllDatasets(TestCase):
    """Test module to GET all Datasets"""
    def setUp(self):
        file_mock=mock.MagicMock(spec=File)
        file_mock.name = 'File_test'

        Dataset.objects.create(
            name="Test 1", 
            upload=file_mock
        )
        Dataset.objects.create(
            name="Test 2", 
            upload=file_mock
        )
        Dataset.objects.create(
            name="Test 3", 
            upload=file_mock
        )
        Dataset.objects.create(
            name="Test 4", 
            upload=file_mock
        )
    
    def test_get_all_datasets(self):
        response = client.get(reverse('all_data'))
        datasets = Dataset.objects.all()
        serializer = DataSerializer(datasets, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
