# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .stats import (
    StatsResource,
    AsyncStatsResource,
    StatsResourceWithRawResponse,
    AsyncStatsResourceWithRawResponse,
    StatsResourceWithStreamingResponse,
    AsyncStatsResourceWithStreamingResponse,
)
from .safety import (
    SafetyResource,
    AsyncSafetyResource,
    SafetyResourceWithRawResponse,
    AsyncSafetyResourceWithRawResponse,
    SafetyResourceWithStreamingResponse,
    AsyncSafetyResourceWithStreamingResponse,
)
from ...types import vehicle_list_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .locations import (
    LocationsResource,
    AsyncLocationsResource,
    LocationsResourceWithRawResponse,
    AsyncLocationsResourceWithRawResponse,
    LocationsResourceWithStreamingResponse,
    AsyncLocationsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .driver_assignments import (
    DriverAssignmentsResource,
    AsyncDriverAssignmentsResource,
    DriverAssignmentsResourceWithRawResponse,
    AsyncDriverAssignmentsResourceWithRawResponse,
    DriverAssignmentsResourceWithStreamingResponse,
    AsyncDriverAssignmentsResourceWithStreamingResponse,
)
from .immobilizer_stream import (
    ImmobilizerStreamResource,
    AsyncImmobilizerStreamResource,
    ImmobilizerStreamResourceWithRawResponse,
    AsyncImmobilizerStreamResourceWithRawResponse,
    ImmobilizerStreamResourceWithStreamingResponse,
    AsyncImmobilizerStreamResourceWithStreamingResponse,
)
from ...types.fleet.vehicles_list_vehicles_response_body import VehiclesListVehiclesResponseBody

__all__ = ["VehiclesResource", "AsyncVehiclesResource"]


class VehiclesResource(SyncAPIResource):
    @cached_property
    def driver_assignments(self) -> DriverAssignmentsResource:
        return DriverAssignmentsResource(self._client)

    @cached_property
    def immobilizer_stream(self) -> ImmobilizerStreamResource:
        return ImmobilizerStreamResource(self._client)

    @cached_property
    def locations(self) -> LocationsResource:
        return LocationsResource(self._client)

    @cached_property
    def stats(self) -> StatsResource:
        return StatsResource(self._client)

    @cached_property
    def safety(self) -> SafetyResource:
        return SafetyResource(self._client)

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
        after: str | NotGiven = NOT_GIVEN,
        attribute_value_ids: str | NotGiven = NOT_GIVEN,
        created_after_time: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        updated_after_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VehiclesListVehiclesResponseBody:
        """
        Returns a list of all vehicles.

        <b>Rate limit:</b> 25 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Vehicles** under the Vehicles category when
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
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          attribute_value_ids: A filter on the data based on this comma-separated list of attribute value IDs.
              Only entities associated with ALL of the referenced values will be returned
              (i.e. the intersection of the sets of entities with each value). Example:
              `attributeValueIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`

          created_after_time: A filter on data to have a created at time after or equal to this specified time
              in RFC 3339 format. Millisecond precision and timezones are supported.
              (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 512 objects.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          updated_after_time: A filter on data to have an updated at time after or equal to this specified
              time in RFC 3339 format. Millisecond precision and timezones are supported.
              (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fleet/vehicles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "attribute_value_ids": attribute_value_ids,
                        "created_after_time": created_after_time,
                        "limit": limit,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "updated_after_time": updated_after_time,
                    },
                    vehicle_list_params.VehicleListParams,
                ),
            ),
            cast_to=VehiclesListVehiclesResponseBody,
        )


class AsyncVehiclesResource(AsyncAPIResource):
    @cached_property
    def driver_assignments(self) -> AsyncDriverAssignmentsResource:
        return AsyncDriverAssignmentsResource(self._client)

    @cached_property
    def immobilizer_stream(self) -> AsyncImmobilizerStreamResource:
        return AsyncImmobilizerStreamResource(self._client)

    @cached_property
    def locations(self) -> AsyncLocationsResource:
        return AsyncLocationsResource(self._client)

    @cached_property
    def stats(self) -> AsyncStatsResource:
        return AsyncStatsResource(self._client)

    @cached_property
    def safety(self) -> AsyncSafetyResource:
        return AsyncSafetyResource(self._client)

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
        after: str | NotGiven = NOT_GIVEN,
        attribute_value_ids: str | NotGiven = NOT_GIVEN,
        created_after_time: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        updated_after_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VehiclesListVehiclesResponseBody:
        """
        Returns a list of all vehicles.

        <b>Rate limit:</b> 25 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Vehicles** under the Vehicles category when
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
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          attribute_value_ids: A filter on the data based on this comma-separated list of attribute value IDs.
              Only entities associated with ALL of the referenced values will be returned
              (i.e. the intersection of the sets of entities with each value). Example:
              `attributeValueIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`

          created_after_time: A filter on data to have a created at time after or equal to this specified time
              in RFC 3339 format. Millisecond precision and timezones are supported.
              (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 512 objects.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          updated_after_time: A filter on data to have an updated at time after or equal to this specified
              time in RFC 3339 format. Millisecond precision and timezones are supported.
              (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fleet/vehicles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "attribute_value_ids": attribute_value_ids,
                        "created_after_time": created_after_time,
                        "limit": limit,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "updated_after_time": updated_after_time,
                    },
                    vehicle_list_params.VehicleListParams,
                ),
            ),
            cast_to=VehiclesListVehiclesResponseBody,
        )


