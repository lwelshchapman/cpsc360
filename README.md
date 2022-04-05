# CPSC 360
## PyOpenGL Setup
### Installation
1. **Download software**:
  - Visual Studio Code (*if not installed already*)
    - https://code.visualstudio.com/download
  - Anaconda (*if not installed already*)
    - https://www.anaconda.com/products/distribution
  - (For Windows only) PyOpenGL-3.1.6 and PyOpenGL_accelerate-3.1.6
    - https://drive.google.com/drive/folders/1-Lr94q2Yfg1NXiNH2ZB9mOMY72GVXAI3?usp=sharing 
2. **Install software** (to default location)
  - Visual Studio Code
  - Anaconda
3. **Create python virtual environment and install PyOpenGL**
#### Windows
  - Open Anaconda Promopt Command Window
  - type `conda create --name cpsc360 python=3.8`
  - type `conda activate cpsc360`
  - Navigate to the folder where you downloaded PyOpenGL-3.1.6 and PyOpenGL_accelerate-3.1.6
    - For example, `cd Downloads\cpsc360`
  - type `pip install PyOpenGL-3.1.6-cp38-cp38-win_amd64.whl --force-reinstall` 
  - type `pip install PyOpenGL_accelerate-3.1.6-cp38-cp38-win_amd64.whl --force-reinstall`
#### MacOS
  - Open Terminal
  - type `conda create --name cpsc360 python=3.8`
  - type `conda activate cpsc360`
  - type `pip install PyOpenGL PyOpenGL_accelerate`
  - *Note: if you got errors when running the above command, try the following*
    - `pip3 install PyOpenGL`
### Run the helloword code
1. **Download code**
  - Under this github repo, go to Code -> Download Zip
  - Alternatively, ***if you are familiar with git/github***, you may also clone the code from: https://github.com/trudiQ/cpsc360.git (**pull only**)
    - if you want to save and upload your changes, ***fork it to your own repo before changing anything***
2. **Open VScode**
  - Install Python extention 
  - Open code folder, e.g.,'cpsc360'
  - Select Interpreter: Python 3.8.x ('cpsc360') *# 'cpsc360' is the conda environment you just created*
3. **Run python file 'hellopyopengl.py'**
