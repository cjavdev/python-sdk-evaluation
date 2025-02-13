# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HoDutyStatusParams"]


class HoDutyStatusParams(TypedDict, total=False):
    duty_status: Required[str]
    """Duty status to set the driver to.

    The only supported values are 'ON_DUTY' and 'OFF_DUTY'.
    """

    location: str
    """Location to associate the duty status change with."""

    remark: str
    """Remark to associate the duty status change with."""

    status_change_at_ms: float
    """Timestamp that the duty status will begin at specified in milliseconds UNIX
    time.

    Defaults to the current time if left blank. This can only be set to up to 8
    hours in the past.
    """

    vehicle_id: float
    """Vehicle ID to associate the duty status change with."""
