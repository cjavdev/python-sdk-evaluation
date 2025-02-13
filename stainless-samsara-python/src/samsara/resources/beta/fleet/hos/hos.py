# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .drivers.drivers import (
    DriversResource,
    AsyncDriversResource,
    DriversResourceWithRawResponse,
    AsyncDriversResourceWithRawResponse,
    DriversResourceWithStreamingResponse,
    AsyncDriversResourceWithStreamingResponse,
)

__all__ = ["HosResource", "AsyncHosResource"]


class HosResource(SyncAPIResource):
    @cached_property
    def drivers(self) -> DriversResource:
        return DriversResource(self._client)

    @cached_property
    def with_raw_response(self) -> HosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return HosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return HosResourceWithStreamingResponse(self)


class AsyncHosResource(AsyncAPIResource):
    @cached_property
    def drivers(self) -> AsyncDriversResource:
        return AsyncDriversResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncHosResourceWithStreamingResponse(self)


class HosResourceWithRawResponse:
    def __init__(self, hos: HosResource) -> None:
        self._hos = hos

    @cached_property
    def drivers(self) -> DriversResourceWithRawResponse:
        return DriversResourceWithRawResponse(self._hos.drivers)


class AsyncHosResourceWithRawResponse:
    def __init__(self, hos: AsyncHosResource) -> None:
        self._hos = hos

    @cached_property
    def drivers(self) -> AsyncDriversResourceWithRawResponse:
        return AsyncDriversResourceWithRawResponse(self._hos.drivers)


class HosResourceWithStreamingResponse:
    def __init__(self, hos: HosResource) -> None:
        self._hos = hos

    @cached_property
    def drivers(self) -> DriversResourceWithStreamingResponse:
        return DriversResourceWithStreamingResponse(self._hos.drivers)


class AsyncHosResourceWithStreamingResponse:
    def __init__(self, hos: AsyncHosResource) -> None:
        self._hos = hos

    @cached_property
    def drivers(self) -> AsyncDriversResourceWithStreamingResponse:
        return AsyncDriversResourceWithStreamingResponse(self._hos.drivers)
