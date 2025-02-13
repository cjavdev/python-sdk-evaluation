# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal

import httpx

from .hos import (
    HosResource,
    AsyncHosResource,
    HosResourceWithRawResponse,
    AsyncHosResourceWithRawResponse,
    HosResourceWithStreamingResponse,
    AsyncHosResourceWithStreamingResponse,
)
from .safety import (
    SafetyResource,
    AsyncSafetyResource,
    SafetyResourceWithRawResponse,
    AsyncSafetyResourceWithRawResponse,
    SafetyResourceWithStreamingResponse,
    AsyncSafetyResourceWithStreamingResponse,
)
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
from ....types.fleet import driver_list_params, driver_create_params, driver_update_params
from ...._base_client import make_request_options
from ....types.fleet.driver import Driver
from .tachograph_files.tachograph_files import (
    TachographFilesResource,
    AsyncTachographFilesResource,
    TachographFilesResourceWithRawResponse,
    AsyncTachographFilesResourceWithRawResponse,
    TachographFilesResourceWithStreamingResponse,
    AsyncTachographFilesResourceWithStreamingResponse,
)
from ....types.fleet.driver_list_response import DriverListResponse
from .tachograph_activity.tachograph_activity import (
    TachographActivityResource,
    AsyncTachographActivityResource,
    TachographActivityResourceWithRawResponse,
    AsyncTachographActivityResourceWithRawResponse,
    TachographActivityResourceWithStreamingResponse,
    AsyncTachographActivityResourceWithStreamingResponse,
)

__all__ = ["DriversResource", "AsyncDriversResource"]


