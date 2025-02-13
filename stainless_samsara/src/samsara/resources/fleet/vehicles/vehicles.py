# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal

import httpx

from .stats import (
    StatsResource,
    AsyncStatsResource,
    StatsResourceWithRawResponse,
    AsyncStatsResourceWithRawResponse,
    StatsResourceWithStreamingResponse,
    AsyncStatsResourceWithStreamingResponse,
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
from ....types.fleet import vehicle_update_params
from ...._base_client import make_request_options
from .tachograph_files import (
    TachographFilesResource,
    AsyncTachographFilesResource,
    TachographFilesResourceWithRawResponse,
    AsyncTachographFilesResourceWithRawResponse,
    TachographFilesResourceWithStreamingResponse,
    AsyncTachographFilesResourceWithStreamingResponse,
)
from ....types.fleet.vehicle_response import VehicleResponse

__all__ = ["VehiclesResource", "AsyncVehiclesResource"]


class VehiclesResource(SyncAPIResource):
    @cached_property
    def stats(self) -> StatsResource:
        return StatsResource(self._client)

    @cached_property
    def tachograph_files(self) -> TachographFilesResource:
        return TachographFilesResource(self._client)

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
    ) -> VehicleResponse:
        """
        Get information about a specific vehicle.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Vehicles** under the Vehicles category when
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
            f"/fleet/vehicles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleResponse,
        )

    def update(
        self,
        id: str,
        *,
        attributes: Iterable[vehicle_update_params.Attribute] | NotGiven = NOT_GIVEN,
        aux_input_type1: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type10: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type11: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type12: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type13: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type2: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type3: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type4: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type5: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type6: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type7: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type8: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type9: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        engine_hours: int | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        gateway_serial: str | NotGiven = NOT_GIVEN,
        gross_vehicle_weight: vehicle_update_params.GrossVehicleWeight | NotGiven = NOT_GIVEN,
        harsh_acceleration_setting_type: Literal["passengerCar", "lightTruck", "heavyDuty", "off", "automatic"]
        | NotGiven = NOT_GIVEN,
        license_plate: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        odometer_meters: int | NotGiven = NOT_GIVEN,
        static_assigned_driver_id: str | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        vehicle_regulation_mode: Literal["regulated", "unregulated", "mixed"] | NotGiven = NOT_GIVEN,
        vehicle_type: str | NotGiven = NOT_GIVEN,
        vin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VehicleResponse:
        """
        Updates the given Vehicle object.

        **Note:** Vehicle objects are automatically created when Samsara Vehicle
        Gateways are installed. You cannot create a Vehicle object via API.

        You are able to _update_ many of the fields of a Vehicle.

        **Note**: There are no required fields in the request body, and you only need to
        provide the fields you wish to update.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Vehicles** under the Vehicles category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          aux_input_type1: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type10: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type11: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type12: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type13: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type2: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type3: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type4: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type5: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type6: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type7: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type8: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type9: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          engine_hours: A manual override for the vehicle's engine hours. You may only override a
              vehicle's engine hours if it cannot be read from on-board diagnostics. When you
              provide a manual engine hours override, Samsara will begin updating a vehicle's
              engine hours based on when the Samsara Vehicle Gateway is recieving power or
              not. Setting the value to 0 will unset the manual engine hours.

          external_ids: The <a href="/docs/external-ids" target="_blank">external IDs</a> for the given
              object.

          gateway_serial: The serial number of the gateway. **By default**: empty. This can be set to a
              different gateway's serial number to pair this vehicle with a different gateway.

          gross_vehicle_weight: The gross weight of the vehicle in either pounds (lb) or kilograms (kg). Only
              returned for customers with commercial speed limits (CSL) enabled.

          harsh_acceleration_setting_type: The harsh acceleration setting type. This setting influences the acceleration
              sensitivity from which a
              <a href="https://kb.samsara.com/hc/en-us/articles/360043051792-Safety-Event-Overview" target="_blank">harsh
              event</a> is triggered. **By default**, this setting is inferred by the Samsara
              Vehicle Gateway from the engine computer, but it may be set or updated through
              the Samsara Dashboard or the API at any time. If set to `off`, then no
              acceleration based harsh events are triggered for the vehicle. Valid values:
              `passengerCar`, `lightTruck`, `heavyDuty`, `off`, `automatic`.

          license_plate: The license plate of the Vehicle. **By default**: empty. Can be set or updated
              through the Samsara Dashboard or the API at any time.

          name: The human-readable name of the Vehicle. This is set by a fleet administrator and
              will appear in both Samsara’s cloud dashboard as well as the Samsara Driver
              mobile app. **By default**, this name is the serial number of the Samsara
              Vehicle Gateway. It can be set or updated through the Samsara Dashboard or
              through the API at any time.

          notes: These are generic notes about the Vehicle. Empty by default. Can be set or
              updated through the Samsara Dashboard or the API at any time.

          odometer_meters: A manual override for the vehicle's odometer. You may only override a vehicle's
              odometer if it cannot be read from on-board diagnostics. When you provide a
              manual odometer override, Samsara will begin updating a vehicle's odometer using
              GPS distance traveled since this override was set. See
              <a href="https://kb.samsara.com/hc/en-us/articles/115005273667" target="_blank">here</a>
              for more details.

          static_assigned_driver_id: ID for the static assigned driver of the vehicle. Setting the value to 0 will
              unassign the current driver.

          tag_ids: An array of IDs of tags to associate with this vehicle. If your access to the
              API is scoped by one or more tags, this field is required to pass in.

          vehicle_regulation_mode: Whether or not the vehicle is regulated, unregulated (non-CMV), or a mixed use
              unregulated vehicle. Valid values: `regulated`, `unregulated`, `mixed`.

          vehicle_type: The type of the vehicle. Only returned for customers with commercial speed
              limits (CSL) enabled.

          vin: The VIN of the Vehicle. Most of the time, this will be automatically read from
              the engine computer by the Samsara Vehicle Gateway. It will be empty if it
              cannot be read. It can be set or updated through the Samsara Dashboard or the
              API at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/fleet/vehicles/{id}",
            body=maybe_transform(
                {
                    "attributes": attributes,
                    "aux_input_type1": aux_input_type1,
                    "aux_input_type10": aux_input_type10,
                    "aux_input_type11": aux_input_type11,
                    "aux_input_type12": aux_input_type12,
                    "aux_input_type13": aux_input_type13,
                    "aux_input_type2": aux_input_type2,
                    "aux_input_type3": aux_input_type3,
                    "aux_input_type4": aux_input_type4,
                    "aux_input_type5": aux_input_type5,
                    "aux_input_type6": aux_input_type6,
                    "aux_input_type7": aux_input_type7,
                    "aux_input_type8": aux_input_type8,
                    "aux_input_type9": aux_input_type9,
                    "engine_hours": engine_hours,
                    "external_ids": external_ids,
                    "gateway_serial": gateway_serial,
                    "gross_vehicle_weight": gross_vehicle_weight,
                    "harsh_acceleration_setting_type": harsh_acceleration_setting_type,
                    "license_plate": license_plate,
                    "name": name,
                    "notes": notes,
                    "odometer_meters": odometer_meters,
                    "static_assigned_driver_id": static_assigned_driver_id,
                    "tag_ids": tag_ids,
                    "vehicle_regulation_mode": vehicle_regulation_mode,
                    "vehicle_type": vehicle_type,
                    "vin": vin,
                },
                vehicle_update_params.VehicleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleResponse,
        )


