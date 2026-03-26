def simple_agent(question: str) -> str:
    q = question.lower()

    if "resume" in q:
        return "Improve your resume by adding relevant skills, projects, certifications, and internship experience."

    elif "data analytics" in q:
        return "A fresher in data analytics should learn Python, Excel, and SQL."

    elif "hr interview" in q:
        return "A fresher should practice communication, build confidence, research the company, and do mock interview practice."

    elif "web development" in q:
        return "A beginner should build a portfolio website, a todo app, and small responsive website projects."

    elif "linkedin" in q:
        return "Improve your LinkedIn profile by adding skills, projects, a strong headline, and an optimized profile summary."

    return "Focus on relevant skills, projects, and consistent practice."