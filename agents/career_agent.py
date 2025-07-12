# import google.generativeai as genai

# @genai
# def CareerAgent(user_input: str) -> str:

#     """Suggests career based on interests."""
#     if "design" in user_input.lower():
#         return "You might be great at UI/UX Design."
#     elif "data" in user_input.lower() or "math" in user_input.lower():
#         return "You should explore Data Science."
#     else:
#         return "Let’s explore your interests more deeply."




# agents/career_agent.py

import os
import google.generativeai as genai  # type: ignore
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def suggest_career(user_input: str) -> str:
    """
    Suggest a career based on user input using the Gemini model.
    Handles greetings, short inputs, and generates detailed career advice.
    """

    user_input = user_input.strip()
    if user_input.lower() in ["hi", "hello", "hey"]:
        return (
            "👋 Hey there! I'm your Career Assistant 🤖\n"
            "Tell me about your passions, favorite subjects, or goals — and I’ll help you discover a perfect career match!"
        )

    # 🧠 Validate input
    if not user_input:
        return "❗ Please tell me your interests, dream job, or skills so I can help you."

    # 👋 Handle greetings
  
    # 📏 Too short input
    if len(user_input) < 8:
        return "❗ Can you share a bit more? Maybe your favorite subject, passion, or a dream job?"

    # 🎯 Prompt for Gemini
    prompt = (
        "You are a professional career advisor AI. Based on the user's interest below, "
        "recommend ONE best-fit career path. Only choose from:\n"
        "→ Web Developer, Data Scientist, AI Engineer, UX Designer, Marketing Specialist.\n\n"
        "For the recommended career, provide:\n"
        "1. Why it's a great fit for the user\n"
        "2. Key skills required\n"
        "3. How to get started with learning or entering this field\n\n"
        f"User Input: {user_input}"
    )

    # 🧠 Gemini API Call
    try:
        response = model.generate_content(prompt)
        return f"🎓 Career Suggestion:\n{response.text.strip()}"
    except Exception as e:
        return f"❌ Sorry, an error occurred while generating the suggestion.\nError: {str(e)}"
