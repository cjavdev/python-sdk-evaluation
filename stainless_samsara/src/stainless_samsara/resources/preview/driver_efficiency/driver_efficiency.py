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
from .vehicles import (
    VehiclesResource,
    AsyncVehiclesResource,
    VehiclesResourceWithRawResponse,
    AsyncVehiclesResourceWithRawResponse,
    VehiclesResourceWithStreamingResponse,
    AsyncVehiclesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DriverEfficiencyResource", "AsyncDriverEfficiencyResource"]


class DriverEfficiencyResource(SyncAPIResource):
    @cached_property
    def drivers(self) -> DriversResource:
        return DriversResource(self._client)

    @cached_property
    def vehicles(self) -> VehiclesResource:
        return VehiclesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DriverEfficiencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DriverEfficiencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DriverEfficiencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DriverEfficiencyResourceWithStreamingResponse(self)


class AsyncDriverEfficiencyResource(AsyncAPIResource):
    @cached_property
    def drivers(self) -> AsyncDriversResource:
        return AsyncDriversResource(self._client)

    @cached_property
    def vehicles(self) -> AsyncVehiclesResource:
        return AsyncVehiclesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDriverEfficiencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDriverEfficiencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDriverEfficiencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDriverEfficiencyResourceWithStreamingResponse(self)


class DriverEfficiencyResourceWithRawResponse:
    def __init__(self, driver_efficiency: DriverEfficiencyResource) -> None:
        self._driver_efficiency = driver_efficiency

    @cached_property
    def drivers(self) -> DriversResourceWithRawResponse:
        return DriversResourceWithRawResponse(self._driver_efficiency.drivers)

    @cached_property
    def vehicles(self) -> VehiclesResourceWithRawResponse:
        return VehiclesResourceWithRawResponse(self._driver_efficiency.vehicles)


class AsyncDriverEfficiencyResourceWithRawResponse:
    def __init__(self, driver_efficiency: AsyncDriverEfficiencyResource) -> None:
        self._driver_efficiency = driver_efficiency

    @cached_property
    def drivers(self) -> AsyncDriversResourceWithRawResponse:
        return AsyncDriversResourceWithRawResponse(self._driver_efficiency.drivers)

    @cached_property
    def vehicles(self) -> AsyncVehiclesResourceWithRawResponse:
        return AsyncVehiclesResourceWithRawResponse(self._driver_efficiency.vehicles)


class DriverEfficiencyResourceWithStreamingResponse:
    def __init__(self, driver_efficiency: DriverEfficiencyResource) -> None:
        self._driver_efficiency = driver_efficiency

    @cached_property
    def drivers(self) -> DriversResourceWithStreamingResponse:
        return DriversResourceWithStreamingResponse(self._driver_efficiency.drivers)

    @cached_property
    def vehicles(self) -> VehiclesResourceWithStreamingResponse:
        return VehiclesResourceWithStreamingResponse(self._driver_efficiency.vehicles)


class AsyncDriverEfficiencyResourceWithStreamingResponse:
    def __init__(self, driver_efficiency: AsyncDriverEfficiencyResource) -> None:
        self._driver_efficiency = driver_efficiency

    @cached_property
    def drivers(self) -> AsyncDriversResourceWithStreamingResponse:
        return AsyncDriversResourceWithStreamingResponse(self._driver_efficiency.drivers)

    @cached_property
    def vehicles(self) -> AsyncVehiclesResourceWithStreamingResponse:
        return AsyncVehiclesResourceWithStreamingResponse(self._driver_efficiency.vehicles)
