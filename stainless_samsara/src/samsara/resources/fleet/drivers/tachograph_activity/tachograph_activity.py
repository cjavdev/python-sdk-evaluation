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

__all__ = ["TachographActivityResource", "AsyncTachographActivityResource"]


class TachographActivityResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> TachographActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return TachographActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TachographActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return TachographActivityResourceWithStreamingResponse(self)


class AsyncTachographActivityResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTachographActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTachographActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTachographActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncTachographActivityResourceWithStreamingResponse(self)


class TachographActivityResourceWithRawResponse:
    def __init__(self, tachograph_activity: TachographActivityResource) -> None:
        self._tachograph_activity = tachograph_activity

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._tachograph_activity.history)


class AsyncTachographActivityResourceWithRawResponse:
    def __init__(self, tachograph_activity: AsyncTachographActivityResource) -> None:
        self._tachograph_activity = tachograph_activity

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._tachograph_activity.history)


class TachographActivityResourceWithStreamingResponse:
    def __init__(self, tachograph_activity: TachographActivityResource) -> None:
        self._tachograph_activity = tachograph_activity

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._tachograph_activity.history)


class AsyncTachographActivityResourceWithStreamingResponse:
    def __init__(self, tachograph_activity: AsyncTachographActivityResource) -> None:
        self._tachograph_activity = tachograph_activity

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._tachograph_activity.history)
