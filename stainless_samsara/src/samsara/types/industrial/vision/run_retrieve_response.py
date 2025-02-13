# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "RunRetrieveResponse",
    "InspectionResult",
    "InspectionResultStepResult",
    "InspectionResultStepResultAngleCheck",
    "InspectionResultStepResultAngleCheckAngleConfigured",
    "InspectionResultStepResultBarcode",
    "InspectionResultStepResultBooleanLogic",
    "InspectionResultStepResultBooleanLogicStep",
    "InspectionResultStepResultCaliper",
    "InspectionResultStepResultCaliperAngleRange",
    "InspectionResultStepResultCaliperContrastRange",
    "InspectionResultStepResultCaliperSharpnessRange",
    "InspectionResultStepResultCaliperStraightnessRange",
    "InspectionResultStepResultContour",
    "InspectionResultStepResultDistance",
    "InspectionResultStepResultExpirationDate",
    "InspectionResultStepResultFindCopies",
    "InspectionResultStepResultFindEdge",
    "InspectionResultStepResultFindEdgeAngleRange",
    "InspectionResultStepResultFindEdgeContrastRange",
    "InspectionResultStepResultFindEdgeSharpnessRange",
    "InspectionResultStepResultFindEdgeStraightnessRange",
    "InspectionResultStepResultFindShapes",
    "InspectionResultStepResultFixture",
    "InspectionResultStepResultFixtureCoordinates",
    "InspectionResultStepResultLabelMatch",
    "InspectionResultStepResultPresenceAbsence",
    "InspectionResultStepResultPresenceAbsenceBlueRange",
    "InspectionResultStepResultPresenceAbsenceGrayscaleRange",
    "InspectionResultStepResultPresenceAbsenceGreenRange",
    "InspectionResultStepResultPresenceAbsenceHueRange",
    "InspectionResultStepResultPresenceAbsenceRedRange",
    "InspectionResultStepResultPresenceAbsenceSaturationRange",
    "InspectionResultStepResultPresenceAbsenceValueRange",
    "InspectionResultStepResultTextMatch",
    "Program",
    "RunSummary",
]


