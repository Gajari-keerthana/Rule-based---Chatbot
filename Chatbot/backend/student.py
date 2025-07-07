# Flask backend for Rule-Based Student Chatbot
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for communication with React frontend

# --- Database Setup (SQLite for FAQs) ---
def init_db():
    conn = sqlite3.connect('faqs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS faqs (
            id INTEGER PRIMARY KEY,
            intent TEXT NOT NULL,
            response TEXT NOT NULL
        )
    ''')
    faqs = [
        ('account', 'To reset your password, visit the "Forgot Password" page or contact support@edtech.com.'),
        ('enrollment', 'Check your course enrollment status in "My Courses". Contact registration help if needed.'),
        ('schedule', 'Find your course schedule under the "Timetable" section of your dashboard.'),
        ('assignment', 'To submit assignments, go to your course page > Assignments > Upload file before due date.'),
        ('technical', 'Try restarting your device or clearing your browser cache. Still stuck? Email techsupport@edtech.com.')
    ]
    c.executemany('INSERT OR IGNORE INTO faqs (intent, response) VALUES (?, ?)', faqs)
    conn.commit()
    conn.close()

# --- Intent Detection (Rule-Based) ---
def detect_intent(message):
    message = message.lower()
    if any(keyword in message for keyword in ["password", "login", "account"]):
        return "account"
    elif any(keyword in message for keyword in ["enroll", "register", "course not showing"]):
        return "enrollment"
    elif any(keyword in message for keyword in ["schedule", "timetable", "class time"]):
        return "schedule"
    elif any(keyword in message for keyword in ["assignment", "submit", "homework"]):
        return "assignment"
    elif any(keyword in message for keyword in ["video", "error", "crash", "not working"]):
        return "technical"
    else:
        return "unknown"

# --- Response Retrieval ---
def get_response(intent):
    if intent == "unknown":
        return "Sorry, I didn’t understand that. Try asking about login, enrollment, schedule, assignments, or technical issues."
    conn = sqlite3.connect('faqs.db')
    c = conn.cursor()
    c.execute("SELECT response FROM faqs WHERE intent = ?", (intent,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else "I couldn't find information for that request."

# --- Health Check Endpoint ---
@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Student Chatbot API is running."})

# --- Chat Endpoint ---
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    intent = detect_intent(user_message)
    response = get_response(intent)
    return jsonify({"response": response})

# --- Main ---
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
