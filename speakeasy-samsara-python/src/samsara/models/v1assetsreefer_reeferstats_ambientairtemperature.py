"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V1AssetsReeferReeferStatsAmbientAirTemperatureTypedDict(TypedDict):
    changed_at_ms: NotRequired[int]
    r"""Timestamp in Unix milliseconds since epoch."""
    temp_in_milli_c: NotRequired[int]
    r"""Ambient temperature in millidegree Celsius."""


class V1AssetsReeferReeferStatsAmbientAirTemperature(BaseModel):
    changed_at_ms: Annotated[Optional[int], pydantic.Field(alias="changedAtMs")] = None
    r"""Timestamp in Unix milliseconds since epoch."""

    temp_in_milli_c: Annotated[Optional[int], pydantic.Field(alias="tempInMilliC")] = (
        None
    )
    r"""Ambient temperature in millidegree Celsius."""
