# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from .clocks import (
    ClocksResource,
    AsyncClocksResource,
    ClocksResourceWithRawResponse,
    AsyncClocksResourceWithRawResponse,
    ClocksResourceWithStreamingResponse,
    AsyncClocksResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .daily_logs import (
    DailyLogsResource,
    AsyncDailyLogsResource,
    DailyLogsResourceWithRawResponse,
    AsyncDailyLogsResourceWithRawResponse,
    DailyLogsResourceWithStreamingResponse,
    AsyncDailyLogsResourceWithStreamingResponse,
)
from .violations import (
    ViolationsResource,
    AsyncViolationsResource,
    ViolationsResourceWithRawResponse,
    AsyncViolationsResourceWithRawResponse,
    ViolationsResourceWithStreamingResponse,
    AsyncViolationsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["HosResource", "AsyncHosResource"]


class HosResource(SyncAPIResource):
    @cached_property
    def clocks(self) -> ClocksResource:
        return ClocksResource(self._client)

    @cached_property
    def daily_logs(self) -> DailyLogsResource:
        return DailyLogsResource(self._client)

    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def violations(self) -> ViolationsResource:
        return ViolationsResource(self._client)

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
    def clocks(self) -> AsyncClocksResource:
        return AsyncClocksResource(self._client)

    @cached_property
    def daily_logs(self) -> AsyncDailyLogsResource:
        return AsyncDailyLogsResource(self._client)

    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def violations(self) -> AsyncViolationsResource:
        return AsyncViolationsResource(self._client)

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
    def clocks(self) -> ClocksResourceWithRawResponse:
        return ClocksResourceWithRawResponse(self._hos.clocks)

    @cached_property
    def daily_logs(self) -> DailyLogsResourceWithRawResponse:
        return DailyLogsResourceWithRawResponse(self._hos.daily_logs)

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._hos.logs)

    @cached_property
    def violations(self) -> ViolationsResourceWithRawResponse:
        return ViolationsResourceWithRawResponse(self._hos.violations)


class AsyncHosResourceWithRawResponse:
    def __init__(self, hos: AsyncHosResource) -> None:
        self._hos = hos

    @cached_property
    def clocks(self) -> AsyncClocksResourceWithRawResponse:
        return AsyncClocksResourceWithRawResponse(self._hos.clocks)

    @cached_property
    def daily_logs(self) -> AsyncDailyLogsResourceWithRawResponse:
        return AsyncDailyLogsResourceWithRawResponse(self._hos.daily_logs)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._hos.logs)

    @cached_property
    def violations(self) -> AsyncViolationsResourceWithRawResponse:
        return AsyncViolationsResourceWithRawResponse(self._hos.violations)


class HosResourceWithStreamingResponse:
    def __init__(self, hos: HosResource) -> None:
        self._hos = hos

    @cached_property
    def clocks(self) -> ClocksResourceWithStreamingResponse:
        return ClocksResourceWithStreamingResponse(self._hos.clocks)

    @cached_property
    def daily_logs(self) -> DailyLogsResourceWithStreamingResponse:
        return DailyLogsResourceWithStreamingResponse(self._hos.daily_logs)

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._hos.logs)

    @cached_property
    def violations(self) -> ViolationsResourceWithStreamingResponse:
        return ViolationsResourceWithStreamingResponse(self._hos.violations)


class AsyncHosResourceWithStreamingResponse:
    def __init__(self, hos: AsyncHosResource) -> None:
        self._hos = hos

    @cached_property
    def clocks(self) -> AsyncClocksResourceWithStreamingResponse:
        return AsyncClocksResourceWithStreamingResponse(self._hos.clocks)

    @cached_property
    def daily_logs(self) -> AsyncDailyLogsResourceWithStreamingResponse:
        return AsyncDailyLogsResourceWithStreamingResponse(self._hos.daily_logs)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._hos.logs)

    @cached_property
    def violations(self) -> AsyncViolationsResourceWithStreamingResponse:
        return AsyncViolationsResourceWithStreamingResponse(self._hos.violations)
