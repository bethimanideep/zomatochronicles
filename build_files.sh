#!/bin/bash

echo "BUILD START"

# Install project dependencies
python3.9 -m pip install -r requirements.txt

# Apply database migrations
python3.9 manage.py migrate

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"
