# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HistoryCreateParams", "Series"]


class HistoryCreateParams(TypedDict, total=False):
    end_ms: Required[Annotated[int, PropertyInfo(alias="endMs")]]
    """End of the time range, specified in milliseconds UNIX time."""

    series: Required[Iterable[Series]]

    start_ms: Required[Annotated[int, PropertyInfo(alias="startMs")]]
    """Beginning of the time range, specified in milliseconds UNIX time."""

    step_ms: Required[Annotated[int, PropertyInfo(alias="stepMs")]]
    """Time resolution for which data should be returned, in milliseconds.

    Specifying 3600000 will return data at hour intervals.
    """

    fill_missing: Annotated[Literal["withNull", "withPrevious"], PropertyInfo(alias="fillMissing")]


class Series(TypedDict, total=False):
    field: Required[
        Literal[
            "ambientTemperature",
            "cargoPercent",
            "currentLoop1Raw",
            "currentLoop1Mapped",
            "currentLoop2Raw",
            "currentLoop2Mapped",
            "doorClosed",
            "humidity",
            "pmPowerTotal",
            "pmPhase1Power",
            "pmPhase2Power",
            "pmPhase3Power",
            "pmPhase1PowerFactor",
            "pmPhase2PowerFactor",
            "pmPhase3PowerFactor",
            "probeTemperature",
        ]
    ]
    """Field to query."""

    widget_id: Required[Annotated[int, PropertyInfo(alias="widgetId")]]
    """V1Sensor ID to query."""
