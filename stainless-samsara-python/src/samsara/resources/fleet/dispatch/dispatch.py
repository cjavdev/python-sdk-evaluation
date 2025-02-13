# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .routes import (
    RoutesResource,
    AsyncRoutesResource,
    RoutesResourceWithRawResponse,
    AsyncRoutesResourceWithRawResponse,
    RoutesResourceWithStreamingResponse,
    AsyncRoutesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DispatchResource", "AsyncDispatchResource"]


class DispatchResource(SyncAPIResource):
    @cached_property
    def routes(self) -> RoutesResource:
        return RoutesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DispatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DispatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DispatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DispatchResourceWithStreamingResponse(self)


class AsyncDispatchResource(AsyncAPIResource):
    @cached_property
    def routes(self) -> AsyncRoutesResource:
        return AsyncRoutesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDispatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDispatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDispatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDispatchResourceWithStreamingResponse(self)


class DispatchResourceWithRawResponse:
    def __init__(self, dispatch: DispatchResource) -> None:
        self._dispatch = dispatch

    @cached_property
    def routes(self) -> RoutesResourceWithRawResponse:
        return RoutesResourceWithRawResponse(self._dispatch.routes)


class AsyncDispatchResourceWithRawResponse:
    def __init__(self, dispatch: AsyncDispatchResource) -> None:
        self._dispatch = dispatch

    @cached_property
    def routes(self) -> AsyncRoutesResourceWithRawResponse:
        return AsyncRoutesResourceWithRawResponse(self._dispatch.routes)


class DispatchResourceWithStreamingResponse:
    def __init__(self, dispatch: DispatchResource) -> None:
        self._dispatch = dispatch

    @cached_property
    def routes(self) -> RoutesResourceWithStreamingResponse:
        return RoutesResourceWithStreamingResponse(self._dispatch.routes)


class AsyncDispatchResourceWithStreamingResponse:
    def __init__(self, dispatch: AsyncDispatchResource) -> None:
        self._dispatch = dispatch

    @cached_property
    def routes(self) -> AsyncRoutesResourceWithStreamingResponse:
        return AsyncRoutesResourceWithStreamingResponse(self._dispatch.routes)
