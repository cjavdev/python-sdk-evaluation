# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CarrierProposedAssignmentCreateParams"]


class CarrierProposedAssignmentCreateParams(TypedDict, total=False):
    driver_id: Required[Annotated[str, PropertyInfo(alias="driverId")]]
    """ID for the driver for the driver that this assignment is for.

    This can be either a unique Samsara ID or an external ID for the driver.
    """

    vehicle_id: Required[Annotated[str, PropertyInfo(alias="vehicleId")]]
    """ID for the vehicle to propose.

    This can be either a unique Samsara ID or an external ID for the vehicle.
    """

    active_time: Annotated[str, PropertyInfo(alias="activeTime")]
    """
    Time after which this assignment will be active and visible to the driver on the
    mobile app. Not setting it makes it active now. UTC timestamp in RFC 3339
    format. Example: `2020-01-27T07:06:25Z`.
    """

    shipping_docs: Annotated[str, PropertyInfo(alias="shippingDocs")]
    """Shipping Documents that this assignment will propose to the driver."""

    trailer_ids: Annotated[List[str], PropertyInfo(alias="trailerIds")]
    """IDs of trailers to propose.

    This can be either a unique Samsara IDs or an external IDs for the trailers.
    (forbidden if trailerNames is set)
    """

    trailer_names: Annotated[List[str], PropertyInfo(alias="trailerNames")]
    """Names of trailers to propose. (forbidden if trailerIds is set)"""
