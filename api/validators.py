"""CSV Validators"""
#Utilities
import os, csv

#Django
from django.core.exceptions import ValidationError

def validate_csv(value):
    """This function allow us to upload only csv files"""
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.csv']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Extension no soportada, revisa el archivo.')

def read_csv_data(data):

    with open(data,'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data