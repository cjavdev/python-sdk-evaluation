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
from ...types.trailers import assignment_list_params, assignment_retrieve_params
from ...types.fleet.trailers.inline_response_200_7 import InlineResponse200_7
from ...types.fleet.trailers.v1_trailer_assignments_response import V1TrailerAssignmentsResponse

__all__ = ["AssignmentsResource", "AsyncAssignmentsResource"]


class AssignmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AssignmentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        trailer_id: int,
        *,
        end_ms: int | NotGiven = NOT_GIVEN,
        start_ms: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1TrailerAssignmentsResponse:
        """
        <n class="warning">
        <nh>
        <i class="fa fa-exclamation-circle"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Fetch trailer assignment data for a single trailer.

        <b>Rate limit:</b> 100 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Assignments** under the Assignments category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          end_ms: Timestamp in Unix epoch milliseconds representing the end of the period to
              fetch. Omitting endMs sets endMs as the current time

          start_ms: Timestamp in Unix epoch milliseconds representing the start of the period to
              fetch. Omitting both startMs and endMs only returns current assignments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v1/fleet/trailers/{trailer_id}/assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_ms": end_ms,
                        "start_ms": start_ms,
                    },
                    assignment_retrieve_params.AssignmentRetrieveParams,
                ),
            ),
            cast_to=V1TrailerAssignmentsResponse,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        end_ms: int | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        start_ms: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InlineResponse200_7:
        """
        <n class="warning">
        <nh>
        <i class="fa fa-exclamation-circle"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Fetch trailer assignment data for all trailers in your organization.

        <b>Rate limit:</b> 100 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Assignments** under the Assignments category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          ending_before: Pagination parameter indicating the cursor position to return results before.
              Used in conjunction with the 'limit' parameter. Mutually exclusive with
              'startingAfter' parameter.

          end_ms: Timestamp in Unix epoch miliseconds representing the end of the period to fetch.
              Omitting endMs sets endMs as the current time

          limit: Pagination parameter indicating the number of results to return in this request.
              Used in conjunction with either 'startingAfter' or 'endingBefore'.

          starting_after: Pagination parameter indicating the cursor position to continue returning
              results after. Used in conjunction with the 'limit' parameter. Mutually
              exclusive with 'endingBefore' parameter.

          start_ms: Timestamp in Unix epoch miliseconds representing the start of the period to
              fetch. Omitting both startMs and endMs only returns current assignments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/fleet/trailers/assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "end_ms": end_ms,
                        "limit": limit,
                        "starting_after": starting_after,
                        "start_ms": start_ms,
                    },
                    assignment_list_params.AssignmentListParams,
                ),
            ),
            cast_to=InlineResponse200_7,
        )


class AsyncAssignmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncAssignmentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        trailer_id: int,
        *,
        end_ms: int | NotGiven = NOT_GIVEN,
        start_ms: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1TrailerAssignmentsResponse:
        """
        <n class="warning">
        <nh>
        <i class="fa fa-exclamation-circle"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Fetch trailer assignment data for a single trailer.

        <b>Rate limit:</b> 100 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Assignments** under the Assignments category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          end_ms: Timestamp in Unix epoch milliseconds representing the end of the period to
              fetch. Omitting endMs sets endMs as the current time

          start_ms: Timestamp in Unix epoch milliseconds representing the start of the period to
              fetch. Omitting both startMs and endMs only returns current assignments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v1/fleet/trailers/{trailer_id}/assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_ms": end_ms,
                        "start_ms": start_ms,
                    },
                    assignment_retrieve_params.AssignmentRetrieveParams,
                ),
            ),
            cast_to=V1TrailerAssignmentsResponse,
        )

    async def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        end_ms: int | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        start_ms: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InlineResponse200_7:
        """
        <n class="warning">
        <nh>
        <i class="fa fa-exclamation-circle"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Fetch trailer assignment data for all trailers in your organization.

        <b>Rate limit:</b> 100 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Assignments** under the Assignments category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          ending_before: Pagination parameter indicating the cursor position to return results before.
              Used in conjunction with the 'limit' parameter. Mutually exclusive with
              'startingAfter' parameter.

          end_ms: Timestamp in Unix epoch miliseconds representing the end of the period to fetch.
              Omitting endMs sets endMs as the current time

          limit: Pagination parameter indicating the number of results to return in this request.
              Used in conjunction with either 'startingAfter' or 'endingBefore'.

          starting_after: Pagination parameter indicating the cursor position to continue returning
              results after. Used in conjunction with the 'limit' parameter. Mutually
              exclusive with 'endingBefore' parameter.

          start_ms: Timestamp in Unix epoch miliseconds representing the start of the period to
              fetch. Omitting both startMs and endMs only returns current assignments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/fleet/trailers/assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ending_before": ending_before,
                        "end_ms": end_ms,
                        "limit": limit,
                        "starting_after": starting_after,
                        "start_ms": start_ms,
                    },
                    assignment_list_params.AssignmentListParams,
                ),
            ),
            cast_to=InlineResponse200_7,
        )


class AssignmentsResourceWithRawResponse:
    def __init__(self, assignments: AssignmentsResource) -> None:
        self._assignments = assignments

        self.retrieve = to_raw_response_wrapper(
            assignments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            assignments.list,
        )


class AsyncAssignmentsResourceWithRawResponse:
    def __init__(self, assignments: AsyncAssignmentsResource) -> None:
        self._assignments = assignments

        self.retrieve = async_to_raw_response_wrapper(
            assignments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            assignments.list,
        )


class AssignmentsResourceWithStreamingResponse:
    def __init__(self, assignments: AssignmentsResource) -> None:
        self._assignments = assignments

        self.retrieve = to_streamed_response_wrapper(
            assignments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            assignments.list,
        )


class AsyncAssignmentsResourceWithStreamingResponse:
    def __init__(self, assignments: AsyncAssignmentsResource) -> None:
        self._assignments = assignments

        self.retrieve = async_to_streamed_response_wrapper(
            assignments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            assignments.list,
        )
