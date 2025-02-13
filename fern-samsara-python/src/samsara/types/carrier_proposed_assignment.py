# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .carrier_proposed_assignment_accepted_time import CarrierProposedAssignmentAcceptedTime
from ..core.serialization import FieldMetadata
from .carrier_proposed_assignment_active_time import CarrierProposedAssignmentActiveTime
from .carrier_proposed_assignment_driver import CarrierProposedAssignmentDriver
from .carrier_proposed_assignment_first_seen_time import CarrierProposedAssignmentFirstSeenTime
from .carrier_proposed_assignment_id import CarrierProposedAssignmentId
from .carrier_proposed_assignment_rejected_time import CarrierProposedAssignmentRejectedTime
from .carrier_proposed_assignment_shipping_docs import CarrierProposedAssignmentShippingDocs
from .carrier_proposed_assignment_trailers import CarrierProposedAssignmentTrailers
from .carrier_proposed_assignment_vehicle import CarrierProposedAssignmentVehicle
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class CarrierProposedAssignment(UniversalBaseModel):
    """
    A carrier proposed assignment object
    """

    accepted_time: typing_extensions.Annotated[
        typing.Optional[CarrierProposedAssignmentAcceptedTime], FieldMetadata(alias="acceptedTime")
    ] = None
    active_time: typing_extensions.Annotated[CarrierProposedAssignmentActiveTime, FieldMetadata(alias="activeTime")]
    driver: typing.Optional[CarrierProposedAssignmentDriver] = None
    first_seen_time: typing_extensions.Annotated[
        typing.Optional[CarrierProposedAssignmentFirstSeenTime], FieldMetadata(alias="firstSeenTime")
    ] = None
    id: CarrierProposedAssignmentId
    rejected_time: typing_extensions.Annotated[
        typing.Optional[CarrierProposedAssignmentRejectedTime], FieldMetadata(alias="rejectedTime")
    ] = None
    shipping_docs: typing_extensions.Annotated[
        typing.Optional[CarrierProposedAssignmentShippingDocs], FieldMetadata(alias="shippingDocs")
    ] = None
    trailers: typing.Optional[CarrierProposedAssignmentTrailers] = None
    vehicle: typing.Optional[CarrierProposedAssignmentVehicle] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
