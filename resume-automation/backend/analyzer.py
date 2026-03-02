import os
import json
import sys
from pypdf import PdfReader
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Groq client (OpenAI-compatible API)
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def extract_text(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()
    except Exception as e:
        return json.dumps({"error": f"PDF extraction failed: {str(e)}"})


def analyze_resume(resume_text, job_description):
    prompt = f"""
You are an AI recruiter.

Compare the following resume against the job description.

Return STRICTLY valid JSON only.
Do NOT add explanations.

Required JSON format:
{{
  "overall_match_score": number (0-100),
  "technical_skill_match_score": number (0-100),
  "experience_match_score": number (0-100),
  "key_skills_found": [],
  "missing_required_skills": [],
  "strengths_against_job": "",
  "gaps_against_job": "",
  "final_recommendation": "Strong Fit" or "Moderate Fit" or "Weak Fit"
}}

Job Description:
{job_description}

Resume:
{resume_text}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        raw_output = response.choices[0].message.content.strip()

        # Ensure valid JSON
        parsed = json.loads(raw_output)

        return json.dumps(parsed)

    except Exception as e:
        return json.dumps({"error": f"LLM error: {str(e)}"})


# CLI execution mode
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(json.dumps({
            "error": "Usage: python analyzer.py <pdf_path> <job_description>"
        }))
        sys.exit(1)

    pdf_path = sys.argv[1]
    job_description = sys.argv[2]

    resume_text = extract_text(pdf_path)
    result = analyze_resume(resume_text, job_description)

    print(result)