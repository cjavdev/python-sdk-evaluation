# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TrailersListTrailersResponseBody", "Data", "DataInstalledGateway", "DataTag", "Pagination"]


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
    id: str
    """The unique Samsara ID of the Trailer.

    This is automatically generated when the Trailer object is created. It cannot be
    changed.
    """

    enabled_for_mobile: Optional[bool] = FieldInfo(alias="enabledForMobile", default=None)
    """Indicates if the trailer is visible on the Samsara mobile apps."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    installed_gateway: Optional[DataInstalledGateway] = FieldInfo(alias="installedGateway", default=None)
    """A minified gateway object.

    This field will be omitted if the trailer does not have a gateway installed.
    """

    license_plate: Optional[str] = FieldInfo(alias="licensePlate", default=None)
    """The license plate of the Trailer.

    **By default**: empty. Can be set or updated through the Samsara Dashboard or
    the API at any time.
    """

    name: Optional[str] = None
    """The human-readable name of the Trailer.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    notes: Optional[str] = None
    """These are generic notes about the Trailer.

    Empty by default. Can be set or updated through the Samsara Dashboard or the API
    at any time.
    """

    tags: Optional[List[DataTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Trailer.
    """

    trailer_serial_number: Optional[str] = FieldInfo(alias="trailerSerialNumber", default=None)
    """The serial number of the trailer."""


class Pagination(BaseModel):
    end_cursor: str = FieldInfo(alias="endCursor")
    """Cursor identifier representing the last element in the response.

    This value should be used in conjunction with a subsequent request's 'after'
    query parameter. This may be an empty string if there are no more pages left to
    view.
    """

    has_next_page: bool = FieldInfo(alias="hasNextPage")
    """
    True if there are more pages of results immediately available after this
    endCursor.
    """


class TrailersListTrailersResponseBody(BaseModel):
    data: List[Data]
    """List of trailer objects."""

    pagination: Pagination
    """Pagination parameters."""
