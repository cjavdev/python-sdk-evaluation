"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DriverEfficiencyDifficultyScoreDataObjectResponseBodyTypedDict(TypedDict):
    r"""Difficulty score won't be available if there is no data to compute it against."""

    overall_score: NotRequired[str]
    r"""Represents the overall difficulty score. It has scores from 1 to 5."""
    topography_score: NotRequired[str]
    r"""Represents the topography difficulty score. It has scores from 1 to 5."""
    vehicle_weight_score: NotRequired[str]
    r"""Represents the average vehicle weight score. It has scores from 1 to 5."""


class DriverEfficiencyDifficultyScoreDataObjectResponseBody(BaseModel):
    r"""Difficulty score won't be available if there is no data to compute it against."""

    overall_score: Annotated[Optional[str], pydantic.Field(alias="overallScore")] = None
    r"""Represents the overall difficulty score. It has scores from 1 to 5."""

    topography_score: Annotated[
        Optional[str], pydantic.Field(alias="topographyScore")
    ] = None
    r"""Represents the topography difficulty score. It has scores from 1 to 5."""

    vehicle_weight_score: Annotated[
        Optional[str], pydantic.Field(alias="vehicleWeightScore")
    ] = None
    r"""Represents the average vehicle weight score. It has scores from 1 to 5."""
