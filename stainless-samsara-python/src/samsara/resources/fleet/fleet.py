# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .dvirs.dvirs import (
    DvirsResource,
    AsyncDvirsResource,
    DvirsResourceWithRawResponse,
    AsyncDvirsResourceWithRawResponse,
    DvirsResourceWithStreamingResponse,
    AsyncDvirsResourceWithStreamingResponse,
)
from .assets.assets import (
    AssetsResource,
    AsyncAssetsResource,
    AssetsResourceWithRawResponse,
    AsyncAssetsResourceWithRawResponse,
    AssetsResourceWithStreamingResponse,
    AsyncAssetsResourceWithStreamingResponse,
)
from .routes.routes import (
    RoutesResource,
    AsyncRoutesResource,
    RoutesResourceWithRawResponse,
    AsyncRoutesResourceWithRawResponse,
    RoutesResourceWithStreamingResponse,
    AsyncRoutesResourceWithStreamingResponse,
)
from .document_types import (
    DocumentTypesResource,
    AsyncDocumentTypesResource,
    DocumentTypesResourceWithRawResponse,
    AsyncDocumentTypesResourceWithRawResponse,
    DocumentTypesResourceWithStreamingResponse,
    AsyncDocumentTypesResourceWithStreamingResponse,
)
from .defects.defects import (
    DefectsResource,
    AsyncDefectsResource,
    DefectsResourceWithRawResponse,
    AsyncDefectsResourceWithRawResponse,
    DefectsResourceWithStreamingResponse,
    AsyncDefectsResourceWithStreamingResponse,
)
from .drivers.drivers import (
    DriversResource,
    AsyncDriversResource,
    DriversResourceWithRawResponse,
    AsyncDriversResourceWithRawResponse,
    DriversResourceWithStreamingResponse,
    AsyncDriversResourceWithStreamingResponse,
)
from .reports.reports import (
    ReportsResource,
    AsyncReportsResource,
    ReportsResourceWithRawResponse,
    AsyncReportsResourceWithRawResponse,
    ReportsResourceWithStreamingResponse,
    AsyncReportsResourceWithStreamingResponse,
)
from .dispatch.dispatch import (
    DispatchResource,
    AsyncDispatchResource,
    DispatchResourceWithRawResponse,
    AsyncDispatchResourceWithRawResponse,
    DispatchResourceWithStreamingResponse,
    AsyncDispatchResourceWithStreamingResponse,
)
from .settings.settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from .trailers.trailers import (
    TrailersResource,
    AsyncTrailersResource,
    TrailersResourceWithRawResponse,
    AsyncTrailersResourceWithRawResponse,
    TrailersResourceWithStreamingResponse,
    AsyncTrailersResourceWithStreamingResponse,
)
from .vehicles.vehicles import (
    VehiclesResource,
    AsyncVehiclesResource,
    VehiclesResourceWithRawResponse,
    AsyncVehiclesResourceWithRawResponse,
    VehiclesResourceWithStreamingResponse,
    AsyncVehiclesResourceWithStreamingResponse,
)
from .documents.documents import (
    DocumentsResource,
    AsyncDocumentsResource,
    DocumentsResourceWithRawResponse,
    AsyncDocumentsResourceWithRawResponse,
    DocumentsResourceWithStreamingResponse,
    AsyncDocumentsResourceWithStreamingResponse,
)
from .equipment.equipment import (
    EquipmentResource,
    AsyncEquipmentResource,
    EquipmentResourceWithRawResponse,
    AsyncEquipmentResourceWithRawResponse,
    EquipmentResourceWithStreamingResponse,
    AsyncEquipmentResourceWithStreamingResponse,
)
from .driver_vehicle_assignments import (
    DriverVehicleAssignmentsResource,
    AsyncDriverVehicleAssignmentsResource,
    DriverVehicleAssignmentsResourceWithRawResponse,
    AsyncDriverVehicleAssignmentsResourceWithRawResponse,
    DriverVehicleAssignmentsResourceWithStreamingResponse,
    AsyncDriverVehicleAssignmentsResourceWithStreamingResponse,
)
from .safety_events.safety_events import (
    SafetyEventsResource,
    AsyncSafetyEventsResource,
    SafetyEventsResourceWithRawResponse,
    AsyncSafetyEventsResourceWithRawResponse,
    SafetyEventsResourceWithStreamingResponse,
    AsyncSafetyEventsResourceWithStreamingResponse,
)
from .carrier_proposed_assignments import (
    CarrierProposedAssignmentsResource,
    AsyncCarrierProposedAssignmentsResource,
    CarrierProposedAssignmentsResourceWithRawResponse,
    AsyncCarrierProposedAssignmentsResourceWithRawResponse,
    CarrierProposedAssignmentsResourceWithStreamingResponse,
    AsyncCarrierProposedAssignmentsResourceWithStreamingResponse,
)

