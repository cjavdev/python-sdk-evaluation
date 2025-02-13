# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["PdfCreateResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """ID of the PDF file generated or being generated for the document."""

    document_id: Optional[str] = FieldInfo(alias="documentId", default=None)
    """ID of the document."""


class PdfCreateResponse(BaseModel):
    data: Optional[Data] = None
