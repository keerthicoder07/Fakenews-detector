#!/usr/bin/env bash

# Install Python dependencies
pip install -r requirements.txt

# Build React frontend
npm install
npm run build

# Start FastAPI
uvicorn backend.main:app --host 0.0.0.0 --port $PORT

