# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["RunListResponse", "VisionRun", "VisionRunReportMetadata"]


class VisionRunReportMetadata(BaseModel):
    items_per_minute: Optional[float] = FieldInfo(alias="itemsPerMinute", default=None)
    """Returns average scanned items per minute. Should be used instead of scanRate."""

    no_read_count: Optional[int] = FieldInfo(alias="noReadCount", default=None)
    """Returns no read count for the run. Should be used instead of noReadScansCount"""

    reject_count: Optional[int] = FieldInfo(alias="rejectCount", default=None)
    """Returns reject count for the run. Should be used instead of failedScansCount"""

    success_count: Optional[int] = FieldInfo(alias="successCount", default=None)
    """Returns success count for the run.

    Should be used instead of successfulScansCount
    """


class VisionRun(BaseModel):
    device_id: Optional[int] = FieldInfo(alias="deviceId", default=None)

    ended_at_ms: Optional[int] = FieldInfo(alias="endedAtMs", default=None)

    program_id: Optional[int] = FieldInfo(alias="programId", default=None)

    report_metadata: Optional[VisionRunReportMetadata] = FieldInfo(alias="reportMetadata", default=None)
    """The response includes 4 additional fields that are now deprecated"""

    started_at_ms: Optional[int] = FieldInfo(alias="startedAtMs", default=None)


class RunListResponse(BaseModel):
    vision_runs: Optional[List[VisionRun]] = FieldInfo(alias="visionRuns", default=None)