class InspectionResultStepResultAngleCheckAngleConfigured(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class InspectionResultStepResultAngleCheck(BaseModel):
    angle_configured: Optional[InspectionResultStepResultAngleCheckAngleConfigured] = FieldInfo(
        alias="angleConfigured", default=None
    )
    """The configured angle allowance range (in degrees)"""

    angle_found: Optional[int] = FieldInfo(alias="angleFound", default=None)
    """The counter-clockwise angle detected from the first edge to the second edge"""

    end_step_name: Optional[str] = FieldInfo(alias="endStepName", default=None)
    """The name of the second reference step used to check the angle"""

    start_step_name: Optional[str] = FieldInfo(alias="startStepName", default=None)
    """The name of the first reference step used to check the angle"""


class InspectionResultStepResultBarcode(BaseModel):
    contents: Optional[str] = None

    match_string: Optional[str] = FieldInfo(alias="matchString", default=None)

    type: Optional[str] = None


class InspectionResultStepResultBooleanLogicStep(BaseModel):
    name: Optional[str] = None

    result: Optional[str] = None


class InspectionResultStepResultBooleanLogic(BaseModel):
    operator: Optional[str] = None

    steps: Optional[List[InspectionResultStepResultBooleanLogicStep]] = None


class InspectionResultStepResultCaliperAngleRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class InspectionResultStepResultCaliperContrastRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class InspectionResultStepResultCaliperSharpnessRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class InspectionResultStepResultCaliperStraightnessRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class InspectionResultStepResultCaliper(BaseModel):
    angle_range: Optional[InspectionResultStepResultCaliperAngleRange] = FieldInfo(alias="angleRange", default=None)
    """The configured angle allowance range"""

    contrast_range: Optional[InspectionResultStepResultCaliperContrastRange] = FieldInfo(
        alias="contrastRange", default=None
    )
    """The configured contrast allowance range"""

    distance_found: Optional[float] = FieldInfo(alias="distanceFound", default=None)
    """The distance found between the found edges"""

    filter_polarity: Optional[Literal["LIGHT TO DARK", "DARK TO LIGHT"]] = FieldInfo(
        alias="filterPolarity", default=None
    )
    """The configured polarity for finding edges.

    Valid values: `LIGHT TO DARK`, `DARK TO LIGHT`.
    """

    max_distance: Optional[float] = FieldInfo(alias="maxDistance", default=None)
    """The maximum allowed distance threshold"""

    min_distance: Optional[float] = FieldInfo(alias="minDistance", default=None)
    """The minumum allowed distance threshold"""

    sharpness_range: Optional[InspectionResultStepResultCaliperSharpnessRange] = FieldInfo(
        alias="sharpnessRange", default=None
    )
    """The configured sharpness allowance range"""

    straightness_range: Optional[InspectionResultStepResultCaliperStraightnessRange] = FieldInfo(
        alias="straightnessRange", default=None
    )
    """The configured straightness allowance range"""

    unit: Optional[str] = None
    """
    The measurement unit of the distance found and the min and max distance
    threshold
    """


class InspectionResultStepResultContour(BaseModel):
    angle_degrees: Optional[int] = FieldInfo(alias="angleDegrees", default=None)
    """The rotation angle found"""

    angle_tolerance: Optional[int] = FieldInfo(alias="angleTolerance", default=None)
    """The rotation angle allowance"""

    match_percentage: Optional[int] = FieldInfo(alias="matchPercentage", default=None)
    """The contour match percentage with the configured contour"""

    match_threshold: Optional[int] = FieldInfo(alias="matchThreshold", default=None)
    """The configured match threshold for contours"""


class InspectionResultStepResultDistance(BaseModel):
    distance_found: Optional[int] = FieldInfo(alias="distanceFound", default=None)
    """The distance found between the start and end references"""

    end_step_name: Optional[str] = FieldInfo(alias="endStepName", default=None)
    """The name of the second reference step that we're checking the distances between"""

    enforce_offset_angle_range: Optional[bool] = FieldInfo(alias="enforceOffsetAngleRange", default=None)
    """Whether an offset angle range is enforced"""

    max_distance: Optional[int] = FieldInfo(alias="maxDistance", default=None)
    """The maximum allowed distance threshold"""

    max_offset_angle: Optional[int] = FieldInfo(alias="maxOffsetAngle", default=None)
    """The maximum angle allowance (in degrees) if enforceOffsetAngleRange is true"""

    min_distance: Optional[int] = FieldInfo(alias="minDistance", default=None)
    """The minumum allowed distance threshold"""

    min_offset_angle: Optional[int] = FieldInfo(alias="minOffsetAngle", default=None)
    """The minimum angle allowance (in degrees) if enforceOffsetAngleRange is true"""

    offset_angle_found: Optional[int] = FieldInfo(alias="offsetAngleFound", default=None)
    """
    The counter-clockwise angle (in degrees) found between the horizontal axis of
    the start reference step and the last
    """

    start_step_name: Optional[str] = FieldInfo(alias="startStepName", default=None)
    """The name of the first reference step that we're checking the distances between"""

    unit: Optional[str] = None
    """
    The measurement unit of the distance found and the min and max distance
    threshold
    """


class InspectionResultStepResultExpirationDate(BaseModel):
    date_offset: Optional[int] = FieldInfo(alias="dateOffset", default=None)

    found_date: Optional[str] = FieldInfo(alias="foundDate", default=None)

    match_date: Optional[str] = FieldInfo(alias="matchDate", default=None)


class InspectionResultStepResultFindCopies(BaseModel):
    angle_tolerance: Optional[int] = FieldInfo(alias="angleTolerance", default=None)
    """The orientation angle tolerance (+/- °)"""

    found_count: Optional[int] = FieldInfo(alias="foundCount", default=None)
    """The number of copies found"""

    max_count: Optional[int] = FieldInfo(alias="maxCount", default=None)
    """The maximum number of copies allowed"""

    min_count: Optional[int] = FieldInfo(alias="minCount", default=None)
    """The minimum number of copies allowed"""

    threshold: Optional[int] = None
    """
    The minimum required similarity (in %) of a found copy compared to the
    configured match region
    """


class InspectionResultStepResultFindEdgeAngleRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class InspectionResultStepResultFindEdgeContrastRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class InspectionResultStepResultFindEdgeSharpnessRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class InspectionResultStepResultFindEdgeStraightnessRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class InspectionResultStepResultFindEdge(BaseModel):
    angle_found: Optional[int] = FieldInfo(alias="angleFound", default=None)
    """The detected angle in degrees"""

    angle_range: Optional[InspectionResultStepResultFindEdgeAngleRange] = FieldInfo(alias="angleRange", default=None)
    """The configured angle allowance range"""

    contrast_percent: Optional[int] = FieldInfo(alias="contrastPercent", default=None)
    """The detected contrast percentage"""

    contrast_range: Optional[InspectionResultStepResultFindEdgeContrastRange] = FieldInfo(
        alias="contrastRange", default=None
    )
    """The configured contrast allowance range"""

    filter_polarity: Optional[str] = FieldInfo(alias="filterPolarity", default=None)
    """The configured polarity for finding edges.

    Valid values: `LIGHT TO DARK`, `DARK TO LIGHT`.
    """

    sharpness_percent: Optional[int] = FieldInfo(alias="sharpnessPercent", default=None)
    """The detected sharpness percentage"""

    sharpness_range: Optional[InspectionResultStepResultFindEdgeSharpnessRange] = FieldInfo(
        alias="sharpnessRange", default=None
    )
    """The configured sharpness allowance range"""

    straightness_found: Optional[int] = FieldInfo(alias="straightnessFound", default=None)
    """The detected straightness percentage"""

    straightness_range: Optional[InspectionResultStepResultFindEdgeStraightnessRange] = FieldInfo(
        alias="straightnessRange", default=None
    )
    """The configured straightness allowance range"""


class InspectionResultStepResultFindShapes(BaseModel):
    found_count: Optional[int] = FieldInfo(alias="foundCount", default=None)

    max_count: Optional[int] = FieldInfo(alias="maxCount", default=None)

    min_count: Optional[int] = FieldInfo(alias="minCount", default=None)


class InspectionResultStepResultFixtureCoordinates(BaseModel):
    x: Optional[int] = None

    y: Optional[int] = None


class InspectionResultStepResultFixture(BaseModel):
    coordinates: Optional[InspectionResultStepResultFixtureCoordinates] = None

    found: Optional[bool] = None

    rotation_degrees: Optional[int] = FieldInfo(alias="rotationDegrees", default=None)


class InspectionResultStepResultLabelMatch(BaseModel):
    score: Optional[int] = None

    threshold: Optional[int] = None


class InspectionResultStepResultPresenceAbsenceBlueRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class InspectionResultStepResultPresenceAbsenceGrayscaleRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class InspectionResultStepResultPresenceAbsenceGreenRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class InspectionResultStepResultPresenceAbsenceHueRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class InspectionResultStepResultPresenceAbsenceRedRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class InspectionResultStepResultPresenceAbsenceSaturationRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class InspectionResultStepResultPresenceAbsenceValueRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class InspectionResultStepResultPresenceAbsence(BaseModel):
    blue_range: Optional[InspectionResultStepResultPresenceAbsenceBlueRange] = FieldInfo(
        alias="blueRange", default=None
    )

    check_for_absence: Optional[bool] = FieldInfo(alias="checkForAbsence", default=None)

    grayscale_range: Optional[InspectionResultStepResultPresenceAbsenceGrayscaleRange] = FieldInfo(
        alias="grayscaleRange", default=None
    )

    green_range: Optional[InspectionResultStepResultPresenceAbsenceGreenRange] = FieldInfo(
        alias="greenRange", default=None
    )

    hue_range: Optional[InspectionResultStepResultPresenceAbsenceHueRange] = FieldInfo(alias="hueRange", default=None)

    red_range: Optional[InspectionResultStepResultPresenceAbsenceRedRange] = FieldInfo(alias="redRange", default=None)

    saturation_range: Optional[InspectionResultStepResultPresenceAbsenceSaturationRange] = FieldInfo(
        alias="saturationRange", default=None
    )

    score: Optional[int] = None

    threshold: Optional[int] = None

    value_range: Optional[InspectionResultStepResultPresenceAbsenceValueRange] = FieldInfo(
        alias="valueRange", default=None
    )


class InspectionResultStepResultTextMatch(BaseModel):
    found_text: Optional[str] = FieldInfo(alias="foundText", default=None)

    match_string: Optional[str] = FieldInfo(alias="matchString", default=None)


class InspectionResultStepResult(BaseModel):
    angle_check: Optional[InspectionResultStepResultAngleCheck] = FieldInfo(alias="angleCheck", default=None)

    barcode: Optional[List[InspectionResultStepResultBarcode]] = None

    boolean_logic: Optional[InspectionResultStepResultBooleanLogic] = FieldInfo(alias="booleanLogic", default=None)

    caliper: Optional[InspectionResultStepResultCaliper] = None

    contour: Optional[InspectionResultStepResultContour] = None

    distance: Optional[InspectionResultStepResultDistance] = None

    expiration_date: Optional[InspectionResultStepResultExpirationDate] = FieldInfo(
        alias="expirationDate", default=None
    )

    find_copies: Optional[InspectionResultStepResultFindCopies] = FieldInfo(alias="findCopies", default=None)

    find_edge: Optional[InspectionResultStepResultFindEdge] = FieldInfo(alias="findEdge", default=None)

    find_shapes: Optional[InspectionResultStepResultFindShapes] = FieldInfo(alias="findShapes", default=None)

    fixture: Optional[InspectionResultStepResultFixture] = None

    label_match: Optional[InspectionResultStepResultLabelMatch] = FieldInfo(alias="labelMatch", default=None)

    name: Optional[str] = None

    presence_absence: Optional[InspectionResultStepResultPresenceAbsence] = FieldInfo(
        alias="presenceAbsence", default=None
    )

    result: Optional[str] = None

    text_match: Optional[InspectionResultStepResultTextMatch] = FieldInfo(alias="textMatch", default=None)


class InspectionResult(BaseModel):
    capture_at_ms: Optional[float] = FieldInfo(alias="captureAtMs", default=None)

    result: Optional[str] = None

    step_results: Optional[List[InspectionResultStepResult]] = FieldInfo(alias="stepResults", default=None)


class Program(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None


class RunSummary(BaseModel):
    items_per_minute: Optional[float] = FieldInfo(alias="itemsPerMinute", default=None)

    no_read_count: Optional[int] = FieldInfo(alias="noReadCount", default=None)

    reject_count: Optional[int] = FieldInfo(alias="rejectCount", default=None)

    success_count: Optional[int] = FieldInfo(alias="successCount", default=None)


class RunRetrieveResponse(BaseModel):
    camera_id: Optional[int] = FieldInfo(alias="cameraId", default=None)

    ended_at_ms: Optional[int] = FieldInfo(alias="endedAtMs", default=None)

    inspection_results: Optional[List[InspectionResult]] = FieldInfo(alias="inspectionResults", default=None)

    is_ongoing: Optional[bool] = FieldInfo(alias="isOngoing", default=None)

    program: Optional[Program] = None

    run_summary: Optional[RunSummary] = FieldInfo(alias="runSummary", default=None)

    started_at_ms: Optional[int] = FieldInfo(alias="startedAtMs", default=None)
