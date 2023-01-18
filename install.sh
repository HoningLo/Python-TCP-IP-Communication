#!/bin/bash
apt-get update
apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip setuptools
pip3 install -r requirements.txt