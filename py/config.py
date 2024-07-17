import os
import ee
from dotenv import load_dotenv


# root_dir        = r'D:\OneDrive - Universität Salzburg\EO_Analytics'
root_dir        = r'/Users/rohitkhati/Library/CloudStorage/OneDrive-UniversitätSalzburg/EO_Analytics/'
project_dir     = os.path.join(root_dir, 'DynamicWorldDataCube')

service_account = os.getenv('SERVICE_ACCOUNT')
ee_key = os.getenv('EE_KEY')

ROI = {
    'cityName'  : 'Salzburg',
    # 'LatMax'    : 47.82671039502662,
    # 'LatMin'    : 47.76259229074499,
    # 'LonMax'    : 13.104838502127727,
    # 'LonMin'    : 12.999095093924602,
    'LatMax'    : 47.82432619322555,
    'LatMin'    : 47.789046341180615,
    'LonMax'    : 13.072778619673802,
    'LonMin'    : 13.010980523970677,
    'start_date': '2022-01-01',
    'end_date'  : '2022-05-02',
}

dynamic_world_v1 = 'GOOGLE/DYNAMICWORLD/V1'

layout_path = os.path.join(project_dir, 'layout.json')
