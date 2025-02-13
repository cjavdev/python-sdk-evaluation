# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import issue_list_params, issue_stream_params, issue_update_params
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
from ..types.issues_get_issues_response_body import IssuesGetIssuesResponseBody
from ..types.issues_patch_issue_response_body import IssuesPatchIssueResponseBody
from ..types.issues_get_issues_stream_response_body import IssuesGetIssuesStreamResponseBody

__all__ = ["IssuesResource", "AsyncIssuesResource"]


class IssuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IssuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return IssuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IssuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return IssuesResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        id: str,
        assigned_to: issue_update_params.AssignedTo | NotGiven = NOT_GIVEN,
        due_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        status: Literal["open", "inProgress", "resolved", "dismissed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IssuesPatchIssueResponseBody:
        """
        Updates an instance of an issue.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Issues** under the Closed Beta category
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
          id: ID of the issue. Can be either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the issue.

          assigned_to: Issue assignee update object

          due_date: Due date of the issue. UTC timestamp in RFC 3339 format.

          external_ids: A map of external ids

          status: Status of the issue. Valid values: `open`, `inProgress`, `resolved`, `dismissed`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/issues",
            body=maybe_transform(
                {
                    "id": id,
                    "assigned_to": assigned_to,
                    "due_date": due_date,
                    "external_ids": external_ids,
                    "status": status,
                },
                issue_update_params.IssueUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuesPatchIssueResponseBody,
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
    ) -> IssuesGetIssuesResponseBody:
        """
        Returns all issues data for the specified IDs.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Issues** under the Closed Beta category when
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
          ids: A comma-separated list containing up to 100 issue IDs to filter on. Can be
              either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the issue.

          include: A comma separated list of additional fields to include on requested objects.
              Valid values: `externalIds`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/issues",
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
                    issue_list_params.IssueListParams,
                ),
            ),
            cast_to=IssuesGetIssuesResponseBody,
        )

    def stream(
        self,
        *,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        asset_ids: List[str] | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        include: List[str] | NotGiven = NOT_GIVEN,
        status: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IssuesGetIssuesStreamResponseBody:
        """
        Returns all issues data that has been created or modified for your organization
        based on the time parameters passed in. Results are paginated and are sorted by
        last modified date. If you include an endTime, the endpoint will return data up
        until that point (exclusive). If you don’t include an endTime, you can continue
        to poll the API real-time with the pagination cursor that gets returned on every
        call.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Issues** under the Closed Beta category when
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
          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          asset_ids: A comma-separated list containing up to 50 asset IDs to filter issues on. Issues
              with untracked assets can also be included by passing the value: 'untracked'.

          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          include: A comma separated list of additional fields to include on requested objects.
              Valid values: `externalIds`

          status: A comma-separated list containing status values to filter issues on. Valid
              values: `open`, `inProgress`, `resolved`, `dismissed`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/issues/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "after": after,
                        "asset_ids": asset_ids,
                        "end_time": end_time,
                        "include": include,
                        "status": status,
                    },
                    issue_stream_params.IssueStreamParams,
                ),
            ),
            cast_to=IssuesGetIssuesStreamResponseBody,
        )


class AsyncIssuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIssuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIssuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIssuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncIssuesResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        id: str,
        assigned_to: issue_update_params.AssignedTo | NotGiven = NOT_GIVEN,
        due_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        status: Literal["open", "inProgress", "resolved", "dismissed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IssuesPatchIssueResponseBody:
        """
        Updates an instance of an issue.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Issues** under the Closed Beta category
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
          id: ID of the issue. Can be either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the issue.

          assigned_to: Issue assignee update object

          due_date: Due date of the issue. UTC timestamp in RFC 3339 format.

          external_ids: A map of external ids

          status: Status of the issue. Valid values: `open`, `inProgress`, `resolved`, `dismissed`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/issues",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "assigned_to": assigned_to,
                    "due_date": due_date,
                    "external_ids": external_ids,
                    "status": status,
                },
                issue_update_params.IssueUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IssuesPatchIssueResponseBody,
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
    ) -> IssuesGetIssuesResponseBody:
        """
        Returns all issues data for the specified IDs.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Issues** under the Closed Beta category when
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
          ids: A comma-separated list containing up to 100 issue IDs to filter on. Can be
              either a unique Samsara ID or an
              [external ID](https://developers.samsara.com/docs/external-ids) for the issue.

          include: A comma separated list of additional fields to include on requested objects.
              Valid values: `externalIds`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/issues",
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
                    issue_list_params.IssueListParams,
                ),
            ),
            cast_to=IssuesGetIssuesResponseBody,
        )

    async def stream(
        self,
        *,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        asset_ids: List[str] | NotGiven = NOT_GIVEN,
        end_time: str | NotGiven = NOT_GIVEN,
        include: List[str] | NotGiven = NOT_GIVEN,
        status: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IssuesGetIssuesStreamResponseBody:
        """
        Returns all issues data that has been created or modified for your organization
        based on the time parameters passed in. Results are paginated and are sorted by
        last modified date. If you include an endTime, the endpoint will return data up
        until that point (exclusive). If you don’t include an endTime, you can continue
        to poll the API real-time with the pagination cursor that gets returned on every
        call.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Issues** under the Closed Beta category when
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
          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          asset_ids: A comma-separated list containing up to 50 asset IDs to filter issues on. Issues
              with untracked assets can also be included by passing the value: 'untracked'.

          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          include: A comma separated list of additional fields to include on requested objects.
              Valid values: `externalIds`

          status: A comma-separated list containing status values to filter issues on. Valid
              values: `open`, `inProgress`, `resolved`, `dismissed`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/issues/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "after": after,
                        "asset_ids": asset_ids,
                        "end_time": end_time,
                        "include": include,
                        "status": status,
                    },
                    issue_stream_params.IssueStreamParams,
                ),
            ),
            cast_to=IssuesGetIssuesStreamResponseBody,
        )


class IssuesResourceWithRawResponse:
    def __init__(self, issues: IssuesResource) -> None:
        self._issues = issues

        self.update = to_raw_response_wrapper(
            issues.update,
        )
        self.list = to_raw_response_wrapper(
            issues.list,
        )
        self.stream = to_raw_response_wrapper(
            issues.stream,
        )


class AsyncIssuesResourceWithRawResponse:
    def __init__(self, issues: AsyncIssuesResource) -> None:
        self._issues = issues

        self.update = async_to_raw_response_wrapper(
            issues.update,
        )
        self.list = async_to_raw_response_wrapper(
            issues.list,
        )
        self.stream = async_to_raw_response_wrapper(
            issues.stream,
        )


class IssuesResourceWithStreamingResponse:
    def __init__(self, issues: IssuesResource) -> None:
        self._issues = issues

        self.update = to_streamed_response_wrapper(
            issues.update,
        )
        self.list = to_streamed_response_wrapper(
            issues.list,
        )
        self.stream = to_streamed_response_wrapper(
            issues.stream,
        )


class AsyncIssuesResourceWithStreamingResponse:
    def __init__(self, issues: AsyncIssuesResource) -> None:
        self._issues = issues

        self.update = async_to_streamed_response_wrapper(
            issues.update,
        )
        self.list = async_to_streamed_response_wrapper(
            issues.list,
        )
        self.stream = async_to_streamed_response_wrapper(
            issues.stream,
        )
