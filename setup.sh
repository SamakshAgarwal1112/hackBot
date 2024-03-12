#!/bin/bash

# Create and activate virtual environment
python -m venv env
source env/bin/activate

# Navigate to the backend directory
cd backend

# Install Django dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Start Django server in the background
python manage.py runserver &

# Sleep for a few seconds to ensure server is up
sleep 5

# Navigate to the frontend directory
cd ../frontend

# Install frontend dependencies
npm install

# Start React frontend
npm run dev