from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the Hugging Face model

chatbot_model = pipeline("text2text-generation", model="google/flan-t5-large", trust_remote_code=True)
conversation_history = []

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'response': 'Please provide a message.'}), 400
    response = generate_response(user_input)
    return jsonify({'response': response})

def generate_response(user_input):
    # Generate a response using the Hugging Face model
    conversation_history.append(
        {"role": "user", "content": user_input},
    )
    result = chatbot_model([f'{message['role']}: {message['message']}' for message in conversation_history], num_return_sequences=1, max_new_tokens=250)
    conversation_history.append(
        {"role": "assistant", "content": result[0]['generated_text'][-1]['content']},
    )
    return result[0]['generated_text'][-1]['content']

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
