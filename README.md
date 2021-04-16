### Ubuntu 18.04

* First install openimageio from source and globally! :-(
* Some libs:
'''
sudo apt-get install libpugixml-dev libavdevice-dev
'''

* Then blender from source:
'''
cd $HOME/git
git clone https://git.blender.org/blender.git
cd blender
#git checkout -b v2.82a
git checkout blender-v2.83-release
git submodule update --init --recursive
mkdir lib; cd lib; svn checkout https://svn.blender.org/svnroot/bf-blender/tags/blender-2.82-release/lib/linux_centos7_x86_64; cd ..
mkdir build; cd build
cmake .. \
-DWITH_MOD_OCEANSIM=OFF \
-DWITH_PYTHON_INSTALL=OFF \
-DWITH_PYTHON_MODULE=ON \
-DWITH_INSTALL_PORTABLE=ON \
-DWITH_OPENCOLORIO=OFF \
-DCMAKE_INSTALL_PREFIX=$HOME/.local/lib/python3.7/site-packages
make -j $(command nproc)
nice -10 make -j1
make install
'''

#cmake .. -DWITH_PYTHON_INSTALL=OFF -DWITH_PYTHON_MODULE=ON -DWITH_INSTALL_PORTABLE=ON -DWITH_CYCLES_EMBREE=OFF -DWITH_MEM_JEMALLOC=OFF  -DOIIO=$HOME/git/oiio


# DID NOT WORK in 20.04 docker:
'''
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.7
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2

sudo apt-get install subversion
sudo apt-get install python3-pip

python3 -m pip install -U testresources wheel future-fstrings setuptools
python3 -m pip install bpy
bpy_post_install
'''
