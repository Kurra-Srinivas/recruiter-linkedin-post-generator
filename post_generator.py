from llm_helper import llm

def generate_recruiter_post(jd_text, tone="Professional", language="English"):
    prompt = f"""
    You are an expert recruiter writing LinkedIn posts.

    Given the job description below, write a professional LinkedIn post that:
    - Starts with a strong hook
    - Highlights 2–3 key benefits/responsibilities
    - Ends with a call-to-action
    - Includes 2–4 emojis naturally in the body (🎯, 🚀, 💼, 🌟, etc.)
    - Closes with 4–6 relevant hashtags
    - Language: {language}
    - Tone: {tone}
    - No bullet points; use plain text formatting

    Job Description:
    \"\"\"{jd_text}\"\"\"

    LinkedIn Post:
    """

    response = llm.invoke(prompt)
    return response.content
