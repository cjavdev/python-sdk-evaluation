"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AssetResponseResponseBodyTypedDict(TypedDict):
    r"""Asset that the location readings are tied to."""

    id: str
    r"""ID of the asset"""
    external_ids: NotRequired[Dict[str, str]]
    r"""A map of external ids"""


class AssetResponseResponseBody(BaseModel):
    r"""Asset that the location readings are tied to."""

    id: str
    r"""ID of the asset"""

    external_ids: Annotated[
        Optional[Dict[str, str]], pydantic.Field(alias="externalIds")
    ] = None
    r"""A map of external ids"""
