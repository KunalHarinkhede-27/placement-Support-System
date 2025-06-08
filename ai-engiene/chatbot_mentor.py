import os
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app and enable CORS for cross-origin requests
app = Flask(__name__)
CORS(app)

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_mentor(question: str, chat_history=None) -> str:
    """
    Sends a question and chat history to OpenAI GPT model
    and returns a helpful mentoring response.

    Parameters:
        question (str): User question
        chat_history (list): Optional list of previous messages as dicts:
            [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]

    Returns:
        str: Mentor's reply text
    """

    if chat_history is None:
        chat_history = []

    # Append current user question
    chat_history.append({"role": "user", "content": question})

    try:
        # Use ChatCompletion for conversational context
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # or use "gpt-4", "gpt-3.5-turbo"
            messages=chat_history,
            temperature=0.7,
            max_tokens=600,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Extract assistant reply
        answer = response.choices[0].message['content'].strip()

        # Append assistant's answer to chat history (optional)
        chat_history.append({"role": "assistant", "content": answer})

        return answer, chat_history

    except Exception as e:
        return f"Error: {str(e)}", chat_history


@app.route('/mentor/chat', methods=['POST'])
def mentor_chat():
    """
    API endpoint to handle mentor chat requests.
    Request JSON body:
    {
        "question": "How do I improve my resume?",
        "chatHistory": [ ...optional previous messages... ]
    }
    Returns:
        JSON with mentor response and updated chat history
    """
    data = request.get_json()

    question = data.get("question")
    chat_history = data.get("chatHistory", [])

    if not question:
        return jsonify({"error": "Question is required"}), 400

    answer, updated_history = ask_mentor(question, chat_history)

    return jsonify({
        "answer": answer,
        "chatHistory": updated_history
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
