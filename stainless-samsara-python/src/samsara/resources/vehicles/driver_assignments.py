# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.vehicles import driver_assignment_list_params
from ...types.fleet.vehicles.vehicles_driver_assignments_get_vehicles_driver_assignments_response_body import (
    VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody,
)

__all__ = ["DriverAssignmentsResource", "AsyncDriverAssignmentsResource"]


class DriverAssignmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DriverAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DriverAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DriverAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DriverAssignmentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        vehicle_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody:
        """
        **Note: This is a legacy endpoint, consider using
        [this endpoint](https://developers.samsara.com/reference/getdrivervehicleassignments)
        instead. The endpoint will continue to function as documented.** Get all driver
        assignments for the requested vehicles in the requested time range. The only
        type of assignment supported right now are assignments created through the
        driver app.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Assignments** under the Assignments category
        when creating or editing an API token.
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

          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). The maximum allowed
              startTime-endTime range is 7 days.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). The maximum allowed
              startTime-endTime range is 7 days.

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
            "/fleet/vehicles/driver-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "end_time": end_time,
                        "parent_tag_ids": parent_tag_ids,
                        "start_time": start_time,
                        "tag_ids": tag_ids,
                        "vehicle_ids": vehicle_ids,
                    },
                    driver_assignment_list_params.DriverAssignmentListParams,
                ),
            ),
            cast_to=VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody,
        )


class AsyncDriverAssignmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDriverAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDriverAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDriverAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDriverAssignmentsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        vehicle_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody:
        """
        **Note: This is a legacy endpoint, consider using
        [this endpoint](https://developers.samsara.com/reference/getdrivervehicleassignments)
        instead. The endpoint will continue to function as documented.** Get all driver
        assignments for the requested vehicles in the requested time range. The only
        type of assignment supported right now are assignments created through the
        driver app.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Assignments** under the Assignments category
        when creating or editing an API token.
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

          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). The maximum allowed
              startTime-endTime range is 7 days.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00). The maximum allowed
              startTime-endTime range is 7 days.

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
            "/fleet/vehicles/driver-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "end_time": end_time,
                        "parent_tag_ids": parent_tag_ids,
                        "start_time": start_time,
                        "tag_ids": tag_ids,
                        "vehicle_ids": vehicle_ids,
                    },
                    driver_assignment_list_params.DriverAssignmentListParams,
                ),
            ),
            cast_to=VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody,
        )


class DriverAssignmentsResourceWithRawResponse:
    def __init__(self, driver_assignments: DriverAssignmentsResource) -> None:
        self._driver_assignments = driver_assignments

        self.list = to_raw_response_wrapper(
            driver_assignments.list,
        )


class AsyncDriverAssignmentsResourceWithRawResponse:
    def __init__(self, driver_assignments: AsyncDriverAssignmentsResource) -> None:
        self._driver_assignments = driver_assignments

        self.list = async_to_raw_response_wrapper(
            driver_assignments.list,
        )


class DriverAssignmentsResourceWithStreamingResponse:
    def __init__(self, driver_assignments: DriverAssignmentsResource) -> None:
        self._driver_assignments = driver_assignments

        self.list = to_streamed_response_wrapper(
            driver_assignments.list,
        )


class AsyncDriverAssignmentsResourceWithStreamingResponse:
    def __init__(self, driver_assignments: AsyncDriverAssignmentsResource) -> None:
        self._driver_assignments = driver_assignments

        self.list = async_to_streamed_response_wrapper(
            driver_assignments.list,
        )
