"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v1sensorhistoryresponse_results import (
    V1SensorHistoryResponseResults,
    V1SensorHistoryResponseResultsTypedDict,
)
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class V1SensorHistoryResponseTypedDict(TypedDict):
    r"""Contains the results for a sensor history request. Each result contains a timestamp and datapoint for each requested (sensor, field) pair."""

    results: NotRequired[List[V1SensorHistoryResponseResultsTypedDict]]


class V1SensorHistoryResponse(BaseModel):
    r"""Contains the results for a sensor history request. Each result contains a timestamp and datapoint for each requested (sensor, field) pair."""

    results: Optional[List[V1SensorHistoryResponseResults]] = None
