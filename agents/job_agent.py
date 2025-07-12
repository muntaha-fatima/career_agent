# import google.generativeai as genai

# @genai
# def JobAgent(career: str) -> str:
#     """Returns job roles related to a career."""
#     jobs = {
#         "data scientist": "🔹 Data Scientist\n🔹 ML Engineer\n🔹 AI Analyst",
#         "ui/ux designer": "🔹 UI Designer\n🔹 UX Researcher\n🔹 Product Designer"
#     }
#     return jobs.get(career.lower(), "No jobs found for this career.")





# agents/job_agent.py

import google.generativeai as genai  # type: ignore
import os
from dotenv import load_dotenv
from tools.job_tool import get_job_roles  # Custom tool for job roles

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini Model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

class JobAgent:
    def __init__(self, model):
        self.model = model

    def run(self, field: str) -> str:
        """
        Combines Gemini AI insights + tool-based job roles.
        """

        # 🔹 Prompt Gemini for career-specific hiring info
        prompt = (
            f"Based on your knowledge, what kinds of companies or industries "
            f"commonly hire {field}s? Give a short summary."
        )
        try:
            gemini_response = self.model.generate_content(prompt).text.strip()
        except Exception as e:
            gemini_response = f"❌ Gemini couldn't fetch insights. Error: {e}"

        # 🔹 Fetch jobs from our own tool (static/dynamic roles)
        try:
            tool_jobs = get_job_roles(field)
        except Exception as e:
            tool_jobs = f"❌ Failed to fetch job roles from tool. Error: {e}"

        return (
            f"📊 **Gemini Insight**:\n{gemini_response}\n\n"
            f"📋 **Suggested Job Roles**:\n{tool_jobs}"
        )
