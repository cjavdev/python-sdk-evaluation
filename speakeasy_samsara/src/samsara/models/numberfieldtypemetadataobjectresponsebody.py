"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class NumberFieldTypeMetaDataObjectResponseBodyTypedDict(TypedDict):
    r"""The number field metadata."""

    number_of_decimal_places: NotRequired[int]
    r"""The number of decimal places allowed for the field."""


class NumberFieldTypeMetaDataObjectResponseBody(BaseModel):
    r"""The number field metadata."""

    number_of_decimal_places: Annotated[
        Optional[int], pydantic.Field(alias="numberOfDecimalPlaces")
    ] = None
    r"""The number of decimal places allowed for the field."""
