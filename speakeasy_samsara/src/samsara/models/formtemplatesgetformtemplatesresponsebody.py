"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .formtemplateresponseobjectresponsebody import (
    FormTemplateResponseObjectResponseBody,
    FormTemplateResponseObjectResponseBodyTypedDict,
)
from .goapaginationresponseresponsebody import (
    GoaPaginationResponseResponseBody,
    GoaPaginationResponseResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class FormTemplatesGetFormTemplatesResponseBodyTypedDict(TypedDict):
    data: List[FormTemplateResponseObjectResponseBodyTypedDict]
    r"""List of form templates."""
    pagination: GoaPaginationResponseResponseBodyTypedDict
    r"""Pagination parameters."""


class FormTemplatesGetFormTemplatesResponseBody(BaseModel):
    data: List[FormTemplateResponseObjectResponseBody]
    r"""List of form templates."""

    pagination: GoaPaginationResponseResponseBody
    r"""Pagination parameters."""
