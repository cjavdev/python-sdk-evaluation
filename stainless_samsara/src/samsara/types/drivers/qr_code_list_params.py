# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["QrCodeListParams"]


class QrCodeListParams(TypedDict, total=False):
    driver_ids: Required[Annotated[List[str], PropertyInfo(alias="driverIds")]]
    """String of comma separated driver IDs.

    List of driver - QR codes for specified driver(s) will be returned.
    """
