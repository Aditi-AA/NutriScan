from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
from scanner import scan_barcode
from db import collection1, collection2
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

from flask import request, jsonify

@app.route("/check_barcode", methods=['GET'])
def check_barcode():
    try:
        barcode = request.args.get("barcode")
        print(f"Received request: /check_barcode?barcode={barcode}")
        if not barcode:
            return jsonify({"error": "Barcode is required"}), 400

        product = collection1.find_one({"_id": barcode})
        return jsonify({"exists": bool(product)})

    except Exception as e:
        print(f"Error in /check_barcode: {str(e)}")  # Print error for debugging
        return jsonify({"error": "Internal server error"}), 500


@app.route('/scan', methods=['GET'])
def scan():
    barcode = request.args.get('barcode')
    if not barcode:
        response = jsonify({"error": "No barcode provided"})
        print("Response:", response.get_json())  # Debugging
        return response, 400

    product = collection1.find_one({"_id": barcode})
    if not product:
        response = jsonify({"message": "Product not found"})
        print("Response:", response.get_json())  # Debugging
        return response, 404

    response = jsonify({
        "barcode": barcode,
        "product_name": product.get("product_name", "N/A"),
        "brand": product.get("brands", "N/A"),
        "classification": product.get("classification", "N/A"),
    })
    print("Response:", response.get_json())  # Debugging
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
