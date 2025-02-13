# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PdfExportCreateParams"]


class PdfExportCreateParams(TypedDict, total=False):
    id: Required[str]
    """ID of the form submission to create a PDF export from."""
