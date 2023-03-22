import arcgis
from arcgis.features import FeatureLayer

lyr_url = 'https://mapprod.cadm.harvard.edu/server/rest/services/Hosted/Facilities/FeatureServer/8'

layer = FeatureLayer(lyr_url)

hu_facilities = layer.query(where="1=1", out_fields='facility_id,name,locality,address,source_name', return_geometry=False, return_centroid=True)
print(hu_facilities.features)