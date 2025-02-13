# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FormSubmissionsGetFormSubmissionsPdfExportsResponseBody", "Data"]


class Data(BaseModel):
    id: str
    """ID of the form submission being exported."""

    expires_at_time: datetime = FieldInfo(alias="expiresAtTime")
    """Time when the PDF export job expires.

    After expiration, GET requests for this job will fail and clients must create a
    new one with another POST request. UTC timestamp in RFC 3339 format.
    """

    job_status: Literal["unknown", "pending", "done", "failed"] = FieldInfo(alias="jobStatus")
    """Status of the PDF export job.

    Valid values: `unknown`, `pending`, `done`, `failed`
    """

    pdf_id: str = FieldInfo(alias="pdfId")
    """Unique ID for the PDF export that is created."""

    requested_at_time: datetime = FieldInfo(alias="requestedAtTime")
    """Time when the PDF export POST request was made.

    UTC timestamp in RFC 3339 format.
    """

    completed_at_time: Optional[datetime] = FieldInfo(alias="completedAtTime", default=None)
    """Time when the PDF export job was completed.

    Included if 'jobStatus' is 'done'. UTC timestamp in RFC 3339 format.
    """

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """An error message for failed PDF export jobs.

    Included if 'jobStatus' is 'failed'.
    """

    pdf_url: Optional[str] = FieldInfo(alias="pdfUrl", default=None)
    """URL to download the PDF file.

    Expires at time specified in 'pdfUrlExpiresAtTime'. Included if 'jobStatus' is
    'done'.
    """

    pdf_url_expires_at_time: Optional[datetime] = FieldInfo(alias="pdfUrlExpiresAtTime", default=None)
    """Time when the PDF export's 'pdfUrl' expires.

    After expiration, clients can retrieve a fresh url with another GET request. UTC
    timestamp in RFC 3339 format.
    """


class FormSubmissionsGetFormSubmissionsPdfExportsResponseBody(BaseModel):
    data: Data
    """Form Submission PDF export response object."""
