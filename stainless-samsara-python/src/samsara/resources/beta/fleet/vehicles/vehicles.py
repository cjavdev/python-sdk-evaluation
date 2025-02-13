# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from .immobilizer import (
    ImmobilizerResource,
    AsyncImmobilizerResource,
    ImmobilizerResourceWithRawResponse,
    AsyncImmobilizerResourceWithRawResponse,
    ImmobilizerResourceWithStreamingResponse,
    AsyncImmobilizerResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["VehiclesResource", "AsyncVehiclesResource"]


class VehiclesResource(SyncAPIResource):
    @cached_property
    def immobilizer(self) -> ImmobilizerResource:
        return ImmobilizerResource(self._client)

    @cached_property
    def with_raw_response(self) -> VehiclesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return VehiclesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VehiclesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return VehiclesResourceWithStreamingResponse(self)


class AsyncVehiclesResource(AsyncAPIResource):
    @cached_property
    def immobilizer(self) -> AsyncImmobilizerResource:
        return AsyncImmobilizerResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVehiclesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVehiclesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVehiclesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncVehiclesResourceWithStreamingResponse(self)


class VehiclesResourceWithRawResponse:
    def __init__(self, vehicles: VehiclesResource) -> None:
        self._vehicles = vehicles

    @cached_property
    def immobilizer(self) -> ImmobilizerResourceWithRawResponse:
        return ImmobilizerResourceWithRawResponse(self._vehicles.immobilizer)


class AsyncVehiclesResourceWithRawResponse:
    def __init__(self, vehicles: AsyncVehiclesResource) -> None:
        self._vehicles = vehicles

    @cached_property
    def immobilizer(self) -> AsyncImmobilizerResourceWithRawResponse:
        return AsyncImmobilizerResourceWithRawResponse(self._vehicles.immobilizer)


class VehiclesResourceWithStreamingResponse:
    def __init__(self, vehicles: VehiclesResource) -> None:
        self._vehicles = vehicles

    @cached_property
    def immobilizer(self) -> ImmobilizerResourceWithStreamingResponse:
        return ImmobilizerResourceWithStreamingResponse(self._vehicles.immobilizer)


class AsyncVehiclesResourceWithStreamingResponse:
    def __init__(self, vehicles: AsyncVehiclesResource) -> None:
        self._vehicles = vehicles

    @cached_property
    def immobilizer(self) -> AsyncImmobilizerResourceWithStreamingResponse:
        return AsyncImmobilizerResourceWithStreamingResponse(self._vehicles.immobilizer)