class DriversResource(SyncAPIResource):
    @cached_property
    def tachograph_activity(self) -> TachographActivityResource:
        return TachographActivityResource(self._client)

    @cached_property
    def tachograph_files(self) -> TachographFilesResource:
        return TachographFilesResource(self._client)

    @cached_property
    def safety(self) -> SafetyResource:
        return SafetyResource(self._client)

    @cached_property
    def hos(self) -> HosResource:
        return HosResource(self._client)

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

    def create(
        self,
        *,
        name: str,
        password: str,
        username: str,
        attributes: Iterable[driver_create_params.Attribute] | NotGiven = NOT_GIVEN,
        carrier_settings: driver_create_params.CarrierSettings | NotGiven = NOT_GIVEN,
        current_id_card_code: str | NotGiven = NOT_GIVEN,
        eld_adverse_weather_exemption_enabled: bool | NotGiven = NOT_GIVEN,
        eld_big_day_exemption_enabled: bool | NotGiven = NOT_GIVEN,
        eld_day_start_hour: int | NotGiven = NOT_GIVEN,
        eld_exempt: bool | NotGiven = NOT_GIVEN,
        eld_exempt_reason: str | NotGiven = NOT_GIVEN,
        eld_pc_enabled: bool | NotGiven = NOT_GIVEN,
        eld_ym_enabled: bool | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        has_driving_features_hidden: bool | NotGiven = NOT_GIVEN,
        hos_setting: driver_create_params.HosSetting | NotGiven = NOT_GIVEN,
        license_number: str | NotGiven = NOT_GIVEN,
        license_state: str | NotGiven = NOT_GIVEN,
        locale: Literal["us", "at", "be", "ca", "gb", "fr", "de", "ie", "it", "lu", "mx", "nl", "es", "ch", "pr"]
        | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        peer_group_tag_id: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        static_assigned_vehicle_id: str | NotGiven = NOT_GIVEN,
        tachograph_card_number: str | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        timezone: str | NotGiven = NOT_GIVEN,
        us_driver_ruleset_override: driver_create_params.UsDriverRulesetOverride | NotGiven = NOT_GIVEN,
        vehicle_group_tag_id: str | NotGiven = NOT_GIVEN,
        waiting_time_duty_status_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Driver:
        """
        Add a driver to the organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Drivers** under the Drivers category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          name: Driver's name.

          password: Password that the driver can use to login to the Samsara driver app.

          username: Driver's login username into the driver app. The username may not contain spaces
              or the '@' symbol. The username must be unique.

          carrier_settings: Carrier for a given driver. If the driver's carrier differs from the general
              organization's carrier settings, the override value is used. Updating this value
              only updates the override setting for this driver.

          current_id_card_code: The ID Card Code on the back of the physical card assigned to the driver.
              Contact Samsara if you would like to enable this feature.

          eld_adverse_weather_exemption_enabled: Flag indicating this driver may use Adverse Weather exemptions in ELD logs.

          eld_big_day_exemption_enabled: Flag indicating this driver may use Big Day exemption in ELD logs.

          eld_day_start_hour: `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate
              noon-to-noon driving hours.

          eld_exempt: Flag indicating this driver is exempt from the Electronic Logging Mandate.

          eld_exempt_reason: Reason that this driver is exempt from the Electronic Logging Mandate (see
              eldExempt).

          eld_pc_enabled: Flag indicating this driver may select the Personal Conveyance duty status in
              ELD logs.

          eld_ym_enabled: Flag indicating this driver may select the Yard Move duty status in ELD logs.

          external_ids: The [external IDs](https://developers.samsara.com/docs/external-ids) for the
              given object.

          has_driving_features_hidden: A boolean indicating whether the driver has driving-related features hidden in
              the Driver App, including Vehicle selection, HOS, Routing, Team Driving,
              Documents, and Trip Logs. Default value is false if omitted. Note: only
              available to customers of Connected Forms.

          hos_setting: Hos settings for a driver.

          license_number: Driver's state issued license number. The combination of this number and
              `licenseState` must be unique.

          license_state: Abbreviation of US state, Canadian province, or US territory that issued
              driver's license.

          locale: Locale override (uncommon). These are specified by ISO 3166-2 country codes for
              supported locales. Valid values: `us`, `at`, `be`, `ca`, `gb`, `fr`, `de`, `ie`,
              `it`, `lu`, `mx`, `nl`, `es`, `ch`, `pr`.

          notes: Notes about the driver.

          peer_group_tag_id: The peer group tag id this driver belong to, used for gamification.

          phone: Phone number of the driver.

          static_assigned_vehicle_id: ID of vehicle that the driver is permanently assigned to. (uncommon).

          tachograph_card_number: Driver's assigned tachograph card number (Europe specific)

          tag_ids: IDs of tags the driver is associated with. If your access to the API is scoped
              by one or more tags, this field is required to pass in.

          timezone: Home terminal timezone, in order to indicate what time zone should be used to
              calculate the ELD logs. Driver timezones use
              [IANA timezone database](https://www.iana.org/time-zones) keys (e.g.
              `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find
              a mapping of common timezone formats to IANA timezone keys
              [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html).

          us_driver_ruleset_override: US Driver Ruleset override for a given driver. If the driver is operating under
              a ruleset different from the organization default, the override is used.
              Updating this value only updates the override setting for this driver.
              Explicitly setting this field to `null` will delete driver's ruleset override.
              If the driver does not have an override ruleset set, the response will not
              include any usDriverRulesetOverride information.

          vehicle_group_tag_id: Tag ID which determines which vehicles a driver will see when selecting
              vehicles.

          waiting_time_duty_status_enabled: Flag indicating this driver may select waiting time duty status in ELD logs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fleet/drivers",
            body=maybe_transform(
                {
                    "name": name,
                    "password": password,
                    "username": username,
                    "attributes": attributes,
                    "carrier_settings": carrier_settings,
                    "current_id_card_code": current_id_card_code,
                    "eld_adverse_weather_exemption_enabled": eld_adverse_weather_exemption_enabled,
                    "eld_big_day_exemption_enabled": eld_big_day_exemption_enabled,
                    "eld_day_start_hour": eld_day_start_hour,
                    "eld_exempt": eld_exempt,
                    "eld_exempt_reason": eld_exempt_reason,
                    "eld_pc_enabled": eld_pc_enabled,
                    "eld_ym_enabled": eld_ym_enabled,
                    "external_ids": external_ids,
                    "has_driving_features_hidden": has_driving_features_hidden,
                    "hos_setting": hos_setting,
                    "license_number": license_number,
                    "license_state": license_state,
                    "locale": locale,
                    "notes": notes,
                    "peer_group_tag_id": peer_group_tag_id,
                    "phone": phone,
                    "static_assigned_vehicle_id": static_assigned_vehicle_id,
                    "tachograph_card_number": tachograph_card_number,
                    "tag_ids": tag_ids,
                    "timezone": timezone,
                    "us_driver_ruleset_override": us_driver_ruleset_override,
                    "vehicle_group_tag_id": vehicle_group_tag_id,
                    "waiting_time_duty_status_enabled": waiting_time_duty_status_enabled,
                },
                driver_create_params.DriverCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Driver,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Driver:
        """
        Get information about a driver.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Drivers** under the Drivers category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/fleet/drivers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Driver,
        )

    def update(
        self,
        id: str,
        *,
        attributes: Iterable[driver_update_params.Attribute] | NotGiven = NOT_GIVEN,
        carrier_settings: driver_update_params.CarrierSettings | NotGiven = NOT_GIVEN,
        current_id_card_code: str | NotGiven = NOT_GIVEN,
        deactivated_at_time: str | NotGiven = NOT_GIVEN,
        driver_activation_status: Literal["active", "deactivated"] | NotGiven = NOT_GIVEN,
        eld_adverse_weather_exemption_enabled: bool | NotGiven = NOT_GIVEN,
        eld_big_day_exemption_enabled: bool | NotGiven = NOT_GIVEN,
        eld_day_start_hour: int | NotGiven = NOT_GIVEN,
        eld_exempt: bool | NotGiven = NOT_GIVEN,
        eld_exempt_reason: str | NotGiven = NOT_GIVEN,
        eld_pc_enabled: bool | NotGiven = NOT_GIVEN,
        eld_ym_enabled: bool | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        has_driving_features_hidden: bool | NotGiven = NOT_GIVEN,
        hos_setting: driver_update_params.HosSetting | NotGiven = NOT_GIVEN,
        license_number: str | NotGiven = NOT_GIVEN,
        license_state: str | NotGiven = NOT_GIVEN,
        locale: Literal["us", "at", "be", "ca", "gb", "fr", "de", "ie", "it", "lu", "mx", "nl", "es", "ch", "pr"]
        | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        peer_group_tag_id: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        static_assigned_vehicle_id: str | NotGiven = NOT_GIVEN,
        tachograph_card_number: str | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        timezone: str | NotGiven = NOT_GIVEN,
        us_driver_ruleset_override: driver_update_params.UsDriverRulesetOverride | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        vehicle_group_tag_id: str | NotGiven = NOT_GIVEN,
        waiting_time_duty_status_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Driver:
        """Update a specific driver's information.

        This can also be used to activate or
        de-activate a given driver by setting the driverActivationStatus field. If the
        driverActivationStatus field is 'deactivated' then the user can also specify the
        deactivatedAtTime. The deactivatedAtTime cannot be more than 6 months in the
        past and must not come before the dirver's latest active HOS log. It will be
        considered an error if deactivatedAtTime is provided with a
        driverActivationStatus of active.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Drivers** under the Drivers category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          carrier_settings: Carrier for a given driver. If the driver's carrier differs from the general
              organization's carrier settings, the override value is used. Updating this value
              only updates the override setting for this driver.

          current_id_card_code: The ID Card Code on the back of the physical card assigned to the driver.
              Contact Samsara if you would like to enable this feature.

          deactivated_at_time: The date and time this driver is considered to be deactivated in RFC 3339
              format.

          driver_activation_status:
              A value indicating whether the driver is active or deactivated. Valid values:
              `active`, `deactivated`.

          eld_adverse_weather_exemption_enabled: Flag indicating this driver may use Adverse Weather exemptions in ELD logs.

          eld_big_day_exemption_enabled: Flag indicating this driver may use Big Day exemption in ELD logs.

          eld_day_start_hour: `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate
              noon-to-noon driving hours.

          eld_exempt: Flag indicating this driver is exempt from the Electronic Logging Mandate.

          eld_exempt_reason: Reason that this driver is exempt from the Electronic Logging Mandate (see
              eldExempt).

          eld_pc_enabled: Flag indicating this driver may select the Personal Conveyance duty status in
              ELD logs.

          eld_ym_enabled: Flag indicating this driver may select the Yard Move duty status in ELD logs.

          external_ids: The [external IDs](https://developers.samsara.com/docs/external-ids) for the
              given object.

          has_driving_features_hidden: A boolean indicating whether the driver has driving-related features hidden in
              the Driver App, including Vehicle selection, HOS, Routing, Team Driving,
              Documents, and Trip Logs. Default value is false if omitted. Note: only
              available to customers of Connected Forms.

          hos_setting: Hos settings for a driver.

          license_number: Driver's state issued license number. The combination of this number and
              `licenseState` must be unique.

          license_state: Abbreviation of US state, Canadian province, or US territory that issued
              driver's license.

          locale: Locale override (uncommon). These are specified by ISO 3166-2 country codes for
              supported locales. Valid values: `us`, `at`, `be`, `ca`, `gb`, `fr`, `de`, `ie`,
              `it`, `lu`, `mx`, `nl`, `es`, `ch`, `pr`.

          name: Driver's name.

          notes: Notes about the driver.

          password: Password that the driver can use to login to the Samsara driver app.

          peer_group_tag_id: The peer group tag id this driver belong to, leave blank to be in group with
              everyone, used for gamification.

          phone: Phone number of the driver.

          static_assigned_vehicle_id: ID of vehicle that the driver is permanently assigned to. (uncommon).

          tachograph_card_number: Driver's assigned tachograph card number (Europe specific)

          tag_ids: IDs of tags the driver is associated with. If your access to the API is scoped
              by one or more tags, this field is required to pass in.

          timezone: Home terminal timezone, in order to indicate what time zone should be used to
              calculate the ELD logs. Driver timezones use
              [IANA timezone database](https://www.iana.org/time-zones) keys (e.g.
              `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find
              a mapping of common timezone formats to IANA timezone keys
              [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html).

          us_driver_ruleset_override: US Driver Ruleset override for a given driver. If the driver is operating under
              a ruleset different from the organization default, the override is used.
              Updating this value only updates the override setting for this driver.
              Explicitly setting this field to `null` will delete driver's ruleset override.
              If the driver does not have an override ruleset set, the response will not
              include any usDriverRulesetOverride information.

          username: Driver's login username into the driver app. The username may not contain spaces
              or the '@' symbol. The username must be unique.

          vehicle_group_tag_id: Tag ID which determines which vehicles a driver will see when selecting
              vehicles.

          waiting_time_duty_status_enabled: Flag indicating this driver may select waiting time duty status in ELD logs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/fleet/drivers/{id}",
            body=maybe_transform(
                {
                    "attributes": attributes,
                    "carrier_settings": carrier_settings,
                    "current_id_card_code": current_id_card_code,
                    "deactivated_at_time": deactivated_at_time,
                    "driver_activation_status": driver_activation_status,
                    "eld_adverse_weather_exemption_enabled": eld_adverse_weather_exemption_enabled,
                    "eld_big_day_exemption_enabled": eld_big_day_exemption_enabled,
                    "eld_day_start_hour": eld_day_start_hour,
                    "eld_exempt": eld_exempt,
                    "eld_exempt_reason": eld_exempt_reason,
                    "eld_pc_enabled": eld_pc_enabled,
                    "eld_ym_enabled": eld_ym_enabled,
                    "external_ids": external_ids,
                    "has_driving_features_hidden": has_driving_features_hidden,
                    "hos_setting": hos_setting,
                    "license_number": license_number,
                    "license_state": license_state,
                    "locale": locale,
                    "name": name,
                    "notes": notes,
                    "password": password,
                    "peer_group_tag_id": peer_group_tag_id,
                    "phone": phone,
                    "static_assigned_vehicle_id": static_assigned_vehicle_id,
                    "tachograph_card_number": tachograph_card_number,
                    "tag_ids": tag_ids,
                    "timezone": timezone,
                    "us_driver_ruleset_override": us_driver_ruleset_override,
                    "username": username,
                    "vehicle_group_tag_id": vehicle_group_tag_id,
                    "waiting_time_duty_status_enabled": waiting_time_duty_status_enabled,
                },
                driver_update_params.DriverUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Driver,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        attribute_value_ids: List[str] | NotGiven = NOT_GIVEN,
        created_after_time: str | NotGiven = NOT_GIVEN,
        driver_activation_status: Literal["active", "deactivated"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        updated_after_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverListResponse:
        """
        Get all drivers in organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Drivers** under the Drivers category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

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

          driver_activation_status: If value is `deactivated`, only drivers that are deactivated will appear in the
              response. This parameter will default to `active` if not provided (fetching only
              active drivers).

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
            "/fleet/drivers",
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
                        "driver_activation_status": driver_activation_status,
                        "limit": limit,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "updated_after_time": updated_after_time,
                    },
                    driver_list_params.DriverListParams,
                ),
            ),
            cast_to=DriverListResponse,
        )


