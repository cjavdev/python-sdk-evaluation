# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "RunRetrievebycameraResponse",
    "RunRetrievebycameraResponseItem",
    "RunRetrievebycameraResponseItemProgram",
    "RunRetrievebycameraResponseItemReportMetadata",
]


class RunRetrievebycameraResponseItemProgram(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None


class RunRetrievebycameraResponseItemReportMetadata(BaseModel):
    items_per_minute: Optional[float] = FieldInfo(alias="itemsPerMinute", default=None)

    no_read_count: Optional[int] = FieldInfo(alias="noReadCount", default=None)

    reject_count: Optional[int] = FieldInfo(alias="rejectCount", default=None)

    success_count: Optional[int] = FieldInfo(alias="successCount", default=None)


class RunRetrievebycameraResponseItem(BaseModel):
    device_id: Optional[int] = FieldInfo(alias="deviceId", default=None)

    ended_at_ms: Optional[int] = FieldInfo(alias="endedAtMs", default=None)

    program: Optional[RunRetrievebycameraResponseItemProgram] = None

    report_metadata: Optional[RunRetrievebycameraResponseItemReportMetadata] = FieldInfo(
        alias="reportMetadata", default=None
    )

    started_at_ms: Optional[int] = FieldInfo(alias="startedAtMs", default=None)


RunRetrievebycameraResponse: TypeAlias = List[RunRetrievebycameraResponseItem]
