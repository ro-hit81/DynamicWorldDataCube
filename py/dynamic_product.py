import ee
from config import service_account, ee_key, dynamic_world_v1
credentials = ee.ServiceAccountCredentials(service_account, ee_key)
ee.Initialize(credentials)

class Product:
    def __init__(self, roi):
        self.roi = roi
        
    def extent(self):
        extent = ee.Geometry.Rectangle([ self.roi['LonMin'], self.roi['LatMin'], self.roi['LonMax'], self.roi['LatMax']])
        
        return extent
    
    def select_product(self):
        image_collection = ee.ImageCollection(dynamic_world_v1)
        image_collection = image_collection.filterDate(self.roi['start_date'], self.roi['end_date'])
        image_collection = image_collection.filterBounds(self.extent())
        
        total_image_collected = image_collection.size().getInfo()
        
        return image_collection
    
    def export_label_collection(self):
        
        pass
        
        