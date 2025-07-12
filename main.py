
import os
import chainlit as cl  # type: ignore
import google.generativeai as genai  # type: ignore
from dotenv import load_dotenv

from agents.career_agent import suggest_career
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent
from tools.roadmap_tool import get_career_roadmap


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-1.5-flash")


@cl.on_message
async def main(message: cl.Message):
    user_input = message.content

    suggested_career = suggest_career(user_input)

    await cl.Message(content=f"🎓 CareerAgent:\n{suggested_career}").send()

    if "❗" in suggested_career or "👋" in suggested_career or "I'm your Career Assistant" in suggested_career:
        return
 
    if "at" in suggested_career:
        career_name = suggested_career.split("at")[-1].strip(". ")
    elif "explore" in suggested_career:
        career_name = suggested_career.split("explore")[-1].strip(". ")
    else:
        career_name = suggested_career.strip(". ")

    skill_agent = SkillAgent(model)
    skills_info = skill_agent.run(career_name)
    await cl.Message(content=skills_info).send()

    job_agent = JobAgent(model)
    job_info = job_agent.run(career_name)
    await cl.Message(content=job_info).send()
