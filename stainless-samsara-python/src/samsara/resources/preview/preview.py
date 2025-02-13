# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .form_templates import (
    FormTemplatesResource,
    AsyncFormTemplatesResource,
    FormTemplatesResourceWithRawResponse,
    AsyncFormTemplatesResourceWithRawResponse,
    FormTemplatesResourceWithStreamingResponse,
    AsyncFormTemplatesResourceWithStreamingResponse,
)
from .cameras.cameras import (
    CamerasResource,
    AsyncCamerasResource,
    CamerasResourceWithRawResponse,
    AsyncCamerasResourceWithRawResponse,
    CamerasResourceWithStreamingResponse,
    AsyncCamerasResourceWithStreamingResponse,
)
from .training_courses import (
    TrainingCoursesResource,
    AsyncTrainingCoursesResource,
    TrainingCoursesResourceWithRawResponse,
    AsyncTrainingCoursesResourceWithRawResponse,
    TrainingCoursesResourceWithStreamingResponse,
    AsyncTrainingCoursesResourceWithStreamingResponse,
)
from .training_assignments import (
    TrainingAssignmentsResource,
    AsyncTrainingAssignmentsResource,
    TrainingAssignmentsResourceWithRawResponse,
    AsyncTrainingAssignmentsResourceWithRawResponse,
    TrainingAssignmentsResourceWithStreamingResponse,
    AsyncTrainingAssignmentsResourceWithStreamingResponse,
)
from .custom_reports.custom_reports import (
    CustomReportsResource,
    AsyncCustomReportsResource,
    CustomReportsResourceWithRawResponse,
    AsyncCustomReportsResourceWithRawResponse,
    CustomReportsResourceWithStreamingResponse,
    AsyncCustomReportsResourceWithStreamingResponse,
)
from .driver_efficiency.driver_efficiency import (
    DriverEfficiencyResource,
    AsyncDriverEfficiencyResource,
    DriverEfficiencyResourceWithRawResponse,
    AsyncDriverEfficiencyResourceWithRawResponse,
    DriverEfficiencyResourceWithStreamingResponse,
    AsyncDriverEfficiencyResourceWithStreamingResponse,
)

__all__ = ["PreviewResource", "AsyncPreviewResource"]


class PreviewResource(SyncAPIResource):
    @cached_property
    def cameras(self) -> CamerasResource:
        return CamerasResource(self._client)

    @cached_property
    def custom_reports(self) -> CustomReportsResource:
        return CustomReportsResource(self._client)

    @cached_property
    def driver_efficiency(self) -> DriverEfficiencyResource:
        return DriverEfficiencyResource(self._client)

    @cached_property
    def form_templates(self) -> FormTemplatesResource:
        return FormTemplatesResource(self._client)

    @cached_property
    def training_assignments(self) -> TrainingAssignmentsResource:
        return TrainingAssignmentsResource(self._client)

    @cached_property
    def training_courses(self) -> TrainingCoursesResource:
        return TrainingCoursesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PreviewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return PreviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreviewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return PreviewResourceWithStreamingResponse(self)


class AsyncPreviewResource(AsyncAPIResource):
    @cached_property
    def cameras(self) -> AsyncCamerasResource:
        return AsyncCamerasResource(self._client)

    @cached_property
    def custom_reports(self) -> AsyncCustomReportsResource:
        return AsyncCustomReportsResource(self._client)

    @cached_property
    def driver_efficiency(self) -> AsyncDriverEfficiencyResource:
        return AsyncDriverEfficiencyResource(self._client)

    @cached_property
    def form_templates(self) -> AsyncFormTemplatesResource:
        return AsyncFormTemplatesResource(self._client)

    @cached_property
    def training_assignments(self) -> AsyncTrainingAssignmentsResource:
        return AsyncTrainingAssignmentsResource(self._client)

    @cached_property
    def training_courses(self) -> AsyncTrainingCoursesResource:
        return AsyncTrainingCoursesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPreviewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreviewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncPreviewResourceWithStreamingResponse(self)


