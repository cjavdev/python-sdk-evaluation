# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["IndustrialResource", "AsyncIndustrialResource"]


class IndustrialResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> IndustrialResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return IndustrialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndustrialResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return IndustrialResourceWithStreamingResponse(self)


class AsyncIndustrialResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIndustrialResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndustrialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndustrialResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncIndustrialResourceWithStreamingResponse(self)


class IndustrialResourceWithRawResponse:
    def __init__(self, industrial: IndustrialResource) -> None:
        self._industrial = industrial

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._industrial.jobs)


class AsyncIndustrialResourceWithRawResponse:
    def __init__(self, industrial: AsyncIndustrialResource) -> None:
        self._industrial = industrial

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._industrial.jobs)


class IndustrialResourceWithStreamingResponse:
    def __init__(self, industrial: IndustrialResource) -> None:
        self._industrial = industrial

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._industrial.jobs)


class AsyncIndustrialResourceWithStreamingResponse:
    def __init__(self, industrial: AsyncIndustrialResource) -> None:
        self._industrial = industrial

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._industrial.jobs)