__all__ = ["FleetResource", "AsyncFleetResource"]


class FleetResource(SyncAPIResource):
    @cached_property
    def carrier_proposed_assignments(self) -> CarrierProposedAssignmentsResource:
        return CarrierProposedAssignmentsResource(self._client)

    @cached_property
    def defects(self) -> DefectsResource:
        return DefectsResource(self._client)

    @cached_property
    def document_types(self) -> DocumentTypesResource:
        return DocumentTypesResource(self._client)

    @cached_property
    def documents(self) -> DocumentsResource:
        return DocumentsResource(self._client)

    @cached_property
    def driver_vehicle_assignments(self) -> DriverVehicleAssignmentsResource:
        return DriverVehicleAssignmentsResource(self._client)

    @cached_property
    def drivers(self) -> DriversResource:
        return DriversResource(self._client)

    @cached_property
    def dvirs(self) -> DvirsResource:
        return DvirsResource(self._client)

    @cached_property
    def equipment(self) -> EquipmentResource:
        return EquipmentResource(self._client)

    @cached_property
    def reports(self) -> ReportsResource:
        return ReportsResource(self._client)

    @cached_property
    def routes(self) -> RoutesResource:
        return RoutesResource(self._client)

    @cached_property
    def safety_events(self) -> SafetyEventsResource:
        return SafetyEventsResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def trailers(self) -> TrailersResource:
        return TrailersResource(self._client)

    @cached_property
    def vehicles(self) -> VehiclesResource:
        return VehiclesResource(self._client)

    @cached_property
    def assets(self) -> AssetsResource:
        return AssetsResource(self._client)

    @cached_property
    def dispatch(self) -> DispatchResource:
        return DispatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> FleetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return FleetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FleetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return FleetResourceWithStreamingResponse(self)


class AsyncFleetResource(AsyncAPIResource):
    @cached_property
    def carrier_proposed_assignments(self) -> AsyncCarrierProposedAssignmentsResource:
        return AsyncCarrierProposedAssignmentsResource(self._client)

    @cached_property
    def defects(self) -> AsyncDefectsResource:
        return AsyncDefectsResource(self._client)

    @cached_property
    def document_types(self) -> AsyncDocumentTypesResource:
        return AsyncDocumentTypesResource(self._client)

    @cached_property
    def documents(self) -> AsyncDocumentsResource:
        return AsyncDocumentsResource(self._client)

    @cached_property
    def driver_vehicle_assignments(self) -> AsyncDriverVehicleAssignmentsResource:
        return AsyncDriverVehicleAssignmentsResource(self._client)

    @cached_property
    def drivers(self) -> AsyncDriversResource:
        return AsyncDriversResource(self._client)

    @cached_property
    def dvirs(self) -> AsyncDvirsResource:
        return AsyncDvirsResource(self._client)

    @cached_property
    def equipment(self) -> AsyncEquipmentResource:
        return AsyncEquipmentResource(self._client)

    @cached_property
    def reports(self) -> AsyncReportsResource:
        return AsyncReportsResource(self._client)

    @cached_property
    def routes(self) -> AsyncRoutesResource:
        return AsyncRoutesResource(self._client)

    @cached_property
    def safety_events(self) -> AsyncSafetyEventsResource:
        return AsyncSafetyEventsResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def trailers(self) -> AsyncTrailersResource:
        return AsyncTrailersResource(self._client)

    @cached_property
    def vehicles(self) -> AsyncVehiclesResource:
        return AsyncVehiclesResource(self._client)

    @cached_property
    def assets(self) -> AsyncAssetsResource:
        return AsyncAssetsResource(self._client)

    @cached_property
    def dispatch(self) -> AsyncDispatchResource:
        return AsyncDispatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFleetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFleetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFleetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncFleetResourceWithStreamingResponse(self)


