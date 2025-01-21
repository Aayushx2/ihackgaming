from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

feedbacks = []

# Root route to prevent 404 for '/'
@app.route('/')
def home():
    return 'Welcome to the Feedback System!'

# Route to submit feedback
@app.route('/submit', methods=['POST'])
def submit_feedback():
    try:
        data = request.json
        if not data or not 'feedback' in data:
            return jsonify({"error": "Invalid feedback format!"}), 400
        feedbacks.append(data)
        return jsonify({"message": "Feedback submitted successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all feedbacks
@app.route('/feedbacks', methods=['GET'])
def get_feedbacks():
    return jsonify(feedbacks), 200

# Favicon route to prevent 404 errors
@app.route('/favicon.ico')
def favicon():
    return '', 204  # No content for favicon

if __name__ == '__main__':
    app.run(debug=True, port=5002)
