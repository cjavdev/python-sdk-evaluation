# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class IftaDetailJobOutputResponseBody(UniversalBaseModel):
    """
    The file outputs produced by a successfully completed job.
    """

    created_at_time: typing_extensions.Annotated[str, FieldMetadata(alias="createdAtTime")] = pydantic.Field()
    """
     When this file was created.
    """

    download_url: typing_extensions.Annotated[str, FieldMetadata(alias="downloadUrl")] = pydantic.Field()
    """
    A url to download the generated file. The contents will be gzipped. This url has an expiration and will no longer be valid after expiration.
    """

    download_url_expiration_time: typing_extensions.Annotated[str, FieldMetadata(alias="downloadUrlExpirationTime")] = (
        pydantic.Field()
    )
    """
     The expiration time of this file's download url. Requesting this job again by ID will refresh the download urls, if expired.
    """

    name: str = pydantic.Field()
    """
    The name of this file.
    """

    record_count: typing_extensions.Annotated[int, FieldMetadata(alias="recordCount")] = pydantic.Field()
    """
    The number of records in this file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
