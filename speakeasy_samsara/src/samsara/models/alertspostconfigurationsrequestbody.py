"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .actionobjectrequestbody import (
    ActionObjectRequestBody,
    ActionObjectRequestBodyTypedDict,
)
from .operationalsettingsobjectrequestbody import (
    OperationalSettingsObjectRequestBody,
    OperationalSettingsObjectRequestBodyTypedDict,
)
from .scopeobjectrequestbody import (
    ScopeObjectRequestBody,
    ScopeObjectRequestBodyTypedDict,
)
from .workflowtriggerobjectrequestbody import (
    WorkflowTriggerObjectRequestBody,
    WorkflowTriggerObjectRequestBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AlertsPostConfigurationsRequestBodyTypedDict(TypedDict):
    r"""The configuration of a alert."""

    actions: List[ActionObjectRequestBodyTypedDict]
    r"""An array of actions."""
    name: str
    r"""The custom name of the configuration."""
    scope: ScopeObjectRequestBodyTypedDict
    r"""What the triggers are scoped to. These are the objects this alert applies to."""
    triggers: List[WorkflowTriggerObjectRequestBodyTypedDict]
    r"""An array of triggers."""
    external_ids: NotRequired[Dict[str, str]]
    r"""A map of external ids"""
    is_enabled: NotRequired[bool]
    r"""Whether the alert is enabled or not."""
    operational_settings: NotRequired[OperationalSettingsObjectRequestBodyTypedDict]
    r"""Settings on when the alert should be operational."""


class AlertsPostConfigurationsRequestBody(BaseModel):
    r"""The configuration of a alert."""

    actions: List[ActionObjectRequestBody]
    r"""An array of actions."""

    name: str
    r"""The custom name of the configuration."""

    scope: ScopeObjectRequestBody
    r"""What the triggers are scoped to. These are the objects this alert applies to."""

    triggers: List[WorkflowTriggerObjectRequestBody]
    r"""An array of triggers."""

    external_ids: Annotated[
        Optional[Dict[str, str]], pydantic.Field(alias="externalIds")
    ] = None
    r"""A map of external ids"""

    is_enabled: Annotated[Optional[bool], pydantic.Field(alias="isEnabled")] = True
    r"""Whether the alert is enabled or not."""

    operational_settings: Annotated[
        Optional[OperationalSettingsObjectRequestBody],
        pydantic.Field(alias="operationalSettings"),
    ] = None
    r"""Settings on when the alert should be operational."""
