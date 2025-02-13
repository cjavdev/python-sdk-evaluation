# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RetrievalRetrieveParams"]


class RetrievalRetrieveParams(TypedDict, total=False):
    retrieval_id: Required[Annotated[str, PropertyInfo(alias="retrievalId")]]
    """Retrieval ID associated with this media capture request.

    Examples: 2308cec4-82e0-46f1-8b3c-a3592e5cc21e
    """
