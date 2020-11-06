"""Forms to upload a csv file"""
#Django
from django import forms
#Model
from api.models import Dataset

#Utilities
from api.validators import validate_csv

class CSVUploadForm(forms.Form):
    """Uploading csv class"""
    csv_file = forms.FileField(validators=[validate_csv])
    