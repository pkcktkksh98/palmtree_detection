@echo off
echo Installing Ultralytics...
pip install ultralytics

echo Installing Ultralytics via Conda...
conda install -c conda-forge ultralytics -y

echo Installing SAHI...
pip install sahi

echo Installing Shapely via Conda...
conda install -c conda-forge shapely -y

echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

echo Installation completed!
