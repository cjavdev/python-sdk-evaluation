# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    form_submission_list_params,
    form_submission_create_params,
    form_submission_stream_params,
    form_submission_update_params,
)
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
from .pdf_exports import (
    PdfExportsResource,
    AsyncPdfExportsResource,
    PdfExportsResourceWithRawResponse,
    AsyncPdfExportsResourceWithRawResponse,
    PdfExportsResourceWithStreamingResponse,
    AsyncPdfExportsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.form_submission_stream_response import FormSubmissionStreamResponse
from ...types.form_submissions_get_form_submissions_response_body import FormSubmissionsGetFormSubmissionsResponseBody
from ...types.form_submissions_post_form_submission_response_body import FormSubmissionsPostFormSubmissionResponseBody
from ...types.form_submissions_patch_form_submission_response_body import FormSubmissionsPatchFormSubmissionResponseBody

__all__ = ["FormSubmissionsResource", "AsyncFormSubmissionsResource"]


class FormSubmissionsResource(SyncAPIResource):
    @cached_property
    def pdf_exports(self) -> PdfExportsResource:
        return PdfExportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FormSubmissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return FormSubmissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FormSubmissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return FormSubmissionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        form_template: form_submission_create_params.FormTemplate,
        status: Literal["toDo"],
        assigned_to: form_submission_create_params.AssignedTo | NotGiven = NOT_GIVEN,
        due_at_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        fields: Iterable[form_submission_create_params.Field] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormSubmissionsPostFormSubmissionResponseBody:
        """
        Creates a form submission.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Form Submissions** under the Closed Beta
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
          form_template: Form template reference object.

          status: Status of the form submission. Valid values: `toDo`

          assigned_to: Form submission assignee update object

          due_at_time: Due date of the form submission. UTC timestamp in RFC 3339 format.

          fields: List of field inputs in a form submission.

          title: Title of the form submission.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/form-submissions",
            body=maybe_transform(
                {
                    "form_template": form_template,
                    "status": status,
                    "assigned_to": assigned_to,
                    "due_at_time": due_at_time,
                    "fields": fields,
                    "title": title,
                },
                form_submission_create_params.FormSubmissionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormSubmissionsPostFormSubmissionResponseBody,
        )

    def update(
        self,
        *,
        id: str,
        assigned_to: form_submission_update_params.AssignedTo | NotGiven = NOT_GIVEN,
        due_at_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: Literal["toDo", "dismissed"] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormSubmissionsPatchFormSubmissionResponseBody:
        """
        Updates an instance of a form submission.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Form Submissions** under the Closed Beta
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
          id: ID of the form submission.

          assigned_to: Form submission assignee update object

          due_at_time: Due date of the form submission. UTC timestamp in RFC 3339 format.

          status: Status of the form submission. Valid values: `toDo`, `dismissed`

          title: Title of the form submission.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/form-submissions",
            body=maybe_transform(
                {
                    "id": id,
                    "assigned_to": assigned_to,
                    "due_at_time": due_at_time,
                    "status": status,
                    "title": title,
                },
                form_submission_update_params.FormSubmissionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormSubmissionsPatchFormSubmissionResponseBody,
        )

    def list(
        self,
        *,
        ids: List[str],
        include: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormSubmissionsGetFormSubmissionsResponseBody:
        """
        Returns all form submissions data for the specified IDs.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Form Submissions** under the Closed Beta
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
          ids: A comma-separated list containing up to 100 form submission IDs to filter on.
              Can be either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the form
              submission.

          include: A comma-separated list of strings indicating whether to return additional
              information. Valid values: `externalIds`, `fieldLabels`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/form-submissions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "include": include,
                    },
                    form_submission_list_params.FormSubmissionListParams,
                ),
            ),
            cast_to=FormSubmissionsGetFormSubmissionsResponseBody,
        )

    def stream(
        self,
        *,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        form_template_ids: List[str] | NotGiven = NOT_GIVEN,
        include: List[str] | NotGiven = NOT_GIVEN,
        user_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormSubmissionStreamResponse:
        """
        Returns all form submissions data that has been created or modified for your
        organization based on the time parameters passed in. Results are paginated and
        are sorted by last modified date. If you include an endTime, the endpoint will
        return data up until that point (exclusive). If you don’t include an endTime,
        you can continue to poll the API real-time with the pagination cursor that gets
        returned on every call.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Form Submissions** under the Closed Beta
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

          driver_ids: A comma-separated list containing up to 50 user IDs to filter data to.

          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          form_template_ids: A comma-separated list containing up to 50 template IDs to filter data to.

          include: A comma-separated list of strings indicating whether to return additional
              information. Valid values: `externalIds`, `fieldLabels`

          user_ids: A comma-separated list containing up to 50 user IDs to filter data to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/form-submissions/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "after": after,
                        "driver_ids": driver_ids,
                        "end_time": end_time,
                        "form_template_ids": form_template_ids,
                        "include": include,
                        "user_ids": user_ids,
                    },
                    form_submission_stream_params.FormSubmissionStreamParams,
                ),
            ),
            cast_to=FormSubmissionStreamResponse,
        )


