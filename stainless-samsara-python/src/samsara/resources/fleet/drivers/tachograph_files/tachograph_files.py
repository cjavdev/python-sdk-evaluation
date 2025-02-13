# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TachographFilesResource", "AsyncTachographFilesResource"]


class TachographFilesResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> TachographFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return TachographFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TachographFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return TachographFilesResourceWithStreamingResponse(self)


class AsyncTachographFilesResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTachographFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTachographFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTachographFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncTachographFilesResourceWithStreamingResponse(self)


class TachographFilesResourceWithRawResponse:
    def __init__(self, tachograph_files: TachographFilesResource) -> None:
        self._tachograph_files = tachograph_files

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._tachograph_files.history)


class AsyncTachographFilesResourceWithRawResponse:
    def __init__(self, tachograph_files: AsyncTachographFilesResource) -> None:
        self._tachograph_files = tachograph_files

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._tachograph_files.history)


class TachographFilesResourceWithStreamingResponse:
    def __init__(self, tachograph_files: TachographFilesResource) -> None:
        self._tachograph_files = tachograph_files

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._tachograph_files.history)


class AsyncTachographFilesResourceWithStreamingResponse:
    def __init__(self, tachograph_files: AsyncTachographFilesResource) -> None:
        self._tachograph_files = tachograph_files

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._tachograph_files.history)
