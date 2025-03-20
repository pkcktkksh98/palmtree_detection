import os
from adds.GenUtils import question, get_types, get_paths, make_folder, askPath, askFile, askInt, askFloat
from adds.DLUtils import get_train_cfg, link_dataset, get_model_cfg, get_args
from adds.inf2shp import det2gdf, copyfiles, get_world_file
import geopandas as gpd
import pandas as pd
import torch
from pyproj import CRS
from IPython.display import Image

home = os.getcwd()
os.chdir(home)
print(home)
import shutil
import os
from shapely.geometry import Point, Polygon
from pyproj import CRS
import fiona

def gen_gpkj(source,LADANG,IMG_PATH):
    DST_CRS= CRS.from_wkt('PROJCRS[\"Equirectangular MARS\",BASEGEOGCRS[\"GCS_MARS\",DATUM[\"unnamed\",ELLIPSOID[\"unnamed\",3396036.8126024,0,LENGTHUNIT[\"metre\",1,ID[\"EPSG\",9001]]]],PRIMEM[\"Reference meridian\",0,ANGLEUNIT[\"degree\",0.0174532925199433,ID[\"EPSG\",9122]]]],CONVERSION[\"unnamed\",METHOD[\"Equidistant Cylindrical (Spherical)\",ID[\"EPSG\",1029]],PARAMETER[\"Latitude of 1st standard parallel\",-5,ANGLEUNIT[\"degree\",0.0174532925199433],ID[\"EPSG\",8823]],PARAMETER[\"Longitude of natural origin\",180,ANGLEUNIT[\"degree\",0.0174532925199433],ID[\"EPSG\",8802]],PARAMETER[\"False easting\",0,LENGTHUNIT[\"metre\",1],ID[\"EPSG\",8806]],PARAMETER[\"False northing\",0,LENGTHUNIT[\"metre\",1],ID[\"EPSG\",8807]]],CS[Cartesian,2],AXIS[\"easting\",east,ORDER[1],LENGTHUNIT[\"metre\",1,ID[\"EPSG\",9001]]],AXIS[\"northing\",north,ORDER[2],LENGTHUNIT[\"metre\",1,ID[\"EPSG\",9001]]]]')
    # print("test:"+source)
    detections = get_paths(source+'/predict/', 'txt')
    detections_paths = [source+'/predict/'+file for file in detections]
    # print(detections_paths)
    geodataframes = det2gdf(detections_paths, 'tif', IMG_PATH)

    # Initialize geoshapes with the first GeoDataFrame
    geoshapes = geodataframes[0].copy()  # Use copy() to avoid modifying the original

    # Set the initial CRS
    init_crs = geoshapes.crs

    # Iterate over the rest of the GeoDataFrames
    for geo in geodataframes[1:]:
        # Transform to the common CRS if necessary
        if geo.crs != init_crs:
            geo = geo.to_crs(init_crs)
        
        # Concatenate the GeoDataFrames
        geoshapes = gpd.GeoDataFrame(pd.concat([geoshapes, geo], ignore_index=True), crs=init_crs)

    # Rest of your code remains the same
    fname = make_folder(source, LADANG)

    print('fname: ' + fname)
    geoshapes.to_file(fname + '/' + LADANG + '.gpkg', driver='GPKG', crs=init_crs, engine='fiona')

    source_path = source + '/' + LADANG
    destination_path = source + '/GPKJ'
    shutil.move(source_path, destination_path)

    print('AFIQ HENSEM.')
