# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import (
    driver_trailer_assignment_list_params,
    driver_trailer_assignment_create_params,
    driver_trailer_assignment_update_params,
)
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
from ..types.driver_trailer_assignment_list_response import DriverTrailerAssignmentListResponse
from ..types.driver_trailer_assignment_create_response import DriverTrailerAssignmentCreateResponse
from ..types.driver_trailer_assignment_update_response import DriverTrailerAssignmentUpdateResponse

__all__ = ["DriverTrailerAssignmentsResource", "AsyncDriverTrailerAssignmentsResource"]


class DriverTrailerAssignmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DriverTrailerAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DriverTrailerAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DriverTrailerAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DriverTrailerAssignmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        driver_id: str,
        trailer_id: str,
        start_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverTrailerAssignmentCreateResponse:
        """
        Create a new driver-trailer assignment

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
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

          trailer_id: ID of the trailer. This can be either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the trailer.

          start_time: The start time in RFC 3339 format. The time needs to be current or within the
              past 7 days. Defaults to now if not provided

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/driver-trailer-assignments",
            body=maybe_transform(
                {
                    "driver_id": driver_id,
                    "trailer_id": trailer_id,
                    "start_time": start_time,
                },
                driver_trailer_assignment_create_params.DriverTrailerAssignmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DriverTrailerAssignmentCreateResponse,
        )

    def update(
        self,
        *,
        id: str,
        end_time: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverTrailerAssignmentUpdateResponse:
        """
        Update an existing driver-trailer assignment.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
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
          id: Samsara ID for the assignment.

          end_time: The end time in RFC 3339 format. The end time should not be in the future

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/driver-trailer-assignments",
            body=maybe_transform(
                {"end_time": end_time}, driver_trailer_assignment_update_params.DriverTrailerAssignmentUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"id": id}, driver_trailer_assignment_update_params.DriverTrailerAssignmentUpdateParams
                ),
            ),
            cast_to=DriverTrailerAssignmentUpdateResponse,
        )

    def list(
        self,
        *,
        driver_ids: List[str],
        after: str | NotGiven = NOT_GIVEN,
        include_external_ids: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverTrailerAssignmentListResponse:
        """
        Get currently active driver-trailer assignments for driver.

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
          driver_ids: A filter on the data based on this comma-separated list of driver IDs and
              externalIds. Example: `driverIds=1234,5678,payroll:4841`

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          include_external_ids: Optional boolean indicating whether to return external IDs on supported entities

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/driver-trailer-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "driver_ids": driver_ids,
                        "after": after,
                        "include_external_ids": include_external_ids,
                    },
                    driver_trailer_assignment_list_params.DriverTrailerAssignmentListParams,
                ),
            ),
            cast_to=DriverTrailerAssignmentListResponse,
        )


class AsyncDriverTrailerAssignmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDriverTrailerAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDriverTrailerAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDriverTrailerAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDriverTrailerAssignmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        driver_id: str,
        trailer_id: str,
        start_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverTrailerAssignmentCreateResponse:
        """
        Create a new driver-trailer assignment

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
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

          trailer_id: ID of the trailer. This can be either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the trailer.

          start_time: The start time in RFC 3339 format. The time needs to be current or within the
              past 7 days. Defaults to now if not provided

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/driver-trailer-assignments",
            body=await async_maybe_transform(
                {
                    "driver_id": driver_id,
                    "trailer_id": trailer_id,
                    "start_time": start_time,
                },
                driver_trailer_assignment_create_params.DriverTrailerAssignmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DriverTrailerAssignmentCreateResponse,
        )

    async def update(
        self,
        *,
        id: str,
        end_time: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverTrailerAssignmentUpdateResponse:
        """
        Update an existing driver-trailer assignment.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
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
          id: Samsara ID for the assignment.

          end_time: The end time in RFC 3339 format. The end time should not be in the future

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/driver-trailer-assignments",
            body=await async_maybe_transform(
                {"end_time": end_time}, driver_trailer_assignment_update_params.DriverTrailerAssignmentUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"id": id}, driver_trailer_assignment_update_params.DriverTrailerAssignmentUpdateParams
                ),
            ),
            cast_to=DriverTrailerAssignmentUpdateResponse,
        )

    async def list(
        self,
        *,
        driver_ids: List[str],
        after: str | NotGiven = NOT_GIVEN,
        include_external_ids: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverTrailerAssignmentListResponse:
        """
        Get currently active driver-trailer assignments for driver.

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
          driver_ids: A filter on the data based on this comma-separated list of driver IDs and
              externalIds. Example: `driverIds=1234,5678,payroll:4841`

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          include_external_ids: Optional boolean indicating whether to return external IDs on supported entities

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/driver-trailer-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "driver_ids": driver_ids,
                        "after": after,
                        "include_external_ids": include_external_ids,
                    },
                    driver_trailer_assignment_list_params.DriverTrailerAssignmentListParams,
                ),
            ),
            cast_to=DriverTrailerAssignmentListResponse,
        )


class DriverTrailerAssignmentsResourceWithRawResponse:
    def __init__(self, driver_trailer_assignments: DriverTrailerAssignmentsResource) -> None:
        self._driver_trailer_assignments = driver_trailer_assignments

        self.create = to_raw_response_wrapper(
            driver_trailer_assignments.create,
        )
        self.update = to_raw_response_wrapper(
            driver_trailer_assignments.update,
        )
        self.list = to_raw_response_wrapper(
            driver_trailer_assignments.list,
        )


class AsyncDriverTrailerAssignmentsResourceWithRawResponse:
    def __init__(self, driver_trailer_assignments: AsyncDriverTrailerAssignmentsResource) -> None:
        self._driver_trailer_assignments = driver_trailer_assignments

        self.create = async_to_raw_response_wrapper(
            driver_trailer_assignments.create,
        )
        self.update = async_to_raw_response_wrapper(
            driver_trailer_assignments.update,
        )
        self.list = async_to_raw_response_wrapper(
            driver_trailer_assignments.list,
        )


class DriverTrailerAssignmentsResourceWithStreamingResponse:
    def __init__(self, driver_trailer_assignments: DriverTrailerAssignmentsResource) -> None:
        self._driver_trailer_assignments = driver_trailer_assignments

        self.create = to_streamed_response_wrapper(
            driver_trailer_assignments.create,
        )
        self.update = to_streamed_response_wrapper(
            driver_trailer_assignments.update,
        )
        self.list = to_streamed_response_wrapper(
            driver_trailer_assignments.list,
        )


class AsyncDriverTrailerAssignmentsResourceWithStreamingResponse:
    def __init__(self, driver_trailer_assignments: AsyncDriverTrailerAssignmentsResource) -> None:
        self._driver_trailer_assignments = driver_trailer_assignments

        self.create = async_to_streamed_response_wrapper(
            driver_trailer_assignments.create,
        )
        self.update = async_to_streamed_response_wrapper(
            driver_trailer_assignments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            driver_trailer_assignments.list,
        )
