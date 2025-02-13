"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V1VisionRunByCameraResponseRunSummaryTypedDict(TypedDict):
    items_per_minute: NotRequired[float]
    no_read_count: NotRequired[int]
    reject_count: NotRequired[int]
    success_count: NotRequired[int]


class V1VisionRunByCameraResponseRunSummary(BaseModel):
    items_per_minute: Annotated[
        Optional[float], pydantic.Field(alias="itemsPerMinute")
    ] = None

    no_read_count: Annotated[Optional[int], pydantic.Field(alias="noReadCount")] = None

    reject_count: Annotated[Optional[int], pydantic.Field(alias="rejectCount")] = None

    success_count: Annotated[Optional[int], pydantic.Field(alias="successCount")] = None
