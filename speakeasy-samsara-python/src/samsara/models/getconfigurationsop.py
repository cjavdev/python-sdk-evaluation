"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .alertsgetconfigurationsbadrequesterrorresponsebody import (
    AlertsGetConfigurationsBadRequestErrorResponseBody,
    AlertsGetConfigurationsBadRequestErrorResponseBodyTypedDict,
)
from .alertsgetconfigurationsresponsebody import (
    AlertsGetConfigurationsResponseBody,
    AlertsGetConfigurationsResponseBodyTypedDict,
)
from enum import Enum
import pydantic
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class QueryParamStatus(str, Enum):
    r"""The status of the alert configuration.  Valid values: `all`, `enabled`, `disabled`"""

    ALL = "all"
    ENABLED = "enabled"
    DISABLED = "disabled"


class GetConfigurationsRequestTypedDict(TypedDict):
    ids: NotRequired[List[str]]
    r"""Filter by the IDs. Returns all if no ids are provided."""
    status: NotRequired[QueryParamStatus]
    r"""The status of the alert configuration.  Valid values: `all`, `enabled`, `disabled`"""
    after: NotRequired[str]
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""
    include_external_ids: NotRequired[bool]
    r"""Optional boolean indicating whether to return external IDs on supported entities"""


class GetConfigurationsRequest(BaseModel):
    ids: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by the IDs. Returns all if no ids are provided."""

    status: Annotated[
        Optional[QueryParamStatus],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = QueryParamStatus.ALL
    r"""The status of the alert configuration.  Valid values: `all`, `enabled`, `disabled`"""

    after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""

    include_external_ids: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeExternalIds"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional boolean indicating whether to return external IDs on supported entities"""


GetConfigurationsResponseTypedDict = TypeAliasType(
    "GetConfigurationsResponseTypedDict",
    Union[
        AlertsGetConfigurationsResponseBodyTypedDict,
        AlertsGetConfigurationsBadRequestErrorResponseBodyTypedDict,
    ],
)


GetConfigurationsResponse = TypeAliasType(
    "GetConfigurationsResponse",
    Union[
        AlertsGetConfigurationsResponseBody,
        AlertsGetConfigurationsBadRequestErrorResponseBody,
    ],
)
