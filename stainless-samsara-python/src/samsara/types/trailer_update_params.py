# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TrailerUpdateParams", "Attribute"]


class TrailerUpdateParams(TypedDict, total=False):
    attributes: Iterable[Attribute]
    """A list of attributes to assign to the trailer."""

    enabled_for_mobile: Annotated[bool, PropertyInfo(alias="enabledForMobile")]
    """Indicates if the trailer is visible on the Samsara mobile apps."""

    external_ids: Annotated[Dict[str, str], PropertyInfo(alias="externalIds")]
    """A map of external ids"""

    license_plate: Annotated[str, PropertyInfo(alias="licensePlate")]
    """The license plate of the Trailer.

    **By default**: empty. Can be set or updated through the Samsara Dashboard or
    the API at any time.
    """

    name: str
    """The human-readable name of the Trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    notes: str
    """These are generic notes about the Trailer.

    Empty by default. Can be set or updated through the Samsara Dashboard or the API
    at any time.
    """

    odometer_meters: Annotated[int, PropertyInfo(alias="odometerMeters")]
    """
    When you provide a manual odometer override, Samsara will begin updating a
    trailer's odometer using GPS distance traveled since this override was set. Only
    applies to trailers installed with Samsara gateways.
    """

    tag_ids: Annotated[List[str], PropertyInfo(alias="tagIds")]
    """An array of IDs of tags to associate with this trailer.

    If your access to the API is scoped by one or more tags, this field is required
    to pass in.
    """

    trailer_serial_number: Annotated[str, PropertyInfo(alias="trailerSerialNumber")]
    """The serial number of the trailer."""


class Attribute(TypedDict, total=False):
    id: str
    """Id of the attribute"""

    name: str
    """Name of the attribute"""

    number_values: Annotated[Iterable[float], PropertyInfo(alias="numberValues")]
    """List of number values associated with the attribute"""

    string_values: Annotated[List[str], PropertyInfo(alias="stringValues")]
    """List of string values associated with the attribute."""
