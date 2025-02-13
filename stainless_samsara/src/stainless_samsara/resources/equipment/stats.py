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
from ..._base_client import make_request_options
from ...types.equipment import stat_feed_params, stat_history_params, stat_retrieve_params
from ...types.equipment.stat_feed_response import StatFeedResponse
from ...types.equipment.stat_history_response import StatHistoryResponse
from ...types.equipment.stat_retrieve_response import StatRetrieveResponse

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

    def retrieve(
        self,
        *,
        types: List[
            Literal[
                "gatewayEngineStates",
                "obdEngineStates",
                "fuelPercents",
                "engineRpm",
                "gatewayEngineSeconds",
                "obdEngineSeconds",
                "gatewayJ1939EngineSeconds",
                "gpsOdometerMeters",
                "gps",
            ]
        ],
        after: str | NotGiven = NOT_GIVEN,
        equipment_ids: List[str] | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatRetrieveResponse:
        """Returns the last known stats for all equipment.

        This can be optionally filtered
        by tags or specific equipment IDs.

        <b>Rate limit:</b> 150 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Equipment Statistics** under the Equipment
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          types: The types of equipment stats you want to query. Currently, you may submit up to
              3 types.

              - `engineRpm`: The revolutions per minute of the engine.
              - `fuelPercents`: The percent of fuel in the unit of equipment.
              - `obdEngineSeconds`: The number of seconds the engine has been running since it
                was new. This value is provided directly from on-board diagnostics.
              - `gatewayEngineSeconds`: An approximation of the number of seconds the engine
                has been running since it was new, based on the amount of time the asset
                gateway has been receiving power with an offset provided manually through the
                Samsara cloud dashboard. This is supported with the following hardware
                configurations:
                - AG24/AG26/AG46P + APWR cable
                  ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d)
                  required)
                - AG52 + BPWR/BEQP cable
                  ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d)
                  required).
              - `gatewayJ1939EngineSeconds`: An approximation of the number of seconds the
                engine has been running since it was new, based on the amount of time the AG26
                device is receiving power via J1939/CAT cable and an offset provided manually
                through the Samsara cloud dashboard.
              - `obdEngineStates`: The state of the engine read from on-board diagnostics. Can
                be `Off`, `On`, or `Idle`.
              - `gatewayEngineStates`: An approximation of engine state based on readings the
                AG26 receives from the aux/digio cable. Can be `Off` or `On`.
              - `gpsOdometerMeters`: An approximation of odometer reading based on GPS
                calculations since the AG26 was activated, and a manual odometer offset
                provided in the Samsara cloud dashboard. Valid values: `Off`, `On`.
              - `gps`: GPS data including lat/long, heading, speed, address book entry (if
                exists), and a reverse geocoded address.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          equipment_ids: A filter on the data based on this comma-separated list of equipment IDs.
              Example: `equipmentIds=1234,5678`

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
            "/fleet/equipment/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "types": types,
                        "after": after,
                        "equipment_ids": equipment_ids,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    stat_retrieve_params.StatRetrieveParams,
                ),
            ),
            cast_to=StatRetrieveResponse,
        )

    def feed(
        self,
        *,
        types: List[
            Literal[
                "gatewayEngineStates",
                "obdEngineStates",
                "fuelPercents",
                "engineRpm",
                "gatewayEngineSeconds",
                "obdEngineSeconds",
                "gatewayJ1939EngineSeconds",
                "gpsOdometerMeters",
                "gps",
            ]
        ],
        after: str | NotGiven = NOT_GIVEN,
        equipment_ids: List[str] | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatFeedResponse:
        """
        Follow a continuous feed of all equipment stats from Samsara AG26s.

        Your first call to this endpoint will provide you with the most recent stats for
        each unit of equipment and a `pagination` object that contains an `endCursor`.

        You can provide the `endCursor` to subsequent calls via the `after` parameter.
        The response will contain any equipment stats updates since that `endCursor`.

        If `hasNextPage` is `false`, no updates are readily available yet. Each stat
        type has a different refresh rate, but in general we'd suggest waiting a minimum
        of 5 seconds before requesting updates.

        <b>Rate limit:</b> 150 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Equipment Statistics** under the Equipment
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          types: The types of equipment stats you want to query. Currently, you may submit up to
              3 types.

              - `engineRpm`: The revolutions per minute of the engine.
              - `fuelPercents`: The percent of fuel in the unit of equipment.
              - `obdEngineSeconds`: The number of seconds the engine has been running since it
                was new. This value is provided directly from on-board diagnostics.
              - `gatewayEngineSeconds`: An approximation of the number of seconds the engine
                has been running since it was new, based on the amount of time the asset
                gateway has been receiving power with an offset provided manually through the
                Samsara cloud dashboard. This is supported with the following hardware
                configurations:
                - AG24/AG26/AG46P + APWR cable
                  ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d)
                  required)
                - AG52 + BPWR/BEQP cable
                  ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d)
                  required).
              - `gatewayJ1939EngineSeconds`: An approximation of the number of seconds the
                engine has been running since it was new, based on the amount of time the AG26
                device is receiving power via J1939/CAT cable and an offset provided manually
                through the Samsara cloud dashboard.
              - `obdEngineStates`: The state of the engine read from on-board diagnostics. Can
                be `Off`, `On`, or `Idle`.
              - `gatewayEngineStates`: An approximation of engine state based on readings the
                AG26 receives from the aux/digio cable. Can be `Off` or `On`.
              - `gpsOdometerMeters`: An approximation of odometer reading based on GPS
                calculations since the AG26 was activated, and a manual odometer offset
                provided in the Samsara cloud dashboard. Valid values: `Off`, `On`.
              - `gps`: GPS data including lat/long, heading, speed, address book entry (if
                exists), and a reverse geocoded address.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          equipment_ids: A filter on the data based on this comma-separated list of equipment IDs.
              Example: `equipmentIds=1234,5678`

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
            "/fleet/equipment/stats/feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "types": types,
                        "after": after,
                        "equipment_ids": equipment_ids,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
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
        types: List[
            Literal[
                "gatewayEngineStates",
                "obdEngineStates",
                "fuelPercents",
                "engineRpm",
                "gatewayEngineSeconds",
                "obdEngineSeconds",
                "gatewayJ1939EngineSeconds",
                "gpsOdometerMeters",
                "gps",
            ]
        ],
        after: str | NotGiven = NOT_GIVEN,
        equipment_ids: List[str] | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatHistoryResponse:
        """Returns historical equipment status during the given time range.

        This can be
        optionally filtered by tags or specific equipment IDs.

        <b>Rate limit:</b> 150 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Equipment Statistics** under the Equipment
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          end_time: An end time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          start_time: A start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          types: The types of equipment stats you want to query. Currently, you may submit up to
              3 types.

              - `engineRpm`: The revolutions per minute of the engine.
              - `fuelPercents`: The percent of fuel in the unit of equipment.
              - `obdEngineSeconds`: The number of seconds the engine has been running since it
                was new. This value is provided directly from on-board diagnostics.
              - `gatewayEngineSeconds`: An approximation of the number of seconds the engine
                has been running since it was new, based on the amount of time the asset
                gateway has been receiving power with an offset provided manually through the
                Samsara cloud dashboard. This is supported with the following hardware
                configurations:
                - AG24/AG26/AG46P + APWR cable
                  ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d)
                  required)
                - AG52 + BPWR/BEQP cable
                  ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d)
                  required).
              - `gatewayJ1939EngineSeconds`: An approximation of the number of seconds the
                engine has been running since it was new, based on the amount of time the AG26
                device is receiving power via J1939/CAT cable and an offset provided manually
                through the Samsara cloud dashboard.
              - `obdEngineStates`: The state of the engine read from on-board diagnostics. Can
                be `Off`, `On`, or `Idle`.
              - `gatewayEngineStates`: An approximation of engine state based on readings the
                AG26 receives from the aux/digio cable. Can be `Off` or `On`.
              - `gpsOdometerMeters`: An approximation of odometer reading based on GPS
                calculations since the AG26 was activated, and a manual odometer offset
                provided in the Samsara cloud dashboard. Valid values: `Off`, `On`.
              - `gps`: GPS data including lat/long, heading, speed, address book entry (if
                exists), and a reverse geocoded address.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          equipment_ids: A filter on the data based on this comma-separated list of equipment IDs.
              Example: `equipmentIds=1234,5678`

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
            "/fleet/equipment/stats/history",
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
                        "equipment_ids": equipment_ids,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
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

    async def retrieve(
        self,
        *,
        types: List[
            Literal[
                "gatewayEngineStates",
                "obdEngineStates",
                "fuelPercents",
                "engineRpm",
                "gatewayEngineSeconds",
                "obdEngineSeconds",
                "gatewayJ1939EngineSeconds",
                "gpsOdometerMeters",
                "gps",
            ]
        ],
        after: str | NotGiven = NOT_GIVEN,
        equipment_ids: List[str] | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatRetrieveResponse:
        """Returns the last known stats for all equipment.

        This can be optionally filtered
        by tags or specific equipment IDs.

        <b>Rate limit:</b> 150 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Equipment Statistics** under the Equipment
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          types: The types of equipment stats you want to query. Currently, you may submit up to
              3 types.

              - `engineRpm`: The revolutions per minute of the engine.
              - `fuelPercents`: The percent of fuel in the unit of equipment.
              - `obdEngineSeconds`: The number of seconds the engine has been running since it
                was new. This value is provided directly from on-board diagnostics.
              - `gatewayEngineSeconds`: An approximation of the number of seconds the engine
                has been running since it was new, based on the amount of time the asset
                gateway has been receiving power with an offset provided manually through the
                Samsara cloud dashboard. This is supported with the following hardware
                configurations:
                - AG24/AG26/AG46P + APWR cable
                  ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d)
                  required)
                - AG52 + BPWR/BEQP cable
                  ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d)
                  required).
              - `gatewayJ1939EngineSeconds`: An approximation of the number of seconds the
                engine has been running since it was new, based on the amount of time the AG26
                device is receiving power via J1939/CAT cable and an offset provided manually
                through the Samsara cloud dashboard.
              - `obdEngineStates`: The state of the engine read from on-board diagnostics. Can
                be `Off`, `On`, or `Idle`.
              - `gatewayEngineStates`: An approximation of engine state based on readings the
                AG26 receives from the aux/digio cable. Can be `Off` or `On`.
              - `gpsOdometerMeters`: An approximation of odometer reading based on GPS
                calculations since the AG26 was activated, and a manual odometer offset
                provided in the Samsara cloud dashboard. Valid values: `Off`, `On`.
              - `gps`: GPS data including lat/long, heading, speed, address book entry (if
                exists), and a reverse geocoded address.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          equipment_ids: A filter on the data based on this comma-separated list of equipment IDs.
              Example: `equipmentIds=1234,5678`

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
            "/fleet/equipment/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "types": types,
                        "after": after,
                        "equipment_ids": equipment_ids,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    stat_retrieve_params.StatRetrieveParams,
                ),
            ),
            cast_to=StatRetrieveResponse,
        )

    async def feed(
        self,
        *,
        types: List[
            Literal[
                "gatewayEngineStates",
                "obdEngineStates",
                "fuelPercents",
                "engineRpm",
                "gatewayEngineSeconds",
                "obdEngineSeconds",
                "gatewayJ1939EngineSeconds",
                "gpsOdometerMeters",
                "gps",
            ]
        ],
        after: str | NotGiven = NOT_GIVEN,
        equipment_ids: List[str] | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatFeedResponse:
        """
        Follow a continuous feed of all equipment stats from Samsara AG26s.

        Your first call to this endpoint will provide you with the most recent stats for
        each unit of equipment and a `pagination` object that contains an `endCursor`.

        You can provide the `endCursor` to subsequent calls via the `after` parameter.
        The response will contain any equipment stats updates since that `endCursor`.

        If `hasNextPage` is `false`, no updates are readily available yet. Each stat
        type has a different refresh rate, but in general we'd suggest waiting a minimum
        of 5 seconds before requesting updates.

        <b>Rate limit:</b> 150 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Equipment Statistics** under the Equipment
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          types: The types of equipment stats you want to query. Currently, you may submit up to
              3 types.

              - `engineRpm`: The revolutions per minute of the engine.
              - `fuelPercents`: The percent of fuel in the unit of equipment.
              - `obdEngineSeconds`: The number of seconds the engine has been running since it
                was new. This value is provided directly from on-board diagnostics.
              - `gatewayEngineSeconds`: An approximation of the number of seconds the engine
                has been running since it was new, based on the amount of time the asset
                gateway has been receiving power with an offset provided manually through the
                Samsara cloud dashboard. This is supported with the following hardware
                configurations:
                - AG24/AG26/AG46P + APWR cable
                  ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d)
                  required)
                - AG52 + BPWR/BEQP cable
                  ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d)
                  required).
              - `gatewayJ1939EngineSeconds`: An approximation of the number of seconds the
                engine has been running since it was new, based on the amount of time the AG26
                device is receiving power via J1939/CAT cable and an offset provided manually
                through the Samsara cloud dashboard.
              - `obdEngineStates`: The state of the engine read from on-board diagnostics. Can
                be `Off`, `On`, or `Idle`.
              - `gatewayEngineStates`: An approximation of engine state based on readings the
                AG26 receives from the aux/digio cable. Can be `Off` or `On`.
              - `gpsOdometerMeters`: An approximation of odometer reading based on GPS
                calculations since the AG26 was activated, and a manual odometer offset
                provided in the Samsara cloud dashboard. Valid values: `Off`, `On`.
              - `gps`: GPS data including lat/long, heading, speed, address book entry (if
                exists), and a reverse geocoded address.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          equipment_ids: A filter on the data based on this comma-separated list of equipment IDs.
              Example: `equipmentIds=1234,5678`

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
            "/fleet/equipment/stats/feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "types": types,
                        "after": after,
                        "equipment_ids": equipment_ids,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
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
        types: List[
            Literal[
                "gatewayEngineStates",
                "obdEngineStates",
                "fuelPercents",
                "engineRpm",
                "gatewayEngineSeconds",
                "obdEngineSeconds",
                "gatewayJ1939EngineSeconds",
                "gpsOdometerMeters",
                "gps",
            ]
        ],
        after: str | NotGiven = NOT_GIVEN,
        equipment_ids: List[str] | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatHistoryResponse:
        """Returns historical equipment status during the given time range.

        This can be
        optionally filtered by tags or specific equipment IDs.

        <b>Rate limit:</b> 150 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Equipment Statistics** under the Equipment
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          end_time: An end time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          start_time: A start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          types: The types of equipment stats you want to query. Currently, you may submit up to
              3 types.

              - `engineRpm`: The revolutions per minute of the engine.
              - `fuelPercents`: The percent of fuel in the unit of equipment.
              - `obdEngineSeconds`: The number of seconds the engine has been running since it
                was new. This value is provided directly from on-board diagnostics.
              - `gatewayEngineSeconds`: An approximation of the number of seconds the engine
                has been running since it was new, based on the amount of time the asset
                gateway has been receiving power with an offset provided manually through the
                Samsara cloud dashboard. This is supported with the following hardware
                configurations:
                - AG24/AG26/AG46P + APWR cable
                  ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d)
                  required)
                - AG52 + BPWR/BEQP cable
                  ([Auxiliary engine configuration](https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs#UUID-d514abff-d10a-efaf-35d9-e10fa6c4888d)
                  required).
              - `gatewayJ1939EngineSeconds`: An approximation of the number of seconds the
                engine has been running since it was new, based on the amount of time the AG26
                device is receiving power via J1939/CAT cable and an offset provided manually
                through the Samsara cloud dashboard.
              - `obdEngineStates`: The state of the engine read from on-board diagnostics. Can
                be `Off`, `On`, or `Idle`.
              - `gatewayEngineStates`: An approximation of engine state based on readings the
                AG26 receives from the aux/digio cable. Can be `Off` or `On`.
              - `gpsOdometerMeters`: An approximation of odometer reading based on GPS
                calculations since the AG26 was activated, and a manual odometer offset
                provided in the Samsara cloud dashboard. Valid values: `Off`, `On`.
              - `gps`: GPS data including lat/long, heading, speed, address book entry (if
                exists), and a reverse geocoded address.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          equipment_ids: A filter on the data based on this comma-separated list of equipment IDs.
              Example: `equipmentIds=1234,5678`

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
            "/fleet/equipment/stats/history",
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
                        "equipment_ids": equipment_ids,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    stat_history_params.StatHistoryParams,
                ),
            ),
            cast_to=StatHistoryResponse,
        )


class StatsResourceWithRawResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.retrieve = to_raw_response_wrapper(
            stats.retrieve,
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

        self.retrieve = async_to_raw_response_wrapper(
            stats.retrieve,
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

        self.retrieve = to_streamed_response_wrapper(
            stats.retrieve,
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

        self.retrieve = async_to_streamed_response_wrapper(
            stats.retrieve,
        )
        self.feed = async_to_streamed_response_wrapper(
            stats.feed,
        )
        self.history = async_to_streamed_response_wrapper(
            stats.history,
        )
