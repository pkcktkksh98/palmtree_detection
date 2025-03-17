# Palm Tree Detection
Detect palm tree using YOLO V8 model and having .gpkj as the final output.

## Step by step

### 1) Installation requirement
* Make sure you have install PYTHON and [GIT](https://git-scm.com/downloads) on your computer.
* Follow the step to install [Anaconda](https://docs.anaconda.com/free/anaconda/install/windows/) from the documentation.
* Press WINDOWS button and find Anaconda Prompt.
* ![Screenshot 2023-08-11 143325](https://github.com/pkcktkksh98/palmtree_detection/assets/71068962/9f7bd43a-53cd-4c6c-8fba-4f1c08c52054)
  
* Check if you have install CUDA by running this line in the prompt.

```bash
nvidia-smi
```

```bash
[OUTPUT]

+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.98                 Driver Version: 535.98       CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                     TCC/WDDM  | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 3080 Ti   WDDM  | 00000000:01:00.0  On |                  N/A |
| 31%   59C    P2             208W / 400W |   2416MiB / 12288MiB |     54%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
```
* If you did not get the output, you can go to this [link](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local). Once you have install, check the output again.
* Then you may change to the desired directory.

```bash
cd folder/directory
```
* Download this repository
```bash
git clone https://github.com/pkcktkksh98/palmtree_detection.git
cd palmtree_detection
```

* Download Yolo V8 repository [here](https://github.com/ultralytics/ultralytics.git) using `git clone`.
* Now install ultralytics for Yolo V8 usage.

```bash
conda install -c conda-forge ultralytics
```

* Now you should be able to run YOLO on your desktop. Next we are going to install [Slicing Aided Hyper Inference(SAHI)](https://github.com/obss/sahi) by following the [Installation details](https://github.com/obss/sahi#installation).

## 2) Folder Management
* In the palmtree_detection folder should contain
  - adds
  - image
  - sahi/sdpr.pt
  - README.md
  - Tree_Counting.ipynb

## 3) Execution
* To execute Jupyter Notebook, you can run `jupyter notebook` in Anaconda Prompt terminal and it will open in one of the browser.
* You may open the Tree Counting.ipynb file in Jupyter Notebook.
* Make sure to change the name of the estate.
* ![Screenshot 2023-08-11 142517](https://github.com/pkcktkksh98/palmtree_detection/assets/71068962/1f35e6ff-22c2-4325-ba83-41c074e1e49d)
* The "source" variable is the directory to the Folder that contains IMG folder and in it is the grided image of the estate.
* Then you may run the program by clicking Restart & Run All.
* ![Screenshot 2023-08-11 111104](https://github.com/pkcktkksh98/palmtree_detection/assets/71068962/1855b82b-a7fc-41ef-8202-a7e32b038180)

* There should be two (2) new folder created in the source directory.
  - predict
  - GPKJ

  


