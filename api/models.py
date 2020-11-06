"""Model creator"""
#Django models
from django.contrib.gis.db import models
#Geospatial libraries
from django.contrib.gis.geos import Point
#Utilities
import csv, os


""" Models for dataset """
class Dataset(models.Model):
    """Information about csv file"""
    name = models.CharField(
        'Dataset name',
        max_length=95,
        default="Users dataset",)
    
    upload = models.FileField(
        'Dataset file', 
        upload_to='csvfiles',
        default=None,)

    date = models.DateTimeField(
        'Dataset date',
        auto_now_add=True,)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """Algorithm to save the file into tables"""
        super(Dataset, self).save(*args, **kwargs)
        #File reading 
        ifile = self.upload.open(mode='r')
        f = csv.reader(ifile)
        #Skips the headers
        header = next(f, None)
        if header != None:
        #Iterate over values in csv
            for row in f:
                stored = self.csv_dict(row)
                self.add_to_db(stored)
        self.upload.close()
    
    def csv_dict(self, row):
        """Returns the given row in a dict format"""
        return {
            'latitude': row[0], 
            'longitude': row[1], 
            'client_id': row[2], 
            'client_name': row[3],
            'point': Point(float(row[1]), float(row[0]))
            }    

    def add_to_db(self, stored):
        """Create the new object in db"""
        Row.objects.create(
            client_name=stored['client_name'],
            client_id=stored['client_id'],
            dataset=self,
            point=stored['point']
        )  

class Row(models.Model):
    """Data inserted into geospatial table"""
    dataset = models.ForeignKey(
        Dataset, 
        on_delete=models.CASCADE)
    
    point = models.PointField(
        'Geographical point',
        geography=True, 
        default=Point(0.0, 0.0))
     
    client_id = models.IntegerField(
        'Client identifier',
        )
        
    client_name = models.CharField(
        'Name of the client',
        max_length=45)
    
    def __str__(self):
        return f'nombre del cliente: {self.client_name} en {self.dataset} para el geopunto {self.point}'