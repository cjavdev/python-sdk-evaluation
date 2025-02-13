# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ImmobilizerUpdateParams", "RelayState"]


class ImmobilizerUpdateParams(TypedDict, total=False):
    relay_states: Required[Annotated[Iterable[RelayState], PropertyInfo(alias="relayStates")]]
    """A list of relay states.

    If a relay is omitted, its state won't be updated. If the list is empty, a 400
    bad request status code will be returned. If there are multiple states for the
    same relay, a 400 bad request status code will be returned.
    """


class RelayState(TypedDict, total=False):
    id: Required[Literal["relay1", "relay2"]]
    """The ID of the relay Valid values: `relay1`, `relay2`"""

    is_open: Required[Annotated[bool, PropertyInfo(alias="isOpen")]]
    """The desired state of the relay.

    Provide `true` to open the relay, or `false` to close the relay.
    """
