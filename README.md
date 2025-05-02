# 🩺 AI-Powered Medical Assistant with Gemini Pro & Streamlit

An intelligent, real-time medical assistant built using **Google's Gemini Pro API** and **Streamlit**. This application interprets natural language symptom descriptions, infers potential medical conditions, and recommends the appropriate medical specialist.

---

## 🚀 Features

- **Natural Language Processing**: Understands and processes user-described symptoms.
- **Condition Inference**: Suggests possible medical conditions based on input.
- **Specialist Recommendation**: Advises on the appropriate medical department or specialist.
- **Real-Time Interaction**: Provides instant feedback through an intuitive UI.
- **Secure API Integration**: Utilizes `.env` for managing API keys securely.

---

## 🧠 How It Works

1. **User Input**: The user describes their symptoms in natural language.
2. **Prompt Engineering**: The input is formatted into a prompt for the Gemini Pro model.
3. **Gemini Pro API**: Processes the prompt and returns a structured response.
4. **Output Parsing**: Extracts relevant information from the response.
5. **Display**: Presents the inferred condition and specialist recommendation to the user.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: [Python](https://www.python.org/)
- **AI Model**: [Google Gemini Pro](https://ai.google.dev/)
- **Environment Management**: [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📦 Installation

```bash
# Clone the Repository
git clone https://github.com/yourusername/symptom_checker.git
cd symptom_checker

# Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt
```

**Configure Environment Variables**:
Create a `.env` file in the root directory with:
```
GOOGLE_API_KEY=your_api_key_here
```

**Run the Application**:
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
symptom_checker/
├── app.py
├── main.py
├── .env.example
├── requirements.txt
├── assets/
│   └── ai_medical_assistant_screenshot.png
├── README.md
└── .gitignore
```

---

## 📚 References

- [Google Gemini Pro API Documentation](https://ai.google.dev/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

## 🙏 Acknowledgements

- Inspired by open-source AI health chatbots
- Special thanks to [OpenAI's ChatGPT](https://chat.openai.com/) for assistance in prompt engineering and design support
