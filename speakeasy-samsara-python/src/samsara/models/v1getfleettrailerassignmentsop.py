"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v1trailerassignmentsresponse import (
    V1TrailerAssignmentsResponse,
    V1TrailerAssignmentsResponseTypedDict,
)
import pydantic
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class V1getFleetTrailerAssignmentsRequestTypedDict(TypedDict):
    trailer_id: int
    r"""ID of trailer. Must contain only digits 0-9."""
    start_ms: NotRequired[int]
    r"""Timestamp in Unix epoch milliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments."""
    end_ms: NotRequired[int]
    r"""Timestamp in Unix epoch milliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time"""


class V1getFleetTrailerAssignmentsRequest(BaseModel):
    trailer_id: Annotated[
        int,
        pydantic.Field(alias="trailerId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""ID of trailer. Must contain only digits 0-9."""

    start_ms: Annotated[
        Optional[int],
        pydantic.Field(alias="startMs"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Timestamp in Unix epoch milliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments."""

    end_ms: Annotated[
        Optional[int],
        pydantic.Field(alias="endMs"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Timestamp in Unix epoch milliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time"""


V1getFleetTrailerAssignmentsResponseTypedDict = TypeAliasType(
    "V1getFleetTrailerAssignmentsResponseTypedDict",
    Union[V1TrailerAssignmentsResponseTypedDict, str],
)


V1getFleetTrailerAssignmentsResponse = TypeAliasType(
    "V1getFleetTrailerAssignmentsResponse", Union[V1TrailerAssignmentsResponse, str]
)