class AsyncDriversResource(AsyncAPIResource):
    @cached_property
    def tachograph_activity(self) -> AsyncTachographActivityResource:
        return AsyncTachographActivityResource(self._client)

    @cached_property
    def tachograph_files(self) -> AsyncTachographFilesResource:
        return AsyncTachographFilesResource(self._client)

    @cached_property
    def safety(self) -> AsyncSafetyResource:
        return AsyncSafetyResource(self._client)

    @cached_property
    def hos(self) -> AsyncHosResource:
        return AsyncHosResource(self._client)

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

    async def create(
        self,
        *,
        name: str,
        password: str,
        username: str,
        attributes: Iterable[driver_create_params.Attribute] | NotGiven = NOT_GIVEN,
        carrier_settings: driver_create_params.CarrierSettings | NotGiven = NOT_GIVEN,
        current_id_card_code: str | NotGiven = NOT_GIVEN,
        eld_adverse_weather_exemption_enabled: bool | NotGiven = NOT_GIVEN,
        eld_big_day_exemption_enabled: bool | NotGiven = NOT_GIVEN,
        eld_day_start_hour: int | NotGiven = NOT_GIVEN,
        eld_exempt: bool | NotGiven = NOT_GIVEN,
        eld_exempt_reason: str | NotGiven = NOT_GIVEN,
        eld_pc_enabled: bool | NotGiven = NOT_GIVEN,
        eld_ym_enabled: bool | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        has_driving_features_hidden: bool | NotGiven = NOT_GIVEN,
        hos_setting: driver_create_params.HosSetting | NotGiven = NOT_GIVEN,
        license_number: str | NotGiven = NOT_GIVEN,
        license_state: str | NotGiven = NOT_GIVEN,
        locale: Literal["us", "at", "be", "ca", "gb", "fr", "de", "ie", "it", "lu", "mx", "nl", "es", "ch", "pr"]
        | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        peer_group_tag_id: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        static_assigned_vehicle_id: str | NotGiven = NOT_GIVEN,
        tachograph_card_number: str | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        timezone: str | NotGiven = NOT_GIVEN,
        us_driver_ruleset_override: driver_create_params.UsDriverRulesetOverride | NotGiven = NOT_GIVEN,
        vehicle_group_tag_id: str | NotGiven = NOT_GIVEN,
        waiting_time_duty_status_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Driver:
        """
        Add a driver to the organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Drivers** under the Drivers category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          name: Driver's name.

          password: Password that the driver can use to login to the Samsara driver app.

          username: Driver's login username into the driver app. The username may not contain spaces
              or the '@' symbol. The username must be unique.

          carrier_settings: Carrier for a given driver. If the driver's carrier differs from the general
              organization's carrier settings, the override value is used. Updating this value
              only updates the override setting for this driver.

          current_id_card_code: The ID Card Code on the back of the physical card assigned to the driver.
              Contact Samsara if you would like to enable this feature.

          eld_adverse_weather_exemption_enabled: Flag indicating this driver may use Adverse Weather exemptions in ELD logs.

          eld_big_day_exemption_enabled: Flag indicating this driver may use Big Day exemption in ELD logs.

          eld_day_start_hour: `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate
              noon-to-noon driving hours.

          eld_exempt: Flag indicating this driver is exempt from the Electronic Logging Mandate.

          eld_exempt_reason: Reason that this driver is exempt from the Electronic Logging Mandate (see
              eldExempt).

          eld_pc_enabled: Flag indicating this driver may select the Personal Conveyance duty status in
              ELD logs.

          eld_ym_enabled: Flag indicating this driver may select the Yard Move duty status in ELD logs.

          external_ids: The [external IDs](https://developers.samsara.com/docs/external-ids) for the
              given object.

          has_driving_features_hidden: A boolean indicating whether the driver has driving-related features hidden in
              the Driver App, including Vehicle selection, HOS, Routing, Team Driving,
              Documents, and Trip Logs. Default value is false if omitted. Note: only
              available to customers of Connected Forms.

          hos_setting: Hos settings for a driver.

          license_number: Driver's state issued license number. The combination of this number and
              `licenseState` must be unique.

          license_state: Abbreviation of US state, Canadian province, or US territory that issued
              driver's license.

          locale: Locale override (uncommon). These are specified by ISO 3166-2 country codes for
              supported locales. Valid values: `us`, `at`, `be`, `ca`, `gb`, `fr`, `de`, `ie`,
              `it`, `lu`, `mx`, `nl`, `es`, `ch`, `pr`.

          notes: Notes about the driver.

          peer_group_tag_id: The peer group tag id this driver belong to, used for gamification.

          phone: Phone number of the driver.

          static_assigned_vehicle_id: ID of vehicle that the driver is permanently assigned to. (uncommon).

          tachograph_card_number: Driver's assigned tachograph card number (Europe specific)

          tag_ids: IDs of tags the driver is associated with. If your access to the API is scoped
              by one or more tags, this field is required to pass in.

          timezone: Home terminal timezone, in order to indicate what time zone should be used to
              calculate the ELD logs. Driver timezones use
              [IANA timezone database](https://www.iana.org/time-zones) keys (e.g.
              `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find
              a mapping of common timezone formats to IANA timezone keys
              [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html).

          us_driver_ruleset_override: US Driver Ruleset override for a given driver. If the driver is operating under
              a ruleset different from the organization default, the override is used.
              Updating this value only updates the override setting for this driver.
              Explicitly setting this field to `null` will delete driver's ruleset override.
              If the driver does not have an override ruleset set, the response will not
              include any usDriverRulesetOverride information.

          vehicle_group_tag_id: Tag ID which determines which vehicles a driver will see when selecting
              vehicles.

          waiting_time_duty_status_enabled: Flag indicating this driver may select waiting time duty status in ELD logs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fleet/drivers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "password": password,
                    "username": username,
                    "attributes": attributes,
                    "carrier_settings": carrier_settings,
                    "current_id_card_code": current_id_card_code,
                    "eld_adverse_weather_exemption_enabled": eld_adverse_weather_exemption_enabled,
                    "eld_big_day_exemption_enabled": eld_big_day_exemption_enabled,
                    "eld_day_start_hour": eld_day_start_hour,
                    "eld_exempt": eld_exempt,
                    "eld_exempt_reason": eld_exempt_reason,
                    "eld_pc_enabled": eld_pc_enabled,
                    "eld_ym_enabled": eld_ym_enabled,
                    "external_ids": external_ids,
                    "has_driving_features_hidden": has_driving_features_hidden,
                    "hos_setting": hos_setting,
                    "license_number": license_number,
                    "license_state": license_state,
                    "locale": locale,
                    "notes": notes,
                    "peer_group_tag_id": peer_group_tag_id,
                    "phone": phone,
                    "static_assigned_vehicle_id": static_assigned_vehicle_id,
                    "tachograph_card_number": tachograph_card_number,
                    "tag_ids": tag_ids,
                    "timezone": timezone,
                    "us_driver_ruleset_override": us_driver_ruleset_override,
                    "vehicle_group_tag_id": vehicle_group_tag_id,
                    "waiting_time_duty_status_enabled": waiting_time_duty_status_enabled,
                },
                driver_create_params.DriverCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Driver,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Driver:
        """
        Get information about a driver.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Drivers** under the Drivers category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/fleet/drivers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Driver,
        )

    async def update(
        self,
        id: str,
        *,
        attributes: Iterable[driver_update_params.Attribute] | NotGiven = NOT_GIVEN,
        carrier_settings: driver_update_params.CarrierSettings | NotGiven = NOT_GIVEN,
        current_id_card_code: str | NotGiven = NOT_GIVEN,
        deactivated_at_time: str | NotGiven = NOT_GIVEN,
        driver_activation_status: Literal["active", "deactivated"] | NotGiven = NOT_GIVEN,
        eld_adverse_weather_exemption_enabled: bool | NotGiven = NOT_GIVEN,
        eld_big_day_exemption_enabled: bool | NotGiven = NOT_GIVEN,
        eld_day_start_hour: int | NotGiven = NOT_GIVEN,
        eld_exempt: bool | NotGiven = NOT_GIVEN,
        eld_exempt_reason: str | NotGiven = NOT_GIVEN,
        eld_pc_enabled: bool | NotGiven = NOT_GIVEN,
        eld_ym_enabled: bool | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        has_driving_features_hidden: bool | NotGiven = NOT_GIVEN,
        hos_setting: driver_update_params.HosSetting | NotGiven = NOT_GIVEN,
        license_number: str | NotGiven = NOT_GIVEN,
        license_state: str | NotGiven = NOT_GIVEN,
        locale: Literal["us", "at", "be", "ca", "gb", "fr", "de", "ie", "it", "lu", "mx", "nl", "es", "ch", "pr"]
        | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        peer_group_tag_id: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        static_assigned_vehicle_id: str | NotGiven = NOT_GIVEN,
        tachograph_card_number: str | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        timezone: str | NotGiven = NOT_GIVEN,
        us_driver_ruleset_override: driver_update_params.UsDriverRulesetOverride | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        vehicle_group_tag_id: str | NotGiven = NOT_GIVEN,
        waiting_time_duty_status_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Driver:
        """Update a specific driver's information.

        This can also be used to activate or
        de-activate a given driver by setting the driverActivationStatus field. If the
        driverActivationStatus field is 'deactivated' then the user can also specify the
        deactivatedAtTime. The deactivatedAtTime cannot be more than 6 months in the
        past and must not come before the dirver's latest active HOS log. It will be
        considered an error if deactivatedAtTime is provided with a
        driverActivationStatus of active.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Drivers** under the Drivers category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          carrier_settings: Carrier for a given driver. If the driver's carrier differs from the general
              organization's carrier settings, the override value is used. Updating this value
              only updates the override setting for this driver.

          current_id_card_code: The ID Card Code on the back of the physical card assigned to the driver.
              Contact Samsara if you would like to enable this feature.

          deactivated_at_time: The date and time this driver is considered to be deactivated in RFC 3339
              format.

          driver_activation_status:
              A value indicating whether the driver is active or deactivated. Valid values:
              `active`, `deactivated`.

          eld_adverse_weather_exemption_enabled: Flag indicating this driver may use Adverse Weather exemptions in ELD logs.

          eld_big_day_exemption_enabled: Flag indicating this driver may use Big Day exemption in ELD logs.

          eld_day_start_hour: `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate
              noon-to-noon driving hours.

          eld_exempt: Flag indicating this driver is exempt from the Electronic Logging Mandate.

          eld_exempt_reason: Reason that this driver is exempt from the Electronic Logging Mandate (see
              eldExempt).

          eld_pc_enabled: Flag indicating this driver may select the Personal Conveyance duty status in
              ELD logs.

          eld_ym_enabled: Flag indicating this driver may select the Yard Move duty status in ELD logs.

          external_ids: The [external IDs](https://developers.samsara.com/docs/external-ids) for the
              given object.

          has_driving_features_hidden: A boolean indicating whether the driver has driving-related features hidden in
              the Driver App, including Vehicle selection, HOS, Routing, Team Driving,
              Documents, and Trip Logs. Default value is false if omitted. Note: only
              available to customers of Connected Forms.

          hos_setting: Hos settings for a driver.

          license_number: Driver's state issued license number. The combination of this number and
              `licenseState` must be unique.

          license_state: Abbreviation of US state, Canadian province, or US territory that issued
              driver's license.

          locale: Locale override (uncommon). These are specified by ISO 3166-2 country codes for
              supported locales. Valid values: `us`, `at`, `be`, `ca`, `gb`, `fr`, `de`, `ie`,
              `it`, `lu`, `mx`, `nl`, `es`, `ch`, `pr`.

          name: Driver's name.

          notes: Notes about the driver.

          password: Password that the driver can use to login to the Samsara driver app.

          peer_group_tag_id: The peer group tag id this driver belong to, leave blank to be in group with
              everyone, used for gamification.

          phone: Phone number of the driver.

          static_assigned_vehicle_id: ID of vehicle that the driver is permanently assigned to. (uncommon).

          tachograph_card_number: Driver's assigned tachograph card number (Europe specific)

          tag_ids: IDs of tags the driver is associated with. If your access to the API is scoped
              by one or more tags, this field is required to pass in.

          timezone: Home terminal timezone, in order to indicate what time zone should be used to
              calculate the ELD logs. Driver timezones use
              [IANA timezone database](https://www.iana.org/time-zones) keys (e.g.
              `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find
              a mapping of common timezone formats to IANA timezone keys
              [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html).

          us_driver_ruleset_override: US Driver Ruleset override for a given driver. If the driver is operating under
              a ruleset different from the organization default, the override is used.
              Updating this value only updates the override setting for this driver.
              Explicitly setting this field to `null` will delete driver's ruleset override.
              If the driver does not have an override ruleset set, the response will not
              include any usDriverRulesetOverride information.

          username: Driver's login username into the driver app. The username may not contain spaces
              or the '@' symbol. The username must be unique.

          vehicle_group_tag_id: Tag ID which determines which vehicles a driver will see when selecting
              vehicles.

          waiting_time_duty_status_enabled: Flag indicating this driver may select waiting time duty status in ELD logs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/fleet/drivers/{id}",
            body=await async_maybe_transform(
                {
                    "attributes": attributes,
                    "carrier_settings": carrier_settings,
                    "current_id_card_code": current_id_card_code,
                    "deactivated_at_time": deactivated_at_time,
                    "driver_activation_status": driver_activation_status,
                    "eld_adverse_weather_exemption_enabled": eld_adverse_weather_exemption_enabled,
                    "eld_big_day_exemption_enabled": eld_big_day_exemption_enabled,
                    "eld_day_start_hour": eld_day_start_hour,
                    "eld_exempt": eld_exempt,
                    "eld_exempt_reason": eld_exempt_reason,
                    "eld_pc_enabled": eld_pc_enabled,
                    "eld_ym_enabled": eld_ym_enabled,
                    "external_ids": external_ids,
                    "has_driving_features_hidden": has_driving_features_hidden,
                    "hos_setting": hos_setting,
                    "license_number": license_number,
                    "license_state": license_state,
                    "locale": locale,
                    "name": name,
                    "notes": notes,
                    "password": password,
                    "peer_group_tag_id": peer_group_tag_id,
                    "phone": phone,
                    "static_assigned_vehicle_id": static_assigned_vehicle_id,
                    "tachograph_card_number": tachograph_card_number,
                    "tag_ids": tag_ids,
                    "timezone": timezone,
                    "us_driver_ruleset_override": us_driver_ruleset_override,
                    "username": username,
                    "vehicle_group_tag_id": vehicle_group_tag_id,
                    "waiting_time_duty_status_enabled": waiting_time_duty_status_enabled,
                },
                driver_update_params.DriverUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Driver,
        )

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        attribute_value_ids: List[str] | NotGiven = NOT_GIVEN,
        created_after_time: str | NotGiven = NOT_GIVEN,
        driver_activation_status: Literal["active", "deactivated"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        updated_after_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DriverListResponse:
        """
        Get all drivers in organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Drivers** under the Drivers category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

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

          driver_activation_status: If value is `deactivated`, only drivers that are deactivated will appear in the
              response. This parameter will default to `active` if not provided (fetching only
              active drivers).

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
            "/fleet/drivers",
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
                        "driver_activation_status": driver_activation_status,
                        "limit": limit,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                        "updated_after_time": updated_after_time,
                    },
                    driver_list_params.DriverListParams,
                ),
            ),
            cast_to=DriverListResponse,
        )


