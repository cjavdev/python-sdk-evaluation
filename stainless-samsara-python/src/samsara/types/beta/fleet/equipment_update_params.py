# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EquipmentUpdateParams", "Attribute"]


class EquipmentUpdateParams(TypedDict, total=False):
    path_id: Required[Annotated[str, PropertyInfo(alias="id")]]

    body_id: Annotated[str, PropertyInfo(alias="id")]
    """The unique Samsara ID of the Equipment.

    This is automatically generated when the Equipment object is created. It cannot
    be changed.
    """

    attributes: Iterable[Attribute]
    """List of attributes associated with the entity"""

    engine_hours: Annotated[int, PropertyInfo(alias="engineHours")]
    """
    When you provide a manual engine hours override, Samsara will begin updating a
    equipment's engine hours used since this override was set.
    """

    equipment_serial_number: Annotated[str, PropertyInfo(alias="equipmentSerialNumber")]
    """The serial number of the equipment."""

    external_ids: Annotated[Dict[str, str], PropertyInfo(alias="externalIds")]
    """A map of external ids"""

    name: str
    """The human-readable name of the Equipment.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    notes: str
    """These are generic notes about the Equipment.

    Empty by default. Can be set or updated through the Samsara Dashboard or the API
    at any time.
    """

    odometer_meters: Annotated[int, PropertyInfo(alias="odometerMeters")]
    """
    When you provide a manual odometer override, Samsara will begin updating a
    equipment's odometer using GPS distance traveled since this override was set.
    """

    tag_ids: Annotated[List[str], PropertyInfo(alias="tagIds")]
    """An array of IDs of tags to associate with this equipment.

    If your access to the API is scoped by one or more tags, this field is required
    to pass in.
    """


class Attribute(TypedDict, total=False):
    id: str
    """Id of the attribute"""

    name: str
    """Name of the attribute"""

    number_values: Annotated[Iterable[float], PropertyInfo(alias="numberValues")]
    """List of number values associated with the attribute"""

    string_values: Annotated[List[str], PropertyInfo(alias="stringValues")]
    """List of string values associated with the attribute."""
