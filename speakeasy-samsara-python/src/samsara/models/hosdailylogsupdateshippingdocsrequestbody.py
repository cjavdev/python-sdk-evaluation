"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class HosDailyLogsUpdateShippingDocsRequestBodyTypedDict(TypedDict):
    r"""Update the shippingDocs field."""

    shipping_docs: str
    r"""ShippingDocs associated with the driver for the day."""


class HosDailyLogsUpdateShippingDocsRequestBody(BaseModel):
    r"""Update the shippingDocs field."""

    shipping_docs: Annotated[str, pydantic.Field(alias="shippingDocs")]
    r"""ShippingDocs associated with the driver for the day."""
