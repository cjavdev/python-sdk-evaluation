# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .programs import (
    ProgramsResource,
    AsyncProgramsResource,
    ProgramsResourceWithRawResponse,
    AsyncProgramsResourceWithRawResponse,
    ProgramsResourceWithStreamingResponse,
    AsyncProgramsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CamerasResource", "AsyncCamerasResource"]


class CamerasResource(SyncAPIResource):
    @cached_property
    def programs(self) -> ProgramsResource:
        return ProgramsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CamerasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return CamerasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CamerasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return CamerasResourceWithStreamingResponse(self)


class AsyncCamerasResource(AsyncAPIResource):
    @cached_property
    def programs(self) -> AsyncProgramsResource:
        return AsyncProgramsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCamerasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCamerasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCamerasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncCamerasResourceWithStreamingResponse(self)


class CamerasResourceWithRawResponse:
    def __init__(self, cameras: CamerasResource) -> None:
        self._cameras = cameras

    @cached_property
    def programs(self) -> ProgramsResourceWithRawResponse:
        return ProgramsResourceWithRawResponse(self._cameras.programs)


class AsyncCamerasResourceWithRawResponse:
    def __init__(self, cameras: AsyncCamerasResource) -> None:
        self._cameras = cameras

    @cached_property
    def programs(self) -> AsyncProgramsResourceWithRawResponse:
        return AsyncProgramsResourceWithRawResponse(self._cameras.programs)


class CamerasResourceWithStreamingResponse:
    def __init__(self, cameras: CamerasResource) -> None:
        self._cameras = cameras

    @cached_property
    def programs(self) -> ProgramsResourceWithStreamingResponse:
        return ProgramsResourceWithStreamingResponse(self._cameras.programs)


class AsyncCamerasResourceWithStreamingResponse:
    def __init__(self, cameras: AsyncCamerasResource) -> None:
        self._cameras = cameras

    @cached_property
    def programs(self) -> AsyncProgramsResourceWithStreamingResponse:
        return AsyncProgramsResourceWithStreamingResponse(self._cameras.programs)
