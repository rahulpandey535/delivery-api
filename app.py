from flask import Flask, request, jsonify
from utils.logic import calculate_minimum_delivery_cost

app = Flask(__name__)

@app.route("/calculate-cost", methods=["POST"])
def calculate_cost():
    try:
        order = request.get_json()
        if not order:
            return jsonify({"error": "Invalid or empty JSON data"}), 400

        min_cost = calculate_minimum_delivery_cost(order)
        return jsonify({"minimum_cost": min_cost})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
