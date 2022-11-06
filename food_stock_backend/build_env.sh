#!/usr/bin/env bash

python3 -m venv venv
set -e
source $PWD/venv/bin/activate
pip3 install .
deactivate
python3 manage.py makemigrations
python3 manage.py migrate

