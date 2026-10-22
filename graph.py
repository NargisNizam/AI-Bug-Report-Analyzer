from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from agents import analyze_bug


class BugState(TypedDict):
    description: str
    title: str
    affected_feature: str
    issue_summary: str
    severity: str
    possible_causes: list[str]
    formatted_report: str


# Node 1: Bug Analysis
def bug_analysis_node(state: BugState) -> dict:
    result = analyze_bug(state["description"])

    return {
        "title": result["title"],
        "affected_feature": result["affected_feature"],
        "issue_summary": result["issue_summary"],
        "severity": result["severity"],
        "possible_causes": result["possible_causes"],
        "formatted_report": result["formatted_report"],
    }


# Node 2: Severity Detection
def severity_detection_node(state: BugState) -> dict:
    # Gemini provides the initial severity classification.
    # This node ensures the value is one of the allowed labels.
    allowed = {"Critical", "High", "Medium", "Low"}
    severity = state.get("severity", "Medium")

    if severity not in allowed:
        severity = "Medium"

    return {"severity": severity}


# Node 3: Root Cause Suggestion
def root_cause_node(state: BugState) -> dict:
    # Possible causes are hypotheses, not confirmed diagnoses.
    causes = state.get("possible_causes", [])

    if not causes:
        causes = [
            "Insufficient information to identify a likely cause. "
            "Check application logs and reproduce the issue."
        ]

    return {"possible_causes": causes}


# Node 4: Format Report
def format_report_node(state: BugState) -> dict:
    causes = state.get("possible_causes", [])
    causes_text = "\n".join(f"- {cause}" for cause in causes)

    report = f"""
BUG REPORT
==========

Title: {state.get("title", "Not identified")}

Affected Feature:
{state.get("affected_feature", "Not identified")}

Issue Summary:
{state.get("issue_summary", "Not available")}

Severity: {state.get("severity", "Medium")}

Possible Root Causes:
{causes_text}

Original Bug Description:
{state["description"]}

Note: Root causes are suggestions and require verification.
""".strip()

    return {"formatted_report": report}


# Build the LangGraph workflow
def build_bug_graph():
    builder = StateGraph(BugState)

    builder.add_node("bug_analysis", bug_analysis_node)
    builder.add_node("severity_detection", severity_detection_node)
    builder.add_node("root_cause_suggestion", root_cause_node)
    builder.add_node("format_report", format_report_node)

    builder.add_edge(START, "bug_analysis")
    builder.add_edge("bug_analysis", "severity_detection")
    builder.add_edge("severity_detection", "root_cause_suggestion")
    builder.add_edge("root_cause_suggestion", "format_report")
    builder.add_edge("format_report", END)

    return builder.compile()


bug_graph = build_bug_graph()


def generate_bug_report(description: str) -> dict:
    result = bug_graph.invoke({
        "description": description,
        "title": "",
        "affected_feature": "",
        "issue_summary": "",
        "severity": "Medium",
        "possible_causes": [],
        "formatted_report": "",
    })

    return result