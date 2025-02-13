# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DailyLogUpdateLogMetadataParams"]


class DailyLogUpdateLogMetadataParams(TypedDict, total=False):
    driver_id: Required[Annotated[str, PropertyInfo(alias="driverID")]]
    """ID of the driver for whom the duty status is being set."""

    hos_date: Required[Annotated[str, PropertyInfo(alias="hosDate")]]
    """A start date in yyyy-mm-dd format. Required."""

    shipping_docs: Required[Annotated[str, PropertyInfo(alias="shippingDocs")]]
    """ShippingDocs associated with the driver for the day."""
