# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["EquipmentUpdateResponse", "Data", "DataAttribute", "DataInstalledGateway", "DataTag"]


class DataAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataInstalledGateway(BaseModel):
    model: Literal[
        "AG15",
        "AG24",
        "AG24EU",
        "AG26",
        "AG26EU",
        "AG41",
        "AG41EU",
        "AG45",
        "AG45EU",
        "AG46",
        "AG46EU",
        "AG46P",
        "AG46PEU",
        "AG51",
        "AG51EU",
        "AG52",
        "AG52EU",
        "AG53",
        "AG53EU",
        "IG15",
        "IG21",
        "IG41",
        "IG61",
        "SG1",
        "SG1B",
        "SG1G",
        "SG1G32",
        "SG1x",
        "VG32",
        "VG33",
        "VG34",
        "VG34EU",
        "VG34FN",
        "VG34M",
        "VG54ATT",
        "VG54EU",
        "VG54FN",
        "VG54NA",
        "VG54NAE",
        "VG54NAH",
        "VG55EU",
        "VG55FN",
        "VG55NA",
    ]
    """The model of the gateway installed on the asset.

    Valid values: `AG15`, `AG24`, `AG24EU`, `AG26`, `AG26EU`, `AG41`, `AG41EU`,
    `AG45`, `AG45EU`, `AG46`, `AG46EU`, `AG46P`, `AG46PEU`, `AG51`, `AG51EU`,
    `AG52`, `AG52EU`, `AG53`, `AG53EU`, `IG15`, `IG21`, `IG41`, `IG61`, `SG1`,
    `SG1B`, `SG1G`, `SG1G32`, `SG1x`, `VG32`, `VG33`, `VG34`, `VG34EU`, `VG34FN`,
    `VG34M`, `VG54ATT`, `VG54EU`, `VG54FN`, `VG54NA`, `VG54NAE`, `VG54NAH`,
    `VG55EU`, `VG55FN`, `VG55NA`
    """

    serial: str
    """The serial number of the gateway installed on the asset."""


class DataTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class Data(BaseModel):
    id: Optional[str] = None
    """The unique Samsara ID of the Equipment.

    This is automatically generated when the Equipment object is created. It cannot
    be changed.
    """

    attributes: Optional[List[DataAttribute]] = None
    """List of attributes associated with the entity"""

    equipment_serial_number: Optional[str] = FieldInfo(alias="equipmentSerialNumber", default=None)
    """The serial number of the equipment."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    installed_gateway: Optional[DataInstalledGateway] = FieldInfo(alias="installedGateway", default=None)
    """A minified gateway object"""

    name: Optional[str] = None
    """The human-readable name of the Equipment.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    notes: Optional[str] = None
    """These are generic notes about the Equipment.

    Empty by default. Can be set or updated through the Samsara Dashboard or the API
    at any time.
    """

    tags: Optional[List[DataTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Equipment.
    """


class EquipmentUpdateResponse(BaseModel):
    data: Data
    """The equipment object."""
