# Palm Tree Detection
Detect palm tree using YOLO V8 model and having .gpkj as the final output.

## Step by step

### 1) Installation requirement
* Make sure you have install PYTHON and [GIT](https://git-scm.com/downloads) on your computer.
* Follow the step to install [Anaconda](https://docs.anaconda.com/free/anaconda/install/windows/) from the documentation.
* Press WINDOWS button and find Anaconda Prompt.
  ![image](https://github.com/pkcktkksh98/palmtree_detection/assets/71068962/f2b1fa0c-6222-4aea-98bb-ee6dd488298b)
  
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

* 


