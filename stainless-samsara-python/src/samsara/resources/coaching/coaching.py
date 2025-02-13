# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .driver_coach_assignments import (
    DriverCoachAssignmentsResource,
    AsyncDriverCoachAssignmentsResource,
    DriverCoachAssignmentsResourceWithRawResponse,
    AsyncDriverCoachAssignmentsResourceWithRawResponse,
    DriverCoachAssignmentsResourceWithStreamingResponse,
    AsyncDriverCoachAssignmentsResourceWithStreamingResponse,
)

__all__ = ["CoachingResource", "AsyncCoachingResource"]


class CoachingResource(SyncAPIResource):
    @cached_property
    def driver_coach_assignments(self) -> DriverCoachAssignmentsResource:
        return DriverCoachAssignmentsResource(self._client)

    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CoachingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return CoachingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CoachingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return CoachingResourceWithStreamingResponse(self)


class AsyncCoachingResource(AsyncAPIResource):
    @cached_property
    def driver_coach_assignments(self) -> AsyncDriverCoachAssignmentsResource:
        return AsyncDriverCoachAssignmentsResource(self._client)

    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCoachingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCoachingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCoachingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncCoachingResourceWithStreamingResponse(self)


class CoachingResourceWithRawResponse:
    def __init__(self, coaching: CoachingResource) -> None:
        self._coaching = coaching

    @cached_property
    def driver_coach_assignments(self) -> DriverCoachAssignmentsResourceWithRawResponse:
        return DriverCoachAssignmentsResourceWithRawResponse(self._coaching.driver_coach_assignments)

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._coaching.sessions)


class AsyncCoachingResourceWithRawResponse:
    def __init__(self, coaching: AsyncCoachingResource) -> None:
        self._coaching = coaching

    @cached_property
    def driver_coach_assignments(self) -> AsyncDriverCoachAssignmentsResourceWithRawResponse:
        return AsyncDriverCoachAssignmentsResourceWithRawResponse(self._coaching.driver_coach_assignments)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._coaching.sessions)


class CoachingResourceWithStreamingResponse:
    def __init__(self, coaching: CoachingResource) -> None:
        self._coaching = coaching

    @cached_property
    def driver_coach_assignments(self) -> DriverCoachAssignmentsResourceWithStreamingResponse:
        return DriverCoachAssignmentsResourceWithStreamingResponse(self._coaching.driver_coach_assignments)

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._coaching.sessions)


class AsyncCoachingResourceWithStreamingResponse:
    def __init__(self, coaching: AsyncCoachingResource) -> None:
        self._coaching = coaching

    @cached_property
    def driver_coach_assignments(self) -> AsyncDriverCoachAssignmentsResourceWithStreamingResponse:
        return AsyncDriverCoachAssignmentsResourceWithStreamingResponse(self._coaching.driver_coach_assignments)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._coaching.sessions)