class FleetResourceWithRawResponse:
    def __init__(self, fleet: FleetResource) -> None:
        self._fleet = fleet

    @cached_property
    def carrier_proposed_assignments(self) -> CarrierProposedAssignmentsResourceWithRawResponse:
        return CarrierProposedAssignmentsResourceWithRawResponse(self._fleet.carrier_proposed_assignments)

    @cached_property
    def defects(self) -> DefectsResourceWithRawResponse:
        return DefectsResourceWithRawResponse(self._fleet.defects)

    @cached_property
    def document_types(self) -> DocumentTypesResourceWithRawResponse:
        return DocumentTypesResourceWithRawResponse(self._fleet.document_types)

    @cached_property
    def documents(self) -> DocumentsResourceWithRawResponse:
        return DocumentsResourceWithRawResponse(self._fleet.documents)

    @cached_property
    def driver_vehicle_assignments(self) -> DriverVehicleAssignmentsResourceWithRawResponse:
        return DriverVehicleAssignmentsResourceWithRawResponse(self._fleet.driver_vehicle_assignments)

    @cached_property
    def drivers(self) -> DriversResourceWithRawResponse:
        return DriversResourceWithRawResponse(self._fleet.drivers)

    @cached_property
    def dvirs(self) -> DvirsResourceWithRawResponse:
        return DvirsResourceWithRawResponse(self._fleet.dvirs)

    @cached_property
    def equipment(self) -> EquipmentResourceWithRawResponse:
        return EquipmentResourceWithRawResponse(self._fleet.equipment)

    @cached_property
    def reports(self) -> ReportsResourceWithRawResponse:
        return ReportsResourceWithRawResponse(self._fleet.reports)

    @cached_property
    def routes(self) -> RoutesResourceWithRawResponse:
        return RoutesResourceWithRawResponse(self._fleet.routes)

    @cached_property
    def safety_events(self) -> SafetyEventsResourceWithRawResponse:
        return SafetyEventsResourceWithRawResponse(self._fleet.safety_events)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._fleet.settings)

    @cached_property
    def trailers(self) -> TrailersResourceWithRawResponse:
        return TrailersResourceWithRawResponse(self._fleet.trailers)

    @cached_property
    def vehicles(self) -> VehiclesResourceWithRawResponse:
        return VehiclesResourceWithRawResponse(self._fleet.vehicles)

    @cached_property
    def assets(self) -> AssetsResourceWithRawResponse:
        return AssetsResourceWithRawResponse(self._fleet.assets)

    @cached_property
    def dispatch(self) -> DispatchResourceWithRawResponse:
        return DispatchResourceWithRawResponse(self._fleet.dispatch)


