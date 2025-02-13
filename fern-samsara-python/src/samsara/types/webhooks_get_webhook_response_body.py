# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .custom_headers_object_response_body import CustomHeadersObjectResponseBody
from ..core.serialization import FieldMetadata
import pydantic
from .webhooks_get_webhook_response_body_event_types_item import WebhooksGetWebhookResponseBodyEventTypesItem
from .webhooks_get_webhook_response_body_version import WebhooksGetWebhookResponseBodyVersion
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class WebhooksGetWebhookResponseBody(UniversalBaseModel):
    custom_headers: typing_extensions.Annotated[
        typing.Optional[typing.List[CustomHeadersObjectResponseBody]], FieldMetadata(alias="customHeaders")
    ] = pydantic.Field(default=None)
    """
    The list of custom headers that users can include with their request
    """

    event_types: typing_extensions.Annotated[
        typing.Optional[typing.List[WebhooksGetWebhookResponseBodyEventTypesItem]], FieldMetadata(alias="eventTypes")
    ] = pydantic.Field(default=None)
    """
    The list of event types associated with a particular webhook.
    """

    id: str = pydantic.Field()
    """
    The ID of the webhook. This will appear in both Samsara’s cloud dashboard and the API. This is the id of the webhook. This is system generated.
    """

    name: str = pydantic.Field()
    """
    The name of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time.
    """

    secret_key: typing_extensions.Annotated[str, FieldMetadata(alias="secretKey")] = pydantic.Field()
    """
    The secret key of the webhook. This will appear in both Samsara’s cloud dashboard and the API.
    """

    url: str = pydantic.Field()
    """
    The url of the webhook. This will appear in both Samsara’s cloud dashboard and the API. It can be set or updated through the Samsara Dashboard or through the API at any time.
    """

    version: WebhooksGetWebhookResponseBodyVersion = pydantic.Field()
    """
    The version of the webhook.  Valid values: `2018-01-01`, `2021-06-09`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
