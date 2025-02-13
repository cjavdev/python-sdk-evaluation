# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .safety import (
    SafetyResource,
    AsyncSafetyResource,
    SafetyResourceWithRawResponse,
    AsyncSafetyResourceWithRawResponse,
    SafetyResourceWithStreamingResponse,
    AsyncSafetyResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .compliance import (
    ComplianceResource,
    AsyncComplianceResource,
    ComplianceResourceWithRawResponse,
    AsyncComplianceResourceWithRawResponse,
    ComplianceResourceWithStreamingResponse,
    AsyncComplianceResourceWithStreamingResponse,
)
from .driver_app import (
    DriverAppResource,
    AsyncDriverAppResource,
    DriverAppResourceWithRawResponse,
    AsyncDriverAppResourceWithRawResponse,
    DriverAppResourceWithStreamingResponse,
    AsyncDriverAppResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def compliance(self) -> ComplianceResource:
        return ComplianceResource(self._client)

    @cached_property
    def driver_app(self) -> DriverAppResource:
        return DriverAppResource(self._client)

    @cached_property
    def safety(self) -> SafetyResource:
        return SafetyResource(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def compliance(self) -> AsyncComplianceResource:
        return AsyncComplianceResource(self._client)

    @cached_property
    def driver_app(self) -> AsyncDriverAppResource:
        return AsyncDriverAppResource(self._client)

    @cached_property
    def safety(self) -> AsyncSafetyResource:
        return AsyncSafetyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def compliance(self) -> ComplianceResourceWithRawResponse:
        return ComplianceResourceWithRawResponse(self._settings.compliance)

    @cached_property
    def driver_app(self) -> DriverAppResourceWithRawResponse:
        return DriverAppResourceWithRawResponse(self._settings.driver_app)

    @cached_property
    def safety(self) -> SafetyResourceWithRawResponse:
        return SafetyResourceWithRawResponse(self._settings.safety)


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def compliance(self) -> AsyncComplianceResourceWithRawResponse:
        return AsyncComplianceResourceWithRawResponse(self._settings.compliance)

    @cached_property
    def driver_app(self) -> AsyncDriverAppResourceWithRawResponse:
        return AsyncDriverAppResourceWithRawResponse(self._settings.driver_app)

    @cached_property
    def safety(self) -> AsyncSafetyResourceWithRawResponse:
        return AsyncSafetyResourceWithRawResponse(self._settings.safety)


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def compliance(self) -> ComplianceResourceWithStreamingResponse:
        return ComplianceResourceWithStreamingResponse(self._settings.compliance)

    @cached_property
    def driver_app(self) -> DriverAppResourceWithStreamingResponse:
        return DriverAppResourceWithStreamingResponse(self._settings.driver_app)

    @cached_property
    def safety(self) -> SafetyResourceWithStreamingResponse:
        return SafetyResourceWithStreamingResponse(self._settings.safety)


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def compliance(self) -> AsyncComplianceResourceWithStreamingResponse:
        return AsyncComplianceResourceWithStreamingResponse(self._settings.compliance)

    @cached_property
    def driver_app(self) -> AsyncDriverAppResourceWithStreamingResponse:
        return AsyncDriverAppResourceWithStreamingResponse(self._settings.driver_app)

    @cached_property
    def safety(self) -> AsyncSafetyResourceWithStreamingResponse:
        return AsyncSafetyResourceWithStreamingResponse(self._settings.safety)
