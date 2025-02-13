# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import training_assignment_create_params, training_assignment_stream_params
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
from ..types.training_assignments_post_training_assignments_response_body import (
    TrainingAssignmentsPostTrainingAssignmentsResponseBody,
)
from ..types.training_assignments_get_training_assignments_stream_response_body import (
    TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody,
)

__all__ = ["TrainingAssignmentsResource", "AsyncTrainingAssignmentsResource"]


class TrainingAssignmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrainingAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return TrainingAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrainingAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return TrainingAssignmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        course_id: str,
        due_at_time: str,
        learner_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingAssignmentsPostTrainingAssignmentsResponseBody:
        """Create training assignments.

        Existing assignments will remain unchanged.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Training APIs
        enabled for your organization.

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Training Assignments** under the Closed
        Beta category when creating or editing an API token.
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
          course_id: String for the course ID.

          due_at_time: Due date of the training assignment in RFC 3339 format. Millisecond precision
              and timezones are supported.

          learner_ids: Optional string of comma separated learner IDs. If learner ID is present,
              training assignments for the specified learner(s) will be returned. Max value
              for this value is 100 objects. Example:
              `learnerIds=driver-281474,driver-46282156`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/training-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "course_id": course_id,
                        "due_at_time": due_at_time,
                        "learner_ids": learner_ids,
                    },
                    training_assignment_create_params.TrainingAssignmentCreateParams,
                ),
            ),
            cast_to=TrainingAssignmentsPostTrainingAssignmentsResponseBody,
        )

    def stream(
        self,
        *,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        course_ids: List[str] | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        learner_ids: List[str] | NotGiven = NOT_GIVEN,
        status: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody:
        """
        Returns all training assignments data that has been created or modified for your
        organization based on the time parameters passed in. Results are paginated and
        are sorted by last modified date. If you include an endTime, the endpoint will
        return data up until that point (exclusive). If you don't include an endTime,
        you can continue to poll the API real-time with the pagination cursor that gets
        returned on every call.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Training APIs
        enabled for your organization.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Training Assignments** under the Closed Beta
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
          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          course_ids: Optional string of comma separated course IDs. If course ID is present, training
              assignments for the specified course ID(s) will be returned. Max value for this
              value is 100 objects. Defaults to returning all courses. Example:
              `courseIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`

          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          learner_ids: Optional string of comma separated learner IDs. If learner ID is present,
              training assignments for the specified learner(s) will be returned. Max value
              for this value is 100 objects. Example:
              `learnerIds=driver-281474,driver-46282156`

          status: Optional string of comma separated values. If status is present, training
              assignments for the specified status(s) will be returned. Valid values:
              "notStarted", "inProgress", "completed". Defaults to returning all courses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/training-assignments/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "after": after,
                        "course_ids": course_ids,
                        "end_time": end_time,
                        "learner_ids": learner_ids,
                        "status": status,
                    },
                    training_assignment_stream_params.TrainingAssignmentStreamParams,
                ),
            ),
            cast_to=TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody,
        )


class AsyncTrainingAssignmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrainingAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrainingAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrainingAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncTrainingAssignmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        course_id: str,
        due_at_time: str,
        learner_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingAssignmentsPostTrainingAssignmentsResponseBody:
        """Create training assignments.

        Existing assignments will remain unchanged.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Training APIs
        enabled for your organization.

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Training Assignments** under the Closed
        Beta category when creating or editing an API token.
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
          course_id: String for the course ID.

          due_at_time: Due date of the training assignment in RFC 3339 format. Millisecond precision
              and timezones are supported.

          learner_ids: Optional string of comma separated learner IDs. If learner ID is present,
              training assignments for the specified learner(s) will be returned. Max value
              for this value is 100 objects. Example:
              `learnerIds=driver-281474,driver-46282156`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/training-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "course_id": course_id,
                        "due_at_time": due_at_time,
                        "learner_ids": learner_ids,
                    },
                    training_assignment_create_params.TrainingAssignmentCreateParams,
                ),
            ),
            cast_to=TrainingAssignmentsPostTrainingAssignmentsResponseBody,
        )

    async def stream(
        self,
        *,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        course_ids: List[str] | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        learner_ids: List[str] | NotGiven = NOT_GIVEN,
        status: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody:
        """
        Returns all training assignments data that has been created or modified for your
        organization based on the time parameters passed in. Results are paginated and
        are sorted by last modified date. If you include an endTime, the endpoint will
        return data up until that point (exclusive). If you don't include an endTime,
        you can continue to poll the API real-time with the pagination cursor that gets
        returned on every call.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Training APIs
        enabled for your organization.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Training Assignments** under the Closed Beta
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
          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          course_ids: Optional string of comma separated course IDs. If course ID is present, training
              assignments for the specified course ID(s) will be returned. Max value for this
              value is 100 objects. Defaults to returning all courses. Example:
              `courseIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`

          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          learner_ids: Optional string of comma separated learner IDs. If learner ID is present,
              training assignments for the specified learner(s) will be returned. Max value
              for this value is 100 objects. Example:
              `learnerIds=driver-281474,driver-46282156`

          status: Optional string of comma separated values. If status is present, training
              assignments for the specified status(s) will be returned. Valid values:
              "notStarted", "inProgress", "completed". Defaults to returning all courses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/training-assignments/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "after": after,
                        "course_ids": course_ids,
                        "end_time": end_time,
                        "learner_ids": learner_ids,
                        "status": status,
                    },
                    training_assignment_stream_params.TrainingAssignmentStreamParams,
                ),
            ),
            cast_to=TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody,
        )


class TrainingAssignmentsResourceWithRawResponse:
    def __init__(self, training_assignments: TrainingAssignmentsResource) -> None:
        self._training_assignments = training_assignments

        self.create = to_raw_response_wrapper(
            training_assignments.create,
        )
        self.stream = to_raw_response_wrapper(
            training_assignments.stream,
        )


class AsyncTrainingAssignmentsResourceWithRawResponse:
    def __init__(self, training_assignments: AsyncTrainingAssignmentsResource) -> None:
        self._training_assignments = training_assignments

        self.create = async_to_raw_response_wrapper(
            training_assignments.create,
        )
        self.stream = async_to_raw_response_wrapper(
            training_assignments.stream,
        )


class TrainingAssignmentsResourceWithStreamingResponse:
    def __init__(self, training_assignments: TrainingAssignmentsResource) -> None:
        self._training_assignments = training_assignments

        self.create = to_streamed_response_wrapper(
            training_assignments.create,
        )
        self.stream = to_streamed_response_wrapper(
            training_assignments.stream,
        )


class AsyncTrainingAssignmentsResourceWithStreamingResponse:
    def __init__(self, training_assignments: AsyncTrainingAssignmentsResource) -> None:
        self._training_assignments = training_assignments

        self.create = async_to_streamed_response_wrapper(
            training_assignments.create,
        )
        self.stream = async_to_streamed_response_wrapper(
            training_assignments.stream,
        )