class AsyncFleetResourceWithRawResponse:
    def __init__(self, fleet: AsyncFleetResource) -> None:
        self._fleet = fleet

    @cached_property
    def carrier_proposed_assignments(self) -> AsyncCarrierProposedAssignmentsResourceWithRawResponse:
        return AsyncCarrierProposedAssignmentsResourceWithRawResponse(self._fleet.carrier_proposed_assignments)

    @cached_property
    def defects(self) -> AsyncDefectsResourceWithRawResponse:
        return AsyncDefectsResourceWithRawResponse(self._fleet.defects)

    @cached_property
    def document_types(self) -> AsyncDocumentTypesResourceWithRawResponse:
        return AsyncDocumentTypesResourceWithRawResponse(self._fleet.document_types)

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithRawResponse:
        return AsyncDocumentsResourceWithRawResponse(self._fleet.documents)

    @cached_property
    def driver_vehicle_assignments(self) -> AsyncDriverVehicleAssignmentsResourceWithRawResponse:
        return AsyncDriverVehicleAssignmentsResourceWithRawResponse(self._fleet.driver_vehicle_assignments)

    @cached_property
    def drivers(self) -> AsyncDriversResourceWithRawResponse:
        return AsyncDriversResourceWithRawResponse(self._fleet.drivers)

    @cached_property
    def dvirs(self) -> AsyncDvirsResourceWithRawResponse:
        return AsyncDvirsResourceWithRawResponse(self._fleet.dvirs)

    @cached_property
    def equipment(self) -> AsyncEquipmentResourceWithRawResponse:
        return AsyncEquipmentResourceWithRawResponse(self._fleet.equipment)

    @cached_property
    def reports(self) -> AsyncReportsResourceWithRawResponse:
        return AsyncReportsResourceWithRawResponse(self._fleet.reports)

    @cached_property
    def routes(self) -> AsyncRoutesResourceWithRawResponse:
        return AsyncRoutesResourceWithRawResponse(self._fleet.routes)

    @cached_property
    def safety_events(self) -> AsyncSafetyEventsResourceWithRawResponse:
        return AsyncSafetyEventsResourceWithRawResponse(self._fleet.safety_events)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._fleet.settings)

    @cached_property
    def trailers(self) -> AsyncTrailersResourceWithRawResponse:
        return AsyncTrailersResourceWithRawResponse(self._fleet.trailers)

    @cached_property
    def vehicles(self) -> AsyncVehiclesResourceWithRawResponse:
        return AsyncVehiclesResourceWithRawResponse(self._fleet.vehicles)

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithRawResponse:
        return AsyncAssetsResourceWithRawResponse(self._fleet.assets)

    @cached_property
    def dispatch(self) -> AsyncDispatchResourceWithRawResponse:
        return AsyncDispatchResourceWithRawResponse(self._fleet.dispatch)


class FleetResourceWithStreamingResponse:
    def __init__(self, fleet: FleetResource) -> None:
        self._fleet = fleet

    @cached_property
    def carrier_proposed_assignments(self) -> CarrierProposedAssignmentsResourceWithStreamingResponse:
        return CarrierProposedAssignmentsResourceWithStreamingResponse(self._fleet.carrier_proposed_assignments)

    @cached_property
    def defects(self) -> DefectsResourceWithStreamingResponse:
        return DefectsResourceWithStreamingResponse(self._fleet.defects)

    @cached_property
    def document_types(self) -> DocumentTypesResourceWithStreamingResponse:
        return DocumentTypesResourceWithStreamingResponse(self._fleet.document_types)

    @cached_property
    def documents(self) -> DocumentsResourceWithStreamingResponse:
        return DocumentsResourceWithStreamingResponse(self._fleet.documents)

    @cached_property
    def driver_vehicle_assignments(self) -> DriverVehicleAssignmentsResourceWithStreamingResponse:
        return DriverVehicleAssignmentsResourceWithStreamingResponse(self._fleet.driver_vehicle_assignments)

    @cached_property
    def drivers(self) -> DriversResourceWithStreamingResponse:
        return DriversResourceWithStreamingResponse(self._fleet.drivers)

    @cached_property
    def dvirs(self) -> DvirsResourceWithStreamingResponse:
        return DvirsResourceWithStreamingResponse(self._fleet.dvirs)

    @cached_property
    def equipment(self) -> EquipmentResourceWithStreamingResponse:
        return EquipmentResourceWithStreamingResponse(self._fleet.equipment)

    @cached_property
    def reports(self) -> ReportsResourceWithStreamingResponse:
        return ReportsResourceWithStreamingResponse(self._fleet.reports)

    @cached_property
    def routes(self) -> RoutesResourceWithStreamingResponse:
        return RoutesResourceWithStreamingResponse(self._fleet.routes)

    @cached_property
    def safety_events(self) -> SafetyEventsResourceWithStreamingResponse:
        return SafetyEventsResourceWithStreamingResponse(self._fleet.safety_events)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._fleet.settings)

    @cached_property
    def trailers(self) -> TrailersResourceWithStreamingResponse:
        return TrailersResourceWithStreamingResponse(self._fleet.trailers)

    @cached_property
    def vehicles(self) -> VehiclesResourceWithStreamingResponse:
        return VehiclesResourceWithStreamingResponse(self._fleet.vehicles)

    @cached_property
    def assets(self) -> AssetsResourceWithStreamingResponse:
        return AssetsResourceWithStreamingResponse(self._fleet.assets)

    @cached_property
    def dispatch(self) -> DispatchResourceWithStreamingResponse:
        return DispatchResourceWithStreamingResponse(self._fleet.dispatch)


