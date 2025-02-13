# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .retrieval import (
    RetrievalResource,
    AsyncRetrievalResource,
    RetrievalResourceWithRawResponse,
    AsyncRetrievalResourceWithRawResponse,
    RetrievalResourceWithStreamingResponse,
    AsyncRetrievalResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MediaResource", "AsyncMediaResource"]


class MediaResource(SyncAPIResource):
    @cached_property
    def retrieval(self) -> RetrievalResource:
        return RetrievalResource(self._client)

    @cached_property
    def with_raw_response(self) -> MediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return MediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return MediaResourceWithStreamingResponse(self)


class AsyncMediaResource(AsyncAPIResource):
    @cached_property
    def retrieval(self) -> AsyncRetrievalResource:
        return AsyncRetrievalResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncMediaResourceWithStreamingResponse(self)


class MediaResourceWithRawResponse:
    def __init__(self, media: MediaResource) -> None:
        self._media = media

    @cached_property
    def retrieval(self) -> RetrievalResourceWithRawResponse:
        return RetrievalResourceWithRawResponse(self._media.retrieval)


class AsyncMediaResourceWithRawResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
        self._media = media

    @cached_property
    def retrieval(self) -> AsyncRetrievalResourceWithRawResponse:
        return AsyncRetrievalResourceWithRawResponse(self._media.retrieval)


class MediaResourceWithStreamingResponse:
    def __init__(self, media: MediaResource) -> None:
        self._media = media

    @cached_property
    def retrieval(self) -> RetrievalResourceWithStreamingResponse:
        return RetrievalResourceWithStreamingResponse(self._media.retrieval)


class AsyncMediaResourceWithStreamingResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
        self._media = media

    @cached_property
    def retrieval(self) -> AsyncRetrievalResourceWithStreamingResponse:
        return AsyncRetrievalResourceWithStreamingResponse(self._media.retrieval)
