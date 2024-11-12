import os
from flask import Flask, render_template, request
import google.generativeai as genai
import requests


app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure Gemini API
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Generation settings for Gemini
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}


@app.route('/', methods=['GET', 'POST'])
def chat_gemini():
    response_text = ""

    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        
        if user_input:
            model = genai.GenerativeModel(
                model_name="gemini-1.0-pro",
                generation_config=generation_config
            )

            # Updated context for a general AI chatbot
            context = f"You are a helpful AI assistant. Respond to the following query: {user_input}"
            
            response = model.generate_content(context)
            response_text = response.text

    return render_template('chat_bot.html', response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
