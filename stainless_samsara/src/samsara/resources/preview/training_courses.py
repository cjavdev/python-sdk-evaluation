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
from ...types.preview import training_course_list_params
from ...types.preview.training_courses_get_training_courses_response_body import (
    TrainingCoursesGetTrainingCoursesResponseBody,
)

__all__ = ["TrainingCoursesResource", "AsyncTrainingCoursesResource"]


class TrainingCoursesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrainingCoursesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return TrainingCoursesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrainingCoursesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return TrainingCoursesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        category_ids: List[str] | NotGiven = NOT_GIVEN,
        course_ids: List[str] | NotGiven = NOT_GIVEN,
        status: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingCoursesGetTrainingCoursesResponseBody:
        """Returns all training courses data.

        Results are paginated. Courses in the ‘draft’
        status are excluded from the data returned by this endpoint.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Preview** under the category when creating
        or editing an API token.
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
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          category_ids: Optional string of comma separated course category IDs. If courseCategoryId is
              present, training courses for the specified course category(s) will be returned.
              Max value for this value is 100 objects. Defaults to returning all courses.
              Example:
              `categoryIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`

          course_ids: Optional string of comma separated course IDs. If course ID is present, training
              assignments for the specified course ID(s) will be returned. Max value for this
              value is 100 objects. Defaults to returning all courses. Example:
              `courseIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`

          status: Optional string of comma separated values. If status is present, training
              courses with the specified status(s) will be returned. Valid values:
              “published”, “deleted”, “archived”. Defaults to returning all courses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/preview/training-courses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "category_ids": category_ids,
                        "course_ids": course_ids,
                        "status": status,
                    },
                    training_course_list_params.TrainingCourseListParams,
                ),
            ),
            cast_to=TrainingCoursesGetTrainingCoursesResponseBody,
        )


class AsyncTrainingCoursesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrainingCoursesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrainingCoursesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrainingCoursesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncTrainingCoursesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        category_ids: List[str] | NotGiven = NOT_GIVEN,
        course_ids: List[str] | NotGiven = NOT_GIVEN,
        status: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrainingCoursesGetTrainingCoursesResponseBody:
        """Returns all training courses data.

        Results are paginated. Courses in the ‘draft’
        status are excluded from the data returned by this endpoint.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Preview** under the category when creating
        or editing an API token.
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
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          category_ids: Optional string of comma separated course category IDs. If courseCategoryId is
              present, training courses for the specified course category(s) will be returned.
              Max value for this value is 100 objects. Defaults to returning all courses.
              Example:
              `categoryIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`

          course_ids: Optional string of comma separated course IDs. If course ID is present, training
              assignments for the specified course ID(s) will be returned. Max value for this
              value is 100 objects. Defaults to returning all courses. Example:
              `courseIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`

          status: Optional string of comma separated values. If status is present, training
              courses with the specified status(s) will be returned. Valid values:
              “published”, “deleted”, “archived”. Defaults to returning all courses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/preview/training-courses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "category_ids": category_ids,
                        "course_ids": course_ids,
                        "status": status,
                    },
                    training_course_list_params.TrainingCourseListParams,
                ),
            ),
            cast_to=TrainingCoursesGetTrainingCoursesResponseBody,
        )


class TrainingCoursesResourceWithRawResponse:
    def __init__(self, training_courses: TrainingCoursesResource) -> None:
        self._training_courses = training_courses

        self.list = to_raw_response_wrapper(
            training_courses.list,
        )


class AsyncTrainingCoursesResourceWithRawResponse:
    def __init__(self, training_courses: AsyncTrainingCoursesResource) -> None:
        self._training_courses = training_courses

        self.list = async_to_raw_response_wrapper(
            training_courses.list,
        )


class TrainingCoursesResourceWithStreamingResponse:
    def __init__(self, training_courses: TrainingCoursesResource) -> None:
        self._training_courses = training_courses

        self.list = to_streamed_response_wrapper(
            training_courses.list,
        )


class AsyncTrainingCoursesResourceWithStreamingResponse:
    def __init__(self, training_courses: AsyncTrainingCoursesResource) -> None:
        self._training_courses = training_courses

        self.list = async_to_streamed_response_wrapper(
            training_courses.list,
        )
