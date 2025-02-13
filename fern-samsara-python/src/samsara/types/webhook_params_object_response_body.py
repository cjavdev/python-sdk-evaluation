# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .webhook_params_object_response_body_payload_type import WebhookParamsObjectResponseBodyPayloadType
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class WebhookParamsObjectResponseBody(UniversalBaseModel):
    """
    The webhook configuration for an Action.
    """

    payload_type: typing_extensions.Annotated[
        typing.Optional[WebhookParamsObjectResponseBodyPayloadType], FieldMetadata(alias="payloadType")
    ] = pydantic.Field(default=None)
    """
    This determines the alert webhook payload type to use. Learn more: https://developers.samsara.com/docs/webhook-reference.  Valid values: `legacy`, `enriched`
    """

    webhook_ids: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="webhookIds")] = pydantic.Field()
    """
    The webhook IDs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
