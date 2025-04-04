#!/bin/bash

# Download and install libzbar
curl -fsSL http://ftp.us.debian.org/debian/pool/main/z/zbar/libzbar0_0.23.90-1_amd64.deb -o libzbar.deb
dpkg -x libzbar.deb .

# Verify installation
ls -l ./usr/lib/x86_64-linux-gnu/
ls -l ./usr/lib/

# Set the library path
export LD_LIBRARY_PATH=$PWD/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH

# Print library paths to debug
echo "LD_LIBRARY_PATH: $LD_LIBRARY_PATH"

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
