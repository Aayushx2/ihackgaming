from flask import Blueprint, request, jsonify

# Blueprint setup
main = Blueprint('main', __name__)

feedbacks = []

@main.route('/')
def home():
    return jsonify({"message": "Welcome to the Feedback System!"}), 200

@main.route('/submit', methods=['POST'])
def submit_feedback():
    try:
        data = request.json
        if not data or 'feedback' not in data:
            return jsonify({"error": "Invalid feedback format!"}), 400
        feedbacks.append(data['feedback'])
        return jsonify({"message": "Feedback submitted successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/feedbacks', methods=['GET'])
def get_feedbacks():
    return jsonify(feedbacks), 200
