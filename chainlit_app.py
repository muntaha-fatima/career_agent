# import os
# import sys


# sys.path.append(os.path.abspath(os.path.dirname(__file__)))
# import google.generativeai as genai
# from agents import career_agent
# from agents.skill_agent import SkillAgent
# from agents.job_agent import JobAgent



# import chainlit as cl
# from dotenv import load_dotenv
# # Load API key from .env
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# @cl.on_message
# async def main(message: cl.Message):
#     user_input = message.content

#     # Step 1: Suggest a career
#     suggested_career = career_agent(user_input)
#     await cl.Message(content=f"🎯 Suggested Career:\n**{suggested_career}**").send()

#     # Extract actual career name from sentence
#     if "at" in suggested_career:
#         career_name = suggested_career.split("at")[-1].strip(". ")
#     elif "explore" in suggested_career:
#         career_name = suggested_career.split("explore")[-1].strip(". ")
#     else:
#         career_name = suggested_career.strip(". ")

#     # Step 2: Get Skill Roadmap
#     roadmap = SkillAgent(career_name)
#     await cl.Message(content=f"📘 Skill Roadmap for **{career_name}**:\n{roadmap}").send()

#     # Step 3: Get Job Roles
#     job_roles = JobAgent(career_name)
#     await cl.Message(content=f"💼 Job Roles:\n{job_roles}").send()











# # C:\Users\Public\carer-mutilpe-agents\chainlit_app.py
# import os
# import sys
# import google.generativeai as genai
# import chainlit as cl
# from dotenv import load_dotenv

# # Add the current directory to the Python path
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# # Import agents
# from agents.career_agent import suggest_career  # Import the function
# from agents.skill_agent import SkillAgent
# from agents.job_agent import JobAgent

# # Load API key from .env
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# # Step 2: Initialize the Gemini model (you can use 'gemini-1.5-pro' for advanced responses)
# model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# @cl.on_message
# async def main(message: cl.Message):
#     user_input = message.content

#     # Step 1: Suggest a career
#     suggested_career = suggest_career(user_input)  # Call the function
#     await cl.Message(content=f"🎯 Suggested Career:\n**{suggested_career}**").send()

#     # Extract actual career name from sentence
#     if "at" in suggested_career:
#         career_name = suggested_career.split("at")[-1].strip(". ")
#     elif "explore" in suggested_career:
#         career_name = suggested_career.split("explore")[-1].strip(". ")
#     else:
#         career_name = suggested_career.strip(". ")

#     # Step 2: Get Skill Roadmap
#     roadmap = SkillAgent(career_name)  # Assuming SkillAgent is a callable class
#     await cl.Message(content=f"📘 Skill Roadmap for **{career_name}**:\n{roadmap}").send()

#     # Step 3: Get Job Roles
#     job_roles = JobAgent(career_name)  # Assuming JobAgent is a callable class
#     await cl.Message(content=f"💼 Job Roles:\n{job_roles}").send()