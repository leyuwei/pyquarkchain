# make sure librocksdb-dev is uninstalled: sudo apt-get purge librocksdb-dev
# cd ~  # or wherever you like
git clone https://github.com/facebook/rocksdb.git
cd rocksdb && make shared_lib  # will probably take 10~20 min
sudo make install-shared
# go back to pyquarkchain directory
sudo pypy3 -m pip uninstall python-rocksdb
sudo pypy3 -m pip install --user --no-cache-dir python-rocksdb  # force reinstalling