class DriversResourceWithRawResponse:
    def __init__(self, drivers: DriversResource) -> None:
        self._drivers = drivers

        self.create = to_raw_response_wrapper(
            drivers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            drivers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            drivers.update,
        )
        self.list = to_raw_response_wrapper(
            drivers.list,
        )

    @cached_property
    def tachograph_activity(self) -> TachographActivityResourceWithRawResponse:
        return TachographActivityResourceWithRawResponse(self._drivers.tachograph_activity)

    @cached_property
    def tachograph_files(self) -> TachographFilesResourceWithRawResponse:
        return TachographFilesResourceWithRawResponse(self._drivers.tachograph_files)

    @cached_property
    def safety(self) -> SafetyResourceWithRawResponse:
        return SafetyResourceWithRawResponse(self._drivers.safety)

    @cached_property
    def hos(self) -> HosResourceWithRawResponse:
        return HosResourceWithRawResponse(self._drivers.hos)


class AsyncDriversResourceWithRawResponse:
    def __init__(self, drivers: AsyncDriversResource) -> None:
        self._drivers = drivers

        self.create = async_to_raw_response_wrapper(
            drivers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            drivers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            drivers.update,
        )
        self.list = async_to_raw_response_wrapper(
            drivers.list,
        )

    @cached_property
    def tachograph_activity(self) -> AsyncTachographActivityResourceWithRawResponse:
        return AsyncTachographActivityResourceWithRawResponse(self._drivers.tachograph_activity)

    @cached_property
    def tachograph_files(self) -> AsyncTachographFilesResourceWithRawResponse:
        return AsyncTachographFilesResourceWithRawResponse(self._drivers.tachograph_files)

    @cached_property
    def safety(self) -> AsyncSafetyResourceWithRawResponse:
        return AsyncSafetyResourceWithRawResponse(self._drivers.safety)

    @cached_property
    def hos(self) -> AsyncHosResourceWithRawResponse:
        return AsyncHosResourceWithRawResponse(self._drivers.hos)


