# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DriverCoachAssignmentUpdateParams"]


class DriverCoachAssignmentUpdateParams(TypedDict, total=False):
    driver_id: Required[Annotated[str, PropertyInfo(alias="driverId")]]
    """Required string ID of the driver. This is a unique Samsara ID of a driver."""

    coach_id: Annotated[str, PropertyInfo(alias="coachId")]
    """Optional string ID of the coach.

    This is a unique Samsara user ID. If not provided, existing coach assignment
    will be removed.
    """
