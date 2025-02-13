# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["SensorHumidityParams"]


class SensorHumidityParams(TypedDict, total=False):
    sensors: Required[Iterable[int]]
    """List of sensor IDs to query."""
