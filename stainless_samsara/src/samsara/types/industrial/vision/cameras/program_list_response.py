# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ProgramListResponse", "ProgramListResponseItem"]


class ProgramListResponseItem(BaseModel):
    program_id: Optional[int] = FieldInfo(alias="programId", default=None)

    program_name: Optional[str] = FieldInfo(alias="programName", default=None)


ProgramListResponse: TypeAlias = List[ProgramListResponseItem]
