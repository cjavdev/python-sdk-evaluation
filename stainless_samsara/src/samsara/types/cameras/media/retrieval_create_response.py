# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["RetrievalCreateResponse", "Data"]


class Data(BaseModel):
    retrieval_id: str = FieldInfo(alias="retrievalId")
    """Retrieval ID associated with this media capture request.

    Examples: 2308cec4-82e0-46f1-8b3c-a3592e5cc21e
    """


class RetrievalCreateResponse(BaseModel):
    data: Data
