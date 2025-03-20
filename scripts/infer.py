from scripts.img_size import get_image_size
from scripts.convert import convert_bbox_to_yolo, convert_pickle_to_yolo
from scripts.maniFile import create_folder, move_file,delete_folder
def print_tif_file_names(folder_path,MODEL,oriPath,source):
    print("START")
    try:
        import os
        import time
        import pickle
        import subprocess
        # List all files in the folder.
        files = os.listdir(folder_path)
        print(files)

        # Filter only the .tif files and print their names.
        i=0
        for file in files:
            print(file)
            if file.lower().endswith('.tif'):
                i=i+1
                print("Start prediction: "+str(i)+" out of "+str(len(files)))
                #=========================================================================#
                #START PREDICTION
                #=========================================================================#
                start_time = time.time()

                command = f"sahi predict --slice_width 640 --slice_height 640 --overlap_height_ratio 0.3 --overlap_width_ratio 0.3 --model_confidence_threshold 0.40 --source {folder_path}{file} --model_path sahi/{MODEL} --model_type yolov8 --export_pickle"

                try:
                    subprocess.run(command, shell=True, check=True)
                    print("SAHI prediction completed successfully!")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Elapsed time: {elapsed_time:.2f} seconds")
                #=========================================================================#                
                #PICKLE TO YOLO                
                #=========================================================================#
                IMG_NAME = os.path.splitext(file)[0]
                print(IMG_NAME)
                dir_path = f'{oriPath}/palmtree_detection/runs/predict/exp/'
                pickle_file = dir_path+'pickles/'+IMG_NAME+'.pickle'
                # Load data from pickle file
                with open(pickle_file, 'rb') as f:
                    data = pickle.load(f)
                print("DATA LOADED")
                #=========================================================================#
                #Image Size
                #=========================================================================#
                # Usage
                image_width, image_height = get_image_size(folder_path+file)
                print("Width:", image_width)
                print("Height:", image_height)
                #=========================================================================#
                #Converting Pickle to YOLO
                #=========================================================================#
                

                # Convert data to YOLO format
                yolo_data = []
                for item in data:
                    yolo_txt = convert_pickle_to_yolo(str(item), image_width, image_height)
                    if yolo_txt:
                        yolo_data.append(yolo_txt)
                # print(yolo_data)
                #=========================================================================#
                #Save YOLO text file
                #=========================================================================#
                # Save YOLO data to a text file
                file_path=dir_path+IMG_NAME+'.txt'
                with open(file_path, 'w') as f:
                    for row in yolo_data:
                        f.write(row + '\n')

                print("CONVERSION COMPLETE")
                
                #=========================================================================#
                #Move
                #=========================================================================#

                folder_path = source+'/predict'
                destination_path = folder_path+"/"+IMG_NAME+'.txt'

                create_folder(folder_path)
                move_file(file_path, folder_path)
                
                #=========================================================================#
                #  Delete previous prediction folder(exp)
                #=========================================================================# 
                # Example usage:
                # folder_path = 'D:/7_Project/palmtree_detection/runs/predict/exp'

                delete_folder(dir_path)                
                #=========================================================================#
                
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to access folder '{folder_path}'.")