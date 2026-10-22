import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from schemas import BugReport

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY missing hai. Apni .env file check karein."
    )

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=api_key,
    temperature=0.2,
)

structured_llm = llm.with_structured_output(BugReport)


def analyze_bug(description: str) -> dict:
    """Analyze a bug description and return a structured bug report."""

    prompt = f"""
    You are an experienced software QA engineer.

    Analyze the following software bug report.

    BUG DESCRIPTION:
    {description}

    Instructions:
    1. Create a short, clear bug title.
    2. Identify the affected feature.
    3. Summarize the issue accurately.
    4. Assign severity: Critical, High, Medium, or Low.
    5. Suggest possible root causes. These are hypotheses,
       not confirmed causes.
    6. Generate a clean, readable formatted bug report.

    Severity guidelines:
    - Critical: Major system outage, data loss, or severe security issue.
    - High: Major functionality is broken for many users.
    - Medium: Important functionality is affected, but a workaround exists.
    - Low: Minor issue with limited impact.

    Do not invent facts that are not provided.
    Clearly distinguish reported facts from possible causes.
    """

    result = structured_llm.invoke(prompt)

    return result.model_dump()