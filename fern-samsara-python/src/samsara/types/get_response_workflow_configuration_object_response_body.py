# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .action_object_response_body import ActionObjectResponseBody
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from .operational_settings_object_response_body import OperationalSettingsObjectResponseBody
from .scope_object_response_body import ScopeObjectResponseBody
from .workflow_trigger_object_response_body import WorkflowTriggerObjectResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GetResponseWorkflowConfigurationObjectResponseBody(UniversalBaseModel):
    """
    The configuration of a alert.
    """

    actions: typing.List[ActionObjectResponseBody] = pydantic.Field()
    """
    An array of actions.
    """

    created_at_time: typing_extensions.Annotated[str, FieldMetadata(alias="createdAtTime")] = pydantic.Field()
    """
    The time the configuration was created in RFC 3339 format.
    """

    external_ids: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="externalIds")
    ] = pydantic.Field(default=None)
    """
    A map of external ids
    """

    id: str = pydantic.Field()
    """
    The unqiue Samsara id of the alert configuration.
    """

    is_enabled: typing_extensions.Annotated[bool, FieldMetadata(alias="isEnabled")] = pydantic.Field()
    """
    Whether the alert is enabled or not.
    """

    last_modified_at_time: typing_extensions.Annotated[str, FieldMetadata(alias="lastModifiedAtTime")] = (
        pydantic.Field()
    )
    """
    The time the configuration was last modified in RFC 3339 format.
    """

    name: str = pydantic.Field()
    """
    The custom name of the configuration.
    """

    operational_settings: typing_extensions.Annotated[
        typing.Optional[OperationalSettingsObjectResponseBody], FieldMetadata(alias="operationalSettings")
    ] = None
    scope: ScopeObjectResponseBody
    triggers: typing.List[WorkflowTriggerObjectResponseBody] = pydantic.Field()
    """
    An array of triggers.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
