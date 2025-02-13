# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InputStreamParams"]


class InputStreamParams(TypedDict, total=False):
    ids: Required[List[str]]
    """Comma-separated list of asset IDs. Limited to 100 ID's for each request."""

    start_time: Required[Annotated[str, PropertyInfo(alias="startTime")]]
    """A start time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    type: Required[
        Literal[
            "auxInput1",
            "auxInput2",
            "auxInput3",
            "auxInput4",
            "auxInput5",
            "auxInput6",
            "auxInput7",
            "auxInput8",
            "auxInput9",
            "auxInput10",
            "auxInput11",
            "auxInput12",
            "auxInput13",
            "analogInput1Voltage",
            "analogInput2Voltage",
            "analogInput1Current",
            "analogInput2Current",
            "batteryVoltage",
        ]
    ]
    """Input stat type to query for.

    Valid values: `auxInput1`, `auxInput2`, `auxInput3`, `auxInput4`, `auxInput5`,
    `auxInput6`, `auxInput7`, `auxInput8`, `auxInput9`, `auxInput10`, `auxInput11`,
    `auxInput12`, `auxInput13`, `analogInput1Voltage`, `analogInput2Voltage`,
    `analogInput1Current`, `analogInput2Current`, `batteryVoltage`
    """

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    end_time: Annotated[str, PropertyInfo(alias="endTime")]
    """An end time in RFC 3339 format.

    Defaults to never if not provided; if not provided then pagination will not
    cease, and a valid pagination cursor will always be returned. Millisecond
    precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
    2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    include_attributes: Annotated[bool, PropertyInfo(alias="includeAttributes")]
    """Optional boolean indicating whether to return attributes on supported entities"""

    include_external_ids: Annotated[bool, PropertyInfo(alias="includeExternalIds")]
    """
    Optional boolean indicating whether to return external IDs on supported entities
    """

    include_tags: Annotated[bool, PropertyInfo(alias="includeTags")]
    """Optional boolean indicating whether to return tags on supported entities"""
