# How to install OpenCV3 on Linux
The following is what I had to do to get OpenCV3 installed on my computer. I was mostly following along with the [OpenCV: installation in Linux](http://docs.opencv.org/master/d7/d9f/tutorial_linux_install.html) instructions and then later on [Building and Installing OpenCV3](https://blog.kevin-brown.com/programming/2014/09/27/building-and-installing-opencv-3.html).

## Installing dependencies
I first had to install the following:

    sudo apt-get install build-essential
    sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
    sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

## Getting OpenCV3
Next I went into my projects directory and cloned the OpenCV repository into it:

    cd ~/Projects
    git clone https://github.com/opencv/opencv.git

## Created virtual environment
I tried installing OpenCV to my system but it kept using Python 2.7.12, so I decided to run the installation under an [Anaconda](https://www.continuum.io/) virtual environment instead:

    conda create -n thumbler
    cd ~/opencv
    mkdir release
    cd !$
    cmake -DBUILD_TIFF=ON -DBUILD_opencv_java=OFF -DWITH_CUDA=OFF -DENABLE_AVX=ON -DWITH_OPENGL=ON -DWITH_OPENCL=ON -DWITH_IPP=ON -DWITH_TBB=ON -DWITH_EIGEN=ON -DWITH_V4L=ON -DWITH_VTK=OFF -DBUILD_TESTS=OFF -DBUILD_PERF_TESTS=OFF -DCMAKE_BUILD_TYPE=RELEASE -DBUILD_opencv_python2=OFF -DCMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") -DPYTHON3_EXECUTABLE=$(which python3) -DPYTHON3_INCLUDE_DIR=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") -DPYTHON3_PACKAGES_PATH=$(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") ..
    make -j4
    make install

## Test OpenCV installation
Making sure that I was still in my virtual environment, I used the following commands:

    python
    import cv2

If you did not get any errors, CONGRATULATIONS! You have just successfully installed OpenCV3 on your system.

## Troubleshooting
> NOTE: I had issues with my installation. Specifically with **libstdc++.so.6** and **libgomp.so.1**. The fix was to remove both of those files and create symlinks to my system ones.

To find out where my Anaconda installation was I used the following command after exiting the python interpreter and deactivating the virtual environment:

    exit()
    source deactivate
    which python
    ~/anaconda3/bin/python

With that information I simply issued the following commands:

    cd ~/anaconda3/lib
    rm ibstdc++.so.6 libgomp.so.1
    ln -s /usr/lib/x86_64-linux-gnu/libstdc++.so.6
    ln -s /usr/lib/x86_64-linux-gnu/libgomp.so.1

## Sample file
I've included a script that I found on [scivision.co](https://www.scivision.co/anaconda-python-opencv3/). You can use it to further test your OpenCV installation:

    python ./opencv_sample.py
    227.5144271879671 fps

![static](static.png)

My machine is old, so you will probably getting better results.