class VehiclesResourceWithRawResponse:
    def __init__(self, vehicles: VehiclesResource) -> None:
        self._vehicles = vehicles

        self.list = to_raw_response_wrapper(
            vehicles.list,
        )

    @cached_property
    def driver_assignments(self) -> DriverAssignmentsResourceWithRawResponse:
        return DriverAssignmentsResourceWithRawResponse(self._vehicles.driver_assignments)

    @cached_property
    def immobilizer_stream(self) -> ImmobilizerStreamResourceWithRawResponse:
        return ImmobilizerStreamResourceWithRawResponse(self._vehicles.immobilizer_stream)

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._vehicles.locations)

    @cached_property
    def stats(self) -> StatsResourceWithRawResponse:
        return StatsResourceWithRawResponse(self._vehicles.stats)

    @cached_property
    def safety(self) -> SafetyResourceWithRawResponse:
        return SafetyResourceWithRawResponse(self._vehicles.safety)


class AsyncVehiclesResourceWithRawResponse:
    def __init__(self, vehicles: AsyncVehiclesResource) -> None:
        self._vehicles = vehicles

        self.list = async_to_raw_response_wrapper(
            vehicles.list,
        )

    @cached_property
    def driver_assignments(self) -> AsyncDriverAssignmentsResourceWithRawResponse:
        return AsyncDriverAssignmentsResourceWithRawResponse(self._vehicles.driver_assignments)

    @cached_property
    def immobilizer_stream(self) -> AsyncImmobilizerStreamResourceWithRawResponse:
        return AsyncImmobilizerStreamResourceWithRawResponse(self._vehicles.immobilizer_stream)

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._vehicles.locations)

    @cached_property
    def stats(self) -> AsyncStatsResourceWithRawResponse:
        return AsyncStatsResourceWithRawResponse(self._vehicles.stats)

    @cached_property
    def safety(self) -> AsyncSafetyResourceWithRawResponse:
        return AsyncSafetyResourceWithRawResponse(self._vehicles.safety)


class VehiclesResourceWithStreamingResponse:
    def __init__(self, vehicles: VehiclesResource) -> None:
        self._vehicles = vehicles

        self.list = to_streamed_response_wrapper(
            vehicles.list,
        )

    @cached_property
    def driver_assignments(self) -> DriverAssignmentsResourceWithStreamingResponse:
        return DriverAssignmentsResourceWithStreamingResponse(self._vehicles.driver_assignments)

    @cached_property
    def immobilizer_stream(self) -> ImmobilizerStreamResourceWithStreamingResponse:
        return ImmobilizerStreamResourceWithStreamingResponse(self._vehicles.immobilizer_stream)

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._vehicles.locations)

    @cached_property
    def stats(self) -> StatsResourceWithStreamingResponse:
        return StatsResourceWithStreamingResponse(self._vehicles.stats)

    @cached_property
    def safety(self) -> SafetyResourceWithStreamingResponse:
        return SafetyResourceWithStreamingResponse(self._vehicles.safety)


class AsyncVehiclesResourceWithStreamingResponse:
    def __init__(self, vehicles: AsyncVehiclesResource) -> None:
        self._vehicles = vehicles

        self.list = async_to_streamed_response_wrapper(
            vehicles.list,
        )

    @cached_property
    def driver_assignments(self) -> AsyncDriverAssignmentsResourceWithStreamingResponse:
        return AsyncDriverAssignmentsResourceWithStreamingResponse(self._vehicles.driver_assignments)

    @cached_property
    def immobilizer_stream(self) -> AsyncImmobilizerStreamResourceWithStreamingResponse:
        return AsyncImmobilizerStreamResourceWithStreamingResponse(self._vehicles.immobilizer_stream)

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._vehicles.locations)

    @cached_property
    def stats(self) -> AsyncStatsResourceWithStreamingResponse:
        return AsyncStatsResourceWithStreamingResponse(self._vehicles.stats)

    @cached_property
    def safety(self) -> AsyncSafetyResourceWithStreamingResponse:
        return AsyncSafetyResourceWithStreamingResponse(self._vehicles.safety)
