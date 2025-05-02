AI-Powered Medical Assistant with Gemini Pro & Streamlit
An intelligent, real-time medical assistant built using Google's Gemini Pro API and Streamlit. This application interprets natural language symptom descriptions, infers potential medical conditions, and recommends the appropriate medical specialist.


🚀 Features
Natural Language Processing: Understands and processes user-described symptoms.

Condition Inference: Suggests possible medical conditions based on input.

Specialist Recommendation: Advises on the appropriate medical department or specialist.

Real-Time Interaction: Provides instant feedback through an intuitive UI.

Secure API Integration: Utilizes .env for managing API keys securely.

🧠 How It Works
User Input: The user describes their symptoms in natural language.

Prompt Engineering: The input is formatted into a prompt for the Gemini Pro model.

Gemini Pro API: Processes the prompt and returns a structured response.

Output Parsing: Extracts relevant information from the response.

Display: Presents the inferred condition and specialist recommendation to the user.

🛠️ Tech Stack
Frontend: Streamlit

Backend: Python

AI Model: Google Gemini Pro

Environment Management: python-dotenv

📦 Installation
Clone the Repository:
git clone https://github.com/yourusername/symptom_checker.git
cd symptom_checker
Create a Virtual Environment:
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the root directory.

Add your Gemini API key:

ini
Copy
Edit
GOOGLE_API_KEY=your_api_key_here

Run the Application:
streamlit run app.py

📁 Project Structure
symptom_checker/
├── app.py
├── main.py
├── .env.example
├── requirements.txt
├── assets/
│   └── ai_medical_assistant_screenshot.png
├── README.md
└── .gitignore

📚 References
Google Gemini Pro API Documentation

Streamlit Documentation


🙏 Acknowledgements
Special thanks to OpenAI's ChatGPT for assistance in image creation and prompt engineering.
