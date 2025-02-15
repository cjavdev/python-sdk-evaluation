"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateCarrierProposedAssignmentRequestTypedDict(TypedDict):
    r"""New assignment for a driver."""

    driver_id: str
    r"""ID for the driver for the driver that this assignment is for. This can be either a unique Samsara ID or an external ID for the driver."""
    vehicle_id: str
    r"""ID for the vehicle to propose. This can be either a unique Samsara ID or an external ID for the vehicle."""
    active_time: NotRequired[str]
    r"""Time after which this assignment will be active and visible to the driver on the mobile app. Not setting it makes it active now. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""
    shipping_docs: NotRequired[str]
    r"""Shipping Documents that this assignment will propose to the driver."""
    trailer_ids: NotRequired[List[str]]
    r"""IDs of trailers to propose. This can be either a unique Samsara IDs or an external IDs for the trailers. (forbidden if trailerNames is set)"""
    trailer_names: NotRequired[List[str]]
    r"""Names of trailers to propose. (forbidden if trailerIds is set)"""


class CreateCarrierProposedAssignmentRequest(BaseModel):
    r"""New assignment for a driver."""

    driver_id: Annotated[str, pydantic.Field(alias="driverId")]
    r"""ID for the driver for the driver that this assignment is for. This can be either a unique Samsara ID or an external ID for the driver."""

    vehicle_id: Annotated[str, pydantic.Field(alias="vehicleId")]
    r"""ID for the vehicle to propose. This can be either a unique Samsara ID or an external ID for the vehicle."""

    active_time: Annotated[Optional[str], pydantic.Field(alias="activeTime")] = None
    r"""Time after which this assignment will be active and visible to the driver on the mobile app. Not setting it makes it active now. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    shipping_docs: Annotated[Optional[str], pydantic.Field(alias="shippingDocs")] = None
    r"""Shipping Documents that this assignment will propose to the driver."""

    trailer_ids: Annotated[Optional[List[str]], pydantic.Field(alias="trailerIds")] = (
        None
    )
    r"""IDs of trailers to propose. This can be either a unique Samsara IDs or an external IDs for the trailers. (forbidden if trailerNames is set)"""

    trailer_names: Annotated[
        Optional[List[str]], pydantic.Field(alias="trailerNames")
    ] = None
    r"""Names of trailers to propose. (forbidden if trailerIds is set)"""
