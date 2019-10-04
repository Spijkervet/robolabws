#!/bin/bash

# LAMBDA STACK
LAMBDA STACK (test)
LAMBDA_REPO=$(mktemp) && \
wget -O${LAMBDA_REPO} https://lambdalabs.com/static/misc/lambda-stack-repo.deb && \
sudo dpkg -i ${LAMBDA_REPO} && rm -f ${LAMBDA_REPO} && \
sudo apt-get update && sudo apt-get install -y lambda-stack-cuda

# REMOVE CHROMIUM
sudo apt-get remove chromium-browser --purge
sudo rm -rf /home/*/.config/chromium
sudo rm -rf /home/*/.cache/chromium
sudo rm -rf /etc/chromium-browser

# REMOVE EMACS
sudo apt-get remove emacs emacs23 emacs24 --purge
sudo apt-get autoremove

# RESET WALLPAPER
sudo apt-get remove --purge lambda-wallpapers

# NVTOP
sudo apt install cmake libncurses5-dev libncursesw5-dev git -y
cd /tmp
git clone https://github.com/Syllo/nvtop.git
mkdir -p nvtop/build && cd nvtop/build
cmake ..

# If it errors with "Could NOT find NVML (missing: NVML_INCLUDE_DIRS)"
# try the following command instead, otherwise skip to the build with make.
cmake .. -DNVML_RETRIEVE_HEADER_ONLINE=True
make
sudo make install # You may need sufficient permission for that (root)


# INSTALL DOCKER
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
sudo usermod -a -G docker robolab


# INSTALL MINICONDA
# wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
# sudo bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda

# NETDATA
sh install_netdata.sh

