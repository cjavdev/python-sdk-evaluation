"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .standarderrorresponse import StandardErrorResponse, StandardErrorResponseTypedDict
from .vehiclelocationslistresponse import (
    VehicleLocationsListResponse,
    VehicleLocationsListResponseTypedDict,
)
import pydantic
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class GetVehicleLocationsFeedRequestTypedDict(TypedDict):
    after: NotRequired[str]
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""
    parent_tag_ids: NotRequired[List[str]]
    r"""A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`"""
    tag_ids: NotRequired[List[str]]
    r"""A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`"""
    vehicle_ids: NotRequired[List[str]]
    r"""A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`"""


class GetVehicleLocationsFeedRequest(BaseModel):
    after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""

    parent_tag_ids: Annotated[
        Optional[List[str]],
        pydantic.Field(alias="parentTagIds"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`"""

    tag_ids: Annotated[
        Optional[List[str]],
        pydantic.Field(alias="tagIds"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`"""

    vehicle_ids: Annotated[
        Optional[List[str]],
        pydantic.Field(alias="vehicleIds"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""A filter on the data based on this comma-separated list of vehicle IDs. Example: `vehicleIds=1234,5678`"""


GetVehicleLocationsFeedResponseTypedDict = TypeAliasType(
    "GetVehicleLocationsFeedResponseTypedDict",
    Union[VehicleLocationsListResponseTypedDict, StandardErrorResponseTypedDict],
)


GetVehicleLocationsFeedResponse = TypeAliasType(
    "GetVehicleLocationsFeedResponse",
    Union[VehicleLocationsListResponse, StandardErrorResponse],
)
