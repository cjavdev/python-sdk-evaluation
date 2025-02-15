"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .formsubmissionsgetformsubmissionspdfexportsbadrequesterrorresponsebody import (
    FormSubmissionsGetFormSubmissionsPdfExportsBadRequestErrorResponseBody,
    FormSubmissionsGetFormSubmissionsPdfExportsBadRequestErrorResponseBodyTypedDict,
)
from .formsubmissionsgetformsubmissionspdfexportsresponsebody import (
    FormSubmissionsGetFormSubmissionsPdfExportsResponseBody,
    FormSubmissionsGetFormSubmissionsPdfExportsResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata
from typing import Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class GetFormSubmissionsPdfExportsRequestTypedDict(TypedDict):
    pdf_id: str
    r"""ID of the form submission PDF export."""


class GetFormSubmissionsPdfExportsRequest(BaseModel):
    pdf_id: Annotated[
        str,
        pydantic.Field(alias="pdfId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""ID of the form submission PDF export."""


GetFormSubmissionsPdfExportsResponseTypedDict = TypeAliasType(
    "GetFormSubmissionsPdfExportsResponseTypedDict",
    Union[
        FormSubmissionsGetFormSubmissionsPdfExportsResponseBodyTypedDict,
        FormSubmissionsGetFormSubmissionsPdfExportsBadRequestErrorResponseBodyTypedDict,
    ],
)


GetFormSubmissionsPdfExportsResponse = TypeAliasType(
    "GetFormSubmissionsPdfExportsResponse",
    Union[
        FormSubmissionsGetFormSubmissionsPdfExportsResponseBody,
        FormSubmissionsGetFormSubmissionsPdfExportsBadRequestErrorResponseBody,
    ],
)
