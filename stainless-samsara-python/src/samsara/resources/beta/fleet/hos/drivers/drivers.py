# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .eld_events import (
    EldEventsResource,
    AsyncEldEventsResource,
    EldEventsResourceWithRawResponse,
    AsyncEldEventsResourceWithRawResponse,
    EldEventsResourceWithStreamingResponse,
    AsyncEldEventsResourceWithStreamingResponse,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DriversResource", "AsyncDriversResource"]


class DriversResource(SyncAPIResource):
    @cached_property
    def eld_events(self) -> EldEventsResource:
        return EldEventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DriversResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DriversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DriversResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DriversResourceWithStreamingResponse(self)


class AsyncDriversResource(AsyncAPIResource):
    @cached_property
    def eld_events(self) -> AsyncEldEventsResource:
        return AsyncEldEventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDriversResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDriversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDriversResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDriversResourceWithStreamingResponse(self)


class DriversResourceWithRawResponse:
    def __init__(self, drivers: DriversResource) -> None:
        self._drivers = drivers

    @cached_property
    def eld_events(self) -> EldEventsResourceWithRawResponse:
        return EldEventsResourceWithRawResponse(self._drivers.eld_events)


class AsyncDriversResourceWithRawResponse:
    def __init__(self, drivers: AsyncDriversResource) -> None:
        self._drivers = drivers

    @cached_property
    def eld_events(self) -> AsyncEldEventsResourceWithRawResponse:
        return AsyncEldEventsResourceWithRawResponse(self._drivers.eld_events)


class DriversResourceWithStreamingResponse:
    def __init__(self, drivers: DriversResource) -> None:
        self._drivers = drivers

    @cached_property
    def eld_events(self) -> EldEventsResourceWithStreamingResponse:
        return EldEventsResourceWithStreamingResponse(self._drivers.eld_events)


class AsyncDriversResourceWithStreamingResponse:
    def __init__(self, drivers: AsyncDriversResource) -> None:
        self._drivers = drivers

    @cached_property
    def eld_events(self) -> AsyncEldEventsResourceWithStreamingResponse:
        return AsyncEldEventsResourceWithStreamingResponse(self._drivers.eld_events)
