# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageCreateParams"]


class MessageCreateParams(TypedDict, total=False):
    driver_ids: Required[Annotated[Iterable[float], PropertyInfo(alias="driverIds")]]
    """IDs of the drivers for whom the messages are sent to."""

    text: Required[str]
    """The text sent in the message. Max 2500 characters allowed."""