class DriversResourceWithStreamingResponse:
    def __init__(self, drivers: DriversResource) -> None:
        self._drivers = drivers

        self.create = to_streamed_response_wrapper(
            drivers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            drivers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            drivers.update,
        )
        self.list = to_streamed_response_wrapper(
            drivers.list,
        )

    @cached_property
    def tachograph_activity(self) -> TachographActivityResourceWithStreamingResponse:
        return TachographActivityResourceWithStreamingResponse(self._drivers.tachograph_activity)

    @cached_property
    def tachograph_files(self) -> TachographFilesResourceWithStreamingResponse:
        return TachographFilesResourceWithStreamingResponse(self._drivers.tachograph_files)

    @cached_property
    def safety(self) -> SafetyResourceWithStreamingResponse:
        return SafetyResourceWithStreamingResponse(self._drivers.safety)

    @cached_property
    def hos(self) -> HosResourceWithStreamingResponse:
        return HosResourceWithStreamingResponse(self._drivers.hos)


class AsyncDriversResourceWithStreamingResponse:
    def __init__(self, drivers: AsyncDriversResource) -> None:
        self._drivers = drivers

        self.create = async_to_streamed_response_wrapper(
            drivers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            drivers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            drivers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            drivers.list,
        )

    @cached_property
    def tachograph_activity(self) -> AsyncTachographActivityResourceWithStreamingResponse:
        return AsyncTachographActivityResourceWithStreamingResponse(self._drivers.tachograph_activity)

    @cached_property
    def tachograph_files(self) -> AsyncTachographFilesResourceWithStreamingResponse:
        return AsyncTachographFilesResourceWithStreamingResponse(self._drivers.tachograph_files)

    @cached_property
    def safety(self) -> AsyncSafetyResourceWithStreamingResponse:
        return AsyncSafetyResourceWithStreamingResponse(self._drivers.safety)

    @cached_property
    def hos(self) -> AsyncHosResourceWithStreamingResponse:
        return AsyncHosResourceWithStreamingResponse(self._drivers.hos)