class PreviewResourceWithRawResponse:
    def __init__(self, preview: PreviewResource) -> None:
        self._preview = preview

    @cached_property
    def cameras(self) -> CamerasResourceWithRawResponse:
        return CamerasResourceWithRawResponse(self._preview.cameras)

    @cached_property
    def custom_reports(self) -> CustomReportsResourceWithRawResponse:
        return CustomReportsResourceWithRawResponse(self._preview.custom_reports)

    @cached_property
    def driver_efficiency(self) -> DriverEfficiencyResourceWithRawResponse:
        return DriverEfficiencyResourceWithRawResponse(self._preview.driver_efficiency)

    @cached_property
    def form_templates(self) -> FormTemplatesResourceWithRawResponse:
        return FormTemplatesResourceWithRawResponse(self._preview.form_templates)

    @cached_property
    def training_assignments(self) -> TrainingAssignmentsResourceWithRawResponse:
        return TrainingAssignmentsResourceWithRawResponse(self._preview.training_assignments)

    @cached_property
    def training_courses(self) -> TrainingCoursesResourceWithRawResponse:
        return TrainingCoursesResourceWithRawResponse(self._preview.training_courses)


class AsyncPreviewResourceWithRawResponse:
    def __init__(self, preview: AsyncPreviewResource) -> None:
        self._preview = preview

    @cached_property
    def cameras(self) -> AsyncCamerasResourceWithRawResponse:
        return AsyncCamerasResourceWithRawResponse(self._preview.cameras)

    @cached_property
    def custom_reports(self) -> AsyncCustomReportsResourceWithRawResponse:
        return AsyncCustomReportsResourceWithRawResponse(self._preview.custom_reports)

    @cached_property
    def driver_efficiency(self) -> AsyncDriverEfficiencyResourceWithRawResponse:
        return AsyncDriverEfficiencyResourceWithRawResponse(self._preview.driver_efficiency)

    @cached_property
    def form_templates(self) -> AsyncFormTemplatesResourceWithRawResponse:
        return AsyncFormTemplatesResourceWithRawResponse(self._preview.form_templates)

    @cached_property
    def training_assignments(self) -> AsyncTrainingAssignmentsResourceWithRawResponse:
        return AsyncTrainingAssignmentsResourceWithRawResponse(self._preview.training_assignments)

    @cached_property
    def training_courses(self) -> AsyncTrainingCoursesResourceWithRawResponse:
        return AsyncTrainingCoursesResourceWithRawResponse(self._preview.training_courses)


class PreviewResourceWithStreamingResponse:
    def __init__(self, preview: PreviewResource) -> None:
        self._preview = preview

    @cached_property
    def cameras(self) -> CamerasResourceWithStreamingResponse:
        return CamerasResourceWithStreamingResponse(self._preview.cameras)

    @cached_property
    def custom_reports(self) -> CustomReportsResourceWithStreamingResponse:
        return CustomReportsResourceWithStreamingResponse(self._preview.custom_reports)

    @cached_property
    def driver_efficiency(self) -> DriverEfficiencyResourceWithStreamingResponse:
        return DriverEfficiencyResourceWithStreamingResponse(self._preview.driver_efficiency)

    @cached_property
    def form_templates(self) -> FormTemplatesResourceWithStreamingResponse:
        return FormTemplatesResourceWithStreamingResponse(self._preview.form_templates)

    @cached_property
    def training_assignments(self) -> TrainingAssignmentsResourceWithStreamingResponse:
        return TrainingAssignmentsResourceWithStreamingResponse(self._preview.training_assignments)

    @cached_property
    def training_courses(self) -> TrainingCoursesResourceWithStreamingResponse:
        return TrainingCoursesResourceWithStreamingResponse(self._preview.training_courses)


class AsyncPreviewResourceWithStreamingResponse:
    def __init__(self, preview: AsyncPreviewResource) -> None:
        self._preview = preview

    @cached_property
    def cameras(self) -> AsyncCamerasResourceWithStreamingResponse:
        return AsyncCamerasResourceWithStreamingResponse(self._preview.cameras)

    @cached_property
    def custom_reports(self) -> AsyncCustomReportsResourceWithStreamingResponse:
        return AsyncCustomReportsResourceWithStreamingResponse(self._preview.custom_reports)

    @cached_property
    def driver_efficiency(self) -> AsyncDriverEfficiencyResourceWithStreamingResponse:
        return AsyncDriverEfficiencyResourceWithStreamingResponse(self._preview.driver_efficiency)

    @cached_property
    def form_templates(self) -> AsyncFormTemplatesResourceWithStreamingResponse:
        return AsyncFormTemplatesResourceWithStreamingResponse(self._preview.form_templates)

    @cached_property
    def training_assignments(self) -> AsyncTrainingAssignmentsResourceWithStreamingResponse:
        return AsyncTrainingAssignmentsResourceWithStreamingResponse(self._preview.training_assignments)

    @cached_property
    def training_courses(self) -> AsyncTrainingCoursesResourceWithStreamingResponse:
        return AsyncTrainingCoursesResourceWithStreamingResponse(self._preview.training_courses)
