import os
import time
from scripts.infer import print_tif_file_names
from scripts.geopkg import gen_gpkj

os.chdir("..")
listDir = os.listdir()
oriPath = os.getcwd()
os.chdir("palmtree_detection")
print(os.path.join(oriPath, listDir[0]))

LADANG = input("Nama Ladang:")
source = f'{os.path.join(oriPath, listDir[0])}/{LADANG}'#directory to a folder that contains image and prediction label.
IMG_PATH = source+'/IMG/'#+IMG_NAME+".tif"
MODEL = "sdpr.pt"
print("imgPath: "+IMG_PATH)

#============================================================
#                       INFERENCING
#============================================================
start_time = time.time()
print_tif_file_names(IMG_PATH,MODEL,oriPath,source)
end_time = time.time()
elapsed_time = (end_time - start_time)/60
print(f"Elapsed time: {elapsed_time:.2f} minutes")
print("PREDICITON FINISH")
#==============================================================
#                       GEOPACKAGING
#==============================================================

gen_gpkj(source,LADANG,IMG_PATH)