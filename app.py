from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample data to simulate responses (you would replace this with a real database or API)
health_data = {
    "fever": "Drink plenty of fluids, rest, and take fever-reducing medications like paracetamol.",
    "cough": "Stay hydrated, use cough drops, and consult a doctor if the cough persists.",
    "headache": "Take over-the-counter pain relief like ibuprofen or paracetamol, and rest in a quiet, dark room."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    response = health_data.get(user_message.lower(), "I'm not sure about that. Please consult a healthcare professional.")
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
