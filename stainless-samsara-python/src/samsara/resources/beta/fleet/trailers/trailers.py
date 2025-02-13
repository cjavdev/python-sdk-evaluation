# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .stats import (
    StatsResource,
    AsyncStatsResource,
    StatsResourceWithRawResponse,
    AsyncStatsResourceWithRawResponse,
    StatsResourceWithStreamingResponse,
    AsyncStatsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TrailersResource", "AsyncTrailersResource"]


class TrailersResource(SyncAPIResource):
    @cached_property
    def stats(self) -> StatsResource:
        return StatsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TrailersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return TrailersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrailersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return TrailersResourceWithStreamingResponse(self)


class AsyncTrailersResource(AsyncAPIResource):
    @cached_property
    def stats(self) -> AsyncStatsResource:
        return AsyncStatsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTrailersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrailersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrailersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncTrailersResourceWithStreamingResponse(self)


class TrailersResourceWithRawResponse:
    def __init__(self, trailers: TrailersResource) -> None:
        self._trailers = trailers

    @cached_property
    def stats(self) -> StatsResourceWithRawResponse:
        return StatsResourceWithRawResponse(self._trailers.stats)


class AsyncTrailersResourceWithRawResponse:
    def __init__(self, trailers: AsyncTrailersResource) -> None:
        self._trailers = trailers

    @cached_property
    def stats(self) -> AsyncStatsResourceWithRawResponse:
        return AsyncStatsResourceWithRawResponse(self._trailers.stats)


class TrailersResourceWithStreamingResponse:
    def __init__(self, trailers: TrailersResource) -> None:
        self._trailers = trailers

    @cached_property
    def stats(self) -> StatsResourceWithStreamingResponse:
        return StatsResourceWithStreamingResponse(self._trailers.stats)


class AsyncTrailersResourceWithStreamingResponse:
    def __init__(self, trailers: AsyncTrailersResource) -> None:
        self._trailers = trailers

    @cached_property
    def stats(self) -> AsyncStatsResourceWithStreamingResponse:
        return AsyncStatsResourceWithStreamingResponse(self._trailers.stats)
