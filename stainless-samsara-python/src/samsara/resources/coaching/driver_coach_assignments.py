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
from ...types.coaching import driver_coach_assignment_list_params, driver_coach_assignment_update_params
from ...types.coaching.driver_coach_assignment_list_response import DriverCoachAssignmentListResponse
from ...types.coaching.driver_coach_assignment_update_response import DriverCoachAssignmentUpdateResponse

__all__ = ["DriverCoachAssignmentsResource", "AsyncDriverCoachAssignmentsResource"]


class DriverCoachAssignmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DriverCoachAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DriverCoachAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DriverCoachAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DriverCoachAssignmentsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        driver_id: str,
        coach_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverCoachAssignmentUpdateResponse:
        """
        This endpoint will update an existing or create a new coach-to-driver assignment
        for your organization based on the parameters passed in. This endpoint should
        only be used for existing Coach to Driver assignments. In order to remove a
        driver-coach-assignment for a given driver, set coachId to null

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Coaching** under the Coaching category when
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
          driver_id: Required string ID of the driver. This is a unique Samsara ID of a driver.

          coach_id: Optional string ID of the coach. This is a unique Samsara user ID. If not
              provided, existing coach assignment will be removed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/coaching/driver-coach-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "driver_id": driver_id,
                        "coach_id": coach_id,
                    },
                    driver_coach_assignment_update_params.DriverCoachAssignmentUpdateParams,
                ),
            ),
            cast_to=DriverCoachAssignmentUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        coach_ids: List[str] | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        include_external_ids: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverCoachAssignmentListResponse:
        """
        This endpoint will return coach assignments for your organization based on the
        parameters passed in. Results are paginated.

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Coaching** under the Coaching category when
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

          coach_ids: Optional string of comma separated IDs of the coaches.

          driver_ids: Optional string of comma separated IDs of the drivers. This can be either a
              unique Samsara driver ID or an external ID for the driver.

          include_external_ids: Optional boolean indicating whether to return external IDs on supported entities

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/coaching/driver-coach-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "coach_ids": coach_ids,
                        "driver_ids": driver_ids,
                        "include_external_ids": include_external_ids,
                    },
                    driver_coach_assignment_list_params.DriverCoachAssignmentListParams,
                ),
            ),
            cast_to=DriverCoachAssignmentListResponse,
        )


class AsyncDriverCoachAssignmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDriverCoachAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDriverCoachAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDriverCoachAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDriverCoachAssignmentsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        driver_id: str,
        coach_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverCoachAssignmentUpdateResponse:
        """
        This endpoint will update an existing or create a new coach-to-driver assignment
        for your organization based on the parameters passed in. This endpoint should
        only be used for existing Coach to Driver assignments. In order to remove a
        driver-coach-assignment for a given driver, set coachId to null

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Coaching** under the Coaching category when
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
          driver_id: Required string ID of the driver. This is a unique Samsara ID of a driver.

          coach_id: Optional string ID of the coach. This is a unique Samsara user ID. If not
              provided, existing coach assignment will be removed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/coaching/driver-coach-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "driver_id": driver_id,
                        "coach_id": coach_id,
                    },
                    driver_coach_assignment_update_params.DriverCoachAssignmentUpdateParams,
                ),
            ),
            cast_to=DriverCoachAssignmentUpdateResponse,
        )

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        coach_ids: List[str] | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        include_external_ids: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverCoachAssignmentListResponse:
        """
        This endpoint will return coach assignments for your organization based on the
        parameters passed in. Results are paginated.

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Coaching** under the Coaching category when
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

          coach_ids: Optional string of comma separated IDs of the coaches.

          driver_ids: Optional string of comma separated IDs of the drivers. This can be either a
              unique Samsara driver ID or an external ID for the driver.

          include_external_ids: Optional boolean indicating whether to return external IDs on supported entities

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/coaching/driver-coach-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "coach_ids": coach_ids,
                        "driver_ids": driver_ids,
                        "include_external_ids": include_external_ids,
                    },
                    driver_coach_assignment_list_params.DriverCoachAssignmentListParams,
                ),
            ),
            cast_to=DriverCoachAssignmentListResponse,
        )


class DriverCoachAssignmentsResourceWithRawResponse:
    def __init__(self, driver_coach_assignments: DriverCoachAssignmentsResource) -> None:
        self._driver_coach_assignments = driver_coach_assignments

        self.update = to_raw_response_wrapper(
            driver_coach_assignments.update,
        )
        self.list = to_raw_response_wrapper(
            driver_coach_assignments.list,
        )


class AsyncDriverCoachAssignmentsResourceWithRawResponse:
    def __init__(self, driver_coach_assignments: AsyncDriverCoachAssignmentsResource) -> None:
        self._driver_coach_assignments = driver_coach_assignments

        self.update = async_to_raw_response_wrapper(
            driver_coach_assignments.update,
        )
        self.list = async_to_raw_response_wrapper(
            driver_coach_assignments.list,
        )


class DriverCoachAssignmentsResourceWithStreamingResponse:
    def __init__(self, driver_coach_assignments: DriverCoachAssignmentsResource) -> None:
        self._driver_coach_assignments = driver_coach_assignments

        self.update = to_streamed_response_wrapper(
            driver_coach_assignments.update,
        )
        self.list = to_streamed_response_wrapper(
            driver_coach_assignments.list,
        )


class AsyncDriverCoachAssignmentsResourceWithStreamingResponse:
    def __init__(self, driver_coach_assignments: AsyncDriverCoachAssignmentsResource) -> None:
        self._driver_coach_assignments = driver_coach_assignments

        self.update = async_to_streamed_response_wrapper(
            driver_coach_assignments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            driver_coach_assignments.list,
        )
