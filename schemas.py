from typing import Literal
from pydantic import BaseModel, Field


class BugReport(BaseModel):
    title: str = Field(description="Short and clear bug title")
    affected_feature: str = Field(description="Feature affected by the bug")
    issue_summary: str = Field(description="Summary of the reported issue")
    severity: Literal["Critical", "High", "Medium", "Low"]
    possible_causes: list[str] = Field(
        description="Possible technical causes of the bug"
    )
    formatted_report: str = Field(
        description="Complete and readable bug report"
    )


class BugRequest(BaseModel):
    description: str = Field(
        min_length=10,
        description="Natural language description of the bug"
    )