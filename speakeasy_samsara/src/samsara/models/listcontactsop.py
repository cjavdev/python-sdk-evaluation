"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .listcontactsresponse import ListContactsResponse, ListContactsResponseTypedDict
from .standarderrorresponse import StandardErrorResponse, StandardErrorResponseTypedDict
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class ListContactsRequestTypedDict(TypedDict):
    limit: NotRequired[int]
    r"""The limit for how many objects will be in the response. Default and max for this value is 512 objects."""
    after: NotRequired[str]
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""


class ListContactsRequest(BaseModel):
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


ListContactsResponse1TypedDict = TypeAliasType(
    "ListContactsResponse1TypedDict",
    Union[ListContactsResponseTypedDict, StandardErrorResponseTypedDict],
)


ListContactsResponse1 = TypeAliasType(
    "ListContactsResponse1", Union[ListContactsResponse, StandardErrorResponse]
)
