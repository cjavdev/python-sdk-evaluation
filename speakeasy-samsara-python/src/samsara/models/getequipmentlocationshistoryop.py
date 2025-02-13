"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .equipmentlocationslistresponse import (
    EquipmentLocationsListResponse,
    EquipmentLocationsListResponseTypedDict,
)
from .standarderrorresponse import StandardErrorResponse, StandardErrorResponseTypedDict
import pydantic
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class GetEquipmentLocationsHistoryRequestTypedDict(TypedDict):
    start_time: str
    r"""A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""
    end_time: str
    r"""An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""
    after: NotRequired[str]
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""
    parent_tag_ids: NotRequired[List[str]]
    r"""A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`"""
    tag_ids: NotRequired[List[str]]
    r"""A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`"""
    equipment_ids: NotRequired[List[str]]
    r"""A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678`"""


class GetEquipmentLocationsHistoryRequest(BaseModel):
    start_time: Annotated[
        str,
        pydantic.Field(alias="startTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""

    end_time: Annotated[
        str,
        pydantic.Field(alias="endTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""

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

    equipment_ids: Annotated[
        Optional[List[str]],
        pydantic.Field(alias="equipmentIds"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""A filter on the data based on this comma-separated list of equipment IDs. Example: `equipmentIds=1234,5678`"""


GetEquipmentLocationsHistoryResponseTypedDict = TypeAliasType(
    "GetEquipmentLocationsHistoryResponseTypedDict",
    Union[EquipmentLocationsListResponseTypedDict, StandardErrorResponseTypedDict],
)


GetEquipmentLocationsHistoryResponse = TypeAliasType(
    "GetEquipmentLocationsHistoryResponse",
    Union[EquipmentLocationsListResponse, StandardErrorResponse],
)
