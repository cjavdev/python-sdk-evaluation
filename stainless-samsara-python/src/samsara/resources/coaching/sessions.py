# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime

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
from ...types.coaching import session_stream_params
from ...types.coaching.session_stream_response import SessionStreamResponse

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def stream(
        self,
        *,
        start_time: Union[str, datetime],
        after: str | NotGiven = NOT_GIVEN,
        coach_ids: List[str] | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        include_coachable_events: bool | NotGiven = NOT_GIVEN,
        include_external_ids: bool | NotGiven = NOT_GIVEN,
        session_statuses: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionStreamResponse:
        """
        This endpoint will return coaching sessions for your organization based on the
        time parameters passed in. Results are paginated by sessions. If you include an
        endTime, the endpoint will return data up until that point. If you don’t include
        an endTime, you can continue to poll the API real-time with the pagination
        cursor that gets returned on every call.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
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
          start_time: Required RFC 3339 timestamp that indicates when to begin receiving data. Value
              is compared against `updatedAtTime`

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          coach_ids: Optional string of comma separated user IDs. If coach ID is present, sessions
              for the specified coach(s) will be returned for either assignedCoach or
              completedCoach. If both driverId(s) and coachId(s) are present, sessions with
              specified driver(s) and coach(es) will be returned.

          driver_ids: Optional string of comma separated driver IDs. If driver ID is present, sessions
              for the specified driver(s) will be returned.

          end_time: Optional RFC 3339 timestamp. If not provided then the endpoint behaves as an
              unending feed of changes. If endTime is set the same as startTime, the most
              recent data point before that time will be returned per asset. Value is compared
              against `updatedAtTime`

          include_coachable_events: Optional boolean to control whether behaviors will include coachableEvents in
              the response. Defaults to false.

          include_external_ids: Optional boolean indicating whether to return external IDs on supported entities

          session_statuses: Optional string of comma separated statuses. Valid values: “upcoming”,
              “completed”, “deleted”.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/coaching/sessions/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_time": start_time,
                        "after": after,
                        "coach_ids": coach_ids,
                        "driver_ids": driver_ids,
                        "end_time": end_time,
                        "include_coachable_events": include_coachable_events,
                        "include_external_ids": include_external_ids,
                        "session_statuses": session_statuses,
                    },
                    session_stream_params.SessionStreamParams,
                ),
            ),
            cast_to=SessionStreamResponse,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def stream(
        self,
        *,
        start_time: Union[str, datetime],
        after: str | NotGiven = NOT_GIVEN,
        coach_ids: List[str] | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        include_coachable_events: bool | NotGiven = NOT_GIVEN,
        include_external_ids: bool | NotGiven = NOT_GIVEN,
        session_statuses: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionStreamResponse:
        """
        This endpoint will return coaching sessions for your organization based on the
        time parameters passed in. Results are paginated by sessions. If you include an
        endTime, the endpoint will return data up until that point. If you don’t include
        an endTime, you can continue to poll the API real-time with the pagination
        cursor that gets returned on every call.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
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
          start_time: Required RFC 3339 timestamp that indicates when to begin receiving data. Value
              is compared against `updatedAtTime`

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          coach_ids: Optional string of comma separated user IDs. If coach ID is present, sessions
              for the specified coach(s) will be returned for either assignedCoach or
              completedCoach. If both driverId(s) and coachId(s) are present, sessions with
              specified driver(s) and coach(es) will be returned.

          driver_ids: Optional string of comma separated driver IDs. If driver ID is present, sessions
              for the specified driver(s) will be returned.

          end_time: Optional RFC 3339 timestamp. If not provided then the endpoint behaves as an
              unending feed of changes. If endTime is set the same as startTime, the most
              recent data point before that time will be returned per asset. Value is compared
              against `updatedAtTime`

          include_coachable_events: Optional boolean to control whether behaviors will include coachableEvents in
              the response. Defaults to false.

          include_external_ids: Optional boolean indicating whether to return external IDs on supported entities

          session_statuses: Optional string of comma separated statuses. Valid values: “upcoming”,
              “completed”, “deleted”.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/coaching/sessions/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_time": start_time,
                        "after": after,
                        "coach_ids": coach_ids,
                        "driver_ids": driver_ids,
                        "end_time": end_time,
                        "include_coachable_events": include_coachable_events,
                        "include_external_ids": include_external_ids,
                        "session_statuses": session_statuses,
                    },
                    session_stream_params.SessionStreamParams,
                ),
            ),
            cast_to=SessionStreamResponse,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.stream = to_raw_response_wrapper(
            sessions.stream,
        )


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.stream = async_to_raw_response_wrapper(
            sessions.stream,
        )


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.stream = to_streamed_response_wrapper(
            sessions.stream,
        )


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.stream = async_to_streamed_response_wrapper(
            sessions.stream,
        )