class AsyncFleetResourceWithStreamingResponse:
    def __init__(self, fleet: AsyncFleetResource) -> None:
        self._fleet = fleet

    @cached_property
    def carrier_proposed_assignments(self) -> AsyncCarrierProposedAssignmentsResourceWithStreamingResponse:
        return AsyncCarrierProposedAssignmentsResourceWithStreamingResponse(self._fleet.carrier_proposed_assignments)

    @cached_property
    def defects(self) -> AsyncDefectsResourceWithStreamingResponse:
        return AsyncDefectsResourceWithStreamingResponse(self._fleet.defects)

    @cached_property
    def document_types(self) -> AsyncDocumentTypesResourceWithStreamingResponse:
        return AsyncDocumentTypesResourceWithStreamingResponse(self._fleet.document_types)

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithStreamingResponse:
        return AsyncDocumentsResourceWithStreamingResponse(self._fleet.documents)

    @cached_property
    def driver_vehicle_assignments(self) -> AsyncDriverVehicleAssignmentsResourceWithStreamingResponse:
        return AsyncDriverVehicleAssignmentsResourceWithStreamingResponse(self._fleet.driver_vehicle_assignments)

    @cached_property
    def drivers(self) -> AsyncDriversResourceWithStreamingResponse:
        return AsyncDriversResourceWithStreamingResponse(self._fleet.drivers)

    @cached_property
    def dvirs(self) -> AsyncDvirsResourceWithStreamingResponse:
        return AsyncDvirsResourceWithStreamingResponse(self._fleet.dvirs)

    @cached_property
    def equipment(self) -> AsyncEquipmentResourceWithStreamingResponse:
        return AsyncEquipmentResourceWithStreamingResponse(self._fleet.equipment)

    @cached_property
    def reports(self) -> AsyncReportsResourceWithStreamingResponse:
        return AsyncReportsResourceWithStreamingResponse(self._fleet.reports)

    @cached_property
    def routes(self) -> AsyncRoutesResourceWithStreamingResponse:
        return AsyncRoutesResourceWithStreamingResponse(self._fleet.routes)

    @cached_property
    def safety_events(self) -> AsyncSafetyEventsResourceWithStreamingResponse:
        return AsyncSafetyEventsResourceWithStreamingResponse(self._fleet.safety_events)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._fleet.settings)

    @cached_property
    def trailers(self) -> AsyncTrailersResourceWithStreamingResponse:
        return AsyncTrailersResourceWithStreamingResponse(self._fleet.trailers)

    @cached_property
    def vehicles(self) -> AsyncVehiclesResourceWithStreamingResponse:
        return AsyncVehiclesResourceWithStreamingResponse(self._fleet.vehicles)

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithStreamingResponse:
        return AsyncAssetsResourceWithStreamingResponse(self._fleet.assets)

    @cached_property
    def dispatch(self) -> AsyncDispatchResourceWithStreamingResponse:
        return AsyncDispatchResourceWithStreamingResponse(self._fleet.dispatch)
