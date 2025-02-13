# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .drivers import (
    DriversResource,
    AsyncDriversResource,
    DriversResourceWithRawResponse,
    AsyncDriversResourceWithRawResponse,
    DriversResourceWithStreamingResponse,
    AsyncDriversResourceWithStreamingResponse,
)
from .hos.hos import (
    HosResource,
    AsyncHosResource,
    HosResourceWithRawResponse,
    AsyncHosResourceWithRawResponse,
    HosResourceWithStreamingResponse,
    AsyncHosResourceWithStreamingResponse,
)
from .equipment import (
    EquipmentResource,
    AsyncEquipmentResource,
    EquipmentResourceWithRawResponse,
    AsyncEquipmentResourceWithRawResponse,
    EquipmentResourceWithStreamingResponse,
    AsyncEquipmentResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
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

__all__ = ["FleetResource", "AsyncFleetResource"]


class FleetResource(SyncAPIResource):
    @cached_property
    def drivers(self) -> DriversResource:
        return DriversResource(self._client)

    @cached_property
    def equipment(self) -> EquipmentResource:
        return EquipmentResource(self._client)

    @cached_property
    def hos(self) -> HosResource:
        return HosResource(self._client)

    @cached_property
    def trailers(self) -> TrailersResource:
        return TrailersResource(self._client)

    @cached_property
    def vehicles(self) -> VehiclesResource:
        return VehiclesResource(self._client)

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
    def drivers(self) -> AsyncDriversResource:
        return AsyncDriversResource(self._client)

    @cached_property
    def equipment(self) -> AsyncEquipmentResource:
        return AsyncEquipmentResource(self._client)

    @cached_property
    def hos(self) -> AsyncHosResource:
        return AsyncHosResource(self._client)

    @cached_property
    def trailers(self) -> AsyncTrailersResource:
        return AsyncTrailersResource(self._client)

    @cached_property
    def vehicles(self) -> AsyncVehiclesResource:
        return AsyncVehiclesResource(self._client)

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
    def drivers(self) -> DriversResourceWithRawResponse:
        return DriversResourceWithRawResponse(self._fleet.drivers)

    @cached_property
    def equipment(self) -> EquipmentResourceWithRawResponse:
        return EquipmentResourceWithRawResponse(self._fleet.equipment)

    @cached_property
    def hos(self) -> HosResourceWithRawResponse:
        return HosResourceWithRawResponse(self._fleet.hos)

    @cached_property
    def trailers(self) -> TrailersResourceWithRawResponse:
        return TrailersResourceWithRawResponse(self._fleet.trailers)

    @cached_property
    def vehicles(self) -> VehiclesResourceWithRawResponse:
        return VehiclesResourceWithRawResponse(self._fleet.vehicles)


class AsyncFleetResourceWithRawResponse:
    def __init__(self, fleet: AsyncFleetResource) -> None:
        self._fleet = fleet

    @cached_property
    def drivers(self) -> AsyncDriversResourceWithRawResponse:
        return AsyncDriversResourceWithRawResponse(self._fleet.drivers)

    @cached_property
    def equipment(self) -> AsyncEquipmentResourceWithRawResponse:
        return AsyncEquipmentResourceWithRawResponse(self._fleet.equipment)

    @cached_property
    def hos(self) -> AsyncHosResourceWithRawResponse:
        return AsyncHosResourceWithRawResponse(self._fleet.hos)

    @cached_property
    def trailers(self) -> AsyncTrailersResourceWithRawResponse:
        return AsyncTrailersResourceWithRawResponse(self._fleet.trailers)

    @cached_property
    def vehicles(self) -> AsyncVehiclesResourceWithRawResponse:
        return AsyncVehiclesResourceWithRawResponse(self._fleet.vehicles)


class FleetResourceWithStreamingResponse:
    def __init__(self, fleet: FleetResource) -> None:
        self._fleet = fleet

    @cached_property
    def drivers(self) -> DriversResourceWithStreamingResponse:
        return DriversResourceWithStreamingResponse(self._fleet.drivers)

    @cached_property
    def equipment(self) -> EquipmentResourceWithStreamingResponse:
        return EquipmentResourceWithStreamingResponse(self._fleet.equipment)

    @cached_property
    def hos(self) -> HosResourceWithStreamingResponse:
        return HosResourceWithStreamingResponse(self._fleet.hos)

    @cached_property
    def trailers(self) -> TrailersResourceWithStreamingResponse:
        return TrailersResourceWithStreamingResponse(self._fleet.trailers)

    @cached_property
    def vehicles(self) -> VehiclesResourceWithStreamingResponse:
        return VehiclesResourceWithStreamingResponse(self._fleet.vehicles)


class AsyncFleetResourceWithStreamingResponse:
    def __init__(self, fleet: AsyncFleetResource) -> None:
        self._fleet = fleet

    @cached_property
    def drivers(self) -> AsyncDriversResourceWithStreamingResponse:
        return AsyncDriversResourceWithStreamingResponse(self._fleet.drivers)

    @cached_property
    def equipment(self) -> AsyncEquipmentResourceWithStreamingResponse:
        return AsyncEquipmentResourceWithStreamingResponse(self._fleet.equipment)

    @cached_property
    def hos(self) -> AsyncHosResourceWithStreamingResponse:
        return AsyncHosResourceWithStreamingResponse(self._fleet.hos)

    @cached_property
    def trailers(self) -> AsyncTrailersResourceWithStreamingResponse:
        return AsyncTrailersResourceWithStreamingResponse(self._fleet.trailers)

    @cached_property
    def vehicles(self) -> AsyncVehiclesResourceWithStreamingResponse:
        return AsyncVehiclesResourceWithStreamingResponse(self._fleet.vehicles)
