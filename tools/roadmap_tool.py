def get_career_roadmap(field: str) -> str:
    roadmap = {
        "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Tailwind"],
        "Data Scientist": ["Python", "Pandas", "Scikit-Learn", "Statistics"],
        "AI Engineer": ["Python", "TensorFlow", "Deep Learning", "MLOps"],
        "UX Designer": ["Figma", "Design Thinking", "Wireframing", "User Research"],
        "Marketing Specialist": ["SEO", "Google Ads", "Social Media Marketing"]
    }
    return "\n- ".join([""] + roadmap.get(field, ["No data found."]))