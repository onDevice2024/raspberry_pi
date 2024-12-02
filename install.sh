#!/bin/bash

sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-libcamera python3-kms++ python3-picamera2

mkdir venv
python3 -m venv --system-site-packages ./venv
source ./venv/bin/activate
pip install --upgrade pip


pip install opencv-python
