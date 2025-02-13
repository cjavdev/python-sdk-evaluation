"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .formsubmissionpdfexportresponseobjectresponsebody import (
    FormSubmissionPdfExportResponseObjectResponseBody,
    FormSubmissionPdfExportResponseObjectResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing_extensions import TypedDict


class FormSubmissionsPostFormSubmissionsPdfExportsResponseBodyTypedDict(TypedDict):
    data: FormSubmissionPdfExportResponseObjectResponseBodyTypedDict
    r"""Form Submission PDF export response object."""


class FormSubmissionsPostFormSubmissionsPdfExportsResponseBody(BaseModel):
    data: FormSubmissionPdfExportResponseObjectResponseBody
    r"""Form Submission PDF export response object."""
