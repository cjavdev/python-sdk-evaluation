"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .inline_response_200_7 import InlineResponse2007, InlineResponse2007TypedDict
import pydantic
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class V1getAllTrailerAssignmentsRequestTypedDict(TypedDict):
    start_ms: NotRequired[int]
    r"""Timestamp in Unix epoch miliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments."""
    end_ms: NotRequired[int]
    r"""Timestamp in Unix epoch miliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time"""
    limit: NotRequired[float]
    r"""Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'."""
    starting_after: NotRequired[str]
    r"""Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter."""
    ending_before: NotRequired[str]
    r"""Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter."""


class V1getAllTrailerAssignmentsRequest(BaseModel):
    start_ms: Annotated[
        Optional[int],
        pydantic.Field(alias="startMs"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Timestamp in Unix epoch miliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments."""

    end_ms: Annotated[
        Optional[int],
        pydantic.Field(alias="endMs"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Timestamp in Unix epoch miliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time"""

    limit: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'."""

    starting_after: Annotated[
        Optional[str],
        pydantic.Field(alias="startingAfter"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter."""

    ending_before: Annotated[
        Optional[str],
        pydantic.Field(alias="endingBefore"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter."""


V1getAllTrailerAssignmentsResponseTypedDict = TypeAliasType(
    "V1getAllTrailerAssignmentsResponseTypedDict",
    Union[InlineResponse2007TypedDict, str],
)


V1getAllTrailerAssignmentsResponse = TypeAliasType(
    "V1getAllTrailerAssignmentsResponse", Union[InlineResponse2007, str]
)
