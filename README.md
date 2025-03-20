# Tree Counting Detection Model

## Overview
This guide provides step-by-step instructions for setting up, preparing data, and executing the tree-counting detection model.

---

## **Step 1: Set Up the Environment**

### **1.1 Copy Project Files**
Copy both folders from:
```
\Aeca_nas\gis\01_Projects\01_Clients\0020_PKPS\00_TreeCounting
```
to your local working directory.

**Important:** Do **NOT** remove the `00_` annotation from the folder names.

**Example Directory Structure:**
```
D:\Projects\00_PKPS\BADAK\IMG
```

### **1.2 Install Required Software**
Ensure that the following software is installed on your system:

- **Python**: Download and install the latest version from [python.org](https://www.python.org).
- **Anaconda**: Manage Python packages and environments with Anaconda. Install it from [Anaconda Documentation](https://docs.anaconda.com/).

#### **Check and Install Anaconda (if needed)**
If unsure about your current Anaconda installation:
1. Open **Settings** > **Apps** > **Installed Apps**.
2. Search for **Anaconda3**.
3. Uninstall any existing Anaconda versions.
4. Download and install the latest Anaconda version.

### **1.3 Create and Activate a Virtual Environment**
Using **Anaconda Prompt**, set up a virtual environment to manage dependencies:

1. **Create a new virtual environment:**
   ```bash
   conda create -n palmtree -y
   ```
2. **Activate the environment:**
   ```bash
   conda activate palmtree
   ```

### **1.4 Install Python Dependencies**
#### **Using Setup Script**
1. **Navigate to the repository directory**:
   ```bash
   D:
   cd path/to/palmtree_detection
   ```
2. **Run the setup script**:
   ```bash
   setup.bat
   ```
   *This will install all required dependencies from `requirements.txt`.*

---

## **Step 2: Prepare the Data**

### **2.1 Organize Input Images**
Ensure that your input images are properly structured.  
**Example Directory:**
```
D:\Projects\00_PKPS\BADAK\IMG
```

### **2.2 Preprocess Images**
1. **Resize Large Images**:  
   - Cut the image into smaller sizes.
   - Recommended size: **40,000 × 40,000 pixels**.  
   - If **Out Of Memory (OOM)** errors occur, reduce the size further.
  
2. **Save Images in the Correct Folder**:  
   - Export the processed images into the **IMG** folder.

---

## **Step 3: Execute the Model**

### **3.1 Run the Detection Script**
1. **Open Anaconda Prompt**.
2. **Navigate to your working directory**:
   ```bash
   D:
   cd path/to/palmtree_detection
   ```
3. **Run the script**:
   ```bash
   python tree_counting.py
   ```
4. **Enter the Plantation Name (LADANG)** when prompted:
   - Example input: `BADAK` (folder name that contains the `IMG` folder).

---

### **3.2 Retrieve the Output (GPKJ File)**
- The generated **GeoPackage (.gpkg)** file will be stored in the same directory as the **IMG** folder.
- **Example Path:**
  ```
  D:\Projects\00_PKPS\BADAK\BADAK.gpkg
  ```

---

## **Additional Notes**
- Always verify that the **tree_counting.py** script is in the correct directory before execution.
- If you encounter errors, ensure all dependencies are installed and re-run the **setup.bat** file.

---

**Author:** AECA Solutions  
**Project:** Palm Tree Counting Detection Model  
**Date:** March 2025

