# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookUpdateParams", "CustomHeader"]


class WebhookUpdateParams(TypedDict, total=False):
    custom_headers: Annotated[Iterable[CustomHeader], PropertyInfo(alias="customHeaders")]
    """The list of custom headers that users can include with their request"""

    name: str
    """The name of the webhook.

    This will appear in both Samsara’s cloud dashboard and the API. It can be set or
    updated through the Samsara Dashboard or through the API at any time.
    """

    url: str
    """The url of the webhook.

    This will appear in both Samsara’s cloud dashboard and the API. It can be set or
    updated through the Samsara Dashboard or through the API at any time.
    """

    version: Literal["2018-01-01", "2021-06-09", "2022-09-13", "2024-02-27"]
    """The version of the webhook.

    Valid values: `2018-01-01`, `2021-06-09`, `2022-09-13`, `2024-02-27`
    """


class CustomHeader(TypedDict, total=False):
    key: Required[str]
    """The alphanumeric key of the custom header."""

    value: Required[str]
    """The value of the custom header.

    The default maximum length of the value is 100 characters.
    """
