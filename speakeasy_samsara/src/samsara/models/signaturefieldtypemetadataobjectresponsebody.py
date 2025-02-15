"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SignatureFieldTypeMetaDataObjectResponseBodyTypedDict(TypedDict):
    r"""The signature field metadata."""

    legal_text: NotRequired[str]
    r"""The signature field legal text."""


class SignatureFieldTypeMetaDataObjectResponseBody(BaseModel):
    r"""The signature field metadata."""

    legal_text: Annotated[Optional[str], pydantic.Field(alias="legalText")] = None
    r"""The signature field legal text."""
