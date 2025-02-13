# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

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
from ...types.hos import daily_log_list_params, daily_log_update_log_metadata_params
from ..._base_client import make_request_options
from ...types.hos.daily_log_list_response import DailyLogListResponse
from ...types.hos.hos_daily_logs_update_shipping_docs_response_body import HosDailyLogsUpdateShippingDocsResponseBody

__all__ = ["DailyLogsResource", "AsyncDailyLogsResource"]


class DailyLogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DailyLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DailyLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DailyLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DailyLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        driver_activation_status: Literal["active", "deactivated"] | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        end_date: str | NotGiven = NOT_GIVEN,
        expand: Literal["vehicle"] | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        start_date: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DailyLogListResponse:
        """
        Get summarized daily Hours of Service charts for the specified drivers.

        The time range for a log is defined by the `driver`'s `eldDayStartHour`. This
        value is configurable per driver.

        The `startDate` and `endDate` parameters indicate the date range you'd like to
        retrieve daily logs for. A daily log will be returned if its `startTime` is on
        any of the days within in this date range (inclusive of `startDate` and
        `endDate`).

        **Note:** If data is still being uploaded from the Samsara Driver App, it may
        not be completely reflected in the response from this endpoint. The best
        practice is to wait a couple of days before querying this endpoint to make sure
        that all data from the Samsara Driver App has been uploaded.

        If you are using the legacy version of this endpoint and looking for its
        documentation, you can find it
        [here](https://www.samsara.com/api-legacy#operation/getFleetDriversHosDailyLogs).

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
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          driver_activation_status: If value is `deactivated`, only drivers that are deactivated will appear in the
              response. This parameter will default to `active` if not provided (fetching only
              active drivers). Valid values: `active`, `deactivated`

          driver_ids: A filter on the data based on this comma-separated list of driver IDs and
              externalIds. Example: `driverIds=1234,5678,payroll:4841`

          end_date: An end date in YYYY-MM-DD. This is a date only without an associated time. Must
              be greater than or equal to the start date. Example: `2019-07-21`. This is a
              required field

          expand: Expands the specified value(s) in the response object. Expansion populates
              additional fields in an object, if supported. Unsupported fields are ignored. To
              expand multiple fields, input a comma-separated list.

              Valid value: `vehicle` Valid values: `vehicle`

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          start_date: A start date in YYYY-MM-DD. This is a date only without an associated time.
              Example: `2019-06-13`. This is a required field

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fleet/hos/daily-logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "driver_activation_status": driver_activation_status,
                        "driver_ids": driver_ids,
                        "end_date": end_date,
                        "expand": expand,
                        "parent_tag_ids": parent_tag_ids,
                        "start_date": start_date,
                        "tag_ids": tag_ids,
                    },
                    daily_log_list_params.DailyLogListParams,
                ),
            ),
            cast_to=DailyLogListResponse,
        )

    def update_log_metadata(
        self,
        *,
        driver_id: str,
        hos_date: str,
        shipping_docs: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HosDailyLogsUpdateShippingDocsResponseBody:
        """
        Update the shippingDocs field of an existing assignment.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write ELD Hours of Service (US)** under the
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
          driver_id: ID of the driver for whom the duty status is being set.

          hos_date: A start date in yyyy-mm-dd format. Required.

          shipping_docs: ShippingDocs associated with the driver for the day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/hos/daily-logs/log-meta-data",
            body=maybe_transform(
                {"shipping_docs": shipping_docs}, daily_log_update_log_metadata_params.DailyLogUpdateLogMetadataParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "driver_id": driver_id,
                        "hos_date": hos_date,
                    },
                    daily_log_update_log_metadata_params.DailyLogUpdateLogMetadataParams,
                ),
            ),
            cast_to=HosDailyLogsUpdateShippingDocsResponseBody,
        )


class AsyncDailyLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDailyLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDailyLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDailyLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDailyLogsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        driver_activation_status: Literal["active", "deactivated"] | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        end_date: str | NotGiven = NOT_GIVEN,
        expand: Literal["vehicle"] | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        start_date: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DailyLogListResponse:
        """
        Get summarized daily Hours of Service charts for the specified drivers.

        The time range for a log is defined by the `driver`'s `eldDayStartHour`. This
        value is configurable per driver.

        The `startDate` and `endDate` parameters indicate the date range you'd like to
        retrieve daily logs for. A daily log will be returned if its `startTime` is on
        any of the days within in this date range (inclusive of `startDate` and
        `endDate`).

        **Note:** If data is still being uploaded from the Samsara Driver App, it may
        not be completely reflected in the response from this endpoint. The best
        practice is to wait a couple of days before querying this endpoint to make sure
        that all data from the Samsara Driver App has been uploaded.

        If you are using the legacy version of this endpoint and looking for its
        documentation, you can find it
        [here](https://www.samsara.com/api-legacy#operation/getFleetDriversHosDailyLogs).

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
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          driver_activation_status: If value is `deactivated`, only drivers that are deactivated will appear in the
              response. This parameter will default to `active` if not provided (fetching only
              active drivers). Valid values: `active`, `deactivated`

          driver_ids: A filter on the data based on this comma-separated list of driver IDs and
              externalIds. Example: `driverIds=1234,5678,payroll:4841`

          end_date: An end date in YYYY-MM-DD. This is a date only without an associated time. Must
              be greater than or equal to the start date. Example: `2019-07-21`. This is a
              required field

          expand: Expands the specified value(s) in the response object. Expansion populates
              additional fields in an object, if supported. Unsupported fields are ignored. To
              expand multiple fields, input a comma-separated list.

              Valid value: `vehicle` Valid values: `vehicle`

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          start_date: A start date in YYYY-MM-DD. This is a date only without an associated time.
              Example: `2019-06-13`. This is a required field

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fleet/hos/daily-logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "driver_activation_status": driver_activation_status,
                        "driver_ids": driver_ids,
                        "end_date": end_date,
                        "expand": expand,
                        "parent_tag_ids": parent_tag_ids,
                        "start_date": start_date,
                        "tag_ids": tag_ids,
                    },
                    daily_log_list_params.DailyLogListParams,
                ),
            ),
            cast_to=DailyLogListResponse,
        )

    async def update_log_metadata(
        self,
        *,
        driver_id: str,
        hos_date: str,
        shipping_docs: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HosDailyLogsUpdateShippingDocsResponseBody:
        """
        Update the shippingDocs field of an existing assignment.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write ELD Hours of Service (US)** under the
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
          driver_id: ID of the driver for whom the duty status is being set.

          hos_date: A start date in yyyy-mm-dd format. Required.

          shipping_docs: ShippingDocs associated with the driver for the day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/hos/daily-logs/log-meta-data",
            body=await async_maybe_transform(
                {"shipping_docs": shipping_docs}, daily_log_update_log_metadata_params.DailyLogUpdateLogMetadataParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "driver_id": driver_id,
                        "hos_date": hos_date,
                    },
                    daily_log_update_log_metadata_params.DailyLogUpdateLogMetadataParams,
                ),
            ),
            cast_to=HosDailyLogsUpdateShippingDocsResponseBody,
        )


class DailyLogsResourceWithRawResponse:
    def __init__(self, daily_logs: DailyLogsResource) -> None:
        self._daily_logs = daily_logs

        self.list = to_raw_response_wrapper(
            daily_logs.list,
        )
        self.update_log_metadata = to_raw_response_wrapper(
            daily_logs.update_log_metadata,
        )


class AsyncDailyLogsResourceWithRawResponse:
    def __init__(self, daily_logs: AsyncDailyLogsResource) -> None:
        self._daily_logs = daily_logs

        self.list = async_to_raw_response_wrapper(
            daily_logs.list,
        )
        self.update_log_metadata = async_to_raw_response_wrapper(
            daily_logs.update_log_metadata,
        )


class DailyLogsResourceWithStreamingResponse:
    def __init__(self, daily_logs: DailyLogsResource) -> None:
        self._daily_logs = daily_logs

        self.list = to_streamed_response_wrapper(
            daily_logs.list,
        )
        self.update_log_metadata = to_streamed_response_wrapper(
            daily_logs.update_log_metadata,
        )


class AsyncDailyLogsResourceWithStreamingResponse:
    def __init__(self, daily_logs: AsyncDailyLogsResource) -> None:
        self._daily_logs = daily_logs

        self.list = async_to_streamed_response_wrapper(
            daily_logs.list,
        )
        self.update_log_metadata = async_to_streamed_response_wrapper(
            daily_logs.update_log_metadata,
        )
