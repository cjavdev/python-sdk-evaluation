# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.fleet.reports import drivers_fuel_energy_list_params
from ....types.fleet.reports.drivers_fuel_energy_list_response import DriversFuelEnergyListResponse

__all__ = ["DriversFuelEnergyResource", "AsyncDriversFuelEnergyResource"]


class DriversFuelEnergyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DriversFuelEnergyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DriversFuelEnergyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DriversFuelEnergyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DriversFuelEnergyResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end_date: str,
        start_date: str,
        after: str | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriversFuelEnergyListResponse:
        """
        Get fuel and energy efficiency driver reports for the requested time range.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy
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
          end_date: An end date in RFC 3339 format. This parameter ignores everything (i.e. hour,
              minutes, seconds, nanoseconds, etc.) besides the date and timezone. If no time
              zone is passed in, then the UTC time zone will be used. This parameter is
              inclusive, so data on the date specified will be considered. Note that the most
              recent 72 hours of data may still be processing and is subject to change and
              latency, so it is not recommended to request data for the most recent 72 hours.
              For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.

          start_date: A start date in RFC 3339 format. This parameter ignores everything (i.e. hour,
              minutes, seconds, nanoseconds, etc.) besides the date and timezone. If no time
              zone is passed in, then the UTC time zone will be used. This parameter is
              inclusive, so data on the date specified will be considered. Note that the most
              recent 72 hours of data may still be processing and is subject to change and
              latency, so it is not recommended to request data for the most recent 72 hours.
              For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          driver_ids: A filter on the data based on this comma-separated list of driver IDs and
              externalIds. Example: `driverIds=1234,5678,payroll:4841`

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
            "/fleet/reports/drivers/fuel-energy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "after": after,
                        "driver_ids": driver_ids,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    drivers_fuel_energy_list_params.DriversFuelEnergyListParams,
                ),
            ),
            cast_to=DriversFuelEnergyListResponse,
        )


class AsyncDriversFuelEnergyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDriversFuelEnergyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDriversFuelEnergyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDriversFuelEnergyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDriversFuelEnergyResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        end_date: str,
        start_date: str,
        after: str | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriversFuelEnergyListResponse:
        """
        Get fuel and energy efficiency driver reports for the requested time range.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy
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
          end_date: An end date in RFC 3339 format. This parameter ignores everything (i.e. hour,
              minutes, seconds, nanoseconds, etc.) besides the date and timezone. If no time
              zone is passed in, then the UTC time zone will be used. This parameter is
              inclusive, so data on the date specified will be considered. Note that the most
              recent 72 hours of data may still be processing and is subject to change and
              latency, so it is not recommended to request data for the most recent 72 hours.
              For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.

          start_date: A start date in RFC 3339 format. This parameter ignores everything (i.e. hour,
              minutes, seconds, nanoseconds, etc.) besides the date and timezone. If no time
              zone is passed in, then the UTC time zone will be used. This parameter is
              inclusive, so data on the date specified will be considered. Note that the most
              recent 72 hours of data may still be processing and is subject to change and
              latency, so it is not recommended to request data for the most recent 72 hours.
              For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          driver_ids: A filter on the data based on this comma-separated list of driver IDs and
              externalIds. Example: `driverIds=1234,5678,payroll:4841`

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
            "/fleet/reports/drivers/fuel-energy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "after": after,
                        "driver_ids": driver_ids,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    drivers_fuel_energy_list_params.DriversFuelEnergyListParams,
                ),
            ),
            cast_to=DriversFuelEnergyListResponse,
        )


class DriversFuelEnergyResourceWithRawResponse:
    def __init__(self, drivers_fuel_energy: DriversFuelEnergyResource) -> None:
        self._drivers_fuel_energy = drivers_fuel_energy

        self.list = to_raw_response_wrapper(
            drivers_fuel_energy.list,
        )


class AsyncDriversFuelEnergyResourceWithRawResponse:
    def __init__(self, drivers_fuel_energy: AsyncDriversFuelEnergyResource) -> None:
        self._drivers_fuel_energy = drivers_fuel_energy

        self.list = async_to_raw_response_wrapper(
            drivers_fuel_energy.list,
        )


class DriversFuelEnergyResourceWithStreamingResponse:
    def __init__(self, drivers_fuel_energy: DriversFuelEnergyResource) -> None:
        self._drivers_fuel_energy = drivers_fuel_energy

        self.list = to_streamed_response_wrapper(
            drivers_fuel_energy.list,
        )


class AsyncDriversFuelEnergyResourceWithStreamingResponse:
    def __init__(self, drivers_fuel_energy: AsyncDriversFuelEnergyResource) -> None:
        self._drivers_fuel_energy = drivers_fuel_energy

        self.list = async_to_streamed_response_wrapper(
            drivers_fuel_energy.list,
        )
