"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .patchjobobjectrequestbody import (
    PatchJobObjectRequestBody,
    PatchJobObjectRequestBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class JobsPatchJobRequestBodyTypedDict(TypedDict):
    r"""Job object with fields to update. If a field is not provided, it will not be updated"""

    job: PatchJobObjectRequestBodyTypedDict
    r"""Job object with fields to update. If a field is not provided, it will not be updated"""
    keep_history: NotRequired[bool]
    r"""Defaults to true if user does not want to overwrite entire history for an active job (irrelevant for scheduled/completed jobs)"""


class JobsPatchJobRequestBody(BaseModel):
    r"""Job object with fields to update. If a field is not provided, it will not be updated"""

    job: PatchJobObjectRequestBody
    r"""Job object with fields to update. If a field is not provided, it will not be updated"""

    keep_history: Annotated[Optional[bool], pydantic.Field(alias="keepHistory")] = True
    r"""Defaults to true if user does not want to overwrite entire history for an active job (irrelevant for scheduled/completed jobs)"""
