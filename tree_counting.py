import os
import time
import pickle
import subprocess
from scripts.infer import print_tif_file_names

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



# def print_tif_file_names(folder_path):
#     print("START")
#     try:
#         import os
#         # List all files in the folder.
#         files = os.listdir(folder_path)
#         print(files)

#         # Filter only the .tif files and print their names.
#         i=0
#         for file in files:
#             print(file)
#             if file.lower().endswith('.tif'):
#                 i=i+1
#                 print("Start prediction: "+str(i)+" out of "+str(len(files)))
#                 #=========================================================================#
#                 #START PREDICTION
#                 #=========================================================================#
#                 start_time = time.time()

#                 command = f"sahi predict --slice_width 640 --slice_height 640 --overlap_height_ratio 0.3 --overlap_width_ratio 0.3 --model_confidence_threshold 0.40 --source {IMG_PATH}{file} --model_path sahi/{MODEL} --model_type yolov8 --export_pickle"

#                 try:
#                     subprocess.run(command, shell=True, check=True)
#                     print("SAHI prediction completed successfully!")
#                 except subprocess.CalledProcessError as e:
#                     print(f"Error: {e}")

#                 end_time = time.time()
#                 elapsed_time = end_time - start_time
#                 print(f"Elapsed time: {elapsed_time:.2f} seconds")
#                 #=========================================================================#                
#                 #PICKLE TO YOLO                
#                 #=========================================================================#
#                 IMG_NAME = os.path.splitext(file)[0]
#                 print(IMG_NAME)
#                 dir_path = f'{oriPath}/palmtree_detection/runs/predict/exp/'
#                 pickle_file = dir_path+'pickles/'+IMG_NAME+'.pickle'
#                 # Load data from pickle file
#                 with open(pickle_file, 'rb') as f:
#                     data = pickle.load(f)
#                 print("DATA LOADED")
#                 #=========================================================================#
#                 #Image Size
#                 #=========================================================================#
#                 import imageio

#                 def get_image_size(file_path):
#                     image = imageio.imread(file_path)
#                     image_width, image_height = image.shape[1], image.shape[0]
#                     return image_width, image_height

#                 # Usage
#                 image_width, image_height = get_image_size(IMG_PATH+file)
#                 print("Width:", image_width)
#                 print("Height:", image_height)
#                 #=========================================================================#
#                 #Converting Pickle to YOLO
#                 #=========================================================================#
#                 import re

#                 def convert_bbox_to_yolo(bbox, image_width, image_height):
#                     x_min, y_min, x_max, y_max = bbox
#                     bbox_height = y_max - y_min
#                     bbox_width = x_max - x_min
#                     x_center = (x_max + x_min)/2.0
#                     y_center = (y_max + y_min)/2.0

#                     normalized_x = x_center / image_width
#                     normalized_y = y_center / image_height
#                     normalized_width = bbox_width / image_width
#                     normalized_height = bbox_height / image_height

#                     return normalized_x, normalized_y, normalized_width, normalized_height


#                 def convert_pickle_to_yolo(pickle_data, image_width, image_height):
#                     bbox_info = re.search(r'bbox: BoundingBox: <\((.*?), (.*?), (.*?), (.*?)\)', pickle_data)
#                     class_id_info = re.search(r'category: Category: <id: (.*?),', pickle_data)
#                     pred_info = re.search(r'score: PredictionScore: <value: (.*?)>,', pickle_data)

#                     if bbox_info and class_id_info:
#                         bbox = tuple(map(float, bbox_info.groups()))
#                         class_id = int(class_id_info.group(1))
#                         pred_id = float(pred_info.group(1))

#                         yolo_data = convert_bbox_to_yolo(bbox, image_width, image_height)
#                         yolo_txt = f"{class_id} {' '.join(map(str, yolo_data))} {pred_id}"
#                         return yolo_txt
#                     else:
#                         return None

#                 # Convert data to YOLO format
#                 yolo_data = []
#                 for item in data:
#                     yolo_txt = convert_pickle_to_yolo(str(item), image_width, image_height)
#                     if yolo_txt:
#                         yolo_data.append(yolo_txt)
#                 # print(yolo_data)
#                 #=========================================================================#
#                 #Save YOLO text file
#                 #=========================================================================#
#                 # Save YOLO data to a text file
#                 file_path=dir_path+IMG_NAME+'.txt'
#                 with open(file_path, 'w') as f:
#                     for row in yolo_data:
#                         f.write(row + '\n')

#                 print("CONVERSION COMPLETE")
                
#                 #=========================================================================#
#                 #Move
#                 #=========================================================================#
#                 import shutil
#                 import os

#                 def create_folder(folder_path):
#                     try:
#                         # Create the folder at the specified path.
#                         os.mkdir(folder_path)
#                         print(f"Folder created successfully at '{folder_path}'.")
#                     except FileExistsError:
#                         print(f"Error: Folder already exists at '{folder_path}'.")

#                 # Example usage:


#                 def move_file(source_path, destination_path):
#                     try:
#                         # Move the file from the source path to the destination path.
#                         shutil.move(source_path, destination_path)
#                         print(f"File moved successfully from '{source_path}' to '{destination_path}'.")
#                     except FileNotFoundError:
#                         print("Error: Source file not found.")
#                     except FileExistsError:
#                         print(f"Error: A file already exists at '{destination_path}'.")

#                 folder_path = source+'/predict'
#                 destination_path = folder_path+"/"+IMG_NAME+'.txt'

#                 create_folder(folder_path)
#                 move_file(file_path, folder_path)
                
#                 #=========================================================================#
#                 #  Delete previous prediction folder(exp)
#                 #=========================================================================#
                
#                 import shutil
#                 def delete_folder(folder_path):
#                     try:
#                         # Delete the folder and its contents recursively.
#                         shutil.rmtree(folder_path)
#                         print(f"Folder '{folder_path}' and its contents have been deleted.")
#                     except FileNotFoundError:
#                         print(f"Error: Folder '{folder_path}' not found.")
#                     except PermissionError:
#                         print(f"Error: Permission denied to delete folder '{folder_path}'.")

#                 # Example usage:
#                 # folder_path = 'D:/7_Project/palmtree_detection/runs/predict/exp'

#                 delete_folder(dir_path)                
#                 #=========================================================================#
                
#     except FileNotFoundError:
#         print(f"Error: Folder '{folder_path}' not found.")
#     except PermissionError:
#         print(f"Error: Permission denied to access folder '{folder_path}'.")
    
    
start_time = time.time()
print_tif_file_names(IMG_PATH,MODEL,oriPath,source)
end_time = time.time()
elapsed_time = (end_time - start_time)/60
print(f"Elapsed time: {elapsed_time:.2f} minutes")
print("PREDICITON FINISH")