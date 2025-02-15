"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .fieldobjectvaluerequestbody import (
    FieldObjectValueRequestBody,
    FieldObjectValueRequestBodyTypedDict,
)
from enum import Enum
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class FieldObjectPostRequestBodyType(str, Enum):
    r"""The type of field.  Valid values: `photo`, `string`, `number`, `multipleChoice`, `signature`, `dateTime`, `scannedDocument`, `barcode`"""

    PHOTO = "photo"
    STRING = "string"
    NUMBER = "number"
    MULTIPLE_CHOICE = "multipleChoice"
    SIGNATURE = "signature"
    DATE_TIME = "dateTime"
    SCANNED_DOCUMENT = "scannedDocument"
    BARCODE = "barcode"


class FieldObjectPostRequestBodyTypedDict(TypedDict):
    label: str
    r"""The name of the field."""
    type: FieldObjectPostRequestBodyType
    r"""The type of field.  Valid values: `photo`, `string`, `number`, `multipleChoice`, `signature`, `dateTime`, `scannedDocument`, `barcode`"""
    value: NotRequired[FieldObjectValueRequestBodyTypedDict]
    r"""The value of the document field. The shape of value depends on the type."""


class FieldObjectPostRequestBody(BaseModel):
    label: str
    r"""The name of the field."""

    type: FieldObjectPostRequestBodyType
    r"""The type of field.  Valid values: `photo`, `string`, `number`, `multipleChoice`, `signature`, `dateTime`, `scannedDocument`, `barcode`"""

    value: Optional[FieldObjectValueRequestBody] = None
    r"""The value of the document field. The shape of value depends on the type."""
