# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .aemp.aemp import (
    AempResource,
    AsyncAempResource,
    AempResourceWithRawResponse,
    AsyncAempResourceWithRawResponse,
    AempResourceWithStreamingResponse,
    AsyncAempResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .fleet.fleet import (
    FleetResource,
    AsyncFleetResource,
    FleetResourceWithRawResponse,
    AsyncFleetResourceWithRawResponse,
    FleetResourceWithStreamingResponse,
    AsyncFleetResourceWithStreamingResponse,
)
from .industrial.industrial import (
    IndustrialResource,
    AsyncIndustrialResource,
    IndustrialResourceWithRawResponse,
    AsyncIndustrialResourceWithRawResponse,
    IndustrialResourceWithStreamingResponse,
    AsyncIndustrialResourceWithStreamingResponse,
)

__all__ = ["BetaResource", "AsyncBetaResource"]


class BetaResource(SyncAPIResource):
    @cached_property
    def aemp(self) -> AempResource:
        return AempResource(self._client)

    @cached_property
    def fleet(self) -> FleetResource:
        return FleetResource(self._client)

    @cached_property
    def industrial(self) -> IndustrialResource:
        return IndustrialResource(self._client)

    @cached_property
    def with_raw_response(self) -> BetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return BetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return BetaResourceWithStreamingResponse(self)


class AsyncBetaResource(AsyncAPIResource):
    @cached_property
    def aemp(self) -> AsyncAempResource:
        return AsyncAempResource(self._client)

    @cached_property
    def fleet(self) -> AsyncFleetResource:
        return AsyncFleetResource(self._client)

    @cached_property
    def industrial(self) -> AsyncIndustrialResource:
        return AsyncIndustrialResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncBetaResourceWithStreamingResponse(self)


class BetaResourceWithRawResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

    @cached_property
    def aemp(self) -> AempResourceWithRawResponse:
        return AempResourceWithRawResponse(self._beta.aemp)

    @cached_property
    def fleet(self) -> FleetResourceWithRawResponse:
        return FleetResourceWithRawResponse(self._beta.fleet)

    @cached_property
    def industrial(self) -> IndustrialResourceWithRawResponse:
        return IndustrialResourceWithRawResponse(self._beta.industrial)


class AsyncBetaResourceWithRawResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

    @cached_property
    def aemp(self) -> AsyncAempResourceWithRawResponse:
        return AsyncAempResourceWithRawResponse(self._beta.aemp)

    @cached_property
    def fleet(self) -> AsyncFleetResourceWithRawResponse:
        return AsyncFleetResourceWithRawResponse(self._beta.fleet)

    @cached_property
    def industrial(self) -> AsyncIndustrialResourceWithRawResponse:
        return AsyncIndustrialResourceWithRawResponse(self._beta.industrial)


class BetaResourceWithStreamingResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

    @cached_property
    def aemp(self) -> AempResourceWithStreamingResponse:
        return AempResourceWithStreamingResponse(self._beta.aemp)

    @cached_property
    def fleet(self) -> FleetResourceWithStreamingResponse:
        return FleetResourceWithStreamingResponse(self._beta.fleet)

    @cached_property
    def industrial(self) -> IndustrialResourceWithStreamingResponse:
        return IndustrialResourceWithStreamingResponse(self._beta.industrial)


class AsyncBetaResourceWithStreamingResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

    @cached_property
    def aemp(self) -> AsyncAempResourceWithStreamingResponse:
        return AsyncAempResourceWithStreamingResponse(self._beta.aemp)

    @cached_property
    def fleet(self) -> AsyncFleetResourceWithStreamingResponse:
        return AsyncFleetResourceWithStreamingResponse(self._beta.fleet)

    @cached_property
    def industrial(self) -> AsyncIndustrialResourceWithStreamingResponse:
        return AsyncIndustrialResourceWithStreamingResponse(self._beta.industrial)
