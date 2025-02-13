# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["V1HosAuthenticationLogsResponse", "AuthenticationLog"]


class AuthenticationLog(BaseModel):
    action_type: Optional[str] = FieldInfo(alias="actionType", default=None)
    """The log type - one of 'signin' or 'signout'"""

    address: Optional[str] = None
    """DEPRECATED: THIS FIELD MAY NOT BE POPULATED"""

    address_name: Optional[str] = FieldInfo(alias="addressName", default=None)
    """DEPRECATED: THIS FIELD MAY NOT BE POPULATED"""

    city: Optional[str] = None
    """DEPRECATED: THIS FIELD MAY NOT BE POPULATED"""

    happened_at_ms: Optional[int] = FieldInfo(alias="happenedAtMs", default=None)
    """The time at which the event was recorded in UNIX milliseconds."""

    state: Optional[str] = None
    """DEPRECATED: THIS FIELD MAY NOT BE POPULATED"""


class V1HosAuthenticationLogsResponse(BaseModel):
    authentication_logs: Optional[List[AuthenticationLog]] = FieldInfo(alias="authenticationLogs", default=None)
