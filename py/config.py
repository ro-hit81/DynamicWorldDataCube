import os
import ee

root_dir        = r'D:\OneDrive - Universität Salzburg\EO_Analytics'
project_dir     = os.path.join(root_dir, 'Sem4GEE')

service_account = 'for-eo-analytics@rohit-81.iam.gserviceaccount.com'
ee_key          = os.path.join(project_dir, 'keys', 'rohit-81-updated_permissions.json')

ROI = {
    'cityName'  : 'Salzburg',
    'LatMax'    : 47.82671039502662,
    'LatMin'    : 47.76259229074499,
    'LonMax'    : 13.104838502127727,
    'LonMin'    : 12.999095093924602,
    'start_date': '2020-05-01',
    'end_date'  : '2020-06-20',
}

dynamic_world_v1 = 'GOOGLE/DYNAMICWORLD/V1'
