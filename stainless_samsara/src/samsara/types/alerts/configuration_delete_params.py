# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConfigurationDeleteParams"]


class ConfigurationDeleteParams(TypedDict, total=False):
    id: Required[str]
    """The unqiue Samsara id of the alert configuration."""
