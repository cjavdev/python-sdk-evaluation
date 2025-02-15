"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .alertsgetincidentsbadrequesterrorresponsebody import (
    AlertsGetIncidentsBadRequestErrorResponseBody,
    AlertsGetIncidentsBadRequestErrorResponseBodyTypedDict,
)
from .alertsgetincidentsresponsebody import (
    AlertsGetIncidentsResponseBody,
    AlertsGetIncidentsResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class GetIncidentsRequestTypedDict(TypedDict):
    start_time: str
    r"""Required RFC 3339 timestamp that indicates when to begin receiving data. This will be based on updatedAtTime."""
    configuration_ids: List[str]
    r"""Required array of alert configuration ids to return incident data for."""
    end_time: NotRequired[str]
    r"""Optional RFC 3339 timestamp to stop receiving data. Defaults to now if not provided. This will be based on updatedAtTime."""
    after: NotRequired[str]
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""


class GetIncidentsRequest(BaseModel):
    start_time: Annotated[
        str,
        pydantic.Field(alias="startTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Required RFC 3339 timestamp that indicates when to begin receiving data. This will be based on updatedAtTime."""

    configuration_ids: Annotated[
        List[str],
        pydantic.Field(alias="configurationIds"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Required array of alert configuration ids to return incident data for."""

    end_time: Annotated[
        Optional[str],
        pydantic.Field(alias="endTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional RFC 3339 timestamp to stop receiving data. Defaults to now if not provided. This will be based on updatedAtTime."""

    after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""


GetIncidentsResponseTypedDict = TypeAliasType(
    "GetIncidentsResponseTypedDict",
    Union[
        AlertsGetIncidentsResponseBodyTypedDict,
        AlertsGetIncidentsBadRequestErrorResponseBodyTypedDict,
    ],
)


GetIncidentsResponse = TypeAliasType(
    "GetIncidentsResponse",
    Union[
        AlertsGetIncidentsResponseBody, AlertsGetIncidentsBadRequestErrorResponseBody
    ],
)
