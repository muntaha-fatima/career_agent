# 🎓 Career Mentor Agent (Multi-Agent System)

An AI-powered interactive **Career Guidance Assistant** built using **Chainlit**, **Gemini AI**, and inspired by **OpenAI Agent SDK-style logic**. This multi-agent system helps students explore future career paths, learn relevant skills, and understand real-world job roles.

---

## ✅ Requirements Met

| Requirement                               | Status |
|-------------------------------------------|--------|
| ✅ Use at least **2 Tools**                | `get_career_roadmap`, `get_job_roles` |
| ✅ Use at least **2 Agents**               | `CareerAgent`, `SkillAgent`, `JobAgent` *(3 total)* |
| ✅ Handoff logic between tools/agents      | ✔ Implemented |
| ✅ Agent SDK-style logic (`@tool`, `on_message`) | ✔ Used |
| ✅ Well-structured code folder             | ✔ Yes |
| ✅ `README.md` with logic & explanation    | ✔ You're reading it! |

---

## 🧠 What It Does

This AI assistant behaves like a **career mentor**. It guides students by:

- 📌 Recommending **career paths** based on user input  
- 🧠 Generating a **skill roadmap** for that career  
- 💼 Listing **real-world job titles** and sample positions  
- 🔄 Using **handoff logic** between 3 smart agents  

---

## 🔁 Architecture Flow

```text
User Input
   │
   ▼
CareerAgent (interprets user goal)
   │
   ▼
SkillAgent (lists tools/skills to learn)
   │
   ▼
JobAgent (recommends real job titles)
   │
   ▼
Chainlit UI: Display full guidance

```
👥 Agents Breakdown
Agent	Description
🤖 CareerAgent	Understands user's goal and selects best-fit career
🧠 SkillAgent	Returns a learning roadmap (tools, languages, skills)
💼 JobAgent	Suggests job roles in the selected career path

All agents use the Gemini 1.5 Flash model to generate personalized answers.


``
🧰 Tools Used
Tool Function	Purpose
get_career_roadmap()	Provides step-by-step skills to learn
get_job_roles()	Returns job titles related to that field

``
📁 Folder Structure

career-mentor-agent/
├── main.py              # Chainlit entry point
├── agents/
│   ├── career_agent.py  # Detects career
│   ├── skill_agent.py   # Generates roadmap
│   └── job_agent.py     # Suggests jobs
├── tools/
│   ├── get_career_roadmap.py
│   └── get_job_roles.py
├── .env                 # Contains Gemini API key
├── requirements.txt
└── README.md

🚀 How to Run This Project
📦 Install dependencies:

pip install chainlit google-generativeai python-dotenv

🔐 Create .env file:

GEMINI_API_KEY=your_gemini_key_here

▶ Start app:

chainlit run main.py
``
💬 Example Conversation
👩 User: I want to become a data scientist

🤖 CareerAgent: Career path selected: Data Scientist

🧠 SkillAgent:
- Learn Python
- Master Pandas, NumPy
- Explore Machine Learning
- Practice data visualization

💼 JobAgent:
- Junior Data Scientist
- Machine Learning Engineer
- AI Research Assistant
- 
``
✨ Features
🤖 AI-powered career discovery using Gemini

🧭 Multi-agent logic with clear handoff

📚 Personalized skill roadmaps

🧑‍💼 Real job title examples

💻 Simple Chainlit chat UI

🙋 Created By
SEERAT FATIMA
🎓 GIAIC Student | 🧠 Passionate about AI & Career Empowerment






