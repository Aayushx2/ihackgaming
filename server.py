from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

feedbacks = []

@app.route('/submit', methods=['POST'])
def submit_feedback():
    data = request.json
    feedbacks.append(data)
    return jsonify({"message": "Feedback submitted successfully!"}), 201

@app.route('/feedbacks', methods=['GET'])
def get_feedbacks():
    return jsonify(feedbacks), 200

if __name__ == '__main__':
    app.run(debug=True)

