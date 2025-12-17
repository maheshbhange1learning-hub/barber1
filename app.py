from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

app.config['SWAGGER'] = {
    'title': 'Beauty & Wellness API',
    'uiversion': 3,
    'version': '1.0.0'
}
swagger = Swagger(app)

SALONS_DB = [
    {
        "shopName": "Elite Cuts",
        "shopRatings": "4.6",
        "shopAddress": "Bengaluru, Karnataka",
        "shopOpenStatus": "Open. Closes 7:00 PM",
        "shopLocation": "https://www.google.com/maps"
    },
    {
        "shopName": "K G N Salon",
        "shopRatings": "4.8",
        "shopAddress": "Bengaluru, Karnataka",
        "shopOpenStatus": "Closed. Open 7:00 AM",
        "shopLocation": "https://www.google.com/maps"
    }
]

@app.route('/')
def home():
    return jsonify({
        "status": "Beauty & Wellness Backend running!",
        "swagger_docs": "/apidocs/"
    })

@app.route('/api/search', methods=['POST'])
def search_salons():
    """
    Search for salons
    ---
    tags:
      - Salons
    parameters:
      - name: body
        in: body
        schema:
          type: object
          properties:
            zipcode:
              type: string
    responses:
      200:
        description: List of salons
    """
    data = request.json or {}
    return jsonify({
        "success": True,
        "results_count": len(SALONS_DB),
        "salons": SALONS_DB
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint
    ---
    tags:
      - System
    responses:
      200:
        description: Health status
    """
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

