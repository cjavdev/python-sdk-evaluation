# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.sensors import history_create_params
from ...types.sensors.history_create_response import HistoryCreateResponse

__all__ = ["HistoryResource", "AsyncHistoryResource"]


class HistoryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return HistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return HistoryResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        end_ms: int,
        series: Iterable[history_create_params.Series],
        start_ms: int,
        step_ms: int,
        fill_missing: Literal["withNull", "withPrevious"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HistoryCreateResponse:
        """
        <n class="warning">
        <nh>
        <i class="fa fa-exclamation-circle"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Get historical data for specified sensors. This method returns a set of
        historical data for the specified sensors in the specified time range and at the
        specified time resolution.

        <b>Rate limit:</b> 100 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Sensors** under the Equipment category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          end_ms: End of the time range, specified in milliseconds UNIX time.

          start_ms: Beginning of the time range, specified in milliseconds UNIX time.

          step_ms: Time resolution for which data should be returned, in milliseconds. Specifying
              3600000 will return data at hour intervals.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/sensors/history",
            body=maybe_transform(
                {
                    "end_ms": end_ms,
                    "series": series,
                    "start_ms": start_ms,
                    "step_ms": step_ms,
                    "fill_missing": fill_missing,
                },
                history_create_params.HistoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HistoryCreateResponse,
        )


class AsyncHistoryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncHistoryResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        end_ms: int,
        series: Iterable[history_create_params.Series],
        start_ms: int,
        step_ms: int,
        fill_missing: Literal["withNull", "withPrevious"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HistoryCreateResponse:
        """
        <n class="warning">
        <nh>
        <i class="fa fa-exclamation-circle"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Get historical data for specified sensors. This method returns a set of
        historical data for the specified sensors in the specified time range and at the
        specified time resolution.

        <b>Rate limit:</b> 100 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Sensors** under the Equipment category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          end_ms: End of the time range, specified in milliseconds UNIX time.

          start_ms: Beginning of the time range, specified in milliseconds UNIX time.

          step_ms: Time resolution for which data should be returned, in milliseconds. Specifying
              3600000 will return data at hour intervals.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/sensors/history",
            body=await async_maybe_transform(
                {
                    "end_ms": end_ms,
                    "series": series,
                    "start_ms": start_ms,
                    "step_ms": step_ms,
                    "fill_missing": fill_missing,
                },
                history_create_params.HistoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HistoryCreateResponse,
        )


class HistoryResourceWithRawResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

        self.create = to_raw_response_wrapper(
            history.create,
        )


class AsyncHistoryResourceWithRawResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

        self.create = async_to_raw_response_wrapper(
            history.create,
        )


class HistoryResourceWithStreamingResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

        self.create = to_streamed_response_wrapper(
            history.create,
        )


class AsyncHistoryResourceWithStreamingResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

        self.create = async_to_streamed_response_wrapper(
            history.create,
        )
