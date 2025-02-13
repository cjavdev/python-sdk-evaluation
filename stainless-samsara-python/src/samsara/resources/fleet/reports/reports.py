# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .ifta_vehicle import (
    IftaVehicleResource,
    AsyncIftaVehicleResource,
    IftaVehicleResourceWithRawResponse,
    AsyncIftaVehicleResourceWithRawResponse,
    IftaVehicleResourceWithStreamingResponse,
    AsyncIftaVehicleResourceWithStreamingResponse,
)
from .vehicle_idling import (
    VehicleIdlingResource,
    AsyncVehicleIdlingResource,
    VehicleIdlingResourceWithRawResponse,
    AsyncVehicleIdlingResourceWithRawResponse,
    VehicleIdlingResourceWithStreamingResponse,
    AsyncVehicleIdlingResourceWithStreamingResponse,
)
from .ifta_jurisdiction import (
    IftaJurisdictionResource,
    AsyncIftaJurisdictionResource,
    IftaJurisdictionResourceWithRawResponse,
    AsyncIftaJurisdictionResourceWithRawResponse,
    IftaJurisdictionResourceWithStreamingResponse,
    AsyncIftaJurisdictionResourceWithStreamingResponse,
)
from .drivers_fuel_energy import (
    DriversFuelEnergyResource,
    AsyncDriversFuelEnergyResource,
    DriversFuelEnergyResourceWithRawResponse,
    AsyncDriversFuelEnergyResourceWithRawResponse,
    DriversFuelEnergyResourceWithStreamingResponse,
    AsyncDriversFuelEnergyResourceWithStreamingResponse,
)
from .vehicles_fuel_energy import (
    VehiclesFuelEnergyResource,
    AsyncVehiclesFuelEnergyResource,
    VehiclesFuelEnergyResourceWithRawResponse,
    AsyncVehiclesFuelEnergyResourceWithRawResponse,
    VehiclesFuelEnergyResourceWithStreamingResponse,
    AsyncVehiclesFuelEnergyResourceWithStreamingResponse,
)

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):
    @cached_property
    def drivers_fuel_energy(self) -> DriversFuelEnergyResource:
        return DriversFuelEnergyResource(self._client)

    @cached_property
    def ifta_jurisdiction(self) -> IftaJurisdictionResource:
        return IftaJurisdictionResource(self._client)

    @cached_property
    def ifta_vehicle(self) -> IftaVehicleResource:
        return IftaVehicleResource(self._client)

    @cached_property
    def vehicle_idling(self) -> VehicleIdlingResource:
        return VehicleIdlingResource(self._client)

    @cached_property
    def vehicles_fuel_energy(self) -> VehiclesFuelEnergyResource:
        return VehiclesFuelEnergyResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return ReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return ReportsResourceWithStreamingResponse(self)


