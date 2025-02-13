# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.beta.fleet.trailers import stat_feed_params, stat_list_params, stat_history_params
from .....types.beta.fleet.trailers.stat_feed_response import StatFeedResponse
from .....types.beta.fleet.trailers.stat_list_response import StatListResponse
from .....types.beta.fleet.trailers.stat_history_response import StatHistoryResponse

__all__ = ["StatsResource", "AsyncStatsResource"]


class StatsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return StatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return StatsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        types: str,
        after: str | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        time: str | NotGiven = NOT_GIVEN,
        trailer_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatListResponse:
        """Returns the last known stats of all trailers at the given `time`.

        If no `time`
        is specified, the current time is used.

        <b>Rate limit:</b> 25 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Trailer Statistics** under the Trailers
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
          types: The stat types you want this endpoint to return information on.

              You may list **up to 3** types using comma-separated format. For example:
              `types=gps,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters`.

              - `gps`: GPS data including lat/long, heading, speed, and a reverse geocode
                address.
              - `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must
                provide a manual odometer reading before this value is updated. Manual
                odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint
                or through the
                [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading).
                Odometer readings wthat are manually set will update as GPS trip data is
                gathered.
              - `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of
                the reefer in millidegree Celsius.
              - `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run
                according to onboard diagnostics. Only supported on reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air
                temperature zone 1 in millidegrees Celsius. For single zone reefers, this
                applies to the single zone. Only supported on multizone reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air
                temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air
                temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferFuelPercent`: The fuel level of the reefer unit in percentage points
                (e.g. `99`, `50`, etc). Only supported on reefer solutions.
              - `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only
                supported on multizone Carrier reefer solutions.
              - `reeferStateZone1`: The state of the reefer in zone 1. For single zone
                reefers, this applies tot he single zone. Only supported on multizone reefer
                solutions.
              - `reeferStateZone2`: The state of the reefer in zone 2. Only supported on
                multizone reefer solutions.
              - `reeferStateZone3`: The state of the reefer in zone 3. Only supported on
                multizone reefer solutions.
              - `reeferRunMode`: The operational mode of the reefer (`Start/Stop`,
                `Continuous`)
              - `reeferAlarms`: Any alarms that are present on the reefer. Only supported on
                reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1
                of the reefer in millidegrees Celsius. For single zone reefers, this applies
                to the single zone. Only supported on multizone reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of
                the reefer in millidegrees Celsius. For single zone reefers, this applies to
                the single zone. Only supported on multizone reefer solutions.
              - `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single
                zone reefers, this applies to the single zone.
              - `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only
                supported on multizone reefer solutions.
              - `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only
                supported on multizone reefer solutions.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          time: A filter on the data that returns the last known data points with timestamps
              less than or equal to this value. Defaults to now if not provided. Must be a
              string in RFC 3339 Format. Millisecond precision and timezones are supported.

          trailer_ids: A filter on the data based on this comma-separated list of trailer IDs and
              externalIds. Example: `trailerIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/beta/fleet/trailers/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "types": types,
                        "after": after,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "time": time,
                        "trailer_ids": trailer_ids,
                    },
                    stat_list_params.StatListParams,
                ),
            ),
            cast_to=StatListResponse,
        )

    def feed(
        self,
        *,
        types: str,
        after: str | NotGiven = NOT_GIVEN,
        decorations: str | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        trailer_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatFeedResponse:
        """
        Follow a feed of trailer stats.

        The first call to this endpoint will provide the most recent stats for each
        trailer and an `endCursor`.

        Providing the `endCursor` value to the `after` query parameter will fetch all
        updates since the previous API call.

        If `hasNextPage` is false, no new data is immediately available. Please wait a
        minimum of 5 seconds before making a subsequent request.

        <b>Rate limit:</b> 25 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Trailer Statistics** under the Trailers
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
          types: The stat types you want this endpoint to return information on.

              You may list **up to 3** types using comma-separated format. For example:
              `types=gps,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters`.

              - `gps`: GPS data including lat/long, heading, speed, and a reverse geocode
                address.
              - `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must
                provide a manual odometer reading before this value is updated. Manual
                odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint
                or through the
                [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading).
                Odometer readings wthat are manually set will update as GPS trip data is
                gathered.
              - `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of
                the reefer in millidegree Celsius.
              - `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run
                according to onboard diagnostics. Only supported on reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air
                temperature zone 1 in millidegrees Celsius. For single zone reefers, this
                applies to the single zone. Only supported on multizone reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air
                temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air
                temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferFuelPercent`: The fuel level of the reefer unit in percentage points
                (e.g. `99`, `50`, etc). Only supported on reefer solutions.
              - `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only
                supported on multizone Carrier reefer solutions.
              - `reeferStateZone1`: The state of the reefer in zone 1. For single zone
                reefers, this applies tot he single zone. Only supported on multizone reefer
                solutions.
              - `reeferStateZone2`: The state of the reefer in zone 2. Only supported on
                multizone reefer solutions.
              - `reeferStateZone3`: The state of the reefer in zone 3. Only supported on
                multizone reefer solutions.
              - `reeferRunMode`: The operational mode of the reefer (`Start/Stop`,
                `Continuous`)
              - `reeferAlarms`: Any alarms that are present on the reefer. Only supported on
                reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1
                of the reefer in millidegrees Celsius. For single zone reefers, this applies
                to the single zone. Only supported on multizone reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of
                the reefer in millidegrees Celsius. For single zone reefers, this applies to
                the single zone. Only supported on multizone reefer solutions.
              - `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single
                zone reefers, this applies to the single zone.
              - `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only
                supported on multizone reefer solutions.
              - `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only
                supported on multizone reefer solutions.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          decorations: Decorations add to the primary stats listed in the `types` parameter. For
              example, if you wish to know the trailer's location whenever the odometer
              updates, you may set `types=gpsOdometerMeters&decorations=gps`.

              You may list **up to 2** types using comma-separated format. If multiple stats
              are listed in the types parameter, the decorations will be added to each type.
              For example:
              `types=reeferStateZone1,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters&decorations=gps`
              will list GPS decorations for each reeferStateZone1 reading, each
              reeferAmbientAirTemperatureMilliC reding, and gpsOdometerMeters reading.

              Note that decorations may significantly increase the response payload size.

              - `gps`: GPS data including lat/long, heading, speed, and a reverse geocode
                address.
              - `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must
                provide a manual odometer reading before this value is updated. Manual
                odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint
                or through the
                [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading).
                Odometer readings wthat are manually set will update as GPS trip data is
                gathered.
              - `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of
                the reefer in millidegree Celsius.
              - `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run
                according to onboard diagnostics. Only supported on reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air
                temperature zone 1 in millidegrees Celsius. For single zone reefers, this
                applies to the single zone. Only supported on multizone reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air
                temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air
                temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferFuelPercent`: The fuel level of the reefer unit in percentage points
                (e.g. `99`, `50`, etc). Only supported on reefer solutions.
              - `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only
                supported on multizone Carrier reefer solutions.
              - `reeferStateZone1`: The state of the reefer in zone 1. For single zone
                reefers, this applies tot he single zone. Only supported on multizone reefer
                solutions.
              - `reeferStateZone2`: The state of the reefer in zone 2. Only supported on
                multizone reefer solutions.
              - `reeferStateZone3`: The state of the reefer in zone 3. Only supported on
                multizone reefer solutions.
              - `reeferRunMode`: The operational mode of the reefer (`Start/Stop`,
                `Continuous`)
              - `reeferAlarms`: Any alarms that are present on the reefer. Only supported on
                reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1
                of the reefer in millidegrees Celsius. For single zone reefers, this applies
                to the single zone. Only supported on multizone reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of
                the reefer in millidegrees Celsius. For single zone reefers, this applies to
                the single zone. Only supported on multizone reefer solutions.
              - `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single
                zone reefers, this applies to the single zone.
              - `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only
                supported on multizone reefer solutions.
              - `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only
                supported on multizone reefer solutions.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          trailer_ids: A filter on the data based on this comma-separated list of trailer IDs and
              externalIds. Example: `trailerIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/beta/fleet/trailers/stats/feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "types": types,
                        "after": after,
                        "decorations": decorations,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "trailer_ids": trailer_ids,
                    },
                    stat_feed_params.StatFeedParams,
                ),
            ),
            cast_to=StatFeedResponse,
        )

    def history(
        self,
        *,
        end_time: str,
        start_time: str,
        types: str,
        after: str | NotGiven = NOT_GIVEN,
        decorations: str | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        trailer_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatHistoryResponse:
        """Returns trailer stats during the given time range for all trailers.

        This can be
        optionally filtered by tags or specific trailer IDs.

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Trailer Statistics** under the Trailers
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
          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          types: The stat types you want this endpoint to return information on.

              You may list **up to 3** types using comma-separated format. For example:
              `types=gps,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters`.

              - `gps`: GPS data including lat/long, heading, speed, and a reverse geocode
                address.
              - `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must
                provide a manual odometer reading before this value is updated. Manual
                odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint
                or through the
                [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading).
                Odometer readings wthat are manually set will update as GPS trip data is
                gathered.
              - `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of
                the reefer in millidegree Celsius.
              - `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run
                according to onboard diagnostics. Only supported on reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air
                temperature zone 1 in millidegrees Celsius. For single zone reefers, this
                applies to the single zone. Only supported on multizone reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air
                temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air
                temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferFuelPercent`: The fuel level of the reefer unit in percentage points
                (e.g. `99`, `50`, etc). Only supported on reefer solutions.
              - `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only
                supported on multizone Carrier reefer solutions.
              - `reeferStateZone1`: The state of the reefer in zone 1. For single zone
                reefers, this applies tot he single zone. Only supported on multizone reefer
                solutions.
              - `reeferStateZone2`: The state of the reefer in zone 2. Only supported on
                multizone reefer solutions.
              - `reeferStateZone3`: The state of the reefer in zone 3. Only supported on
                multizone reefer solutions.
              - `reeferRunMode`: The operational mode of the reefer (`Start/Stop`,
                `Continuous`)
              - `reeferAlarms`: Any alarms that are present on the reefer. Only supported on
                reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1
                of the reefer in millidegrees Celsius. For single zone reefers, this applies
                to the single zone. Only supported on multizone reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of
                the reefer in millidegrees Celsius. For single zone reefers, this applies to
                the single zone. Only supported on multizone reefer solutions.
              - `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single
                zone reefers, this applies to the single zone.
              - `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only
                supported on multizone reefer solutions.
              - `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only
                supported on multizone reefer solutions.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          decorations: Decorations add to the primary stats listed in the `types` parameter. For
              example, if you wish to know the trailer's location whenever the odometer
              updates, you may set `types=gpsOdometerMeters&decorations=gps`.

              You may list **up to 2** types using comma-separated format. If multiple stats
              are listed in the types parameter, the decorations will be added to each type.
              For example:
              `types=reeferStateZone1,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters&decorations=gps`
              will list GPS decorations for each reeferStateZone1 reading, each
              reeferAmbientAirTemperatureMilliC reding, and gpsOdometerMeters reading.

              Note that decorations may significantly increase the response payload size.

              - `gps`: GPS data including lat/long, heading, speed, and a reverse geocode
                address.
              - `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must
                provide a manual odometer reading before this value is updated. Manual
                odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint
                or through the
                [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading).
                Odometer readings wthat are manually set will update as GPS trip data is
                gathered.
              - `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of
                the reefer in millidegree Celsius.
              - `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run
                according to onboard diagnostics. Only supported on reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air
                temperature zone 1 in millidegrees Celsius. For single zone reefers, this
                applies to the single zone. Only supported on multizone reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air
                temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air
                temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferFuelPercent`: The fuel level of the reefer unit in percentage points
                (e.g. `99`, `50`, etc). Only supported on reefer solutions.
              - `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only
                supported on multizone Carrier reefer solutions.
              - `reeferStateZone1`: The state of the reefer in zone 1. For single zone
                reefers, this applies tot he single zone. Only supported on multizone reefer
                solutions.
              - `reeferStateZone2`: The state of the reefer in zone 2. Only supported on
                multizone reefer solutions.
              - `reeferStateZone3`: The state of the reefer in zone 3. Only supported on
                multizone reefer solutions.
              - `reeferRunMode`: The operational mode of the reefer (`Start/Stop`,
                `Continuous`)
              - `reeferAlarms`: Any alarms that are present on the reefer. Only supported on
                reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1
                of the reefer in millidegrees Celsius. For single zone reefers, this applies
                to the single zone. Only supported on multizone reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of
                the reefer in millidegrees Celsius. For single zone reefers, this applies to
                the single zone. Only supported on multizone reefer solutions.
              - `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single
                zone reefers, this applies to the single zone.
              - `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only
                supported on multizone reefer solutions.
              - `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only
                supported on multizone reefer solutions.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          trailer_ids: A filter on the data based on this comma-separated list of trailer IDs and
              externalIds. Example: `trailerIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/beta/fleet/trailers/stats/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "start_time": start_time,
                        "types": types,
                        "after": after,
                        "decorations": decorations,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "trailer_ids": trailer_ids,
                    },
                    stat_history_params.StatHistoryParams,
                ),
            ),
            cast_to=StatHistoryResponse,
        )


class AsyncStatsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncStatsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        types: str,
        after: str | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        time: str | NotGiven = NOT_GIVEN,
        trailer_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatListResponse:
        """Returns the last known stats of all trailers at the given `time`.

        If no `time`
        is specified, the current time is used.

        <b>Rate limit:</b> 25 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Trailer Statistics** under the Trailers
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
          types: The stat types you want this endpoint to return information on.

              You may list **up to 3** types using comma-separated format. For example:
              `types=gps,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters`.

              - `gps`: GPS data including lat/long, heading, speed, and a reverse geocode
                address.
              - `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must
                provide a manual odometer reading before this value is updated. Manual
                odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint
                or through the
                [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading).
                Odometer readings wthat are manually set will update as GPS trip data is
                gathered.
              - `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of
                the reefer in millidegree Celsius.
              - `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run
                according to onboard diagnostics. Only supported on reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air
                temperature zone 1 in millidegrees Celsius. For single zone reefers, this
                applies to the single zone. Only supported on multizone reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air
                temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air
                temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferFuelPercent`: The fuel level of the reefer unit in percentage points
                (e.g. `99`, `50`, etc). Only supported on reefer solutions.
              - `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only
                supported on multizone Carrier reefer solutions.
              - `reeferStateZone1`: The state of the reefer in zone 1. For single zone
                reefers, this applies tot he single zone. Only supported on multizone reefer
                solutions.
              - `reeferStateZone2`: The state of the reefer in zone 2. Only supported on
                multizone reefer solutions.
              - `reeferStateZone3`: The state of the reefer in zone 3. Only supported on
                multizone reefer solutions.
              - `reeferRunMode`: The operational mode of the reefer (`Start/Stop`,
                `Continuous`)
              - `reeferAlarms`: Any alarms that are present on the reefer. Only supported on
                reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1
                of the reefer in millidegrees Celsius. For single zone reefers, this applies
                to the single zone. Only supported on multizone reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of
                the reefer in millidegrees Celsius. For single zone reefers, this applies to
                the single zone. Only supported on multizone reefer solutions.
              - `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single
                zone reefers, this applies to the single zone.
              - `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only
                supported on multizone reefer solutions.
              - `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only
                supported on multizone reefer solutions.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          time: A filter on the data that returns the last known data points with timestamps
              less than or equal to this value. Defaults to now if not provided. Must be a
              string in RFC 3339 Format. Millisecond precision and timezones are supported.

          trailer_ids: A filter on the data based on this comma-separated list of trailer IDs and
              externalIds. Example: `trailerIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/beta/fleet/trailers/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "types": types,
                        "after": after,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "time": time,
                        "trailer_ids": trailer_ids,
                    },
                    stat_list_params.StatListParams,
                ),
            ),
            cast_to=StatListResponse,
        )

    async def feed(
        self,
        *,
        types: str,
        after: str | NotGiven = NOT_GIVEN,
        decorations: str | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        trailer_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatFeedResponse:
        """
        Follow a feed of trailer stats.

        The first call to this endpoint will provide the most recent stats for each
        trailer and an `endCursor`.

        Providing the `endCursor` value to the `after` query parameter will fetch all
        updates since the previous API call.

        If `hasNextPage` is false, no new data is immediately available. Please wait a
        minimum of 5 seconds before making a subsequent request.

        <b>Rate limit:</b> 25 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Trailer Statistics** under the Trailers
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
          types: The stat types you want this endpoint to return information on.

              You may list **up to 3** types using comma-separated format. For example:
              `types=gps,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters`.

              - `gps`: GPS data including lat/long, heading, speed, and a reverse geocode
                address.
              - `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must
                provide a manual odometer reading before this value is updated. Manual
                odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint
                or through the
                [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading).
                Odometer readings wthat are manually set will update as GPS trip data is
                gathered.
              - `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of
                the reefer in millidegree Celsius.
              - `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run
                according to onboard diagnostics. Only supported on reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air
                temperature zone 1 in millidegrees Celsius. For single zone reefers, this
                applies to the single zone. Only supported on multizone reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air
                temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air
                temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferFuelPercent`: The fuel level of the reefer unit in percentage points
                (e.g. `99`, `50`, etc). Only supported on reefer solutions.
              - `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only
                supported on multizone Carrier reefer solutions.
              - `reeferStateZone1`: The state of the reefer in zone 1. For single zone
                reefers, this applies tot he single zone. Only supported on multizone reefer
                solutions.
              - `reeferStateZone2`: The state of the reefer in zone 2. Only supported on
                multizone reefer solutions.
              - `reeferStateZone3`: The state of the reefer in zone 3. Only supported on
                multizone reefer solutions.
              - `reeferRunMode`: The operational mode of the reefer (`Start/Stop`,
                `Continuous`)
              - `reeferAlarms`: Any alarms that are present on the reefer. Only supported on
                reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1
                of the reefer in millidegrees Celsius. For single zone reefers, this applies
                to the single zone. Only supported on multizone reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of
                the reefer in millidegrees Celsius. For single zone reefers, this applies to
                the single zone. Only supported on multizone reefer solutions.
              - `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single
                zone reefers, this applies to the single zone.
              - `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only
                supported on multizone reefer solutions.
              - `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only
                supported on multizone reefer solutions.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          decorations: Decorations add to the primary stats listed in the `types` parameter. For
              example, if you wish to know the trailer's location whenever the odometer
              updates, you may set `types=gpsOdometerMeters&decorations=gps`.

              You may list **up to 2** types using comma-separated format. If multiple stats
              are listed in the types parameter, the decorations will be added to each type.
              For example:
              `types=reeferStateZone1,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters&decorations=gps`
              will list GPS decorations for each reeferStateZone1 reading, each
              reeferAmbientAirTemperatureMilliC reding, and gpsOdometerMeters reading.

              Note that decorations may significantly increase the response payload size.

              - `gps`: GPS data including lat/long, heading, speed, and a reverse geocode
                address.
              - `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must
                provide a manual odometer reading before this value is updated. Manual
                odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint
                or through the
                [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading).
                Odometer readings wthat are manually set will update as GPS trip data is
                gathered.
              - `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of
                the reefer in millidegree Celsius.
              - `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run
                according to onboard diagnostics. Only supported on reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air
                temperature zone 1 in millidegrees Celsius. For single zone reefers, this
                applies to the single zone. Only supported on multizone reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air
                temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air
                temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferFuelPercent`: The fuel level of the reefer unit in percentage points
                (e.g. `99`, `50`, etc). Only supported on reefer solutions.
              - `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only
                supported on multizone Carrier reefer solutions.
              - `reeferStateZone1`: The state of the reefer in zone 1. For single zone
                reefers, this applies tot he single zone. Only supported on multizone reefer
                solutions.
              - `reeferStateZone2`: The state of the reefer in zone 2. Only supported on
                multizone reefer solutions.
              - `reeferStateZone3`: The state of the reefer in zone 3. Only supported on
                multizone reefer solutions.
              - `reeferRunMode`: The operational mode of the reefer (`Start/Stop`,
                `Continuous`)
              - `reeferAlarms`: Any alarms that are present on the reefer. Only supported on
                reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1
                of the reefer in millidegrees Celsius. For single zone reefers, this applies
                to the single zone. Only supported on multizone reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of
                the reefer in millidegrees Celsius. For single zone reefers, this applies to
                the single zone. Only supported on multizone reefer solutions.
              - `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single
                zone reefers, this applies to the single zone.
              - `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only
                supported on multizone reefer solutions.
              - `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only
                supported on multizone reefer solutions.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          trailer_ids: A filter on the data based on this comma-separated list of trailer IDs and
              externalIds. Example: `trailerIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/beta/fleet/trailers/stats/feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "types": types,
                        "after": after,
                        "decorations": decorations,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "trailer_ids": trailer_ids,
                    },
                    stat_feed_params.StatFeedParams,
                ),
            ),
            cast_to=StatFeedResponse,
        )

    async def history(
        self,
        *,
        end_time: str,
        start_time: str,
        types: str,
        after: str | NotGiven = NOT_GIVEN,
        decorations: str | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        trailer_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatHistoryResponse:
        """Returns trailer stats during the given time range for all trailers.

        This can be
        optionally filtered by tags or specific trailer IDs.

        <b>Rate limit:</b> 10 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Trailer Statistics** under the Trailers
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
          end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond
              precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
              2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          types: The stat types you want this endpoint to return information on.

              You may list **up to 3** types using comma-separated format. For example:
              `types=gps,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters`.

              - `gps`: GPS data including lat/long, heading, speed, and a reverse geocode
                address.
              - `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must
                provide a manual odometer reading before this value is updated. Manual
                odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint
                or through the
                [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading).
                Odometer readings wthat are manually set will update as GPS trip data is
                gathered.
              - `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of
                the reefer in millidegree Celsius.
              - `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run
                according to onboard diagnostics. Only supported on reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air
                temperature zone 1 in millidegrees Celsius. For single zone reefers, this
                applies to the single zone. Only supported on multizone reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air
                temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air
                temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferFuelPercent`: The fuel level of the reefer unit in percentage points
                (e.g. `99`, `50`, etc). Only supported on reefer solutions.
              - `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only
                supported on multizone Carrier reefer solutions.
              - `reeferStateZone1`: The state of the reefer in zone 1. For single zone
                reefers, this applies tot he single zone. Only supported on multizone reefer
                solutions.
              - `reeferStateZone2`: The state of the reefer in zone 2. Only supported on
                multizone reefer solutions.
              - `reeferStateZone3`: The state of the reefer in zone 3. Only supported on
                multizone reefer solutions.
              - `reeferRunMode`: The operational mode of the reefer (`Start/Stop`,
                `Continuous`)
              - `reeferAlarms`: Any alarms that are present on the reefer. Only supported on
                reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1
                of the reefer in millidegrees Celsius. For single zone reefers, this applies
                to the single zone. Only supported on multizone reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of
                the reefer in millidegrees Celsius. For single zone reefers, this applies to
                the single zone. Only supported on multizone reefer solutions.
              - `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single
                zone reefers, this applies to the single zone.
              - `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only
                supported on multizone reefer solutions.
              - `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only
                supported on multizone reefer solutions.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          decorations: Decorations add to the primary stats listed in the `types` parameter. For
              example, if you wish to know the trailer's location whenever the odometer
              updates, you may set `types=gpsOdometerMeters&decorations=gps`.

              You may list **up to 2** types using comma-separated format. If multiple stats
              are listed in the types parameter, the decorations will be added to each type.
              For example:
              `types=reeferStateZone1,reeferAmbientAirTemperatureMilliC,gpsOdometerMeters&decorations=gps`
              will list GPS decorations for each reeferStateZone1 reading, each
              reeferAmbientAirTemperatureMilliC reding, and gpsOdometerMeters reading.

              Note that decorations may significantly increase the response payload size.

              - `gps`: GPS data including lat/long, heading, speed, and a reverse geocode
                address.
              - `gpsOdometerMeters`: Odometer reading provided by GPS calculations. You must
                provide a manual odometer reading before this value is updated. Manual
                odometer readings can be provided via the PATCH /fleet/trailers/{id} endpoint
                or through the
                [cloud dashboard](https://kb.samsara.com/hc/en-us/articles/115005273667-Editing-Odometer-Reading).
                Odometer readings wthat are manually set will update as GPS trip data is
                gathered.
              - `reeferAmbientAirTemperatureMilliC`: The ambient air temperature reading of
                the reefer in millidegree Celsius.
              - `reeferObdEngineSeconds`: The cumulative number of seconds the reefer has run
                according to onboard diagnostics. Only supported on reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone1`: The supply or discharge air
                temperature zone 1 in millidegrees Celsius. For single zone reefers, this
                applies to the single zone. Only supported on multizone reefer solutions.
              - `reeferSupplyAirTemperatureMilliCZone2`: The supply or discharge air
                temperature zone 2 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSupplyAirTemperatureMilliCZone3`: The supply or discharge air
                temperature zone 3 in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferFuelPercent`: The fuel level of the reefer unit in percentage points
                (e.g. `99`, `50`, etc). Only supported on reefer solutions.
              - `carrierReeferState`: The overall state of the reefer (`Off`, `On`). Only
                supported on multizone Carrier reefer solutions.
              - `reeferStateZone1`: The state of the reefer in zone 1. For single zone
                reefers, this applies tot he single zone. Only supported on multizone reefer
                solutions.
              - `reeferStateZone2`: The state of the reefer in zone 2. Only supported on
                multizone reefer solutions.
              - `reeferStateZone3`: The state of the reefer in zone 3. Only supported on
                multizone reefer solutions.
              - `reeferRunMode`: The operational mode of the reefer (`Start/Stop`,
                `Continuous`)
              - `reeferAlarms`: Any alarms that are present on the reefer. Only supported on
                reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone1`: The return air temperature in zone 1
                of the reefer in millidegrees Celsius. For single zone reefers, this applies
                to the single zone. Only supported on multizone reefer solutions.
              - `reeferReturnAirTemperatureMilliCZone2`: The return air temperature in zone 2
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferReturnAirTemperatureMilliCZone3`: The return air temperature in zone 3
                of the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone1`: The set point temperature in zone 1 of
                the reefer in millidegrees Celsius. For single zone reefers, this applies to
                the single zone. Only supported on multizone reefer solutions.
              - `reeferSetPointTemperatureMilliCZone2`: The set point temperature in zone 2 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferSetPointTemperatureMilliCZone3`: The set point temperature in zone 3 of
                the reefer in millidegrees Celsius. Only supported on multizone reefer
                solutions.
              - `reeferDoorStateZone1`: The door status in zone 1 of the reefer. For single
                zone reefers, this applies to the single zone.
              - `reeferDoorStateZone2`: The door status in zone 2 of the reefer. Only
                supported on multizone reefer solutions.
              - `reeferDoorStateZone3`: The door status in zone 3 of the reefer. Only
                supported on multizone reefer solutions.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          trailer_ids: A filter on the data based on this comma-separated list of trailer IDs and
              externalIds. Example: `trailerIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/beta/fleet/trailers/stats/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_time": end_time,
                        "start_time": start_time,
                        "types": types,
                        "after": after,
                        "decorations": decorations,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "trailer_ids": trailer_ids,
                    },
                    stat_history_params.StatHistoryParams,
                ),
            ),
            cast_to=StatHistoryResponse,
        )


class StatsResourceWithRawResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.list = to_raw_response_wrapper(
            stats.list,
        )
        self.feed = to_raw_response_wrapper(
            stats.feed,
        )
        self.history = to_raw_response_wrapper(
            stats.history,
        )


class AsyncStatsResourceWithRawResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

        self.list = async_to_raw_response_wrapper(
            stats.list,
        )
        self.feed = async_to_raw_response_wrapper(
            stats.feed,
        )
        self.history = async_to_raw_response_wrapper(
            stats.history,
        )


class StatsResourceWithStreamingResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.list = to_streamed_response_wrapper(
            stats.list,
        )
        self.feed = to_streamed_response_wrapper(
            stats.feed,
        )
        self.history = to_streamed_response_wrapper(
            stats.history,
        )


class AsyncStatsResourceWithStreamingResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

        self.list = async_to_streamed_response_wrapper(
            stats.list,
        )
        self.feed = async_to_streamed_response_wrapper(
            stats.feed,
        )
        self.history = async_to_streamed_response_wrapper(
            stats.history,
        )
