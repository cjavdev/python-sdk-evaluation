# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ListIndustrialAssetsResponse",
    "Data",
    "DataDataOutput",
    "DataDataOutputDataInput",
    "DataDataOutputDataInputLastPoint",
    "DataLocation",
    "DataLocationDataInput",
    "DataParentAsset",
    "DataRunningStatusDataInput",
    "DataTag",
    "Pagination",
]


class DataDataOutputDataInputLastPoint(BaseModel):
    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[float] = None
    """Numeric value of the data point."""


class DataDataOutputDataInput(BaseModel):
    id: Optional[str] = None
    """ID of the data input"""

    data_group: Optional[str] = FieldInfo(alias="dataGroup", default=None)
    """Name of the data group that the data input is associated with"""

    last_point: Optional[DataDataOutputDataInputLastPoint] = FieldInfo(alias="lastPoint", default=None)
    """The last reported point of a data input."""

    name: Optional[str] = None
    """Name of the data input"""

    units: Optional[str] = None
    """Units of data for this data input"""


class DataDataOutput(BaseModel):
    id: Optional[str] = None
    """ID of the data output"""

    data_group: Optional[str] = FieldInfo(alias="dataGroup", default=None)
    """Name of the data group that the data output is associated with"""

    data_input: Optional[DataDataOutputDataInput] = FieldInfo(alias="dataInput", default=None)

    device_id: Optional[str] = FieldInfo(alias="deviceId", default=None)
    """ID of the device that the data output is configured on"""

    name: Optional[str] = None
    """Name of the data output"""


class DataLocation(BaseModel):
    formatted_address: Optional[str] = FieldInfo(alias="formattedAddress", default=None)
    """Formatted address of the location"""

    latitude: Optional[float] = None
    """The latitude of the asset in decimal degrees."""

    longitude: Optional[float] = None
    """The longitude of the asset in decimal degrees."""


class DataLocationDataInput(BaseModel):
    id: str
    """Id of the data input"""


class DataParentAsset(BaseModel):
    id: str
    """The id of the parent asset that the asset belongs to."""

    name: str
    """The name of the asset."""


class DataRunningStatusDataInput(BaseModel):
    id: str
    """Id of the data input"""


class DataTag(BaseModel):
    id: Optional[str] = None
    """ID of the tag."""

    name: Optional[str] = None
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class Data(BaseModel):
    id: str
    """The id of the asset"""

    is_running: bool = FieldInfo(alias="isRunning")
    """The running status of the asset. Returns True for On, and False for Off."""

    name: str
    """The name of the asset."""

    custom_metadata: Optional[Dict[str, str]] = FieldInfo(alias="customMetadata", default=None)
    """The custom fields of an asset."""

    data_outputs: Optional[List[DataDataOutput]] = FieldInfo(alias="dataOutputs", default=None)
    """The list of data outputs configured on the asset."""

    location: Optional[DataLocation] = None
    """For locationType "point", latitude and longitude are required.

    For "address", formattedAddress must be provided, and lat/long can be optionally
    included for displaying a dot on the assets map. For "dataInput", this object
    should not be passed in.
    """

    location_data_input: Optional[DataLocationDataInput] = FieldInfo(alias="locationDataInput", default=None)
    """
    The associated location data input (only applicable when locationType is
    "dataInput").
    """

    location_type: Optional[Literal["point", "address", "dataInput"]] = FieldInfo(alias="locationType", default=None)
    """The format of the location.

    This field is required if a location is provided. Valid values: `point`,
    `address`, `dataInput`.
    """

    parent_asset: Optional[DataParentAsset] = FieldInfo(alias="parentAsset", default=None)
    """The asset's parent"""

    running_status_data_input: Optional[DataRunningStatusDataInput] = FieldInfo(
        alias="runningStatusDataInput", default=None
    )
    """The associated running status data input.

    isRunning will be true when the data input's value is 1.
    """

    tags: Optional[List[DataTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Industrial Asset. **By default**: empty. Can be set or
    updated through the Samsara Dashboard or the API at any time.
    """


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


class ListIndustrialAssetsResponse(BaseModel):
    data: Optional[List[Data]] = None

    pagination: Optional[Pagination] = None
    """Pagination parameters."""
