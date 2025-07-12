# agents/skill_agent.py

import google.generativeai as genai  # type: ignore
import os
from dotenv import load_dotenv
from tools.roadmap_tool import get_career_roadmap

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini Model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

class SkillAgent:
    def __init__(self, model):
        self.model = model

    def run(self, field: str) -> str:
        """
        Combines Gemini AI advice + tool-based career roadmap for given field.
        """

        # 🔹 Gemini prompt
        prompt = (
            f"As a career coach, list the essential skills one needs to become a successful {field}. "
            "Explain why these skills matter in a friendly tone."
        )

        # 🔹 Gemini AI Response
        try:
            gemini_response = self.model.generate_content(prompt).text.strip()
        except Exception as e:
            gemini_response = f"❌ Gemini couldn't load skills. Error: {e}"

        # 🔹 Tool-based roadmap
        try:
            tool_skills = get_career_roadmap(field)
        except Exception as e:
            tool_skills = f"❌ Roadmap tool failed. Error: {e}"

        return (
            f"🧠 **Gemini AI Says:**\n{gemini_response}\n\n"
            f"📘 **Practical Skill Roadmap:**\n{tool_skills}"
        )
