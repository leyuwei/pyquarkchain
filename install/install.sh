#!/bin/bash
#Modified by LeYuwei 2018.10.16
sudo apt-get update

sudo apt-get install -y git gcc make libffi-dev pkg-config zlib1g-dev libbz2-dev \
libsqlite3-dev libncurses5-dev libexpat1-dev libssl-dev libgdbm-dev \
libgc-dev python-cffi \
liblzma-dev libncursesw5-dev libgmp-dev liblz4-dev librocksdb-dev \
libsnappy-dev zlib1g-dev libbz2-dev libzstd-dev

#Following package only needs to be downloaded once.
wget https://bitbucket.org/pypy/pypy/downloads/pypy3-v6.0.0-linux64.tar.bz2
sudo tar -x -C /opt -f  pypy3-v6.0.0-linux64.tar.bz2
sudo mv /opt/pypy3-v6.0.0-linux64 /opt/pypy3
sudo ln -s /opt/pypy3/bin/pypy3 /usr/local/bin/pypy3

curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
sudo pypy3 get-pip.py --user
export PATH=~/.local/bin:$PATH
rm get-pip.py

git clone https://github.com/QuarkChain/pyquarkchain.git
cd pyquarkchain
sudo pypy3 -m pip --default-timeout=800 install --user -e .

# https://github.com/ethereum/pyethapp/issues/274#issuecomment-385268798
sudo pypy3 -m pip uninstall pyelliptic
sudo pypy3 -m pip --default-timeout=120 install --user https://github.com/mfranciszkiewicz/pyelliptic/archive/1.5.10.tar.gz#egg=pyelliptic

pypy3 -m unittest  # should succeed
