from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
import json

app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')

@app.route('/encode/vectors', methods=['POST'])
def encode_vectors():
    # Check if the Content-Type header is missing or not set to application/json
    if request.content_type != 'application/json':
        # Try to handle the data by manually parsing it as JSON
        try:
            # Read raw data and parse it as JSON
            data = json.loads(request.data)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid input, expected JSON data"}), 400
    else:
        # Use get_json() if Content-Type is correct
        data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "Invalid input, expected JSON with 'text' key"}), 400

    text = data['text']
    vector = model.encode([text])[0]  # Get the first (and only) embedding
    # Create response with text, vector, and dimension
    response_data = {
        "text": text,
        "vector": vector.tolist(),  # Convert to list for JSON serialization
        "dim": len(vector),  # Dimension of the vector
    }
    return jsonify(response_data), 200  # Return with HTTP 200

@app.route('/encode/meta', methods=['GET'])
def encode_meta():
    metadata = {
        "api_version": "1.0",
        "description": "This API provides an encoding service for text using a pre-trained model.",
        "endpoints": {
            "/encode": {
                "method": "POST",
                "description": "Encodes text to vector",
                "content_type": "application/json"
            },
            "/encode/vectors": {
                "method": "POST",
                "description": "Encodes text to vector",
                "content_type": "application/json"
            },
            "/encode/meta": {
                "method": "GET",
                "description": "Provides metadata about the API",
                "content_type": "application/json"
            }
        }
    }
    return jsonify(metadata)


@app.route('/encode/.well-known/ready', methods=['GET'])
def ready_check():
    return "Ready", 200

# Endpoint to check if the app is alive
@app.route('/.well-known/live', methods=['GET'])
def live():
    return '', 204  # HTTP 204 means "No Content"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000)
