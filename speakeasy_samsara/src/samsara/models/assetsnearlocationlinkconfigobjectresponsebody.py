"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class AssetsNearLocationLinkConfigObjectResponseBodyTypedDict(TypedDict):
    r"""Configuration details specific to the 'By Location' Live Sharing Link."""

    address_id: str
    r"""ID of the address. Can be either a unique Samsara ID or an external ID for the address."""


class AssetsNearLocationLinkConfigObjectResponseBody(BaseModel):
    r"""Configuration details specific to the 'By Location' Live Sharing Link."""

    address_id: Annotated[str, pydantic.Field(alias="addressId")]
    r"""ID of the address. Can be either a unique Samsara ID or an external ID for the address."""
