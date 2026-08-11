from typing import List, Optional, Literal

from pydantic import BaseModel, Field

class WalkDecision(BaseModel):
    """Structured recommendation for whether to walk the dog."""

    recommendation: Literal[ "WALK", "SHORT_WALK", "WAIT", "SKIP"] = Field(
        description="The recommended action, such as WALK, SHORT_WALK, WAIT, or SKIP."
    )

    duration_minutes: Optional[int] = Field(
        default=None,
        description="Recommended walk duration in minutes, if applicable."
    )

    reasons: List[str] = Field(
        description="Reasons supporting the recommendations."
    )

    risks: List[str] = Field(
        description="Potential risks or concerns for the walk."
    )