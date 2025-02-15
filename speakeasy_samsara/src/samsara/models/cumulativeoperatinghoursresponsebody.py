"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CumulativeOperatingHoursResponseBodyTypedDict(TypedDict):
    r"""Equipment operating hours."""

    hour: NotRequired[float]
    r"""Total number of equipment operating hours."""
    datetime: NotRequired[str]
    r"""Date time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""


class CumulativeOperatingHoursResponseBody(BaseModel):
    r"""Equipment operating hours."""

    hour: Annotated[Optional[float], pydantic.Field(alias="Hour")] = None
    r"""Total number of equipment operating hours."""

    datetime: Optional[str] = None
    r"""Date time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""
