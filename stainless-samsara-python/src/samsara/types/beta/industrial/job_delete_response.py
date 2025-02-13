# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["JobDeleteResponse"]


class JobDeleteResponse(BaseModel):
    id: Optional[str] = None
    """The job id of the failed request"""

    uuid: Optional[str] = None
    """The uuid of the failed request"""
