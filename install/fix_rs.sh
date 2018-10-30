# make sure librocksdb-dev is uninstalled: sudo apt-get purge librocksdb-dev
# cd ~  # or wherever you like
sudo apt-get install cmake
sudo make uninstall INSTALL_PATH=/usr
sudo apt-get install build-essential libsnappy-dev zlib1g-dev libbz2-dev libgflags-dev
git clone https://github.com/facebook/rocksdb.git
cd rocksdb
mkdir build && cd build
cmake .
make
make install-shared INSTALL_PATH=/usr
sudo pypy3 -m pip uninstall python-rocksdb
sudo pypy3 -m pip install "Cython>=0.20"
sudo pypy3 -m pip install git+git://github.com/twmht/python-rocksdb.git
