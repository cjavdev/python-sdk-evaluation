# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import trip_list_params, trip_stream_params
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
from ..types.fleet.v1_trip_response import V1TripResponse
from ..types.trips_get_trips_response_body import TripsGetTripsResponseBody

__all__ = ["TripsResource", "AsyncTripsResource"]


class TripsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TripsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return TripsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TripsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return TripsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end_ms: int,
        start_ms: int,
        vehicle_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1TripResponse:
        """
        <n class="warning">
        <nh>
        <i class="fa fa-exclamation-circle"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Get historical trips data for specified vehicle. This method returns a set of
        historical trips data for the specified vehicle in the specified time range.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Vehicle Trips** under the Vehicles category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          end_ms: End of the time range, specified in milliseconds UNIX time.

          start_ms: Beginning of the time range, specified in milliseconds UNIX time. Limited to a
              90 day window with respect to startMs and endMs

          vehicle_id: Vehicle ID to query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/fleet/trips",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_ms": end_ms,
                        "start_ms": start_ms,
                        "vehicle_id": vehicle_id,
                    },
                    trip_list_params.TripListParams,
                ),
            ),
            cast_to=V1TripResponse,
        )

    def stream(
        self,
        *,
        ids: List[str],
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        completion_status: Literal["inProgress", "completed", "all"] | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        include_asset: bool | NotGiven = NOT_GIVEN,
        query_by: Literal["updatedAtTime", "tripStartTime"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TripsGetTripsResponseBody:
        """
        This endpoint will return trips that have been collected for your organization
        based on the time parameters passed in. Results are paginated. Reach out to your
        Samsara Representative to have this API enabled for your organization.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Trips** under the Trips category when
        creating or editing an API token.
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
          ids: Comma-separated list of asset IDs. Include up to 50 asset IDs.

          start_time: RFC 3339 timestamp that indicates when to begin receiving data. Value is
              compared against `updatedAtTime` or `tripStartTime` depending on the queryBy
              parameter.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          completion_status: Filters trips based on a specific completion status Valid values: `inProgress`,
              `completed`, `all`

          end_time: RFC 3339 timestamp which is compared against `updatedAtTime` or `tripStartTime`
              depending on the queryBy parameter. If not provided then the endpoint behaves as
              an unending feed of changes.

          include_asset: Indicates whether or not to return expanded “asset” data

          query_by: Decide which timestamp the `startTime` and `endTime` are compared to. Valid
              values: `updatedAtTime`, `tripStartTime`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/trips/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "start_time": start_time,
                        "after": after,
                        "completion_status": completion_status,
                        "end_time": end_time,
                        "include_asset": include_asset,
                        "query_by": query_by,
                    },
                    trip_stream_params.TripStreamParams,
                ),
            ),
            cast_to=TripsGetTripsResponseBody,
        )


class AsyncTripsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTripsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTripsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTripsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncTripsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        end_ms: int,
        start_ms: int,
        vehicle_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1TripResponse:
        """
        <n class="warning">
        <nh>
        <i class="fa fa-exclamation-circle"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Get historical trips data for specified vehicle. This method returns a set of
        historical trips data for the specified vehicle in the specified time range.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Vehicle Trips** under the Vehicles category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          end_ms: End of the time range, specified in milliseconds UNIX time.

          start_ms: Beginning of the time range, specified in milliseconds UNIX time. Limited to a
              90 day window with respect to startMs and endMs

          vehicle_id: Vehicle ID to query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/fleet/trips",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_ms": end_ms,
                        "start_ms": start_ms,
                        "vehicle_id": vehicle_id,
                    },
                    trip_list_params.TripListParams,
                ),
            ),
            cast_to=V1TripResponse,
        )

    async def stream(
        self,
        *,
        ids: List[str],
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        completion_status: Literal["inProgress", "completed", "all"] | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        include_asset: bool | NotGiven = NOT_GIVEN,
        query_by: Literal["updatedAtTime", "tripStartTime"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TripsGetTripsResponseBody:
        """
        This endpoint will return trips that have been collected for your organization
        based on the time parameters passed in. Results are paginated. Reach out to your
        Samsara Representative to have this API enabled for your organization.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Trips** under the Trips category when
        creating or editing an API token.
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
          ids: Comma-separated list of asset IDs. Include up to 50 asset IDs.

          start_time: RFC 3339 timestamp that indicates when to begin receiving data. Value is
              compared against `updatedAtTime` or `tripStartTime` depending on the queryBy
              parameter.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          completion_status: Filters trips based on a specific completion status Valid values: `inProgress`,
              `completed`, `all`

          end_time: RFC 3339 timestamp which is compared against `updatedAtTime` or `tripStartTime`
              depending on the queryBy parameter. If not provided then the endpoint behaves as
              an unending feed of changes.

          include_asset: Indicates whether or not to return expanded “asset” data

          query_by: Decide which timestamp the `startTime` and `endTime` are compared to. Valid
              values: `updatedAtTime`, `tripStartTime`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/trips/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ids": ids,
                        "start_time": start_time,
                        "after": after,
                        "completion_status": completion_status,
                        "end_time": end_time,
                        "include_asset": include_asset,
                        "query_by": query_by,
                    },
                    trip_stream_params.TripStreamParams,
                ),
            ),
            cast_to=TripsGetTripsResponseBody,
        )


class TripsResourceWithRawResponse:
    def __init__(self, trips: TripsResource) -> None:
        self._trips = trips

        self.list = to_raw_response_wrapper(
            trips.list,
        )
        self.stream = to_raw_response_wrapper(
            trips.stream,
        )


class AsyncTripsResourceWithRawResponse:
    def __init__(self, trips: AsyncTripsResource) -> None:
        self._trips = trips

        self.list = async_to_raw_response_wrapper(
            trips.list,
        )
        self.stream = async_to_raw_response_wrapper(
            trips.stream,
        )


class TripsResourceWithStreamingResponse:
    def __init__(self, trips: TripsResource) -> None:
        self._trips = trips

        self.list = to_streamed_response_wrapper(
            trips.list,
        )
        self.stream = to_streamed_response_wrapper(
            trips.stream,
        )


class AsyncTripsResourceWithStreamingResponse:
    def __init__(self, trips: AsyncTripsResource) -> None:
        self._trips = trips

        self.list = async_to_streamed_response_wrapper(
            trips.list,
        )
        self.stream = async_to_streamed_response_wrapper(
            trips.stream,
        )
