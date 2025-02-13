# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HistoryCreateResponse", "Result"]


class Result(BaseModel):
    series: Optional[List[int]] = None
    """List of datapoints, one for each requested (sensor, field) pair."""

    time_ms: Optional[int] = FieldInfo(alias="timeMs", default=None)
    """Timestamp in UNIX milliseconds."""


class HistoryCreateResponse(BaseModel):
    results: Optional[List[Result]] = None
