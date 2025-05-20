# 📌 Task 2: Meeting Transcript Summarizer

## ✅ Overview

A minimal Flask web application that:
- Accepts a meeting transcript through a large input text box on a web page.
- Uses OpenAI GPT to generate a **3-line summary** of the meeting.
- Displays the summary directly below the input field.

## 🧪 Example Use Case

1. Paste a transcript like:
    ```
    Welcome to the Q3 planning meeting. Sarah gave updates on development progress...
    ```
2. Press "Generate Summary".
3. Output:
    - Discussed Q3 planning and development milestones.
    - Marketing reported strong campaign performance.
    - Budget status and next steps were outlined.

## 🔧 Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/ahmedali1902/EagleEvalTask2.git
    ```

2. Create a `.env` file with:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:

    ```bash
    python app.py
    ```