# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .fleet import (
    FleetResource,
    AsyncFleetResource,
    FleetResourceWithRawResponse,
    AsyncFleetResourceWithRawResponse,
    FleetResourceWithStreamingResponse,
    AsyncFleetResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AempResource", "AsyncAempResource"]


class AempResource(SyncAPIResource):
    @cached_property
    def fleet(self) -> FleetResource:
        return FleetResource(self._client)

    @cached_property
    def with_raw_response(self) -> AempResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AempResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AempResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AempResourceWithStreamingResponse(self)


class AsyncAempResource(AsyncAPIResource):
    @cached_property
    def fleet(self) -> AsyncFleetResource:
        return AsyncFleetResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAempResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAempResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAempResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncAempResourceWithStreamingResponse(self)


class AempResourceWithRawResponse:
    def __init__(self, aemp: AempResource) -> None:
        self._aemp = aemp

    @cached_property
    def fleet(self) -> FleetResourceWithRawResponse:
        return FleetResourceWithRawResponse(self._aemp.fleet)


class AsyncAempResourceWithRawResponse:
    def __init__(self, aemp: AsyncAempResource) -> None:
        self._aemp = aemp

    @cached_property
    def fleet(self) -> AsyncFleetResourceWithRawResponse:
        return AsyncFleetResourceWithRawResponse(self._aemp.fleet)


class AempResourceWithStreamingResponse:
    def __init__(self, aemp: AempResource) -> None:
        self._aemp = aemp

    @cached_property
    def fleet(self) -> FleetResourceWithStreamingResponse:
        return FleetResourceWithStreamingResponse(self._aemp.fleet)


class AsyncAempResourceWithStreamingResponse:
    def __init__(self, aemp: AsyncAempResource) -> None:
        self._aemp = aemp

    @cached_property
    def fleet(self) -> AsyncFleetResourceWithStreamingResponse:
        return AsyncFleetResourceWithStreamingResponse(self._aemp.fleet)
