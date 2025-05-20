import os
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = "gpt-4o"

def standard_response(message, status, data=None, error_code=None, http_status=None):
    response = {
        "message": message,
        "status": status,
        "data": data if status == "success" else None
    }
    if status == "error":
        response["error_code"] = error_code
    return jsonify(response), http_status or (200 if status == "success" else 400)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        content = request.get_json()
        transcript = content.get("transcript", "").strip()

        if not transcript:
            return standard_response(
                "Transcript is missing or empty.",
                "error",
                error_code="NO_TRANSCRIPT_PROVIDED",
                http_status=400
            )

        prompt = (
            "You will be given a meeting transcript.\n"
            "Summarize the transcript in very concise 3 line paragraph.\n"
            "Do not make up information. Focus on clarity and accuracy.\n\n"
            f"Transcript:\n{transcript}"
        )

        res = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are an expert meeting summarizer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        summary_text = res.choices[0].message.content.strip()

        return standard_response(
            "Meeting summary generated successfully.",
            "success",
            data={"summary": summary_text}
        )

    except Exception as e:
        return standard_response(
            f"Internal server error: {str(e)}",
            "error",
            error_code="SERVER_ERROR",
            http_status=500
        )

if __name__ == '__main__':
    app.run(debug=True)
