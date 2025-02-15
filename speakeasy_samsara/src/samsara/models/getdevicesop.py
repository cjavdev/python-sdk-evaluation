"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .devicesgetdevicesbadrequesterrorresponsebody import (
    DevicesGetDevicesBadRequestErrorResponseBody,
    DevicesGetDevicesBadRequestErrorResponseBodyTypedDict,
)
from .devicesgetdevicesresponsebody import (
    DevicesGetDevicesResponseBody,
    DevicesGetDevicesResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class GetDevicesRequestTypedDict(TypedDict):
    models: NotRequired[List[str]]
    r"""Optional string of comma separated device models. Valid values: `CM31`, `CM32`, `CM33`, `CM34`, `VG34`, `VG34M`, `VG34EU`, `VG34FN`, `VG54NA`, `VG54EU`, `VG55NA`, `VG55EU`, `AG24`, `AG24EU`, `AG26`, `AG26EU`, `AG45`, `AG45EU`, `AG46`, `AG46EU`, `AG46P`, `AG46PEU`, `AG51`, `AG51EU`, `AG52`, `AG52EU`, `AG53`, `AG53EU`"""
    health_statuses: NotRequired[List[str]]
    r"""Optional string of comma separated device health statuses. Valid values: `healthy`, `needsAttention`, `needsReplacement`, `dataPending`."""
    include_health: NotRequired[bool]
    r"""Optional boolean to control whether device health information is returned in the response. Defaults to false."""
    after: NotRequired[str]
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""
    limit: NotRequired[int]
    r"""The limit for how many objects will be in the response. Default and max for this value is 100 objects."""


class GetDevicesRequest(BaseModel):
    models: Annotated[
        Optional[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Optional string of comma separated device models. Valid values: `CM31`, `CM32`, `CM33`, `CM34`, `VG34`, `VG34M`, `VG34EU`, `VG34FN`, `VG54NA`, `VG54EU`, `VG55NA`, `VG55EU`, `AG24`, `AG24EU`, `AG26`, `AG26EU`, `AG45`, `AG45EU`, `AG46`, `AG46EU`, `AG46P`, `AG46PEU`, `AG51`, `AG51EU`, `AG52`, `AG52EU`, `AG53`, `AG53EU`"""

    health_statuses: Annotated[
        Optional[List[str]],
        pydantic.Field(alias="healthStatuses"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=False)),
    ] = None
    r"""Optional string of comma separated device health statuses. Valid values: `healthy`, `needsAttention`, `needsReplacement`, `dataPending`."""

    include_health: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeHealth"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional boolean to control whether device health information is returned in the response. Defaults to false."""

    after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results."""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 100
    r"""The limit for how many objects will be in the response. Default and max for this value is 100 objects."""


GetDevicesResponseTypedDict = TypeAliasType(
    "GetDevicesResponseTypedDict",
    Union[
        DevicesGetDevicesResponseBodyTypedDict,
        DevicesGetDevicesBadRequestErrorResponseBodyTypedDict,
    ],
)


GetDevicesResponse = TypeAliasType(
    "GetDevicesResponse",
    Union[DevicesGetDevicesResponseBody, DevicesGetDevicesBadRequestErrorResponseBody],
)
