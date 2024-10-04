from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Health check endpoint for liveness probe
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Health check endpoint for readiness probe
@app.route('/ready', methods=['GET'])
def ready_check():
    return jsonify({"status": "ready"}), 200

# Simulated in-memory payment storage
payments = []

@app.route('/payments', methods=['POST'])
def process_payment():
    data = request.get_json()
    new_payment = {
        "id": len(payments) + 1,
        "order_id": data['order_id'],
        "amount": data['amount'],
        "status": "Success"
    }
    payments.append(new_payment)
    return jsonify({"message": "Payment processed successfully", "payment": new_payment}), 201

@app.route('/payments', methods=['GET'])
def get_payments():
    return jsonify(payments)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)