class AsyncReportsResource(AsyncAPIResource):
    @cached_property
    def drivers_fuel_energy(self) -> AsyncDriversFuelEnergyResource:
        return AsyncDriversFuelEnergyResource(self._client)

    @cached_property
    def ifta_jurisdiction(self) -> AsyncIftaJurisdictionResource:
        return AsyncIftaJurisdictionResource(self._client)

    @cached_property
    def ifta_vehicle(self) -> AsyncIftaVehicleResource:
        return AsyncIftaVehicleResource(self._client)

    @cached_property
    def vehicle_idling(self) -> AsyncVehicleIdlingResource:
        return AsyncVehicleIdlingResource(self._client)

    @cached_property
    def vehicles_fuel_energy(self) -> AsyncVehiclesFuelEnergyResource:
        return AsyncVehiclesFuelEnergyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncReportsResourceWithStreamingResponse(self)


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

    @cached_property
    def drivers_fuel_energy(self) -> DriversFuelEnergyResourceWithRawResponse:
        return DriversFuelEnergyResourceWithRawResponse(self._reports.drivers_fuel_energy)

    @cached_property
    def ifta_jurisdiction(self) -> IftaJurisdictionResourceWithRawResponse:
        return IftaJurisdictionResourceWithRawResponse(self._reports.ifta_jurisdiction)

    @cached_property
    def ifta_vehicle(self) -> IftaVehicleResourceWithRawResponse:
        return IftaVehicleResourceWithRawResponse(self._reports.ifta_vehicle)

    @cached_property
    def vehicle_idling(self) -> VehicleIdlingResourceWithRawResponse:
        return VehicleIdlingResourceWithRawResponse(self._reports.vehicle_idling)

    @cached_property
    def vehicles_fuel_energy(self) -> VehiclesFuelEnergyResourceWithRawResponse:
        return VehiclesFuelEnergyResourceWithRawResponse(self._reports.vehicles_fuel_energy)


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

    @cached_property
    def drivers_fuel_energy(self) -> AsyncDriversFuelEnergyResourceWithRawResponse:
        return AsyncDriversFuelEnergyResourceWithRawResponse(self._reports.drivers_fuel_energy)

    @cached_property
    def ifta_jurisdiction(self) -> AsyncIftaJurisdictionResourceWithRawResponse:
        return AsyncIftaJurisdictionResourceWithRawResponse(self._reports.ifta_jurisdiction)

    @cached_property
    def ifta_vehicle(self) -> AsyncIftaVehicleResourceWithRawResponse:
        return AsyncIftaVehicleResourceWithRawResponse(self._reports.ifta_vehicle)

    @cached_property
    def vehicle_idling(self) -> AsyncVehicleIdlingResourceWithRawResponse:
        return AsyncVehicleIdlingResourceWithRawResponse(self._reports.vehicle_idling)

    @cached_property
    def vehicles_fuel_energy(self) -> AsyncVehiclesFuelEnergyResourceWithRawResponse:
        return AsyncVehiclesFuelEnergyResourceWithRawResponse(self._reports.vehicles_fuel_energy)


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

    @cached_property
    def drivers_fuel_energy(self) -> DriversFuelEnergyResourceWithStreamingResponse:
        return DriversFuelEnergyResourceWithStreamingResponse(self._reports.drivers_fuel_energy)

    @cached_property
    def ifta_jurisdiction(self) -> IftaJurisdictionResourceWithStreamingResponse:
        return IftaJurisdictionResourceWithStreamingResponse(self._reports.ifta_jurisdiction)

    @cached_property
    def ifta_vehicle(self) -> IftaVehicleResourceWithStreamingResponse:
        return IftaVehicleResourceWithStreamingResponse(self._reports.ifta_vehicle)

    @cached_property
    def vehicle_idling(self) -> VehicleIdlingResourceWithStreamingResponse:
        return VehicleIdlingResourceWithStreamingResponse(self._reports.vehicle_idling)

    @cached_property
    def vehicles_fuel_energy(self) -> VehiclesFuelEnergyResourceWithStreamingResponse:
        return VehiclesFuelEnergyResourceWithStreamingResponse(self._reports.vehicles_fuel_energy)


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

    @cached_property
    def drivers_fuel_energy(self) -> AsyncDriversFuelEnergyResourceWithStreamingResponse:
        return AsyncDriversFuelEnergyResourceWithStreamingResponse(self._reports.drivers_fuel_energy)

    @cached_property
    def ifta_jurisdiction(self) -> AsyncIftaJurisdictionResourceWithStreamingResponse:
        return AsyncIftaJurisdictionResourceWithStreamingResponse(self._reports.ifta_jurisdiction)

    @cached_property
    def ifta_vehicle(self) -> AsyncIftaVehicleResourceWithStreamingResponse:
        return AsyncIftaVehicleResourceWithStreamingResponse(self._reports.ifta_vehicle)

    @cached_property
    def vehicle_idling(self) -> AsyncVehicleIdlingResourceWithStreamingResponse:
        return AsyncVehicleIdlingResourceWithStreamingResponse(self._reports.vehicle_idling)

    @cached_property
    def vehicles_fuel_energy(self) -> AsyncVehiclesFuelEnergyResourceWithStreamingResponse:
        return AsyncVehiclesFuelEnergyResourceWithStreamingResponse(self._reports.vehicles_fuel_energy)
