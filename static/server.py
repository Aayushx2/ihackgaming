import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app = Flask(__name__)
CORS(app)

# Set up the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedbacks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Create a Feedback model for the database
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feedback = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Feedback {self.id}: {self.feedback}>'

# Create the tables in the database (run this only once)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return 'Welcome to the Feedback System!'

@app.route('/submit', methods=['POST'])
def submit_feedback():
    try:
        data = request.json
        if not data or not 'feedback' in data:
            return jsonify({"error": "Invalid feedback format!"}), 400
        
        # Save feedback to the database
        new_feedback = Feedback(feedback=data['feedback'])
        db.session.add(new_feedback)
        db.session.commit()

        return jsonify({"message": "Feedback submitted successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/feedbacks', methods=['GET'])
def get_feedbacks():
    # Retrieve all feedbacks from the database
    feedbacks = Feedback.query.all()
    return jsonify([{'id': feedback.id, 'feedback': feedback.feedback} for feedback in feedbacks]), 200

@app.route('/favicon.ico')
def favicon():
    return '', 204  # No content for favicon

if __name__ == '__main__':
    # Use 'PORT' from the environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=5002)
