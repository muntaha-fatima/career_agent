def get_job_roles(field: str) -> str:
    jobs = {
        "Web Developer": ["Frontend Developer @Google", "React Dev @Shopify"],
        "Data Scientist": ["ML Engineer @Meta", "Data Analyst @Amazon"],
        "AI Engineer": ["AI Researcher @OpenAI", "ML Ops Engineer @Nvidia"],
        "UX Designer": ["UX Designer @Adobe", "UI Designer @Figma"],
        "Marketing Specialist": ["SEO Manager @Moz", "Growth Marketer @HubSpot"]
    }
    return "\n- ".join([""] + jobs.get(field, ["No jobs found."]))
