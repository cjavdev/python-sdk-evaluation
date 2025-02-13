"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .alertobjectmachineinputresponsebody import (
    AlertObjectMachineInputResponseBody,
    AlertObjectMachineInputResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DataInputValueResponseBodyTypedDict(TypedDict):
    r"""Details specific to Data Input Value."""

    machine_input: NotRequired[AlertObjectMachineInputResponseBodyTypedDict]
    r"""A machine input associated with the alert"""


class DataInputValueResponseBody(BaseModel):
    r"""Details specific to Data Input Value."""

    machine_input: Annotated[
        Optional[AlertObjectMachineInputResponseBody],
        pydantic.Field(alias="machineInput"),
    ] = None
    r"""A machine input associated with the alert"""
