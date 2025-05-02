import os
import json
import re
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def process_symptoms(symptom_text):
    prompt = f"""
You are a professional medical assistant.

Analyze the following patient's symptom description:
\"\"\"{symptom_text}\"\"\"

Provide the output strictly in the following JSON format (nothing more, nothing less):

{{
  "summary": "...",
  "conditions": ["...", "..."],
  "specialist": "..."
}}
"""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        return parse_response(response.text)
    except Exception as e:
        print("❌ Error from Gemini:", e)
        return {
            "summary": "Error",
            "conditions": ["Error"],
            "specialist": "Error"
        }

def parse_response(text):
    try:
        match = re.search(r'\{.*}', text, re.DOTALL)
        if not match:
            raise ValueError("No JSON found in Gemini response")

        json_block = match.group(0)
        response_data = json.loads(json_block)

        return {
            "summary": response_data.get("summary", "N/A"),
            "conditions": response_data.get("conditions", []),
            "specialist": response_data.get("specialist", "N/A")
        }

    except Exception as e:
        print("❌ JSON parsing failed:", e)
        return {
            "summary": text,
            "conditions": ["Could not parse conditions"],
            "specialist": "Could not parse specialist"
        }
