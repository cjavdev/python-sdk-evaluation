# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .cameras import (
    CamerasResource,
    AsyncCamerasResource,
    CamerasResourceWithRawResponse,
    AsyncCamerasResourceWithRawResponse,
    CamerasResourceWithStreamingResponse,
    AsyncCamerasResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["VisionResource", "AsyncVisionResource"]


class VisionResource(SyncAPIResource):
    @cached_property
    def cameras(self) -> CamerasResource:
        return CamerasResource(self._client)

    @cached_property
    def with_raw_response(self) -> VisionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return VisionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VisionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return VisionResourceWithStreamingResponse(self)


class AsyncVisionResource(AsyncAPIResource):
    @cached_property
    def cameras(self) -> AsyncCamerasResource:
        return AsyncCamerasResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVisionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVisionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVisionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncVisionResourceWithStreamingResponse(self)


class VisionResourceWithRawResponse:
    def __init__(self, vision: VisionResource) -> None:
        self._vision = vision

    @cached_property
    def cameras(self) -> CamerasResourceWithRawResponse:
        return CamerasResourceWithRawResponse(self._vision.cameras)


class AsyncVisionResourceWithRawResponse:
    def __init__(self, vision: AsyncVisionResource) -> None:
        self._vision = vision

    @cached_property
    def cameras(self) -> AsyncCamerasResourceWithRawResponse:
        return AsyncCamerasResourceWithRawResponse(self._vision.cameras)


class VisionResourceWithStreamingResponse:
    def __init__(self, vision: VisionResource) -> None:
        self._vision = vision

    @cached_property
    def cameras(self) -> CamerasResourceWithStreamingResponse:
        return CamerasResourceWithStreamingResponse(self._vision.cameras)


class AsyncVisionResourceWithStreamingResponse:
    def __init__(self, vision: AsyncVisionResource) -> None:
        self._vision = vision

    @cached_property
    def cameras(self) -> AsyncCamerasResourceWithStreamingResponse:
        return AsyncCamerasResourceWithStreamingResponse(self._vision.cameras)