class AsyncFormSubmissionsResource(AsyncAPIResource):
    @cached_property
    def pdf_exports(self) -> AsyncPdfExportsResource:
        return AsyncPdfExportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFormSubmissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFormSubmissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFormSubmissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncFormSubmissionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        form_template: form_submission_create_params.FormTemplate,
        status: Literal["toDo"],
        assigned_to: form_submission_create_params.AssignedTo | NotGiven = NOT_GIVEN,
        due_at_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        fields: Iterable[form_submission_create_params.Field] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormSubmissionsPostFormSubmissionResponseBody:
        """
        Creates a form submission.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Form Submissions** under the Closed Beta
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
          form_template: Form template reference object.

          status: Status of the form submission. Valid values: `toDo`

          assigned_to: Form submission assignee update object

          due_at_time: Due date of the form submission. UTC timestamp in RFC 3339 format.

          fields: List of field inputs in a form submission.

          title: Title of the form submission.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/form-submissions",
            body=await async_maybe_transform(
                {
                    "form_template": form_template,
                    "status": status,
                    "assigned_to": assigned_to,
                    "due_at_time": due_at_time,
                    "fields": fields,
                    "title": title,
                },
                form_submission_create_params.FormSubmissionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormSubmissionsPostFormSubmissionResponseBody,
        )

    async def update(
        self,
        *,
        id: str,
        assigned_to: form_submission_update_params.AssignedTo | NotGiven = NOT_GIVEN,
        due_at_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: Literal["toDo", "dismissed"] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormSubmissionsPatchFormSubmissionResponseBody:
        """
        Updates an instance of a form submission.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Form Submissions** under the Closed Beta
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
          id: ID of the form submission.

          assigned_to: Form submission assignee update object

          due_at_time: Due date of the form submission. UTC timestamp in RFC 3339 format.

          status: Status of the form submission. Valid values: `toDo`, `dismissed`

          title: Title of the form submission.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/form-submissions",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "assigned_to": assigned_to,
                    "due_at_time": due_at_time,
                    "status": status,
                    "title": title,
                },
                form_submission_update_params.FormSubmissionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormSubmissionsPatchFormSubmissionResponseBody,
        )

    async def list(
        self,
        *,
        ids: List[str],
        include: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormSubmissionsGetFormSubmissionsResponseBody:
        """
        Returns all form submissions data for the specified IDs.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Form Submissions** under the Closed Beta
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
          ids: A comma-separated list containing up to 100 form submission IDs to filter on.
              Can be either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the form
              submission.

          include: A comma-separated list of strings indicating whether to return additional
              information. Valid values: `externalIds`, `fieldLabels`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/form-submissions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ids": ids,
                        "include": include,
                    },
                    form_submission_list_params.FormSubmissionListParams,
                ),
            ),
            cast_to=FormSubmissionsGetFormSubmissionsResponseBody,
        )

    async def stream(
        self,
        *,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        form_template_ids: List[str] | NotGiven = NOT_GIVEN,
        include: List[str] | NotGiven = NOT_GIVEN,
        user_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormSubmissionStreamResponse:
        """
        Returns all form submissions data that has been created or modified for your
        organization based on the time parameters passed in. Results are paginated and
        are sorted by last modified date. If you include an endTime, the endpoint will
        return data up until that point (exclusive). If you don’t include an endTime,
        you can continue to poll the API real-time with the pagination cursor that gets
        returned on every call.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Form Submissions** under the Closed Beta
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

          driver_ids: A comma-separated list containing up to 50 user IDs to filter data to.

          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          form_template_ids: A comma-separated list containing up to 50 template IDs to filter data to.

          include: A comma-separated list of strings indicating whether to return additional
              information. Valid values: `externalIds`, `fieldLabels`

          user_ids: A comma-separated list containing up to 50 user IDs to filter data to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/form-submissions/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "after": after,
                        "driver_ids": driver_ids,
                        "end_time": end_time,
                        "form_template_ids": form_template_ids,
                        "include": include,
                        "user_ids": user_ids,
                    },
                    form_submission_stream_params.FormSubmissionStreamParams,
                ),
            ),
            cast_to=FormSubmissionStreamResponse,
        )


