# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.beta.fleet.hos.drivers import eld_event_list_params
from ......types.beta.fleet.hos.drivers.eld_event_list_response import EldEventListResponse

__all__ = ["EldEventsResource", "AsyncEldEventsResource"]


class EldEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EldEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return EldEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EldEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return EldEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end_time: str,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        driver_activation_status: Literal["active", "deactivated"] | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EldEventListResponse:
        """Get all HOS ELD events in a time range, grouped by driver.

        Attributes will be
        populated depending on which ELD Event Type is being returned.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read ELD Compliance Settings (US)** under the
        Compliance category when creating or editing an API token.
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
          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          driver_activation_status: If value is `deactivated`, only drivers that are deactivated will appear in the
              response. This parameter will default to `active` if not provided (fetching only
              active drivers). Valid values: `active`, `deactivated`

          driver_ids: A filter on the data based on this comma-separated list of driver IDs and
              externalIds. Example: `driverIds=1234,5678,payroll:4841`

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 25 objects.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/beta/fleet/hos/drivers/eld-events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "start_time": start_time,
                        "after": after,
                        "driver_activation_status": driver_activation_status,
                        "driver_ids": driver_ids,
                        "limit": limit,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    eld_event_list_params.EldEventListParams,
                ),
            ),
            cast_to=EldEventListResponse,
        )


class AsyncEldEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEldEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEldEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEldEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncEldEventsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        end_time: str,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        driver_activation_status: Literal["active", "deactivated"] | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EldEventListResponse:
        """Get all HOS ELD events in a time range, grouped by driver.

        Attributes will be
        populated depending on which ELD Event Type is being returned.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read ELD Compliance Settings (US)** under the
        Compliance category when creating or editing an API token.
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
          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          driver_activation_status: If value is `deactivated`, only drivers that are deactivated will appear in the
              response. This parameter will default to `active` if not provided (fetching only
              active drivers). Valid values: `active`, `deactivated`

          driver_ids: A filter on the data based on this comma-separated list of driver IDs and
              externalIds. Example: `driverIds=1234,5678,payroll:4841`

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 25 objects.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/beta/fleet/hos/drivers/eld-events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_time": end_time,
                        "start_time": start_time,
                        "after": after,
                        "driver_activation_status": driver_activation_status,
                        "driver_ids": driver_ids,
                        "limit": limit,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    eld_event_list_params.EldEventListParams,
                ),
            ),
            cast_to=EldEventListResponse,
        )


class EldEventsResourceWithRawResponse:
    def __init__(self, eld_events: EldEventsResource) -> None:
        self._eld_events = eld_events

        self.list = to_raw_response_wrapper(
            eld_events.list,
        )


class AsyncEldEventsResourceWithRawResponse:
    def __init__(self, eld_events: AsyncEldEventsResource) -> None:
        self._eld_events = eld_events

        self.list = async_to_raw_response_wrapper(
            eld_events.list,
        )


class EldEventsResourceWithStreamingResponse:
    def __init__(self, eld_events: EldEventsResource) -> None:
        self._eld_events = eld_events

        self.list = to_streamed_response_wrapper(
            eld_events.list,
        )


class AsyncEldEventsResourceWithStreamingResponse:
    def __init__(self, eld_events: AsyncEldEventsResource) -> None:
        self._eld_events = eld_events

        self.list = async_to_streamed_response_wrapper(
            eld_events.list,
        )
