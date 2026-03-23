import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173", "http://localhost:3000"])

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "message": "Mock backend is running"})

@app.route('/api/catalog', methods=['GET'])
def catalog():
    return jsonify({
        "supportedCrops": ["Apple", "Corn", "Grape", "Tomato", "Potato"],
        "totalClasses": 39
    })

@app.route('/api/warmup', methods=['POST'])
def warmup():
    return jsonify({"status": "warming up", "message": "Mock backend warming up"}), 202

@app.route('/api/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    # Mock prediction response
    return jsonify({
        "prediction": "Apple___Apple_scab",
        "confidence": 0.85,
        "displayName": "Apple Scab",
        "isHealthy": False,
        "prevention": [
            "Apply fungicide treatments at appropriate times",
            "Remove fallen leaves and infected fruit",
            "Prune trees to improve air circulation"
        ],
        "supplement": {
            "name": "Copper Fungicide",
            "buyLink": "https://example.com/copper-fungicide"
        },
        "referenceImage": "https://example.com/apple-scab.jpg"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Disable debug mode in production
    debug = os.environ.get('ENVIRONMENT') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug)
