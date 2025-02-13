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
from ....types.preview.driver_efficiency import vehicle_list_params
from ....types.preview.driver_efficiency.driver_efficiency_get_driver_efficiency_by_vehicles_response_body import (
    DriverEfficiencyGetDriverEfficiencyByVehiclesResponseBody,
)

__all__ = ["VehiclesResource", "AsyncVehiclesResource"]


class VehiclesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VehiclesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return VehiclesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VehiclesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return VehiclesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end_time: str,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        data_formats: List[str] | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        vehicle_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverEfficiencyGetDriverEfficiencyByVehiclesResponseBody:
        """
        This endpoint will return driver efficiency data that has been collected for
        your organization and grouped by vehicle drivers used based on the time
        parameters passed in. Results are paginated.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Driver Efficiency** under the Closed Beta
        category when creating or editing an API token.
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
          end_time: An end time in RFC 3339 format. Must be in multiple of hours and no later than 3
              hours before the current time. Timezones are supported. Note that the most
              recent 72 hours of data may still be processing and is subject to change and
              latency, so it is not recommended to request data for the most recent 72 hours.
              (Examples: 2019-06-13T19:00:00Z, 2015-09-15T14:00:00-04:00).

          start_time: A start time in RFC 3339 format. Must be in multiple of hours and at least 1 day
              before endTime. Timezones are supported. Note that the most recent 72 hours of
              data may still be processing and is subject to change and latency, so it is not
              recommended to request data for the most recent 72 hours. (Examples:
              2019-06-11T19:00:00Z, 2015-09-12T14:00:00-04:00).

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          data_formats: A comma-separated list of data formats you want to fetch. Valid values: `score`,
              `raw` and `percentage`. The default data format is `score`. Example:
              `dataFormats=raw,score`

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          vehicle_ids: A filter on the data based on this comma-separated list of vehicle IDs and
              externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/preview/driver-efficiency/vehicles",
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
                        "data_formats": data_formats,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "vehicle_ids": vehicle_ids,
                    },
                    vehicle_list_params.VehicleListParams,
                ),
            ),
            cast_to=DriverEfficiencyGetDriverEfficiencyByVehiclesResponseBody,
        )


class AsyncVehiclesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVehiclesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVehiclesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVehiclesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncVehiclesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        end_time: str,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        data_formats: List[str] | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        vehicle_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverEfficiencyGetDriverEfficiencyByVehiclesResponseBody:
        """
        This endpoint will return driver efficiency data that has been collected for
        your organization and grouped by vehicle drivers used based on the time
        parameters passed in. Results are paginated.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Driver Efficiency** under the Closed Beta
        category when creating or editing an API token.
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
          end_time: An end time in RFC 3339 format. Must be in multiple of hours and no later than 3
              hours before the current time. Timezones are supported. Note that the most
              recent 72 hours of data may still be processing and is subject to change and
              latency, so it is not recommended to request data for the most recent 72 hours.
              (Examples: 2019-06-13T19:00:00Z, 2015-09-15T14:00:00-04:00).

          start_time: A start time in RFC 3339 format. Must be in multiple of hours and at least 1 day
              before endTime. Timezones are supported. Note that the most recent 72 hours of
              data may still be processing and is subject to change and latency, so it is not
              recommended to request data for the most recent 72 hours. (Examples:
              2019-06-11T19:00:00Z, 2015-09-12T14:00:00-04:00).

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          data_formats: A comma-separated list of data formats you want to fetch. Valid values: `score`,
              `raw` and `percentage`. The default data format is `score`. Example:
              `dataFormats=raw,score`

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          vehicle_ids: A filter on the data based on this comma-separated list of vehicle IDs and
              externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/preview/driver-efficiency/vehicles",
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
                        "data_formats": data_formats,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "vehicle_ids": vehicle_ids,
                    },
                    vehicle_list_params.VehicleListParams,
                ),
            ),
            cast_to=DriverEfficiencyGetDriverEfficiencyByVehiclesResponseBody,
        )


class VehiclesResourceWithRawResponse:
    def __init__(self, vehicles: VehiclesResource) -> None:
        self._vehicles = vehicles

        self.list = to_raw_response_wrapper(
            vehicles.list,
        )


class AsyncVehiclesResourceWithRawResponse:
    def __init__(self, vehicles: AsyncVehiclesResource) -> None:
        self._vehicles = vehicles

        self.list = async_to_raw_response_wrapper(
            vehicles.list,
        )


class VehiclesResourceWithStreamingResponse:
    def __init__(self, vehicles: VehiclesResource) -> None:
        self._vehicles = vehicles

        self.list = to_streamed_response_wrapper(
            vehicles.list,
        )


class AsyncVehiclesResourceWithStreamingResponse:
    def __init__(self, vehicles: AsyncVehiclesResource) -> None:
        self._vehicles = vehicles

        self.list = async_to_streamed_response_wrapper(
            vehicles.list,
        )
