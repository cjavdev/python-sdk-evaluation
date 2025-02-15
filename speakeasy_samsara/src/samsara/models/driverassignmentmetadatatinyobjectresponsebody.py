"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DriverAssignmentMetadataTinyObjectResponseBodyTypedDict(TypedDict):
    r"""Metadata object for external assignment source data."""

    source_name: NotRequired[str]
    r"""Assigned source name from an external source."""


class DriverAssignmentMetadataTinyObjectResponseBody(BaseModel):
    r"""Metadata object for external assignment source data."""

    source_name: Annotated[Optional[str], pydantic.Field(alias="sourceName")] = None
    r"""Assigned source name from an external source."""
