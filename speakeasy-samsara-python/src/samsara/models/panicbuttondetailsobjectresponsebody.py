"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class PanicButtonDetailsObjectResponseBodyTypedDict(TypedDict):
    r"""Details specific to Panic Button"""

    is_filtering_out_power_loss: bool
    r"""If true, only receive alerts when the panic button is pressed, otherwise receive alerts when the panic button is pressed or looses connection."""


class PanicButtonDetailsObjectResponseBody(BaseModel):
    r"""Details specific to Panic Button"""

    is_filtering_out_power_loss: Annotated[
        bool, pydantic.Field(alias="isFilteringOutPowerLoss")
    ]
    r"""If true, only receive alerts when the panic button is pressed, otherwise receive alerts when the panic button is pressed or looses connection."""
