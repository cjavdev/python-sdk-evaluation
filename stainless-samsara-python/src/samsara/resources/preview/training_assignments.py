# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

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
from ..._base_client import make_request_options
from ...types.preview import training_assignment_delete_params, training_assignment_update_params
from ...types.preview.training_assignments_patch_training_assignments_response_body import (
    TrainingAssignmentsPatchTrainingAssignmentsResponseBody,
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

    def update(
        self,
        *,
        due_at_time: str,
        ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingAssignmentsPatchTrainingAssignmentsResponseBody:
        """
        **Preview:** This endpoint is in preview and is likely to change before being
        broadly available. Reach out to your Samsara Representative to have Training
        APIs enabled for your organization.

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Training Assignments** under the Closed
        Beta category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Endpoints in this section are in Preview. These APIs are not functional and are
        instead for soliciting feedback from our API users on the intended design of
        this API. Additionally, it is not guaranteed that we will be releasing an
        endpoint included in this section to production. This means that developers
        should **NOT** rely on these APIs to build business critical applications

        - Samsara may change the structure of a preview API's interface without
          versioning or any notice to API users.

        - When an endpoint becomes generally available, it will be announced in the API
          [changelog](https://developers.samsara.com/changelog).

          **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
          as feedback in our
          <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
          form</a>. If you encountered an issue or noticed inaccuracies in the API
          documentation, please
          <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to
          our support team.

        Args:
          due_at_time: Due date of the training assignment in RFC 3339 format. Millisecond precision
              and timezones are supported.

          ids: String of comma separated assignments IDs. Max value for this value is 100
              objects .Example:
              `ids=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/preview/training-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "due_at_time": due_at_time,
                        "ids": ids,
                    },
                    training_assignment_update_params.TrainingAssignmentUpdateParams,
                ),
            ),
            cast_to=TrainingAssignmentsPatchTrainingAssignmentsResponseBody,
        )

    def delete(
        self,
        *,
        ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """This endpoint supports batch deletion operations.

        The response does not indicate
        which specific deletions, if any, have failed. On a successful deletion or
        partial failure, a ‘204 No Content’ status is returned.

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Training Assignments** under the Closed
        Beta category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Endpoints in this section are in Preview. These APIs are not functional and are
        instead for soliciting feedback from our API users on the intended design of
        this API. Additionally, it is not guaranteed that we will be releasing an
        endpoint included in this section to production. This means that developers
        should **NOT** rely on these APIs to build business critical applications

        - Samsara may change the structure of a preview API's interface without
          versioning or any notice to API users.

        - When an endpoint becomes generally available, it will be announced in the API
          [changelog](https://developers.samsara.com/changelog).

          **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
          as feedback in our
          <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
          form</a>. If you encountered an issue or noticed inaccuracies in the API
          documentation, please
          <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to
          our support team.

        Args:
          ids: String of comma separated assignments IDs. Max value for this value is 100
              objects .Example:
              `ids=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/preview/training-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ids": ids}, training_assignment_delete_params.TrainingAssignmentDeleteParams),
            ),
            cast_to=NoneType,
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

    async def update(
        self,
        *,
        due_at_time: str,
        ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingAssignmentsPatchTrainingAssignmentsResponseBody:
        """
        **Preview:** This endpoint is in preview and is likely to change before being
        broadly available. Reach out to your Samsara Representative to have Training
        APIs enabled for your organization.

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Training Assignments** under the Closed
        Beta category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Endpoints in this section are in Preview. These APIs are not functional and are
        instead for soliciting feedback from our API users on the intended design of
        this API. Additionally, it is not guaranteed that we will be releasing an
        endpoint included in this section to production. This means that developers
        should **NOT** rely on these APIs to build business critical applications

        - Samsara may change the structure of a preview API's interface without
          versioning or any notice to API users.

        - When an endpoint becomes generally available, it will be announced in the API
          [changelog](https://developers.samsara.com/changelog).

          **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
          as feedback in our
          <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
          form</a>. If you encountered an issue or noticed inaccuracies in the API
          documentation, please
          <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to
          our support team.

        Args:
          due_at_time: Due date of the training assignment in RFC 3339 format. Millisecond precision
              and timezones are supported.

          ids: String of comma separated assignments IDs. Max value for this value is 100
              objects .Example:
              `ids=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/preview/training-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "due_at_time": due_at_time,
                        "ids": ids,
                    },
                    training_assignment_update_params.TrainingAssignmentUpdateParams,
                ),
            ),
            cast_to=TrainingAssignmentsPatchTrainingAssignmentsResponseBody,
        )

    async def delete(
        self,
        *,
        ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """This endpoint supports batch deletion operations.

        The response does not indicate
        which specific deletions, if any, have failed. On a successful deletion or
        partial failure, a ‘204 No Content’ status is returned.

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Training Assignments** under the Closed
        Beta category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Endpoints in this section are in Preview. These APIs are not functional and are
        instead for soliciting feedback from our API users on the intended design of
        this API. Additionally, it is not guaranteed that we will be releasing an
        endpoint included in this section to production. This means that developers
        should **NOT** rely on these APIs to build business critical applications

        - Samsara may change the structure of a preview API's interface without
          versioning or any notice to API users.

        - When an endpoint becomes generally available, it will be announced in the API
          [changelog](https://developers.samsara.com/changelog).

          **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
          as feedback in our
          <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
          form</a>. If you encountered an issue or noticed inaccuracies in the API
          documentation, please
          <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to
          our support team.

        Args:
          ids: String of comma separated assignments IDs. Max value for this value is 100
              objects .Example:
              `ids=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/preview/training-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"ids": ids}, training_assignment_delete_params.TrainingAssignmentDeleteParams
                ),
            ),
            cast_to=NoneType,
        )


class TrainingAssignmentsResourceWithRawResponse:
    def __init__(self, training_assignments: TrainingAssignmentsResource) -> None:
        self._training_assignments = training_assignments

        self.update = to_raw_response_wrapper(
            training_assignments.update,
        )
        self.delete = to_raw_response_wrapper(
            training_assignments.delete,
        )


class AsyncTrainingAssignmentsResourceWithRawResponse:
    def __init__(self, training_assignments: AsyncTrainingAssignmentsResource) -> None:
        self._training_assignments = training_assignments

        self.update = async_to_raw_response_wrapper(
            training_assignments.update,
        )
        self.delete = async_to_raw_response_wrapper(
            training_assignments.delete,
        )


class TrainingAssignmentsResourceWithStreamingResponse:
    def __init__(self, training_assignments: TrainingAssignmentsResource) -> None:
        self._training_assignments = training_assignments

        self.update = to_streamed_response_wrapper(
            training_assignments.update,
        )
        self.delete = to_streamed_response_wrapper(
            training_assignments.delete,
        )


class AsyncTrainingAssignmentsResourceWithStreamingResponse:
    def __init__(self, training_assignments: AsyncTrainingAssignmentsResource) -> None:
        self._training_assignments = training_assignments

        self.update = async_to_streamed_response_wrapper(
            training_assignments.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            training_assignments.delete,
        )