class AsyncVehiclesResource(AsyncAPIResource):
    @cached_property
    def stats(self) -> AsyncStatsResource:
        return AsyncStatsResource(self._client)

    @cached_property
    def tachograph_files(self) -> AsyncTachographFilesResource:
        return AsyncTachographFilesResource(self._client)

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
    ) -> VehicleResponse:
        """
        Get information about a specific vehicle.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Vehicles** under the Vehicles category when
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
            f"/fleet/vehicles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleResponse,
        )

    async def update(
        self,
        id: str,
        *,
        attributes: Iterable[vehicle_update_params.Attribute] | NotGiven = NOT_GIVEN,
        aux_input_type1: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type10: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type11: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type12: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type13: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type2: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type3: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type4: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type5: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type6: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type7: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type8: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        aux_input_type9: Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ]
        | NotGiven = NOT_GIVEN,
        engine_hours: int | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        gateway_serial: str | NotGiven = NOT_GIVEN,
        gross_vehicle_weight: vehicle_update_params.GrossVehicleWeight | NotGiven = NOT_GIVEN,
        harsh_acceleration_setting_type: Literal["passengerCar", "lightTruck", "heavyDuty", "off", "automatic"]
        | NotGiven = NOT_GIVEN,
        license_plate: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        odometer_meters: int | NotGiven = NOT_GIVEN,
        static_assigned_driver_id: str | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        vehicle_regulation_mode: Literal["regulated", "unregulated", "mixed"] | NotGiven = NOT_GIVEN,
        vehicle_type: str | NotGiven = NOT_GIVEN,
        vin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VehicleResponse:
        """
        Updates the given Vehicle object.

        **Note:** Vehicle objects are automatically created when Samsara Vehicle
        Gateways are installed. You cannot create a Vehicle object via API.

        You are able to _update_ many of the fields of a Vehicle.

        **Note**: There are no required fields in the request body, and you only need to
        provide the fields you wish to update.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Vehicles** under the Vehicles category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          aux_input_type1: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type10: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type11: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type12: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type13: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type2: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type3: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type4: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type5: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type6: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type7: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type8: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          aux_input_type9: The type of
              <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
              input</a> configured for this Vehicle. Once configured, these inputs will
              generate dynamic, time-series data that will be available to view in the Samsara
              Dashboard. **By default**: empty. This can be set or updated through the Samsara
              Dashboard or the API at any time. Inputs 3-13 are only available on gateways
              with an attached aux expander. Valid values: `None`, `Emergency Lights`,
              `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
              `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
              `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
              `Secondary Fuel Source`, `(ECU) Power Take-Off`.

          engine_hours: A manual override for the vehicle's engine hours. You may only override a
              vehicle's engine hours if it cannot be read from on-board diagnostics. When you
              provide a manual engine hours override, Samsara will begin updating a vehicle's
              engine hours based on when the Samsara Vehicle Gateway is recieving power or
              not. Setting the value to 0 will unset the manual engine hours.

          external_ids: The <a href="/docs/external-ids" target="_blank">external IDs</a> for the given
              object.

          gateway_serial: The serial number of the gateway. **By default**: empty. This can be set to a
              different gateway's serial number to pair this vehicle with a different gateway.

          gross_vehicle_weight: The gross weight of the vehicle in either pounds (lb) or kilograms (kg). Only
              returned for customers with commercial speed limits (CSL) enabled.

          harsh_acceleration_setting_type: The harsh acceleration setting type. This setting influences the acceleration
              sensitivity from which a
              <a href="https://kb.samsara.com/hc/en-us/articles/360043051792-Safety-Event-Overview" target="_blank">harsh
              event</a> is triggered. **By default**, this setting is inferred by the Samsara
              Vehicle Gateway from the engine computer, but it may be set or updated through
              the Samsara Dashboard or the API at any time. If set to `off`, then no
              acceleration based harsh events are triggered for the vehicle. Valid values:
              `passengerCar`, `lightTruck`, `heavyDuty`, `off`, `automatic`.

          license_plate: The license plate of the Vehicle. **By default**: empty. Can be set or updated
              through the Samsara Dashboard or the API at any time.

          name: The human-readable name of the Vehicle. This is set by a fleet administrator and
              will appear in both Samsara’s cloud dashboard as well as the Samsara Driver
              mobile app. **By default**, this name is the serial number of the Samsara
              Vehicle Gateway. It can be set or updated through the Samsara Dashboard or
              through the API at any time.

          notes: These are generic notes about the Vehicle. Empty by default. Can be set or
              updated through the Samsara Dashboard or the API at any time.

          odometer_meters: A manual override for the vehicle's odometer. You may only override a vehicle's
              odometer if it cannot be read from on-board diagnostics. When you provide a
              manual odometer override, Samsara will begin updating a vehicle's odometer using
              GPS distance traveled since this override was set. See
              <a href="https://kb.samsara.com/hc/en-us/articles/115005273667" target="_blank">here</a>
              for more details.

          static_assigned_driver_id: ID for the static assigned driver of the vehicle. Setting the value to 0 will
              unassign the current driver.

          tag_ids: An array of IDs of tags to associate with this vehicle. If your access to the
              API is scoped by one or more tags, this field is required to pass in.

          vehicle_regulation_mode: Whether or not the vehicle is regulated, unregulated (non-CMV), or a mixed use
              unregulated vehicle. Valid values: `regulated`, `unregulated`, `mixed`.

          vehicle_type: The type of the vehicle. Only returned for customers with commercial speed
              limits (CSL) enabled.

          vin: The VIN of the Vehicle. Most of the time, this will be automatically read from
              the engine computer by the Samsara Vehicle Gateway. It will be empty if it
              cannot be read. It can be set or updated through the Samsara Dashboard or the
              API at any time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/fleet/vehicles/{id}",
            body=await async_maybe_transform(
                {
                    "attributes": attributes,
                    "aux_input_type1": aux_input_type1,
                    "aux_input_type10": aux_input_type10,
                    "aux_input_type11": aux_input_type11,
                    "aux_input_type12": aux_input_type12,
                    "aux_input_type13": aux_input_type13,
                    "aux_input_type2": aux_input_type2,
                    "aux_input_type3": aux_input_type3,
                    "aux_input_type4": aux_input_type4,
                    "aux_input_type5": aux_input_type5,
                    "aux_input_type6": aux_input_type6,
                    "aux_input_type7": aux_input_type7,
                    "aux_input_type8": aux_input_type8,
                    "aux_input_type9": aux_input_type9,
                    "engine_hours": engine_hours,
                    "external_ids": external_ids,
                    "gateway_serial": gateway_serial,
                    "gross_vehicle_weight": gross_vehicle_weight,
                    "harsh_acceleration_setting_type": harsh_acceleration_setting_type,
                    "license_plate": license_plate,
                    "name": name,
                    "notes": notes,
                    "odometer_meters": odometer_meters,
                    "static_assigned_driver_id": static_assigned_driver_id,
                    "tag_ids": tag_ids,
                    "vehicle_regulation_mode": vehicle_regulation_mode,
                    "vehicle_type": vehicle_type,
                    "vin": vin,
                },
                vehicle_update_params.VehicleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleResponse,
        )


class VehiclesResourceWithRawResponse:
    def __init__(self, vehicles: VehiclesResource) -> None:
        self._vehicles = vehicles

        self.retrieve = to_raw_response_wrapper(
            vehicles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            vehicles.update,
        )

    @cached_property
    def stats(self) -> StatsResourceWithRawResponse:
        return StatsResourceWithRawResponse(self._vehicles.stats)

    @cached_property
    def tachograph_files(self) -> TachographFilesResourceWithRawResponse:
        return TachographFilesResourceWithRawResponse(self._vehicles.tachograph_files)


class AsyncVehiclesResourceWithRawResponse:
    def __init__(self, vehicles: AsyncVehiclesResource) -> None:
        self._vehicles = vehicles

        self.retrieve = async_to_raw_response_wrapper(
            vehicles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            vehicles.update,
        )

    @cached_property
    def stats(self) -> AsyncStatsResourceWithRawResponse:
        return AsyncStatsResourceWithRawResponse(self._vehicles.stats)

    @cached_property
    def tachograph_files(self) -> AsyncTachographFilesResourceWithRawResponse:
        return AsyncTachographFilesResourceWithRawResponse(self._vehicles.tachograph_files)


class VehiclesResourceWithStreamingResponse:
    def __init__(self, vehicles: VehiclesResource) -> None:
        self._vehicles = vehicles

        self.retrieve = to_streamed_response_wrapper(
            vehicles.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            vehicles.update,
        )

    @cached_property
    def stats(self) -> StatsResourceWithStreamingResponse:
        return StatsResourceWithStreamingResponse(self._vehicles.stats)

    @cached_property
    def tachograph_files(self) -> TachographFilesResourceWithStreamingResponse:
        return TachographFilesResourceWithStreamingResponse(self._vehicles.tachograph_files)


class AsyncVehiclesResourceWithStreamingResponse:
    def __init__(self, vehicles: AsyncVehiclesResource) -> None:
        self._vehicles = vehicles

        self.retrieve = async_to_streamed_response_wrapper(
            vehicles.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            vehicles.update,
        )

    @cached_property
    def stats(self) -> AsyncStatsResourceWithStreamingResponse:
        return AsyncStatsResourceWithStreamingResponse(self._vehicles.stats)

    @cached_property
    def tachograph_files(self) -> AsyncTachographFilesResourceWithStreamingResponse:
        return AsyncTachographFilesResourceWithStreamingResponse(self._vehicles.tachograph_files)
