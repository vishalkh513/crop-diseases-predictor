# Backend Deployment Instructions

## Deploy to Render (Recommended)

1. Go to [render.com](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository: https://github.com/vishalkh513/crop-diseases-predictor
4. Set these settings:
   - **Root Directory**: `backend`
   - **Python Version**: `3.11.8`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT --timeout 180`

5. Add Environment Variables:
   ```
   PYTHON_VERSION=3.11.8
   HF_MODEL_REPO_ID=your-huggingface-username/plant-disease-detection-model
   HF_MODEL_FILENAME=plant_disease_model_1_latest.pt
   CORS_ALLOWED_ORIGINS=https://your-vercel-project.vercel.app
   ```

6. Deploy and get your backend URL (e.g., https://your-app.onrender.com)

## Update Frontend Environment Variable

In your deployment platform (Vercel/Netlify):
- Set `VITE_API_BASE_URL=https://your-backend-url.onrender.com`

## Alternative: Hugging Face Spaces

If Render keeps failing due to memory limits:
1. Create a new Space on Hugging Face
2. Choose Docker SDK
3. Copy backend files to the Space
4. Set environment variables
5. Use the Space URL as your `VITE_API_BASE_URL`
