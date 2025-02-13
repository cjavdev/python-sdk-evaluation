# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.fleet.reports import vehicle_idling_list_params
from ....types.fleet.reports.vehicle_idling_list_response import VehicleIdlingListResponse

__all__ = ["VehicleIdlingResource", "AsyncVehicleIdlingResource"]


class VehicleIdlingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VehicleIdlingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return VehicleIdlingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VehicleIdlingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return VehicleIdlingResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end_time: str,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        is_pto_active: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        min_idling_duration_minutes: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        vehicle_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VehicleIdlingListResponse:
        """
        Get all vehicle idling reports for the requested time duration.

        <b>Rate limit:</b> 25 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy
        category when creating or editing an API token.
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
          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. Note that the most recent 72 hours of
              data may still be processing and is subject to change and latency, so it is not
              recommended to request data for the most recent 72 hours. (Examples:
              2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. Note that the most recent 72 hours of
              data may still be processing and is subject to change and latency, so it is not
              recommended to request data for the most recent 72 hours. (Examples:
              2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          is_pto_active: A filter on the data based on power take-off being active or inactive.

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 512 objects.

          min_idling_duration_minutes: A filter on the data based on a minimum idling duration.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          vehicle_ids: A filter on the data based on this comma-separated list of vehicle IDs and
              externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fleet/reports/vehicle/idling",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "start_time": start_time,
                        "after": after,
                        "is_pto_active": is_pto_active,
                        "limit": limit,
                        "min_idling_duration_minutes": min_idling_duration_minutes,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "vehicle_ids": vehicle_ids,
                    },
                    vehicle_idling_list_params.VehicleIdlingListParams,
                ),
            ),
            cast_to=VehicleIdlingListResponse,
        )


class AsyncVehicleIdlingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVehicleIdlingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVehicleIdlingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVehicleIdlingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncVehicleIdlingResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        end_time: str,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        is_pto_active: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        min_idling_duration_minutes: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        vehicle_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VehicleIdlingListResponse:
        """
        Get all vehicle idling reports for the requested time duration.

        <b>Rate limit:</b> 25 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy
        category when creating or editing an API token.
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
          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. Note that the most recent 72 hours of
              data may still be processing and is subject to change and latency, so it is not
              recommended to request data for the most recent 72 hours. (Examples:
              2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. Note that the most recent 72 hours of
              data may still be processing and is subject to change and latency, so it is not
              recommended to request data for the most recent 72 hours. (Examples:
              2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          is_pto_active: A filter on the data based on power take-off being active or inactive.

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 512 objects.

          min_idling_duration_minutes: A filter on the data based on a minimum idling duration.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          vehicle_ids: A filter on the data based on this comma-separated list of vehicle IDs and
              externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fleet/reports/vehicle/idling",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_time": end_time,
                        "start_time": start_time,
                        "after": after,
                        "is_pto_active": is_pto_active,
                        "limit": limit,
                        "min_idling_duration_minutes": min_idling_duration_minutes,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "vehicle_ids": vehicle_ids,
                    },
                    vehicle_idling_list_params.VehicleIdlingListParams,
                ),
            ),
            cast_to=VehicleIdlingListResponse,
        )


class VehicleIdlingResourceWithRawResponse:
    def __init__(self, vehicle_idling: VehicleIdlingResource) -> None:
        self._vehicle_idling = vehicle_idling

        self.list = to_raw_response_wrapper(
            vehicle_idling.list,
        )


class AsyncVehicleIdlingResourceWithRawResponse:
    def __init__(self, vehicle_idling: AsyncVehicleIdlingResource) -> None:
        self._vehicle_idling = vehicle_idling

        self.list = async_to_raw_response_wrapper(
            vehicle_idling.list,
        )


class VehicleIdlingResourceWithStreamingResponse:
    def __init__(self, vehicle_idling: VehicleIdlingResource) -> None:
        self._vehicle_idling = vehicle_idling

        self.list = to_streamed_response_wrapper(
            vehicle_idling.list,
        )


class AsyncVehicleIdlingResourceWithStreamingResponse:
    def __init__(self, vehicle_idling: AsyncVehicleIdlingResource) -> None:
        self._vehicle_idling = vehicle_idling

        self.list = async_to_streamed_response_wrapper(
            vehicle_idling.list,
        )
