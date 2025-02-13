# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import (
    tags,
    dvirs,
    trips,
    users,
    issues,
    defects,
    contacts,
    gateways,
    messages,
    webhooks,
    addresses,
    attributes,
    user_roles,
    live_shares,
    maintenance,
    defect_types,
    ifta_details,
    fuel_purchases,
    organization_info,
    speeding_intervals,
    training_assignments,
    hos_authentication_logs,
    driver_trailer_assignments,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import SamsaraError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.hos import hos
from .resources.beta import beta
from .resources.fleet import fleet
from .resources.alerts import alerts
from .resources.assets import assets
from .resources.vision import vision
from .resources.cameras import cameras
from .resources.drivers import drivers
from .resources.preview import preview
from .resources.sensors import sensors
from .resources.coaching import coaching
from .resources.machines import machines
from .resources.trailers import trailers
from .resources.vehicles import vehicles
from .resources.equipment import equipment
from .resources.industrial import industrial
from .resources.form_submissions import form_submissions

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Samsara",
    "AsyncSamsara",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.samsara.com/",
    "environment_1": "https://api.eu.samsara.com/",
}


class Samsara(SyncAPIClient):
    addresses: addresses.AddressesResource
    alerts: alerts.AlertsResource
    assets: assets.AssetsResource
    attributes: attributes.AttributesResource
    beta: beta.BetaResource
    cameras: cameras.CamerasResource
    coaching: coaching.CoachingResource
    contacts: contacts.ContactsResource
    defect_types: defect_types.DefectTypesResource
    defects: defects.DefectsResource
    driver_trailer_assignments: driver_trailer_assignments.DriverTrailerAssignmentsResource
    drivers: drivers.DriversResource
    dvirs: dvirs.DvirsResource
    fleet: fleet.FleetResource
    equipment: equipment.EquipmentResource
    hos: hos.HosResource
    trailers: trailers.TrailersResource
    vehicles: vehicles.VehiclesResource
    form_submissions: form_submissions.FormSubmissionsResource
    fuel_purchases: fuel_purchases.FuelPurchasesResource
    gateways: gateways.GatewaysResource
    ifta_details: ifta_details.IftaDetailsResource
    industrial: industrial.IndustrialResource
    issues: issues.IssuesResource
    live_shares: live_shares.LiveSharesResource
    organization_info: organization_info.OrganizationInfoResource
    preview: preview.PreviewResource
    speeding_intervals: speeding_intervals.SpeedingIntervalsResource
    tags: tags.TagsResource
    training_assignments: training_assignments.TrainingAssignmentsResource
    trips: trips.TripsResource
    user_roles: user_roles.UserRolesResource
    users: users.UsersResource
    hos_authentication_logs: hos_authentication_logs.HosAuthenticationLogsResource
    maintenance: maintenance.MaintenanceResource
    messages: messages.MessagesResource
    vision: vision.VisionResource
    machines: machines.MachinesResource
    sensors: sensors.SensorsResource
    webhooks: webhooks.WebhooksResource
    with_raw_response: SamsaraWithRawResponse
    with_streaming_response: SamsaraWithStreamedResponse

    # client options
    access_token: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        access_token: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous samsara client instance.

        This automatically infers the `access_token` argument from the `ACCESS_TOKEN` environment variable if it is not provided.
        """
        if access_token is None:
            access_token = os.environ.get("ACCESS_TOKEN")
        if access_token is None:
            raise SamsaraError(
                "The access_token client option must be set either by passing access_token to the client or by setting the ACCESS_TOKEN environment variable"
            )
        self.access_token = access_token

        self._environment = environment

        base_url_env = os.environ.get("SAMSARA_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `SAMSARA_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.addresses = addresses.AddressesResource(self)
        self.alerts = alerts.AlertsResource(self)
        self.assets = assets.AssetsResource(self)
        self.attributes = attributes.AttributesResource(self)
        self.beta = beta.BetaResource(self)
        self.cameras = cameras.CamerasResource(self)
        self.coaching = coaching.CoachingResource(self)
        self.contacts = contacts.ContactsResource(self)
        self.defect_types = defect_types.DefectTypesResource(self)
        self.defects = defects.DefectsResource(self)
        self.driver_trailer_assignments = driver_trailer_assignments.DriverTrailerAssignmentsResource(self)
        self.drivers = drivers.DriversResource(self)
        self.dvirs = dvirs.DvirsResource(self)
        self.fleet = fleet.FleetResource(self)
        self.equipment = equipment.EquipmentResource(self)
        self.hos = hos.HosResource(self)
        self.trailers = trailers.TrailersResource(self)
        self.vehicles = vehicles.VehiclesResource(self)
        self.form_submissions = form_submissions.FormSubmissionsResource(self)
        self.fuel_purchases = fuel_purchases.FuelPurchasesResource(self)
        self.gateways = gateways.GatewaysResource(self)
        self.ifta_details = ifta_details.IftaDetailsResource(self)
        self.industrial = industrial.IndustrialResource(self)
        self.issues = issues.IssuesResource(self)
        self.live_shares = live_shares.LiveSharesResource(self)
        self.organization_info = organization_info.OrganizationInfoResource(self)
        self.preview = preview.PreviewResource(self)
        self.speeding_intervals = speeding_intervals.SpeedingIntervalsResource(self)
        self.tags = tags.TagsResource(self)
        self.training_assignments = training_assignments.TrainingAssignmentsResource(self)
        self.trips = trips.TripsResource(self)
        self.user_roles = user_roles.UserRolesResource(self)
        self.users = users.UsersResource(self)
        self.hos_authentication_logs = hos_authentication_logs.HosAuthenticationLogsResource(self)
        self.maintenance = maintenance.MaintenanceResource(self)
        self.messages = messages.MessagesResource(self)
        self.vision = vision.VisionResource(self)
        self.machines = machines.MachinesResource(self)
        self.sensors = sensors.SensorsResource(self)
        self.webhooks = webhooks.WebhooksResource(self)
        self.with_raw_response = SamsaraWithRawResponse(self)
        self.with_streaming_response = SamsaraWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        access_token = self.access_token
        return {"Authorization": f"Bearer {access_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        access_token: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            access_token=access_token or self.access_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncSamsara(AsyncAPIClient):
    addresses: addresses.AsyncAddressesResource
    alerts: alerts.AsyncAlertsResource
    assets: assets.AsyncAssetsResource
    attributes: attributes.AsyncAttributesResource
    beta: beta.AsyncBetaResource
    cameras: cameras.AsyncCamerasResource
    coaching: coaching.AsyncCoachingResource
    contacts: contacts.AsyncContactsResource
    defect_types: defect_types.AsyncDefectTypesResource
    defects: defects.AsyncDefectsResource
    driver_trailer_assignments: driver_trailer_assignments.AsyncDriverTrailerAssignmentsResource
    drivers: drivers.AsyncDriversResource
    dvirs: dvirs.AsyncDvirsResource
    fleet: fleet.AsyncFleetResource
    equipment: equipment.AsyncEquipmentResource
    hos: hos.AsyncHosResource
    trailers: trailers.AsyncTrailersResource
    vehicles: vehicles.AsyncVehiclesResource
    form_submissions: form_submissions.AsyncFormSubmissionsResource
    fuel_purchases: fuel_purchases.AsyncFuelPurchasesResource
    gateways: gateways.AsyncGatewaysResource
    ifta_details: ifta_details.AsyncIftaDetailsResource
    industrial: industrial.AsyncIndustrialResource
    issues: issues.AsyncIssuesResource
    live_shares: live_shares.AsyncLiveSharesResource
    organization_info: organization_info.AsyncOrganizationInfoResource
    preview: preview.AsyncPreviewResource
    speeding_intervals: speeding_intervals.AsyncSpeedingIntervalsResource
    tags: tags.AsyncTagsResource
    training_assignments: training_assignments.AsyncTrainingAssignmentsResource
    trips: trips.AsyncTripsResource
    user_roles: user_roles.AsyncUserRolesResource
    users: users.AsyncUsersResource
    hos_authentication_logs: hos_authentication_logs.AsyncHosAuthenticationLogsResource
    maintenance: maintenance.AsyncMaintenanceResource
    messages: messages.AsyncMessagesResource
    vision: vision.AsyncVisionResource
    machines: machines.AsyncMachinesResource
    sensors: sensors.AsyncSensorsResource
    webhooks: webhooks.AsyncWebhooksResource
    with_raw_response: AsyncSamsaraWithRawResponse
    with_streaming_response: AsyncSamsaraWithStreamedResponse

    # client options
    access_token: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        access_token: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async samsara client instance.

        This automatically infers the `access_token` argument from the `ACCESS_TOKEN` environment variable if it is not provided.
        """
        if access_token is None:
            access_token = os.environ.get("ACCESS_TOKEN")
        if access_token is None:
            raise SamsaraError(
                "The access_token client option must be set either by passing access_token to the client or by setting the ACCESS_TOKEN environment variable"
            )
        self.access_token = access_token

        self._environment = environment

        base_url_env = os.environ.get("SAMSARA_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `SAMSARA_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.addresses = addresses.AsyncAddressesResource(self)
        self.alerts = alerts.AsyncAlertsResource(self)
        self.assets = assets.AsyncAssetsResource(self)
        self.attributes = attributes.AsyncAttributesResource(self)
        self.beta = beta.AsyncBetaResource(self)
        self.cameras = cameras.AsyncCamerasResource(self)
        self.coaching = coaching.AsyncCoachingResource(self)
        self.contacts = contacts.AsyncContactsResource(self)
        self.defect_types = defect_types.AsyncDefectTypesResource(self)
        self.defects = defects.AsyncDefectsResource(self)
        self.driver_trailer_assignments = driver_trailer_assignments.AsyncDriverTrailerAssignmentsResource(self)
        self.drivers = drivers.AsyncDriversResource(self)
        self.dvirs = dvirs.AsyncDvirsResource(self)
        self.fleet = fleet.AsyncFleetResource(self)
        self.equipment = equipment.AsyncEquipmentResource(self)
        self.hos = hos.AsyncHosResource(self)
        self.trailers = trailers.AsyncTrailersResource(self)
        self.vehicles = vehicles.AsyncVehiclesResource(self)
        self.form_submissions = form_submissions.AsyncFormSubmissionsResource(self)
        self.fuel_purchases = fuel_purchases.AsyncFuelPurchasesResource(self)
        self.gateways = gateways.AsyncGatewaysResource(self)
        self.ifta_details = ifta_details.AsyncIftaDetailsResource(self)
        self.industrial = industrial.AsyncIndustrialResource(self)
        self.issues = issues.AsyncIssuesResource(self)
        self.live_shares = live_shares.AsyncLiveSharesResource(self)
        self.organization_info = organization_info.AsyncOrganizationInfoResource(self)
        self.preview = preview.AsyncPreviewResource(self)
        self.speeding_intervals = speeding_intervals.AsyncSpeedingIntervalsResource(self)
        self.tags = tags.AsyncTagsResource(self)
        self.training_assignments = training_assignments.AsyncTrainingAssignmentsResource(self)
        self.trips = trips.AsyncTripsResource(self)
        self.user_roles = user_roles.AsyncUserRolesResource(self)
        self.users = users.AsyncUsersResource(self)
        self.hos_authentication_logs = hos_authentication_logs.AsyncHosAuthenticationLogsResource(self)
        self.maintenance = maintenance.AsyncMaintenanceResource(self)
        self.messages = messages.AsyncMessagesResource(self)
        self.vision = vision.AsyncVisionResource(self)
        self.machines = machines.AsyncMachinesResource(self)
        self.sensors = sensors.AsyncSensorsResource(self)
        self.webhooks = webhooks.AsyncWebhooksResource(self)
        self.with_raw_response = AsyncSamsaraWithRawResponse(self)
        self.with_streaming_response = AsyncSamsaraWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        access_token = self.access_token
        return {"Authorization": f"Bearer {access_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        access_token: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            access_token=access_token or self.access_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class SamsaraWithRawResponse:
    def __init__(self, client: Samsara) -> None:
        self.addresses = addresses.AddressesResourceWithRawResponse(client.addresses)
        self.alerts = alerts.AlertsResourceWithRawResponse(client.alerts)
        self.assets = assets.AssetsResourceWithRawResponse(client.assets)
        self.attributes = attributes.AttributesResourceWithRawResponse(client.attributes)
        self.beta = beta.BetaResourceWithRawResponse(client.beta)
        self.cameras = cameras.CamerasResourceWithRawResponse(client.cameras)
        self.coaching = coaching.CoachingResourceWithRawResponse(client.coaching)
        self.contacts = contacts.ContactsResourceWithRawResponse(client.contacts)
        self.defect_types = defect_types.DefectTypesResourceWithRawResponse(client.defect_types)
        self.defects = defects.DefectsResourceWithRawResponse(client.defects)
        self.driver_trailer_assignments = driver_trailer_assignments.DriverTrailerAssignmentsResourceWithRawResponse(
            client.driver_trailer_assignments
        )
        self.drivers = drivers.DriversResourceWithRawResponse(client.drivers)
        self.dvirs = dvirs.DvirsResourceWithRawResponse(client.dvirs)
        self.fleet = fleet.FleetResourceWithRawResponse(client.fleet)
        self.equipment = equipment.EquipmentResourceWithRawResponse(client.equipment)
        self.hos = hos.HosResourceWithRawResponse(client.hos)
        self.trailers = trailers.TrailersResourceWithRawResponse(client.trailers)
        self.vehicles = vehicles.VehiclesResourceWithRawResponse(client.vehicles)
        self.form_submissions = form_submissions.FormSubmissionsResourceWithRawResponse(client.form_submissions)
        self.fuel_purchases = fuel_purchases.FuelPurchasesResourceWithRawResponse(client.fuel_purchases)
        self.gateways = gateways.GatewaysResourceWithRawResponse(client.gateways)
        self.ifta_details = ifta_details.IftaDetailsResourceWithRawResponse(client.ifta_details)
        self.industrial = industrial.IndustrialResourceWithRawResponse(client.industrial)
        self.issues = issues.IssuesResourceWithRawResponse(client.issues)
        self.live_shares = live_shares.LiveSharesResourceWithRawResponse(client.live_shares)
        self.organization_info = organization_info.OrganizationInfoResourceWithRawResponse(client.organization_info)
        self.preview = preview.PreviewResourceWithRawResponse(client.preview)
        self.speeding_intervals = speeding_intervals.SpeedingIntervalsResourceWithRawResponse(client.speeding_intervals)
        self.tags = tags.TagsResourceWithRawResponse(client.tags)
        self.training_assignments = training_assignments.TrainingAssignmentsResourceWithRawResponse(
            client.training_assignments
        )
        self.trips = trips.TripsResourceWithRawResponse(client.trips)
        self.user_roles = user_roles.UserRolesResourceWithRawResponse(client.user_roles)
        self.users = users.UsersResourceWithRawResponse(client.users)
        self.hos_authentication_logs = hos_authentication_logs.HosAuthenticationLogsResourceWithRawResponse(
            client.hos_authentication_logs
        )
        self.maintenance = maintenance.MaintenanceResourceWithRawResponse(client.maintenance)
        self.messages = messages.MessagesResourceWithRawResponse(client.messages)
        self.vision = vision.VisionResourceWithRawResponse(client.vision)
        self.machines = machines.MachinesResourceWithRawResponse(client.machines)
        self.sensors = sensors.SensorsResourceWithRawResponse(client.sensors)
        self.webhooks = webhooks.WebhooksResourceWithRawResponse(client.webhooks)


class AsyncSamsaraWithRawResponse:
    def __init__(self, client: AsyncSamsara) -> None:
        self.addresses = addresses.AsyncAddressesResourceWithRawResponse(client.addresses)
        self.alerts = alerts.AsyncAlertsResourceWithRawResponse(client.alerts)
        self.assets = assets.AsyncAssetsResourceWithRawResponse(client.assets)
        self.attributes = attributes.AsyncAttributesResourceWithRawResponse(client.attributes)
        self.beta = beta.AsyncBetaResourceWithRawResponse(client.beta)
        self.cameras = cameras.AsyncCamerasResourceWithRawResponse(client.cameras)
        self.coaching = coaching.AsyncCoachingResourceWithRawResponse(client.coaching)
        self.contacts = contacts.AsyncContactsResourceWithRawResponse(client.contacts)
        self.defect_types = defect_types.AsyncDefectTypesResourceWithRawResponse(client.defect_types)
        self.defects = defects.AsyncDefectsResourceWithRawResponse(client.defects)
        self.driver_trailer_assignments = (
            driver_trailer_assignments.AsyncDriverTrailerAssignmentsResourceWithRawResponse(
                client.driver_trailer_assignments
            )
        )
        self.drivers = drivers.AsyncDriversResourceWithRawResponse(client.drivers)
        self.dvirs = dvirs.AsyncDvirsResourceWithRawResponse(client.dvirs)
        self.fleet = fleet.AsyncFleetResourceWithRawResponse(client.fleet)
        self.equipment = equipment.AsyncEquipmentResourceWithRawResponse(client.equipment)
        self.hos = hos.AsyncHosResourceWithRawResponse(client.hos)
        self.trailers = trailers.AsyncTrailersResourceWithRawResponse(client.trailers)
        self.vehicles = vehicles.AsyncVehiclesResourceWithRawResponse(client.vehicles)
        self.form_submissions = form_submissions.AsyncFormSubmissionsResourceWithRawResponse(client.form_submissions)
        self.fuel_purchases = fuel_purchases.AsyncFuelPurchasesResourceWithRawResponse(client.fuel_purchases)
        self.gateways = gateways.AsyncGatewaysResourceWithRawResponse(client.gateways)
        self.ifta_details = ifta_details.AsyncIftaDetailsResourceWithRawResponse(client.ifta_details)
        self.industrial = industrial.AsyncIndustrialResourceWithRawResponse(client.industrial)
        self.issues = issues.AsyncIssuesResourceWithRawResponse(client.issues)
        self.live_shares = live_shares.AsyncLiveSharesResourceWithRawResponse(client.live_shares)
        self.organization_info = organization_info.AsyncOrganizationInfoResourceWithRawResponse(
            client.organization_info
        )
        self.preview = preview.AsyncPreviewResourceWithRawResponse(client.preview)
        self.speeding_intervals = speeding_intervals.AsyncSpeedingIntervalsResourceWithRawResponse(
            client.speeding_intervals
        )
        self.tags = tags.AsyncTagsResourceWithRawResponse(client.tags)
        self.training_assignments = training_assignments.AsyncTrainingAssignmentsResourceWithRawResponse(
            client.training_assignments
        )
        self.trips = trips.AsyncTripsResourceWithRawResponse(client.trips)
        self.user_roles = user_roles.AsyncUserRolesResourceWithRawResponse(client.user_roles)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)
        self.hos_authentication_logs = hos_authentication_logs.AsyncHosAuthenticationLogsResourceWithRawResponse(
            client.hos_authentication_logs
        )
        self.maintenance = maintenance.AsyncMaintenanceResourceWithRawResponse(client.maintenance)
        self.messages = messages.AsyncMessagesResourceWithRawResponse(client.messages)
        self.vision = vision.AsyncVisionResourceWithRawResponse(client.vision)
        self.machines = machines.AsyncMachinesResourceWithRawResponse(client.machines)
        self.sensors = sensors.AsyncSensorsResourceWithRawResponse(client.sensors)
        self.webhooks = webhooks.AsyncWebhooksResourceWithRawResponse(client.webhooks)


class SamsaraWithStreamedResponse:
    def __init__(self, client: Samsara) -> None:
        self.addresses = addresses.AddressesResourceWithStreamingResponse(client.addresses)
        self.alerts = alerts.AlertsResourceWithStreamingResponse(client.alerts)
        self.assets = assets.AssetsResourceWithStreamingResponse(client.assets)
        self.attributes = attributes.AttributesResourceWithStreamingResponse(client.attributes)
        self.beta = beta.BetaResourceWithStreamingResponse(client.beta)
        self.cameras = cameras.CamerasResourceWithStreamingResponse(client.cameras)
        self.coaching = coaching.CoachingResourceWithStreamingResponse(client.coaching)
        self.contacts = contacts.ContactsResourceWithStreamingResponse(client.contacts)
        self.defect_types = defect_types.DefectTypesResourceWithStreamingResponse(client.defect_types)
        self.defects = defects.DefectsResourceWithStreamingResponse(client.defects)
        self.driver_trailer_assignments = (
            driver_trailer_assignments.DriverTrailerAssignmentsResourceWithStreamingResponse(
                client.driver_trailer_assignments
            )
        )
        self.drivers = drivers.DriversResourceWithStreamingResponse(client.drivers)
        self.dvirs = dvirs.DvirsResourceWithStreamingResponse(client.dvirs)
        self.fleet = fleet.FleetResourceWithStreamingResponse(client.fleet)
        self.equipment = equipment.EquipmentResourceWithStreamingResponse(client.equipment)
        self.hos = hos.HosResourceWithStreamingResponse(client.hos)
        self.trailers = trailers.TrailersResourceWithStreamingResponse(client.trailers)
        self.vehicles = vehicles.VehiclesResourceWithStreamingResponse(client.vehicles)
        self.form_submissions = form_submissions.FormSubmissionsResourceWithStreamingResponse(client.form_submissions)
        self.fuel_purchases = fuel_purchases.FuelPurchasesResourceWithStreamingResponse(client.fuel_purchases)
        self.gateways = gateways.GatewaysResourceWithStreamingResponse(client.gateways)
        self.ifta_details = ifta_details.IftaDetailsResourceWithStreamingResponse(client.ifta_details)
        self.industrial = industrial.IndustrialResourceWithStreamingResponse(client.industrial)
        self.issues = issues.IssuesResourceWithStreamingResponse(client.issues)
        self.live_shares = live_shares.LiveSharesResourceWithStreamingResponse(client.live_shares)
        self.organization_info = organization_info.OrganizationInfoResourceWithStreamingResponse(
            client.organization_info
        )
        self.preview = preview.PreviewResourceWithStreamingResponse(client.preview)
        self.speeding_intervals = speeding_intervals.SpeedingIntervalsResourceWithStreamingResponse(
            client.speeding_intervals
        )
        self.tags = tags.TagsResourceWithStreamingResponse(client.tags)
        self.training_assignments = training_assignments.TrainingAssignmentsResourceWithStreamingResponse(
            client.training_assignments
        )
        self.trips = trips.TripsResourceWithStreamingResponse(client.trips)
        self.user_roles = user_roles.UserRolesResourceWithStreamingResponse(client.user_roles)
        self.users = users.UsersResourceWithStreamingResponse(client.users)
        self.hos_authentication_logs = hos_authentication_logs.HosAuthenticationLogsResourceWithStreamingResponse(
            client.hos_authentication_logs
        )
        self.maintenance = maintenance.MaintenanceResourceWithStreamingResponse(client.maintenance)
        self.messages = messages.MessagesResourceWithStreamingResponse(client.messages)
        self.vision = vision.VisionResourceWithStreamingResponse(client.vision)
        self.machines = machines.MachinesResourceWithStreamingResponse(client.machines)
        self.sensors = sensors.SensorsResourceWithStreamingResponse(client.sensors)
        self.webhooks = webhooks.WebhooksResourceWithStreamingResponse(client.webhooks)


class AsyncSamsaraWithStreamedResponse:
    def __init__(self, client: AsyncSamsara) -> None:
        self.addresses = addresses.AsyncAddressesResourceWithStreamingResponse(client.addresses)
        self.alerts = alerts.AsyncAlertsResourceWithStreamingResponse(client.alerts)
        self.assets = assets.AsyncAssetsResourceWithStreamingResponse(client.assets)
        self.attributes = attributes.AsyncAttributesResourceWithStreamingResponse(client.attributes)
        self.beta = beta.AsyncBetaResourceWithStreamingResponse(client.beta)
        self.cameras = cameras.AsyncCamerasResourceWithStreamingResponse(client.cameras)
        self.coaching = coaching.AsyncCoachingResourceWithStreamingResponse(client.coaching)
        self.contacts = contacts.AsyncContactsResourceWithStreamingResponse(client.contacts)
        self.defect_types = defect_types.AsyncDefectTypesResourceWithStreamingResponse(client.defect_types)
        self.defects = defects.AsyncDefectsResourceWithStreamingResponse(client.defects)
        self.driver_trailer_assignments = (
            driver_trailer_assignments.AsyncDriverTrailerAssignmentsResourceWithStreamingResponse(
                client.driver_trailer_assignments
            )
        )
        self.drivers = drivers.AsyncDriversResourceWithStreamingResponse(client.drivers)
        self.dvirs = dvirs.AsyncDvirsResourceWithStreamingResponse(client.dvirs)
        self.fleet = fleet.AsyncFleetResourceWithStreamingResponse(client.fleet)
        self.equipment = equipment.AsyncEquipmentResourceWithStreamingResponse(client.equipment)
        self.hos = hos.AsyncHosResourceWithStreamingResponse(client.hos)
        self.trailers = trailers.AsyncTrailersResourceWithStreamingResponse(client.trailers)
        self.vehicles = vehicles.AsyncVehiclesResourceWithStreamingResponse(client.vehicles)
        self.form_submissions = form_submissions.AsyncFormSubmissionsResourceWithStreamingResponse(
            client.form_submissions
        )
        self.fuel_purchases = fuel_purchases.AsyncFuelPurchasesResourceWithStreamingResponse(client.fuel_purchases)
        self.gateways = gateways.AsyncGatewaysResourceWithStreamingResponse(client.gateways)
        self.ifta_details = ifta_details.AsyncIftaDetailsResourceWithStreamingResponse(client.ifta_details)
        self.industrial = industrial.AsyncIndustrialResourceWithStreamingResponse(client.industrial)
        self.issues = issues.AsyncIssuesResourceWithStreamingResponse(client.issues)
        self.live_shares = live_shares.AsyncLiveSharesResourceWithStreamingResponse(client.live_shares)
        self.organization_info = organization_info.AsyncOrganizationInfoResourceWithStreamingResponse(
            client.organization_info
        )
        self.preview = preview.AsyncPreviewResourceWithStreamingResponse(client.preview)
        self.speeding_intervals = speeding_intervals.AsyncSpeedingIntervalsResourceWithStreamingResponse(
            client.speeding_intervals
        )
        self.tags = tags.AsyncTagsResourceWithStreamingResponse(client.tags)
        self.training_assignments = training_assignments.AsyncTrainingAssignmentsResourceWithStreamingResponse(
            client.training_assignments
        )
        self.trips = trips.AsyncTripsResourceWithStreamingResponse(client.trips)
        self.user_roles = user_roles.AsyncUserRolesResourceWithStreamingResponse(client.user_roles)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)
        self.hos_authentication_logs = hos_authentication_logs.AsyncHosAuthenticationLogsResourceWithStreamingResponse(
            client.hos_authentication_logs
        )
        self.maintenance = maintenance.AsyncMaintenanceResourceWithStreamingResponse(client.maintenance)
        self.messages = messages.AsyncMessagesResourceWithStreamingResponse(client.messages)
        self.vision = vision.AsyncVisionResourceWithStreamingResponse(client.vision)
        self.machines = machines.AsyncMachinesResourceWithStreamingResponse(client.machines)
        self.sensors = sensors.AsyncSensorsResourceWithStreamingResponse(client.sensors)
        self.webhooks = webhooks.AsyncWebhooksResourceWithStreamingResponse(client.webhooks)


Client = Samsara

AsyncClient = AsyncSamsara