class FormSubmissionsResourceWithRawResponse:
    def __init__(self, form_submissions: FormSubmissionsResource) -> None:
        self._form_submissions = form_submissions

        self.create = to_raw_response_wrapper(
            form_submissions.create,
        )
        self.update = to_raw_response_wrapper(
            form_submissions.update,
        )
        self.list = to_raw_response_wrapper(
            form_submissions.list,
        )
        self.stream = to_raw_response_wrapper(
            form_submissions.stream,
        )

    @cached_property
    def pdf_exports(self) -> PdfExportsResourceWithRawResponse:
        return PdfExportsResourceWithRawResponse(self._form_submissions.pdf_exports)


class AsyncFormSubmissionsResourceWithRawResponse:
    def __init__(self, form_submissions: AsyncFormSubmissionsResource) -> None:
        self._form_submissions = form_submissions

        self.create = async_to_raw_response_wrapper(
            form_submissions.create,
        )
        self.update = async_to_raw_response_wrapper(
            form_submissions.update,
        )
        self.list = async_to_raw_response_wrapper(
            form_submissions.list,
        )
        self.stream = async_to_raw_response_wrapper(
            form_submissions.stream,
        )

    @cached_property
    def pdf_exports(self) -> AsyncPdfExportsResourceWithRawResponse:
        return AsyncPdfExportsResourceWithRawResponse(self._form_submissions.pdf_exports)


class FormSubmissionsResourceWithStreamingResponse:
    def __init__(self, form_submissions: FormSubmissionsResource) -> None:
        self._form_submissions = form_submissions

        self.create = to_streamed_response_wrapper(
            form_submissions.create,
        )
        self.update = to_streamed_response_wrapper(
            form_submissions.update,
        )
        self.list = to_streamed_response_wrapper(
            form_submissions.list,
        )
        self.stream = to_streamed_response_wrapper(
            form_submissions.stream,
        )

    @cached_property
    def pdf_exports(self) -> PdfExportsResourceWithStreamingResponse:
        return PdfExportsResourceWithStreamingResponse(self._form_submissions.pdf_exports)


class AsyncFormSubmissionsResourceWithStreamingResponse:
    def __init__(self, form_submissions: AsyncFormSubmissionsResource) -> None:
        self._form_submissions = form_submissions

        self.create = async_to_streamed_response_wrapper(
            form_submissions.create,
        )
        self.update = async_to_streamed_response_wrapper(
            form_submissions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            form_submissions.list,
        )
        self.stream = async_to_streamed_response_wrapper(
            form_submissions.stream,
        )

    @cached_property
    def pdf_exports(self) -> AsyncPdfExportsResourceWithStreamingResponse:
        return AsyncPdfExportsResourceWithStreamingResponse(self._form_submissions.pdf_exports)
