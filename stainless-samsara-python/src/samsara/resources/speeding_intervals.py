# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import speeding_interval_stream_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.speeding_intervals_get_speeding_intervals_response_body import (
    SpeedingIntervalsGetSpeedingIntervalsResponseBody,
)

__all__ = ["SpeedingIntervalsResource", "AsyncSpeedingIntervalsResource"]


class SpeedingIntervalsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpeedingIntervalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return SpeedingIntervalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpeedingIntervalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return SpeedingIntervalsResourceWithStreamingResponse(self)

    def stream(
        self,
        *,
        asset_ids: List[str],
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        include_asset: bool | NotGiven = NOT_GIVEN,
        include_driver_id: bool | NotGiven = NOT_GIVEN,
        query_by: Literal["updatedAtTime", "tripStartTime"] | NotGiven = NOT_GIVEN,
        severity_levels: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpeedingIntervalsGetSpeedingIntervalsResponseBody:
        """
        This endpoint will return all speeding intervals associated with trips that have
        been collected for your organization based on the time parameters passed in.
        Only completed trips are included. Results are paginated.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Speeding Intervals** under the Speeding
        Intervals category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        Args:
          asset_ids: Comma-separated list of asset IDs. Include up to 50 asset IDs.

          start_time: RFC 3339 timestamp that indicates when to begin receiving data. Value is
              compared against `updatedAtTime` or `tripStartTime` depending on the queryBy
              parameter.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          end_time: RFC 3339 timestamp which is compared against `updatedAtTime` or `tripStartTime`
              depending on the queryBy parameter. If not provided then the endpoint behaves as
              an unending feed of changes.

          include_asset: Indicates whether or not to return expanded “asset” data

          include_driver_id: Indicates whether or not to return trip's driver id

          query_by: Decide which timestamp the `startTime` and `endTime` are compared to. Valid
              values: `updatedAtTime`, `tripStartTime`

          severity_levels: Optional string of comma-separated severity levels to filter speeding intervals
              by. Valid values: “light”, ”moderate”, ”heavy”, “severe”.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/speeding-intervals/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_ids": asset_ids,
                        "start_time": start_time,
                        "after": after,
                        "end_time": end_time,
                        "include_asset": include_asset,
                        "include_driver_id": include_driver_id,
                        "query_by": query_by,
                        "severity_levels": severity_levels,
                    },
                    speeding_interval_stream_params.SpeedingIntervalStreamParams,
                ),
            ),
            cast_to=SpeedingIntervalsGetSpeedingIntervalsResponseBody,
        )


class AsyncSpeedingIntervalsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpeedingIntervalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpeedingIntervalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpeedingIntervalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncSpeedingIntervalsResourceWithStreamingResponse(self)

    async def stream(
        self,
        *,
        asset_ids: List[str],
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        include_asset: bool | NotGiven = NOT_GIVEN,
        include_driver_id: bool | NotGiven = NOT_GIVEN,
        query_by: Literal["updatedAtTime", "tripStartTime"] | NotGiven = NOT_GIVEN,
        severity_levels: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpeedingIntervalsGetSpeedingIntervalsResponseBody:
        """
        This endpoint will return all speeding intervals associated with trips that have
        been collected for your organization based on the time parameters passed in.
        Only completed trips are included. Results are paginated.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Speeding Intervals** under the Speeding
        Intervals category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        Args:
          asset_ids: Comma-separated list of asset IDs. Include up to 50 asset IDs.

          start_time: RFC 3339 timestamp that indicates when to begin receiving data. Value is
              compared against `updatedAtTime` or `tripStartTime` depending on the queryBy
              parameter.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          end_time: RFC 3339 timestamp which is compared against `updatedAtTime` or `tripStartTime`
              depending on the queryBy parameter. If not provided then the endpoint behaves as
              an unending feed of changes.

          include_asset: Indicates whether or not to return expanded “asset” data

          include_driver_id: Indicates whether or not to return trip's driver id

          query_by: Decide which timestamp the `startTime` and `endTime` are compared to. Valid
              values: `updatedAtTime`, `tripStartTime`

          severity_levels: Optional string of comma-separated severity levels to filter speeding intervals
              by. Valid values: “light”, ”moderate”, ”heavy”, “severe”.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/speeding-intervals/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asset_ids": asset_ids,
                        "start_time": start_time,
                        "after": after,
                        "end_time": end_time,
                        "include_asset": include_asset,
                        "include_driver_id": include_driver_id,
                        "query_by": query_by,
                        "severity_levels": severity_levels,
                    },
                    speeding_interval_stream_params.SpeedingIntervalStreamParams,
                ),
            ),
            cast_to=SpeedingIntervalsGetSpeedingIntervalsResponseBody,
        )


class SpeedingIntervalsResourceWithRawResponse:
    def __init__(self, speeding_intervals: SpeedingIntervalsResource) -> None:
        self._speeding_intervals = speeding_intervals

        self.stream = to_raw_response_wrapper(
            speeding_intervals.stream,
        )


class AsyncSpeedingIntervalsResourceWithRawResponse:
    def __init__(self, speeding_intervals: AsyncSpeedingIntervalsResource) -> None:
        self._speeding_intervals = speeding_intervals

        self.stream = async_to_raw_response_wrapper(
            speeding_intervals.stream,
        )


class SpeedingIntervalsResourceWithStreamingResponse:
    def __init__(self, speeding_intervals: SpeedingIntervalsResource) -> None:
        self._speeding_intervals = speeding_intervals

        self.stream = to_streamed_response_wrapper(
            speeding_intervals.stream,
        )


class AsyncSpeedingIntervalsResourceWithStreamingResponse:
    def __init__(self, speeding_intervals: AsyncSpeedingIntervalsResource) -> None:
        self._speeding_intervals = speeding_intervals

        self.stream = async_to_streamed_response_wrapper(
            speeding_intervals.stream,
        )
