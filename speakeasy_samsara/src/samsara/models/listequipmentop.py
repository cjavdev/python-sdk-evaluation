"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .equipmentlistresponse import EquipmentListResponse, EquipmentListResponseTypedDict
from .standarderrorresponse import StandardErrorResponse, StandardErrorResponseTypedDict
import pydantic
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class ListEquipmentRequestTypedDict(TypedDict):
    limit: NotRequired[int]
    r"""The limit for how many objects will be in the response. Default and max for this value is 512 objects."""
    after: NotRequired[str]
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""
    parent_tag_ids: NotRequired[List[str]]
    r"""A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`"""
    tag_ids: NotRequired[List[str]]
    r"""A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`"""


class ListEquipmentRequest(BaseModel):
    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The limit for how many objects will be in the response. Default and max for this value is 512 objects."""

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


ListEquipmentResponseTypedDict = TypeAliasType(
    "ListEquipmentResponseTypedDict",
    Union[EquipmentListResponseTypedDict, StandardErrorResponseTypedDict],
)


ListEquipmentResponse = TypeAliasType(
    "ListEquipmentResponse", Union[EquipmentListResponse, StandardErrorResponse]
)
