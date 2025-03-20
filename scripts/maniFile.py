import shutil
import os

def create_folder(folder_path):
    try:
        # Create the folder at the specified path.
        os.mkdir(folder_path)
        print(f"Folder created successfully at '{folder_path}'.")
    except FileExistsError:
        print(f"Error: Folder already exists at '{folder_path}'.")

# Example usage:


def move_file(source_path, destination_path):
    try:
        # Move the file from the source path to the destination path.
        shutil.move(source_path, destination_path)
        print(f"File moved successfully from '{source_path}' to '{destination_path}'.")
    except FileNotFoundError:
        print("Error: Source file not found.")
    except FileExistsError:
        print(f"Error: A file already exists at '{destination_path}'.")

import shutil
def delete_folder(folder_path):
    try:
        # Delete the folder and its contents recursively.
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' and its contents have been deleted.")
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to delete folder '{folder_path}'.")