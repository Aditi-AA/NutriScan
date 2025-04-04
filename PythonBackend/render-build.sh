#!/bin/bash

# Install system dependencies (libzbar0)
sudo apt-get update
sudo apt-get install -y libzbar0

# Verify installation
echo "Checking for zbar library:"
ldconfig -p | grep zbar

# Print library paths for debugging
echo "Library paths:"
echo $LD_LIBRARY_PATH

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt