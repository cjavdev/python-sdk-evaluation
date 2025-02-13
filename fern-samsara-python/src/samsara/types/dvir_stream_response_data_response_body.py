# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from .author_signature_object_response_body import AuthorSignatureObjectResponseBody
from ..core.serialization import FieldMetadata
import typing
import pydantic
from .dvir_stream_response_data_response_body_safety_status import DvirStreamResponseDataResponseBodySafetyStatus
from .trailer_dvir_object_response_body import TrailerDvirObjectResponseBody
from .dvir_stream_response_data_response_body_type import DvirStreamResponseDataResponseBodyType
from .vehicle_dvir_object_response_body import VehicleDvirObjectResponseBody
from .walkaround_photo_object_response_body import WalkaroundPhotoObjectResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DvirStreamResponseDataResponseBody(UniversalBaseModel):
    author_signature: typing_extensions.Annotated[
        AuthorSignatureObjectResponseBody, FieldMetadata(alias="authorSignature")
    ]
    defect_ids: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="defectIds")] = (
        pydantic.Field(default=None)
    )
    """
    IDs of defects registered for the DVIR.
    """

    dvir_submission_begin_time: typing_extensions.Annotated[str, FieldMetadata(alias="dvirSubmissionBeginTime")] = (
        pydantic.Field()
    )
    """
    Time when driver created DVIR. UTC timestamp in RFC 3339 format.
    """

    dvir_submission_time: typing_extensions.Annotated[str, FieldMetadata(alias="dvirSubmissionTime")] = pydantic.Field()
    """
    Time when driver submitted the DVIR. UTC timestamp in RFC 3339 format.
    """

    formatted_address: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="formattedAddress")] = None
    id: str = pydantic.Field()
    """
    The unique id of the DVIR
    """

    mechanic_notes: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="mechanicNotes")] = (
        pydantic.Field(default=None)
    )
    """
    The mechanics notes on the DVIR.
    """

    odometer_meters: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="odometerMeters")] = (
        pydantic.Field(default=None)
    )
    """
    The odometer reading in meters.
    """

    safety_status: typing_extensions.Annotated[
        typing.Optional[DvirStreamResponseDataResponseBodySafetyStatus], FieldMetadata(alias="safetyStatus")
    ] = pydantic.Field(default=None)
    """
    The condition of vehicle on which DVIR was done.  Valid values: `unknown`, `safe`, `unsafe`, `resolved`
    """

    second_signature: typing_extensions.Annotated[
        typing.Optional[AuthorSignatureObjectResponseBody], FieldMetadata(alias="secondSignature")
    ] = None
    third_signature: typing_extensions.Annotated[
        typing.Optional[AuthorSignatureObjectResponseBody], FieldMetadata(alias="thirdSignature")
    ] = None
    trailer: typing.Optional[TrailerDvirObjectResponseBody] = None
    type: DvirStreamResponseDataResponseBodyType = pydantic.Field()
    """
    Inspection type of the DVIR.  Valid values: `preTrip`, `postTrip`, `mechanic`, `unspecified`
    """

    updated_at_time: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAtTime")] = pydantic.Field()
    """
    Time of any DVIR updates. UTC timestamp in RFC 3339 format.
    """

    vehicle: typing.Optional[VehicleDvirObjectResponseBody] = None
    walkaround_photos: typing_extensions.Annotated[
        typing.Optional[typing.List[WalkaroundPhotoObjectResponseBody]], FieldMetadata(alias="walkaroundPhotos")
    ] = pydantic.Field(default=None)
    """
    List of walkaround photos
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
