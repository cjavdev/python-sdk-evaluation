# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.fleet.settings import driver_app_update_params
from ....types.fleet.settings.settings_get_driver_app_settings_response_body import (
    SettingsGetDriverAppSettingsResponseBody,
)
from ....types.fleet.settings.settings_patch_driver_app_settings_response_body import (
    SettingsPatchDriverAppSettingsResponseBody,
)

__all__ = ["DriverAppResource", "AsyncDriverAppResource"]


class DriverAppResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DriverAppResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DriverAppResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DriverAppResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DriverAppResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingsGetDriverAppSettingsResponseBody:
        """
        Get driver app settings.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Driver App Settings** under the Drivers
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
        """
        return self._get(
            "/fleet/settings/driver-app",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsGetDriverAppSettingsResponseBody,
        )

    def update(
        self,
        *,
        driver_fleet_id: str | NotGiven = NOT_GIVEN,
        gamification: bool | NotGiven = NOT_GIVEN,
        gamification_config: driver_app_update_params.GamificationConfig | NotGiven = NOT_GIVEN,
        org_vehicle_search: bool | NotGiven = NOT_GIVEN,
        trailer_selection: bool | NotGiven = NOT_GIVEN,
        trailer_selection_config: driver_app_update_params.TrailerSelectionConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingsPatchDriverAppSettingsResponseBody:
        """
        Update driver app settings.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Driver App Settings** under the Drivers
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
          driver_fleet_id: Global login user name for the fleet driver app

          gamification: Driver gamification feature. Enabling this will turn on the feature for all
              drivers using the mobile app. Drivers can be configured into peer groups within
              the Drivers Page. Unconfigured drivers will be grouped on an organization level.

          gamification_config: Gamification configuration for the Driver App.

          org_vehicle_search: Allow drivers to search for vehicles outside of their selection tag when
              connected to the internet.

          trailer_selection: Allow drivers to see and select trailers in the Samsara Driver app.

          trailer_selection_config: Trailer selection setting configuration for the Driver App.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/fleet/settings/driver-app",
            body=maybe_transform(
                {
                    "driver_fleet_id": driver_fleet_id,
                    "gamification": gamification,
                    "gamification_config": gamification_config,
                    "org_vehicle_search": org_vehicle_search,
                    "trailer_selection": trailer_selection,
                    "trailer_selection_config": trailer_selection_config,
                },
                driver_app_update_params.DriverAppUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsPatchDriverAppSettingsResponseBody,
        )


class AsyncDriverAppResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDriverAppResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDriverAppResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDriverAppResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDriverAppResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingsGetDriverAppSettingsResponseBody:
        """
        Get driver app settings.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Driver App Settings** under the Drivers
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
        """
        return await self._get(
            "/fleet/settings/driver-app",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsGetDriverAppSettingsResponseBody,
        )

    async def update(
        self,
        *,
        driver_fleet_id: str | NotGiven = NOT_GIVEN,
        gamification: bool | NotGiven = NOT_GIVEN,
        gamification_config: driver_app_update_params.GamificationConfig | NotGiven = NOT_GIVEN,
        org_vehicle_search: bool | NotGiven = NOT_GIVEN,
        trailer_selection: bool | NotGiven = NOT_GIVEN,
        trailer_selection_config: driver_app_update_params.TrailerSelectionConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingsPatchDriverAppSettingsResponseBody:
        """
        Update driver app settings.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Driver App Settings** under the Drivers
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
          driver_fleet_id: Global login user name for the fleet driver app

          gamification: Driver gamification feature. Enabling this will turn on the feature for all
              drivers using the mobile app. Drivers can be configured into peer groups within
              the Drivers Page. Unconfigured drivers will be grouped on an organization level.

          gamification_config: Gamification configuration for the Driver App.

          org_vehicle_search: Allow drivers to search for vehicles outside of their selection tag when
              connected to the internet.

          trailer_selection: Allow drivers to see and select trailers in the Samsara Driver app.

          trailer_selection_config: Trailer selection setting configuration for the Driver App.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/fleet/settings/driver-app",
            body=await async_maybe_transform(
                {
                    "driver_fleet_id": driver_fleet_id,
                    "gamification": gamification,
                    "gamification_config": gamification_config,
                    "org_vehicle_search": org_vehicle_search,
                    "trailer_selection": trailer_selection,
                    "trailer_selection_config": trailer_selection_config,
                },
                driver_app_update_params.DriverAppUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsPatchDriverAppSettingsResponseBody,
        )


class DriverAppResourceWithRawResponse:
    def __init__(self, driver_app: DriverAppResource) -> None:
        self._driver_app = driver_app

        self.retrieve = to_raw_response_wrapper(
            driver_app.retrieve,
        )
        self.update = to_raw_response_wrapper(
            driver_app.update,
        )


class AsyncDriverAppResourceWithRawResponse:
    def __init__(self, driver_app: AsyncDriverAppResource) -> None:
        self._driver_app = driver_app

        self.retrieve = async_to_raw_response_wrapper(
            driver_app.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            driver_app.update,
        )


class DriverAppResourceWithStreamingResponse:
    def __init__(self, driver_app: DriverAppResource) -> None:
        self._driver_app = driver_app

        self.retrieve = to_streamed_response_wrapper(
            driver_app.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            driver_app.update,
        )


class AsyncDriverAppResourceWithStreamingResponse:
    def __init__(self, driver_app: AsyncDriverAppResource) -> None:
        self._driver_app = driver_app

        self.retrieve = async_to_streamed_response_wrapper(
            driver_app.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            driver_app.update,
        )
