
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

from schemas import BugRequest
from graph import generate_bug_report

app = FastAPI(
    title="AI Bug Report Analyzer",
    description="Analyze software bugs using Gemini and LangGraph",
    version="1.0.0",
)

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"


@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "AI Bug Report Analyzer is running"
    }


@app.post("/analyze")
def analyze_bug_endpoint(request: BugRequest):
    print("STEP 1: Bug request received")

    try:
        print("STEP 2: Calling LangGraph...")

        result = generate_bug_report(request.description)

        print("STEP 3: LangGraph completed")

        return {
            "success": True,
            "report": result["formatted_report"],
            "details": {
                "title": result["title"],
                "affected_feature": result["affected_feature"],
                "issue_summary": result["issue_summary"],
                "severity": result["severity"],
                "possible_causes": result["possible_causes"],
            },
        }

    except Exception as exc:
        print(f"ERROR: {exc}")

        raise HTTPException(
            status_code=500,
            detail=f"Bug analysis failed: {str(exc)}",
        ) from exc


app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static",
)
