"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .aempequipmentgetaempequipmentlistbadrequesterrorresponsebody import (
    AempEquipmentGetAempEquipmentListBadRequestErrorResponseBody,
    AempEquipmentGetAempEquipmentListBadRequestErrorResponseBodyTypedDict,
)
from .aempequipmentgetaempequipmentlistresponsebody import (
    AempEquipmentGetAempEquipmentListResponseBody,
    AempEquipmentGetAempEquipmentListResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, PathParamMetadata
from typing import Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class GetAempEquipmentListRequestTypedDict(TypedDict):
    page_number: str
    r"""The number corresponding to a specific page of paginated results, defaulting to the first page if not provided. The default page size is 100 records."""


class GetAempEquipmentListRequest(BaseModel):
    page_number: Annotated[
        str,
        pydantic.Field(alias="pageNumber"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The number corresponding to a specific page of paginated results, defaulting to the first page if not provided. The default page size is 100 records."""


GetAempEquipmentListResponseTypedDict = TypeAliasType(
    "GetAempEquipmentListResponseTypedDict",
    Union[
        AempEquipmentGetAempEquipmentListResponseBodyTypedDict,
        AempEquipmentGetAempEquipmentListBadRequestErrorResponseBodyTypedDict,
    ],
)


GetAempEquipmentListResponse = TypeAliasType(
    "GetAempEquipmentListResponse",
    Union[
        AempEquipmentGetAempEquipmentListResponseBody,
        AempEquipmentGetAempEquipmentListBadRequestErrorResponseBody,
    ],
)
