"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .drivercoachassignmentsgetdrivercoachassignmentbadrequesterrorresponsebody import (
    DriverCoachAssignmentsGetDriverCoachAssignmentBadRequestErrorResponseBody,
    DriverCoachAssignmentsGetDriverCoachAssignmentBadRequestErrorResponseBodyTypedDict,
)
from .drivercoachassignmentsgetdrivercoachassignmentresponsebody import (
    DriverCoachAssignmentsGetDriverCoachAssignmentResponseBody,
    DriverCoachAssignmentsGetDriverCoachAssignmentResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class GetDriverCoachAssignmentRequestTypedDict(TypedDict):
    driver_ids: NotRequired[List[str]]
    r"""Optional string of comma separated IDs of the drivers. This can be either a unique Samsara driver ID or an external ID for the driver."""
    coach_ids: NotRequired[List[str]]
    r"""Optional string of comma separated IDs of the coaches."""
    include_external_ids: NotRequired[bool]
    r"""Optional boolean indicating whether to return external IDs on supported entities"""
    after: NotRequired[str]
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""


class GetDriverCoachAssignmentRequest(BaseModel):
    driver_ids: Annotated[
        Optional[List[str]],
        pydantic.Field(alias="driverIds"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Optional string of comma separated IDs of the drivers. This can be either a unique Samsara driver ID or an external ID for the driver."""

    coach_ids: Annotated[
        Optional[List[str]],
        pydantic.Field(alias="coachIds"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Optional string of comma separated IDs of the coaches."""

    include_external_ids: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeExternalIds"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional boolean indicating whether to return external IDs on supported entities"""

    after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""


GetDriverCoachAssignmentResponseTypedDict = TypeAliasType(
    "GetDriverCoachAssignmentResponseTypedDict",
    Union[
        DriverCoachAssignmentsGetDriverCoachAssignmentResponseBodyTypedDict,
        DriverCoachAssignmentsGetDriverCoachAssignmentBadRequestErrorResponseBodyTypedDict,
    ],
)


GetDriverCoachAssignmentResponse = TypeAliasType(
    "GetDriverCoachAssignmentResponse",
    Union[
        DriverCoachAssignmentsGetDriverCoachAssignmentResponseBody,
        DriverCoachAssignmentsGetDriverCoachAssignmentBadRequestErrorResponseBody,
    ],
)
