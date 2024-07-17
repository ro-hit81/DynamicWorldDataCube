import ee
import json
import os
from config import service_account, ee_key, dynamic_world_v1, layout_path
credentials = ee.ServiceAccountCredentials(service_account, ee_key)
ee.Initialize(credentials, opt_url='https://earthengine-highvolume.googleapis.com')

class Product:
    def __init__(self, roi, layout_path):
        self.roi = roi
        self.layout_path = layout_path
        
    def bound(self):
        return ee.Geometry.Rectangle([ self.roi['LonMin'], self.roi['LatMin'], self.roi['LonMax'], self.roi['LatMax']])

    
    def select_product(self):
        image_collection = ee.ImageCollection(dynamic_world_v1)
        image_collection = image_collection.filterDate(self.roi['start_date'], self.roi['end_date'])
        image_collection = image_collection.filterBounds(self.bound())
        
        total_image_collected = image_collection.size().getInfo()
        
        dates = image_collection.aggregate_array("system:time_start")
        
        def iso_date(date):
            return ee.Date(date).format('yyyy-MM-dd\'T\'HH:mm:ss')
        
        iso_dates = dates.map(iso_date).getInfo()
        
        try:
            with open(self.layout_path, 'r') as file:
                json_data = json.load(file)
        except FileNotFoundError:
            print(f"File {self.layout_path} not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {self.layout_path}.")
            return None
        
        json_data['appearance']['colortype']['times'] = iso_dates
        
        try:
            with open('./layout.json', 'w') as file:
                json.dump(json_data, file, indent=2)
            print(f"Updated layout saved to {layout_path}.")
        except IOError:
            print(f"Error writing to file {layout_path}.")
            return None
        
        return image_collection, total_image_collected, iso_dates

    
    def export_label_collection(self):
        
        pass

