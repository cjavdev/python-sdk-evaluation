"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .equipmentresponse import EquipmentResponse, EquipmentResponseTypedDict
from .standarderrorresponse import StandardErrorResponse, StandardErrorResponseTypedDict
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, PathParamMetadata
from typing import Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class GetEquipmentRequestTypedDict(TypedDict):
    id: str
    r"""Samsara ID of the Equipment."""


class GetEquipmentRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Samsara ID of the Equipment."""


GetEquipmentResponseTypedDict = TypeAliasType(
    "GetEquipmentResponseTypedDict",
    Union[EquipmentResponseTypedDict, StandardErrorResponseTypedDict],
)


GetEquipmentResponse = TypeAliasType(
    "GetEquipmentResponse", Union[EquipmentResponse, StandardErrorResponse]
)
