# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DriverTrailerAssignmentCreateParams"]


class DriverTrailerAssignmentCreateParams(TypedDict, total=False):
    driver_id: Required[Annotated[str, PropertyInfo(alias="driverId")]]
    """ID of the driver.

    This can be either a unique Samsara ID or an
    [external ID](https://developers.samsara.com/docs/external-ids) for the driver.
    """

    trailer_id: Required[Annotated[str, PropertyInfo(alias="trailerId")]]
    """ID of the trailer.

    This can be either a unique Samsara ID or an
    [external ID](https://developers.samsara.com/docs/external-ids) for the trailer.
    """

    start_time: Annotated[str, PropertyInfo(alias="startTime")]
    """The start time in RFC 3339 format.

    The time needs to be current or within the past 7 days. Defaults to now if not
    provided
    """
