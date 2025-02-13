# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

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
from ...types.assets import location_and_speed_stream_params
from ...types.assets.location_and_speed_stream_response import LocationAndSpeedStreamResponse

__all__ = ["LocationAndSpeedResource", "AsyncLocationAndSpeedResource"]


class LocationAndSpeedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LocationAndSpeedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return LocationAndSpeedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationAndSpeedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return LocationAndSpeedResourceWithStreamingResponse(self)

    def stream(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        include_external_ids: bool | NotGiven = NOT_GIVEN,
        include_geofence_lookup: bool | NotGiven = NOT_GIVEN,
        include_reverse_geo: bool | NotGiven = NOT_GIVEN,
        include_speed: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocationAndSpeedStreamResponse:
        """
        This endpoint will return asset locations and speed data that has been collected
        for your organization based on the time parameters passed in. Results are
        paginated. If you include an endTime, the endpoint will return data up until
        that point. If you don’t include an endTime, you can continue to poll the API
        real-time with the pagination cursor that gets returned on every call. The
        endpoint will only return data up until the endTime that has been processed by
        the server at the time of the original request. You will need to request the
        same [startTime, endTime) range again to receive data for assets processed after
        the original request time. This endpoint sorts the time-series data by device.

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Vehicles** under the Vehicles category when
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
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          end_time: An end time in RFC 3339 format. Defaults to never if not provided; if not
              provided then pagination will not cease, and a valid pagination cursor will
              always be returned. Millisecond precision and timezones are supported.
              (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          ids: Comma-separated list of asset IDs.

          include_external_ids: Optional boolean indicating whether to return external IDs on supported entities

          include_geofence_lookup: Optional boolean indicating whether or not to return the 'geofence' object

          include_reverse_geo: Optional boolean indicating whether or not to return the 'address' object

          include_speed: Optional boolean indicating whether or not to return the 'speed' object

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 512 objects.

          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/assets/location-and-speed/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "end_time": end_time,
                        "ids": ids,
                        "include_external_ids": include_external_ids,
                        "include_geofence_lookup": include_geofence_lookup,
                        "include_reverse_geo": include_reverse_geo,
                        "include_speed": include_speed,
                        "limit": limit,
                        "start_time": start_time,
                    },
                    location_and_speed_stream_params.LocationAndSpeedStreamParams,
                ),
            ),
            cast_to=LocationAndSpeedStreamResponse,
        )


class AsyncLocationAndSpeedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLocationAndSpeedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLocationAndSpeedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationAndSpeedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncLocationAndSpeedResourceWithStreamingResponse(self)

    async def stream(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        include_external_ids: bool | NotGiven = NOT_GIVEN,
        include_geofence_lookup: bool | NotGiven = NOT_GIVEN,
        include_reverse_geo: bool | NotGiven = NOT_GIVEN,
        include_speed: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocationAndSpeedStreamResponse:
        """
        This endpoint will return asset locations and speed data that has been collected
        for your organization based on the time parameters passed in. Results are
        paginated. If you include an endTime, the endpoint will return data up until
        that point. If you don’t include an endTime, you can continue to poll the API
        real-time with the pagination cursor that gets returned on every call. The
        endpoint will only return data up until the endTime that has been processed by
        the server at the time of the original request. You will need to request the
        same [startTime, endTime) range again to receive data for assets processed after
        the original request time. This endpoint sorts the time-series data by device.

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Vehicles** under the Vehicles category when
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
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          end_time: An end time in RFC 3339 format. Defaults to never if not provided; if not
              provided then pagination will not cease, and a valid pagination cursor will
              always be returned. Millisecond precision and timezones are supported.
              (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          ids: Comma-separated list of asset IDs.

          include_external_ids: Optional boolean indicating whether to return external IDs on supported entities

          include_geofence_lookup: Optional boolean indicating whether or not to return the 'geofence' object

          include_reverse_geo: Optional boolean indicating whether or not to return the 'address' object

          include_speed: Optional boolean indicating whether or not to return the 'speed' object

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 512 objects.

          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/assets/location-and-speed/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "end_time": end_time,
                        "ids": ids,
                        "include_external_ids": include_external_ids,
                        "include_geofence_lookup": include_geofence_lookup,
                        "include_reverse_geo": include_reverse_geo,
                        "include_speed": include_speed,
                        "limit": limit,
                        "start_time": start_time,
                    },
                    location_and_speed_stream_params.LocationAndSpeedStreamParams,
                ),
            ),
            cast_to=LocationAndSpeedStreamResponse,
        )


class LocationAndSpeedResourceWithRawResponse:
    def __init__(self, location_and_speed: LocationAndSpeedResource) -> None:
        self._location_and_speed = location_and_speed

        self.stream = to_raw_response_wrapper(
            location_and_speed.stream,
        )


class AsyncLocationAndSpeedResourceWithRawResponse:
    def __init__(self, location_and_speed: AsyncLocationAndSpeedResource) -> None:
        self._location_and_speed = location_and_speed

        self.stream = async_to_raw_response_wrapper(
            location_and_speed.stream,
        )


class LocationAndSpeedResourceWithStreamingResponse:
    def __init__(self, location_and_speed: LocationAndSpeedResource) -> None:
        self._location_and_speed = location_and_speed

        self.stream = to_streamed_response_wrapper(
            location_and_speed.stream,
        )


class AsyncLocationAndSpeedResourceWithStreamingResponse:
    def __init__(self, location_and_speed: AsyncLocationAndSpeedResource) -> None:
        self._location_and_speed = location_and_speed

        self.stream = async_to_streamed_response_wrapper(
            location_and_speed.stream,
        )
