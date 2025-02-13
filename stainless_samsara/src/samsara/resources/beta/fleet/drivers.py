# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

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
from ....types.beta.fleet import driver_efficiency_params
from ....types.beta.fleet.driver_efficiency_response import DriverEfficiencyResponse

__all__ = ["DriversResource", "AsyncDriversResource"]


class DriversResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DriversResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DriversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DriversResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DriversResourceWithStreamingResponse(self)

    def efficiency(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        driver_activation_status: Literal["active", "deactivated"] | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        driver_parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        driver_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverEfficiencyResponse:
        """
        Get all driver and associated vehicle efficiency data.

        <b>Rate limit:</b> 50 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          driver_activation_status: If value is `deactivated`, only drivers that are deactivated will appear in the
              response. This parameter will default to `active` if not provided (fetching only
              active drivers).

          driver_ids: A filter on the data based on this comma-separated list of driver IDs. Cannot be
              used with tag filtering or driver status. Example: `driverIds=1234,5678`

          driver_parent_tag_ids: Filters like `driverTagIds` but includes descendants of all the given parent
              tags. Should not be provided in addition to `driverIds`. Example:
              `driverParentTagIds=1234,5678`

          driver_tag_ids: Filters summary to drivers based on this comma-separated list of tag IDs. Data
              from all the drivers' respective vehicles will be included in the summary,
              regardless of which tag the vehicle is associated with. Should not be provided
              in addition to `driverIds`. Example: driverTagIds=1234,5678

          end_time: An end time in RFC 3339 format. The results will be truncated to the hour mark
              for the provided time. For example, if `endTime` is 2020-03-17T12:06:19Z then
              the results will include data up until 2020-03-17T12:00:00Z. The provided end
              time cannot be in the future. End time can be at most 31 days after the start
              time. Default: The current time truncated to the hour mark.

              Note that the most recent 72 hours of data may still be processing and is
              subject to change and latency, so it is not recommended to request data for the
              most recent 72 hours

          start_time: A start time in RFC 3339 format. The results will be truncated to the hour mark
              for the provided time. For example, if `startTime` is 2020-03-17T12:06:19Z then
              the results will include data starting from 2020-03-17T12:00:00Z. The provided
              start time cannot be in the future. Start time can be at most 31 days before the
              end time. If the start time is within the last hour, the results will be empty.
              Default: 24 hours prior to endTime.

              Note that the most recent 72 hours of data may still be processing and is
              subject to change and latency, so it is not recommended to request data for the
              most recent 72 hours.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/beta/fleet/drivers/efficiency",
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
                        "driver_parent_tag_ids": driver_parent_tag_ids,
                        "driver_tag_ids": driver_tag_ids,
                        "end_time": end_time,
                        "start_time": start_time,
                    },
                    driver_efficiency_params.DriverEfficiencyParams,
                ),
            ),
            cast_to=DriverEfficiencyResponse,
        )


class AsyncDriversResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDriversResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDriversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDriversResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDriversResourceWithStreamingResponse(self)

    async def efficiency(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        driver_activation_status: Literal["active", "deactivated"] | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        driver_parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        driver_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverEfficiencyResponse:
        """
        Get all driver and associated vehicle efficiency data.

        <b>Rate limit:</b> 50 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          driver_activation_status: If value is `deactivated`, only drivers that are deactivated will appear in the
              response. This parameter will default to `active` if not provided (fetching only
              active drivers).

          driver_ids: A filter on the data based on this comma-separated list of driver IDs. Cannot be
              used with tag filtering or driver status. Example: `driverIds=1234,5678`

          driver_parent_tag_ids: Filters like `driverTagIds` but includes descendants of all the given parent
              tags. Should not be provided in addition to `driverIds`. Example:
              `driverParentTagIds=1234,5678`

          driver_tag_ids: Filters summary to drivers based on this comma-separated list of tag IDs. Data
              from all the drivers' respective vehicles will be included in the summary,
              regardless of which tag the vehicle is associated with. Should not be provided
              in addition to `driverIds`. Example: driverTagIds=1234,5678

          end_time: An end time in RFC 3339 format. The results will be truncated to the hour mark
              for the provided time. For example, if `endTime` is 2020-03-17T12:06:19Z then
              the results will include data up until 2020-03-17T12:00:00Z. The provided end
              time cannot be in the future. End time can be at most 31 days after the start
              time. Default: The current time truncated to the hour mark.

              Note that the most recent 72 hours of data may still be processing and is
              subject to change and latency, so it is not recommended to request data for the
              most recent 72 hours

          start_time: A start time in RFC 3339 format. The results will be truncated to the hour mark
              for the provided time. For example, if `startTime` is 2020-03-17T12:06:19Z then
              the results will include data starting from 2020-03-17T12:00:00Z. The provided
              start time cannot be in the future. Start time can be at most 31 days before the
              end time. If the start time is within the last hour, the results will be empty.
              Default: 24 hours prior to endTime.

              Note that the most recent 72 hours of data may still be processing and is
              subject to change and latency, so it is not recommended to request data for the
              most recent 72 hours.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/beta/fleet/drivers/efficiency",
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
                        "driver_parent_tag_ids": driver_parent_tag_ids,
                        "driver_tag_ids": driver_tag_ids,
                        "end_time": end_time,
                        "start_time": start_time,
                    },
                    driver_efficiency_params.DriverEfficiencyParams,
                ),
            ),
            cast_to=DriverEfficiencyResponse,
        )


class DriversResourceWithRawResponse:
    def __init__(self, drivers: DriversResource) -> None:
        self._drivers = drivers

        self.efficiency = to_raw_response_wrapper(
            drivers.efficiency,
        )


class AsyncDriversResourceWithRawResponse:
    def __init__(self, drivers: AsyncDriversResource) -> None:
        self._drivers = drivers

        self.efficiency = async_to_raw_response_wrapper(
            drivers.efficiency,
        )


class DriversResourceWithStreamingResponse:
    def __init__(self, drivers: DriversResource) -> None:
        self._drivers = drivers

        self.efficiency = to_streamed_response_wrapper(
            drivers.efficiency,
        )


class AsyncDriversResourceWithStreamingResponse:
    def __init__(self, drivers: AsyncDriversResource) -> None:
        self._drivers = drivers

        self.efficiency = async_to_streamed_response_wrapper(
            drivers.efficiency,
        )
