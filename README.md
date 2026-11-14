
# 🔐 An AI-Powered Escape Room

An interactive AI escape room built using Python, Streamlit and Google's Gemini API.

The project explores how AI can create an engaging escape room experience while Python ensures reliable game rules and validation.

## 🎮 Project Overview

This project contains two versions:

### Version 1 – Basic AI Escape Room
- Interactive Streamlit web application.
- Gemini acts as the AI Game Master.
- Three riddles with natural language interaction.
- AI-generated clues, responses and storytelling.

### Version 2 – Structured AI Escape Room
- Python-based Game Engine.
- Structured inventory and game-state management.
- Action validation before changing game progress.
- Key-based drawer access.
- Four-digit exit code validation.
- Gemini used for storytelling, not deciding puzzle success.

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK
- python-dotenv
- Git and GitHub

## 📁 Project Structure

```text
AI-Escape-Room/
│
├── version1/
│   ├── app.py
│   └── game_master.py
│
├── version2/
│   ├── app.py
│   ├── game_engine.py
│   ├── game_master.py
│   └── game_config.json
│
├── docs/
│   ├── architecture.md
│   ├── test_cases.md
│   └── project_report.md
│
├── screenshots/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Escape-Room
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root and add:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

Never upload your actual API key to GitHub.

### 5. Run Version 1

```bash
streamlit run version1/app.py
```

### 6. Run Version 2

Stop the first application and run:

```bash
streamlit run version2/app.py
```

## 🧪 Testing

The project was tested with:

- Normal puzzle-solving actions.
- Incorrect door codes.
- Opening the drawer without a key.
- Administrator impersonation attempts.
- Attempts to skip puzzles.
- Attempts to unlock the exit without completing the required steps.

See `docs/test_cases.md` for the detailed comparison.

## 📊 Main Learning Outcome

The project demonstrates the importance of separating AI-generated storytelling from deterministic application logic.

Version 1 provides an engaging AI-driven experience, while Version 2 introduces Python-based state management and validation for more reliable gameplay.

## 👨‍💻 Author

M.Sc. Data Science Student

University of Europe for Applied Sciences

