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
from ...types.vehicles import location_feed_params, location_list_params, location_history_params
from ...types.fleet.vehicles.vehicle_locations_response import VehicleLocationsResponse
from ...types.fleet.vehicles.vehicle_locations_list_response import VehicleLocationsListResponse

__all__ = ["LocationsResource", "AsyncLocationsResource"]


class LocationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return LocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return LocationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        time: str | NotGiven = NOT_GIVEN,
        vehicle_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VehicleLocationsResponse:
        """
        **_NOTE: The Vehicle Locations API is an older API that does not combine GPS
        data with onboard diagnostics. Try our new
        [Vehicle Stats API](ref:getvehiclestats) instead._**

        Returns the last known location of all vehicles at the given `time`. If no
        `time` is specified, the current time is used. This can be optionally filtered
        by tags or specific vehicle IDs.

        Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle
        Locations</a>.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Vehicle Statistics** under the Vehicles
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          time: A filter on the data that returns the last known data points with timestamps
              less than or equal to this value. Defaults to now if not provided. Must be a
              string in RFC 3339 format. Millisecond precision and timezones are supported.
              (Example: `2020-01-27T07:06:25Z`).

          vehicle_ids:
              A filter on the data based on this comma-separated list of vehicle IDs. Example:
              `vehicleIds=1234,5678`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fleet/vehicles/locations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "time": time,
                        "vehicle_ids": vehicle_ids,
                    },
                    location_list_params.LocationListParams,
                ),
            ),
            cast_to=VehicleLocationsResponse,
        )

    def feed(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        vehicle_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VehicleLocationsListResponse:
        """
        **_NOTE: The Vehicle Locations API is an older API that does not combine GPS
        data with onboard diagnostics. Try our new
        [Vehicle Stats API](ref:getvehiclestatsfeed) instead._**

        Follow a continuous feed of all vehicle locations from Samsara Vehicle Gateways.

        Your first call to this endpoint will provide you with the most recent location
        for each vehicle and a `pagination` object that contains an `endCursor`.

        You can provide the `endCursor` to the `after` parameter of this endpoint to get
        location updates since that `endCursor`.

        If `hasNextPage` is `false`, no updates are readily available yet. We'd suggest
        waiting a minimum of 5 seconds before requesting updates.

        Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle
        Locations</a>.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Vehicle Statistics** under the Vehicle
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          vehicle_ids:
              A filter on the data based on this comma-separated list of vehicle IDs. Example:
              `vehicleIds=1234,5678`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fleet/vehicles/locations/feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "vehicle_ids": vehicle_ids,
                    },
                    location_feed_params.LocationFeedParams,
                ),
            ),
            cast_to=VehicleLocationsListResponse,
        )

    def history(
        self,
        *,
        end_time: str,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        vehicle_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VehicleLocationsListResponse:
        """
        **_NOTE: The Vehicle Locations API is an older API that does not combine GPS
        data with onboard diagnostics. Try our new
        [Vehicle Stats API](ref:getvehiclestatshistory) instead._**

        Returns all known vehicle locations during the given time range. This can be
        optionally filtered by tags or specific vehicle IDs.

        Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle
        Locations</a>.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Vehicle Statistics** under the Vehicle
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          end_time: An end time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          start_time: A start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          vehicle_ids:
              A filter on the data based on this comma-separated list of vehicle IDs. Example:
              `vehicleIds=1234,5678`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fleet/vehicles/locations/history",
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
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "vehicle_ids": vehicle_ids,
                    },
                    location_history_params.LocationHistoryParams,
                ),
            ),
            cast_to=VehicleLocationsListResponse,
        )


class AsyncLocationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncLocationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        time: str | NotGiven = NOT_GIVEN,
        vehicle_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VehicleLocationsResponse:
        """
        **_NOTE: The Vehicle Locations API is an older API that does not combine GPS
        data with onboard diagnostics. Try our new
        [Vehicle Stats API](ref:getvehiclestats) instead._**

        Returns the last known location of all vehicles at the given `time`. If no
        `time` is specified, the current time is used. This can be optionally filtered
        by tags or specific vehicle IDs.

        Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle
        Locations</a>.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Vehicle Statistics** under the Vehicles
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          time: A filter on the data that returns the last known data points with timestamps
              less than or equal to this value. Defaults to now if not provided. Must be a
              string in RFC 3339 format. Millisecond precision and timezones are supported.
              (Example: `2020-01-27T07:06:25Z`).

          vehicle_ids:
              A filter on the data based on this comma-separated list of vehicle IDs. Example:
              `vehicleIds=1234,5678`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fleet/vehicles/locations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "time": time,
                        "vehicle_ids": vehicle_ids,
                    },
                    location_list_params.LocationListParams,
                ),
            ),
            cast_to=VehicleLocationsResponse,
        )

    async def feed(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        vehicle_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VehicleLocationsListResponse:
        """
        **_NOTE: The Vehicle Locations API is an older API that does not combine GPS
        data with onboard diagnostics. Try our new
        [Vehicle Stats API](ref:getvehiclestatsfeed) instead._**

        Follow a continuous feed of all vehicle locations from Samsara Vehicle Gateways.

        Your first call to this endpoint will provide you with the most recent location
        for each vehicle and a `pagination` object that contains an `endCursor`.

        You can provide the `endCursor` to the `after` parameter of this endpoint to get
        location updates since that `endCursor`.

        If `hasNextPage` is `false`, no updates are readily available yet. We'd suggest
        waiting a minimum of 5 seconds before requesting updates.

        Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle
        Locations</a>.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Vehicle Statistics** under the Vehicle
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          vehicle_ids:
              A filter on the data based on this comma-separated list of vehicle IDs. Example:
              `vehicleIds=1234,5678`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fleet/vehicles/locations/feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "vehicle_ids": vehicle_ids,
                    },
                    location_feed_params.LocationFeedParams,
                ),
            ),
            cast_to=VehicleLocationsListResponse,
        )

    async def history(
        self,
        *,
        end_time: str,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        vehicle_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VehicleLocationsListResponse:
        """
        **_NOTE: The Vehicle Locations API is an older API that does not combine GPS
        data with onboard diagnostics. Try our new
        [Vehicle Stats API](ref:getvehiclestatshistory) instead._**

        Returns all known vehicle locations during the given time range. This can be
        optionally filtered by tags or specific vehicle IDs.

        Related guide: <a href="/docs/vehicle-locations-1" target="_blank">Vehicle
        Locations</a>.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Vehicle Statistics** under the Vehicle
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          end_time: An end time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          start_time: A start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          vehicle_ids:
              A filter on the data based on this comma-separated list of vehicle IDs. Example:
              `vehicleIds=1234,5678`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fleet/vehicles/locations/history",
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
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "vehicle_ids": vehicle_ids,
                    },
                    location_history_params.LocationHistoryParams,
                ),
            ),
            cast_to=VehicleLocationsListResponse,
        )


class LocationsResourceWithRawResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.list = to_raw_response_wrapper(
            locations.list,
        )
        self.feed = to_raw_response_wrapper(
            locations.feed,
        )
        self.history = to_raw_response_wrapper(
            locations.history,
        )


class AsyncLocationsResourceWithRawResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.list = async_to_raw_response_wrapper(
            locations.list,
        )
        self.feed = async_to_raw_response_wrapper(
            locations.feed,
        )
        self.history = async_to_raw_response_wrapper(
            locations.history,
        )


class LocationsResourceWithStreamingResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.list = to_streamed_response_wrapper(
            locations.list,
        )
        self.feed = to_streamed_response_wrapper(
            locations.feed,
        )
        self.history = to_streamed_response_wrapper(
            locations.history,
        )


class AsyncLocationsResourceWithStreamingResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.list = async_to_streamed_response_wrapper(
            locations.list,
        )
        self.feed = async_to_streamed_response_wrapper(
            locations.feed,
        )
        self.history = async_to_streamed_response_wrapper(
            locations.history,
        )
