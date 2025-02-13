# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ...types.fleet import (
    driver_vehicle_assignment_list_params,
    driver_vehicle_assignment_create_params,
    driver_vehicle_assignment_delete_params,
    driver_vehicle_assignment_update_params,
)
from ..._base_client import make_request_options
from ...types.fleet.driver_vehicle_assignment_list_response import DriverVehicleAssignmentListResponse
from ...types.fleet.driver_vehicle_assignment_create_response import DriverVehicleAssignmentCreateResponse
from ...types.fleet.driver_vehicle_assignment_update_response import DriverVehicleAssignmentUpdateResponse

__all__ = ["DriverVehicleAssignmentsResource", "AsyncDriverVehicleAssignmentsResource"]


class DriverVehicleAssignmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DriverVehicleAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DriverVehicleAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DriverVehicleAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DriverVehicleAssignmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        driver_id: str,
        vehicle_id: str,
        assigned_at_time: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        is_passenger: bool | NotGiven = NOT_GIVEN,
        metadata: driver_vehicle_assignment_create_params.Metadata | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverVehicleAssignmentCreateResponse:
        """Assign vehicle drive-time to a driver via API.

        For a step-by-step instruction on
        how to leverage this endpoint, see
        [this guide](https://developers.samsara.com/docs/creating-driver-vehicle-assignments)

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assignments** under the Assignments
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
          driver_id: ID of the driver. This can be either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the driver.

          vehicle_id: ID of the vehicle. This can be either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.

          assigned_at_time: The time at which the assignment was made in RFC 3339 format. Defaults to now if
              not provided. Millisecond precision and timezones are supported. (Examples:
              2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          end_time: The end time in RFC 3339 format. Defaults to max-time (meaning it's an ongoing
              assignment) if not provided. Millisecond precision and timezones are supported.
              (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          is_passenger: Is this driver a passenger? Defaults to false if not provided

          metadata: Metadata about this driver assignment

          start_time: The start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fleet/driver-vehicle-assignments",
            body=maybe_transform(
                {
                    "driver_id": driver_id,
                    "vehicle_id": vehicle_id,
                    "assigned_at_time": assigned_at_time,
                    "end_time": end_time,
                    "is_passenger": is_passenger,
                    "metadata": metadata,
                    "start_time": start_time,
                },
                driver_vehicle_assignment_create_params.DriverVehicleAssignmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DriverVehicleAssignmentCreateResponse,
        )

    def update(
        self,
        *,
        driver_id: str,
        start_time: str,
        vehicle_id: str,
        assigned_at_time: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        is_passenger: bool | NotGiven = NOT_GIVEN,
        metadata: driver_vehicle_assignment_update_params.Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverVehicleAssignmentUpdateResponse:
        """
        Update driver assignments that were created using the
        `POST fleet/driver-vehicle-assignments`. Vehicle Id, Driver Id, and Start Time
        must match an existing assignment.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assignments** under the Assignments
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
          driver_id: ID of the driver. This can be either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the driver.

          start_time: The start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          vehicle_id: ID of the vehicle. This can be either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.

          assigned_at_time: The time at which the assignment was made in RFC 3339 format. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          end_time: The end time in RFC 3339 format. To make this an ongoing assignment (ie. an
              assignment with no end time), provide an endTime value of 'null'. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          is_passenger: Is this driver a passenger?

          metadata: Metadata about this driver assignment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/fleet/driver-vehicle-assignments",
            body=maybe_transform(
                {
                    "driver_id": driver_id,
                    "start_time": start_time,
                    "vehicle_id": vehicle_id,
                    "assigned_at_time": assigned_at_time,
                    "end_time": end_time,
                    "is_passenger": is_passenger,
                    "metadata": metadata,
                },
                driver_vehicle_assignment_update_params.DriverVehicleAssignmentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DriverVehicleAssignmentUpdateResponse,
        )

    def list(
        self,
        *,
        filter_by: Literal["drivers", "vehicles"],
        after: str | NotGiven = NOT_GIVEN,
        assignment_type: Literal[
            "HOS", "idCard", "static", "faceId", "tachograph", "safetyManual", "RFID", "trailer", "external", "qrCode"
        ]
        | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        driver_tag_ids: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        vehicle_ids: List[str] | NotGiven = NOT_GIVEN,
        vehicle_tag_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverVehicleAssignmentListResponse:
        """
        Get all driver-vehicle assignments for the requested drivers or vehicles in the
        requested time range. To fetch driver-vehicle assignments out of the vehicle
        trips' time ranges, assignmentType needs to be specified. Note: this endpoint
        replaces past endpoints to fetch assignments by driver or by vehicle. Visit
        [this migration guide](https://developers.samsara.com/docs/migrating-from-driver-vehicle-assignment-or-vehicle-driver-assignment-endpoints)
        for more information.

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
          filter_by: Option to filter by drivers or vehicles. Valid values: `drivers`, `vehicles`

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          assignment_type: Specifies which assignment type to filter by. Valid values: `HOS`, `idCard`,
              `static`, `faceId`, `tachograph`, `safetyManual`, `RFID`, `trailer`, `external`,
              `qrCode`

          driver_ids: A filter on the data based on this comma-separated list of driver IDs and
              externalIds. Example: `driverIds=1234,5678,payroll:4841`

          driver_tag_ids: A filter on the data based on this comma-separated list of driver tag IDs.
              Example: `tagIds=1234,5678`

          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          vehicle_ids: ID of the vehicle. This can either be the Samsara-specified ID, or an external
              ID. External IDs are customer specified key-value pairs created in the POST or
              PATCH requests of this resource. To specify an external ID as part of a path
              parameter, use the following format: "key:value". For example,
              "maintenanceId:250020".

          vehicle_tag_ids: A filter on the data based on this comma-separated list of vehicle tag IDs.
              Example: `tagIds=1234,5678`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fleet/driver-vehicle-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_by": filter_by,
                        "after": after,
                        "assignment_type": assignment_type,
                        "driver_ids": driver_ids,
                        "driver_tag_ids": driver_tag_ids,
                        "end_time": end_time,
                        "start_time": start_time,
                        "vehicle_ids": vehicle_ids,
                        "vehicle_tag_ids": vehicle_tag_ids,
                    },
                    driver_vehicle_assignment_list_params.DriverVehicleAssignmentListParams,
                ),
            ),
            cast_to=DriverVehicleAssignmentListResponse,
        )

    def delete(
        self,
        *,
        vehicle_id: str,
        assigned_at_time: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        is_passenger: bool | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete driver assignments that were created using the
        `POST fleet/driver-vehicle-assignments` endpoint for the requested vehicle in
        the requested time range.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assignments** under the Assignments
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
          vehicle_id: ID of the vehicle. This can be either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.

          assigned_at_time: Assigned at time in RFC 3339 format. Defaults to now if not provided.
              Millisecond precision and timezones are supported. (Examples:
              2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          end_time: An end time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          is_passenger: Indicates if assigned driver is passenger

          start_time: A start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/fleet/driver-vehicle-assignments",
            body=maybe_transform(
                {
                    "vehicle_id": vehicle_id,
                    "assigned_at_time": assigned_at_time,
                    "end_time": end_time,
                    "is_passenger": is_passenger,
                    "start_time": start_time,
                },
                driver_vehicle_assignment_delete_params.DriverVehicleAssignmentDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDriverVehicleAssignmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDriverVehicleAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDriverVehicleAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDriverVehicleAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDriverVehicleAssignmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        driver_id: str,
        vehicle_id: str,
        assigned_at_time: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        is_passenger: bool | NotGiven = NOT_GIVEN,
        metadata: driver_vehicle_assignment_create_params.Metadata | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverVehicleAssignmentCreateResponse:
        """Assign vehicle drive-time to a driver via API.

        For a step-by-step instruction on
        how to leverage this endpoint, see
        [this guide](https://developers.samsara.com/docs/creating-driver-vehicle-assignments)

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assignments** under the Assignments
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
          driver_id: ID of the driver. This can be either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the driver.

          vehicle_id: ID of the vehicle. This can be either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.

          assigned_at_time: The time at which the assignment was made in RFC 3339 format. Defaults to now if
              not provided. Millisecond precision and timezones are supported. (Examples:
              2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          end_time: The end time in RFC 3339 format. Defaults to max-time (meaning it's an ongoing
              assignment) if not provided. Millisecond precision and timezones are supported.
              (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          is_passenger: Is this driver a passenger? Defaults to false if not provided

          metadata: Metadata about this driver assignment

          start_time: The start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fleet/driver-vehicle-assignments",
            body=await async_maybe_transform(
                {
                    "driver_id": driver_id,
                    "vehicle_id": vehicle_id,
                    "assigned_at_time": assigned_at_time,
                    "end_time": end_time,
                    "is_passenger": is_passenger,
                    "metadata": metadata,
                    "start_time": start_time,
                },
                driver_vehicle_assignment_create_params.DriverVehicleAssignmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DriverVehicleAssignmentCreateResponse,
        )

    async def update(
        self,
        *,
        driver_id: str,
        start_time: str,
        vehicle_id: str,
        assigned_at_time: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        is_passenger: bool | NotGiven = NOT_GIVEN,
        metadata: driver_vehicle_assignment_update_params.Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverVehicleAssignmentUpdateResponse:
        """
        Update driver assignments that were created using the
        `POST fleet/driver-vehicle-assignments`. Vehicle Id, Driver Id, and Start Time
        must match an existing assignment.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assignments** under the Assignments
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
          driver_id: ID of the driver. This can be either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the driver.

          start_time: The start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          vehicle_id: ID of the vehicle. This can be either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.

          assigned_at_time: The time at which the assignment was made in RFC 3339 format. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          end_time: The end time in RFC 3339 format. To make this an ongoing assignment (ie. an
              assignment with no end time), provide an endTime value of 'null'. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          is_passenger: Is this driver a passenger?

          metadata: Metadata about this driver assignment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/fleet/driver-vehicle-assignments",
            body=await async_maybe_transform(
                {
                    "driver_id": driver_id,
                    "start_time": start_time,
                    "vehicle_id": vehicle_id,
                    "assigned_at_time": assigned_at_time,
                    "end_time": end_time,
                    "is_passenger": is_passenger,
                    "metadata": metadata,
                },
                driver_vehicle_assignment_update_params.DriverVehicleAssignmentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DriverVehicleAssignmentUpdateResponse,
        )

    async def list(
        self,
        *,
        filter_by: Literal["drivers", "vehicles"],
        after: str | NotGiven = NOT_GIVEN,
        assignment_type: Literal[
            "HOS", "idCard", "static", "faceId", "tachograph", "safetyManual", "RFID", "trailer", "external", "qrCode"
        ]
        | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        driver_tag_ids: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        vehicle_ids: List[str] | NotGiven = NOT_GIVEN,
        vehicle_tag_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverVehicleAssignmentListResponse:
        """
        Get all driver-vehicle assignments for the requested drivers or vehicles in the
        requested time range. To fetch driver-vehicle assignments out of the vehicle
        trips' time ranges, assignmentType needs to be specified. Note: this endpoint
        replaces past endpoints to fetch assignments by driver or by vehicle. Visit
        [this migration guide](https://developers.samsara.com/docs/migrating-from-driver-vehicle-assignment-or-vehicle-driver-assignment-endpoints)
        for more information.

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
          filter_by: Option to filter by drivers or vehicles. Valid values: `drivers`, `vehicles`

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          assignment_type: Specifies which assignment type to filter by. Valid values: `HOS`, `idCard`,
              `static`, `faceId`, `tachograph`, `safetyManual`, `RFID`, `trailer`, `external`,
              `qrCode`

          driver_ids: A filter on the data based on this comma-separated list of driver IDs and
              externalIds. Example: `driverIds=1234,5678,payroll:4841`

          driver_tag_ids: A filter on the data based on this comma-separated list of driver tag IDs.
              Example: `tagIds=1234,5678`

          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          vehicle_ids: ID of the vehicle. This can either be the Samsara-specified ID, or an external
              ID. External IDs are customer specified key-value pairs created in the POST or
              PATCH requests of this resource. To specify an external ID as part of a path
              parameter, use the following format: "key:value". For example,
              "maintenanceId:250020".

          vehicle_tag_ids: A filter on the data based on this comma-separated list of vehicle tag IDs.
              Example: `tagIds=1234,5678`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fleet/driver-vehicle-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_by": filter_by,
                        "after": after,
                        "assignment_type": assignment_type,
                        "driver_ids": driver_ids,
                        "driver_tag_ids": driver_tag_ids,
                        "end_time": end_time,
                        "start_time": start_time,
                        "vehicle_ids": vehicle_ids,
                        "vehicle_tag_ids": vehicle_tag_ids,
                    },
                    driver_vehicle_assignment_list_params.DriverVehicleAssignmentListParams,
                ),
            ),
            cast_to=DriverVehicleAssignmentListResponse,
        )

    async def delete(
        self,
        *,
        vehicle_id: str,
        assigned_at_time: str | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        is_passenger: bool | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete driver assignments that were created using the
        `POST fleet/driver-vehicle-assignments` endpoint for the requested vehicle in
        the requested time range.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Assignments** under the Assignments
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
          vehicle_id: ID of the vehicle. This can be either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.

          assigned_at_time: Assigned at time in RFC 3339 format. Defaults to now if not provided.
              Millisecond precision and timezones are supported. (Examples:
              2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          end_time: An end time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          is_passenger: Indicates if assigned driver is passenger

          start_time: A start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/fleet/driver-vehicle-assignments",
            body=await async_maybe_transform(
                {
                    "vehicle_id": vehicle_id,
                    "assigned_at_time": assigned_at_time,
                    "end_time": end_time,
                    "is_passenger": is_passenger,
                    "start_time": start_time,
                },
                driver_vehicle_assignment_delete_params.DriverVehicleAssignmentDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DriverVehicleAssignmentsResourceWithRawResponse:
    def __init__(self, driver_vehicle_assignments: DriverVehicleAssignmentsResource) -> None:
        self._driver_vehicle_assignments = driver_vehicle_assignments

        self.create = to_raw_response_wrapper(
            driver_vehicle_assignments.create,
        )
        self.update = to_raw_response_wrapper(
            driver_vehicle_assignments.update,
        )
        self.list = to_raw_response_wrapper(
            driver_vehicle_assignments.list,
        )
        self.delete = to_raw_response_wrapper(
            driver_vehicle_assignments.delete,
        )


class AsyncDriverVehicleAssignmentsResourceWithRawResponse:
    def __init__(self, driver_vehicle_assignments: AsyncDriverVehicleAssignmentsResource) -> None:
        self._driver_vehicle_assignments = driver_vehicle_assignments

        self.create = async_to_raw_response_wrapper(
            driver_vehicle_assignments.create,
        )
        self.update = async_to_raw_response_wrapper(
            driver_vehicle_assignments.update,
        )
        self.list = async_to_raw_response_wrapper(
            driver_vehicle_assignments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            driver_vehicle_assignments.delete,
        )


class DriverVehicleAssignmentsResourceWithStreamingResponse:
    def __init__(self, driver_vehicle_assignments: DriverVehicleAssignmentsResource) -> None:
        self._driver_vehicle_assignments = driver_vehicle_assignments

        self.create = to_streamed_response_wrapper(
            driver_vehicle_assignments.create,
        )
        self.update = to_streamed_response_wrapper(
            driver_vehicle_assignments.update,
        )
        self.list = to_streamed_response_wrapper(
            driver_vehicle_assignments.list,
        )
        self.delete = to_streamed_response_wrapper(
            driver_vehicle_assignments.delete,
        )


class AsyncDriverVehicleAssignmentsResourceWithStreamingResponse:
    def __init__(self, driver_vehicle_assignments: AsyncDriverVehicleAssignmentsResource) -> None:
        self._driver_vehicle_assignments = driver_vehicle_assignments

        self.create = async_to_streamed_response_wrapper(
            driver_vehicle_assignments.create,
        )
        self.update = async_to_streamed_response_wrapper(
            driver_vehicle_assignments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            driver_vehicle_assignments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            driver_vehicle_assignments.delete,
        )
