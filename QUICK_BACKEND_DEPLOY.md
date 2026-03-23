# Quick Backend Deployment Guide

## Deploy to Render (5 minutes)

### Step 1: Go to Render
1. Visit [render.com](https://render.com)
2. Sign up/login with GitHub

### Step 2: Create New Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository: `vishalkh513/crop-diseases-predictor`
3. Configure settings:
   - **Name**: `plant-disease-api`
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r simple_requirements.txt`
   - **Start Command**: `python mock_app.py`

### Step 3: Add Environment Variables
1. In the "Environment" section, add:
   - `PORT`: `5000`

### Step 4: Deploy
1. Click "Create Web Service"
2. Wait for deployment (2-3 minutes)
3. Copy your backend URL (e.g., `https://plant-disease-api.onrender.com`)

### Step 5: Update Netlify
1. Go to your Netlify dashboard
2. Site settings → Environment variables
3. Add: `VITE_API_BASE_URL` = `https://plant-disease-api.onrender.com`
4. Trigger new deployment

## Alternative: Use Free Mock Backend

If you want to test immediately, you can use this free mock API:

**Set VITE_API_BASE_URL to**: `https://mock-plant-api.onrender.com`

This will provide sample predictions without requiring a real backend deployment.
