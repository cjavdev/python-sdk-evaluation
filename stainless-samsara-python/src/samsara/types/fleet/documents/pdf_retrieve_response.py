# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["PdfRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """ID of the PDF file generated or being generated for the document"""

    completed_at_time: Optional[str] = FieldInfo(alias="completedAtTime", default=None)
    """Time that PDF generation was completed, in RFC 3339 format."""

    document_id: Optional[str] = FieldInfo(alias="documentId", default=None)
    """ID of the document."""

    download_document_pdf_url: Optional[str] = FieldInfo(alias="downloadDocumentPdfUrl", default=None)
    """S3 pre-signed URL to download PDF file."""

    job_status: Optional[Literal["requested", "processing", "completed"]] = FieldInfo(alias="jobStatus", default=None)
    """Describes status of the PDF generation job.

    Valid values: `requested`, `processing`, `completed`.
    """

    requested_at_time: Optional[str] = FieldInfo(alias="requestedAtTime", default=None)
    """Time that PDF generation was requested, in RFC 3339 format."""


class PdfRetrieveResponse(BaseModel):
    data: Optional[Data] = None
