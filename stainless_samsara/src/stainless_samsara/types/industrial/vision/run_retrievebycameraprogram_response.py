# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "RunRetrievebycameraprogramResponse",
    "ReportMetadata",
    "Result",
    "ResultStepResult",
    "ResultStepResultAngleCheck",
    "ResultStepResultAngleCheckAngleConfigured",
    "ResultStepResultBarcode",
    "ResultStepResultBooleanLogic",
    "ResultStepResultBooleanLogicStep",
    "ResultStepResultCaliper",
    "ResultStepResultCaliperAngleRange",
    "ResultStepResultCaliperContrastRange",
    "ResultStepResultCaliperSharpnessRange",
    "ResultStepResultCaliperStraightnessRange",
    "ResultStepResultContour",
    "ResultStepResultDistance",
    "ResultStepResultExpirationDate",
    "ResultStepResultFindCopies",
    "ResultStepResultFindEdge",
    "ResultStepResultFindEdgeAngleRange",
    "ResultStepResultFindEdgeContrastRange",
    "ResultStepResultFindEdgeSharpnessRange",
    "ResultStepResultFindEdgeStraightnessRange",
    "ResultStepResultFindShapes",
    "ResultStepResultFixture",
    "ResultStepResultFixtureCoordinates",
    "ResultStepResultLabelMatch",
    "ResultStepResultPresenceAbsence",
    "ResultStepResultPresenceAbsenceBlueRange",
    "ResultStepResultPresenceAbsenceGrayscaleRange",
    "ResultStepResultPresenceAbsenceGreenRange",
    "ResultStepResultPresenceAbsenceHueRange",
    "ResultStepResultPresenceAbsenceRedRange",
    "ResultStepResultPresenceAbsenceSaturationRange",
    "ResultStepResultPresenceAbsenceValueRange",
    "ResultStepResultTextMatch",
]


class ReportMetadata(BaseModel):
    items_per_minute: Optional[float] = FieldInfo(alias="itemsPerMinute", default=None)

    no_read_count: Optional[int] = FieldInfo(alias="noReadCount", default=None)

    reject_count: Optional[int] = FieldInfo(alias="rejectCount", default=None)

    success_count: Optional[int] = FieldInfo(alias="successCount", default=None)


class ResultStepResultAngleCheckAngleConfigured(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class ResultStepResultAngleCheck(BaseModel):
    angle_configured: Optional[ResultStepResultAngleCheckAngleConfigured] = FieldInfo(
        alias="angleConfigured", default=None
    )
    """The configured angle allowance range (in degrees)"""

    angle_found: Optional[int] = FieldInfo(alias="angleFound", default=None)
    """The counter-clockwise angle detected from the first edge to the second edge"""

    end_step_name: Optional[str] = FieldInfo(alias="endStepName", default=None)
    """The name of the second reference step used to check the angle"""

    start_step_name: Optional[str] = FieldInfo(alias="startStepName", default=None)
    """The name of the first reference step used to check the angle"""


class ResultStepResultBarcode(BaseModel):
    contents: Optional[str] = None

    match_string: Optional[str] = FieldInfo(alias="matchString", default=None)

    type: Optional[str] = None


class ResultStepResultBooleanLogicStep(BaseModel):
    name: Optional[str] = None

    result: Optional[str] = None


class ResultStepResultBooleanLogic(BaseModel):
    operator: Optional[str] = None

    steps: Optional[List[ResultStepResultBooleanLogicStep]] = None


class ResultStepResultCaliperAngleRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class ResultStepResultCaliperContrastRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class ResultStepResultCaliperSharpnessRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class ResultStepResultCaliperStraightnessRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class ResultStepResultCaliper(BaseModel):
    angle_range: Optional[ResultStepResultCaliperAngleRange] = FieldInfo(alias="angleRange", default=None)
    """The configured angle allowance range"""

    contrast_range: Optional[ResultStepResultCaliperContrastRange] = FieldInfo(alias="contrastRange", default=None)
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

    sharpness_range: Optional[ResultStepResultCaliperSharpnessRange] = FieldInfo(alias="sharpnessRange", default=None)
    """The configured sharpness allowance range"""

    straightness_range: Optional[ResultStepResultCaliperStraightnessRange] = FieldInfo(
        alias="straightnessRange", default=None
    )
    """The configured straightness allowance range"""

    unit: Optional[str] = None
    """
    The measurement unit of the distance found and the min and max distance
    threshold
    """


class ResultStepResultContour(BaseModel):
    angle_degrees: Optional[int] = FieldInfo(alias="angleDegrees", default=None)
    """The rotation angle found"""

    angle_tolerance: Optional[int] = FieldInfo(alias="angleTolerance", default=None)
    """The rotation angle allowance"""

    match_percentage: Optional[int] = FieldInfo(alias="matchPercentage", default=None)
    """The contour match percentage with the configured contour"""

    match_threshold: Optional[int] = FieldInfo(alias="matchThreshold", default=None)
    """The configured match threshold for contours"""


class ResultStepResultDistance(BaseModel):
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


class ResultStepResultExpirationDate(BaseModel):
    date_offset: Optional[int] = FieldInfo(alias="dateOffset", default=None)

    found_date: Optional[str] = FieldInfo(alias="foundDate", default=None)

    match_date: Optional[str] = FieldInfo(alias="matchDate", default=None)


class ResultStepResultFindCopies(BaseModel):
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


class ResultStepResultFindEdgeAngleRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class ResultStepResultFindEdgeContrastRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class ResultStepResultFindEdgeSharpnessRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class ResultStepResultFindEdgeStraightnessRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class ResultStepResultFindEdge(BaseModel):
    angle_found: Optional[int] = FieldInfo(alias="angleFound", default=None)
    """The detected angle in degrees"""

    angle_range: Optional[ResultStepResultFindEdgeAngleRange] = FieldInfo(alias="angleRange", default=None)
    """The configured angle allowance range"""

    contrast_percent: Optional[int] = FieldInfo(alias="contrastPercent", default=None)
    """The detected contrast percentage"""

    contrast_range: Optional[ResultStepResultFindEdgeContrastRange] = FieldInfo(alias="contrastRange", default=None)
    """The configured contrast allowance range"""

    filter_polarity: Optional[str] = FieldInfo(alias="filterPolarity", default=None)
    """The configured polarity for finding edges.

    Valid values: `LIGHT TO DARK`, `DARK TO LIGHT`.
    """

    sharpness_percent: Optional[int] = FieldInfo(alias="sharpnessPercent", default=None)
    """The detected sharpness percentage"""

    sharpness_range: Optional[ResultStepResultFindEdgeSharpnessRange] = FieldInfo(alias="sharpnessRange", default=None)
    """The configured sharpness allowance range"""

    straightness_found: Optional[int] = FieldInfo(alias="straightnessFound", default=None)
    """The detected straightness percentage"""

    straightness_range: Optional[ResultStepResultFindEdgeStraightnessRange] = FieldInfo(
        alias="straightnessRange", default=None
    )
    """The configured straightness allowance range"""


class ResultStepResultFindShapes(BaseModel):
    found_count: Optional[int] = FieldInfo(alias="foundCount", default=None)

    max_count: Optional[int] = FieldInfo(alias="maxCount", default=None)

    min_count: Optional[int] = FieldInfo(alias="minCount", default=None)


class ResultStepResultFixtureCoordinates(BaseModel):
    x: Optional[int] = None

    y: Optional[int] = None


class ResultStepResultFixture(BaseModel):
    coordinates: Optional[ResultStepResultFixtureCoordinates] = None

    found: Optional[bool] = None

    rotation_degrees: Optional[int] = FieldInfo(alias="rotationDegrees", default=None)


class ResultStepResultLabelMatch(BaseModel):
    score: Optional[int] = None

    threshold: Optional[int] = None


class ResultStepResultPresenceAbsenceBlueRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class ResultStepResultPresenceAbsenceGrayscaleRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class ResultStepResultPresenceAbsenceGreenRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class ResultStepResultPresenceAbsenceHueRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class ResultStepResultPresenceAbsenceRedRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class ResultStepResultPresenceAbsenceSaturationRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class ResultStepResultPresenceAbsenceValueRange(BaseModel):
    high: Optional[int] = None

    low: Optional[int] = None


class ResultStepResultPresenceAbsence(BaseModel):
    blue_range: Optional[ResultStepResultPresenceAbsenceBlueRange] = FieldInfo(alias="blueRange", default=None)

    check_for_absence: Optional[bool] = FieldInfo(alias="checkForAbsence", default=None)

    grayscale_range: Optional[ResultStepResultPresenceAbsenceGrayscaleRange] = FieldInfo(
        alias="grayscaleRange", default=None
    )

    green_range: Optional[ResultStepResultPresenceAbsenceGreenRange] = FieldInfo(alias="greenRange", default=None)

    hue_range: Optional[ResultStepResultPresenceAbsenceHueRange] = FieldInfo(alias="hueRange", default=None)

    red_range: Optional[ResultStepResultPresenceAbsenceRedRange] = FieldInfo(alias="redRange", default=None)

    saturation_range: Optional[ResultStepResultPresenceAbsenceSaturationRange] = FieldInfo(
        alias="saturationRange", default=None
    )

    score: Optional[int] = None

    threshold: Optional[int] = None

    value_range: Optional[ResultStepResultPresenceAbsenceValueRange] = FieldInfo(alias="valueRange", default=None)


class ResultStepResultTextMatch(BaseModel):
    found_text: Optional[str] = FieldInfo(alias="foundText", default=None)

    match_string: Optional[str] = FieldInfo(alias="matchString", default=None)


class ResultStepResult(BaseModel):
    angle_check: Optional[ResultStepResultAngleCheck] = FieldInfo(alias="angleCheck", default=None)

    barcode: Optional[List[ResultStepResultBarcode]] = None

    boolean_logic: Optional[ResultStepResultBooleanLogic] = FieldInfo(alias="booleanLogic", default=None)

    caliper: Optional[ResultStepResultCaliper] = None

    contour: Optional[ResultStepResultContour] = None

    distance: Optional[ResultStepResultDistance] = None

    expiration_date: Optional[ResultStepResultExpirationDate] = FieldInfo(alias="expirationDate", default=None)

    find_copies: Optional[ResultStepResultFindCopies] = FieldInfo(alias="findCopies", default=None)

    find_edge: Optional[ResultStepResultFindEdge] = FieldInfo(alias="findEdge", default=None)

    find_shapes: Optional[ResultStepResultFindShapes] = FieldInfo(alias="findShapes", default=None)

    fixture: Optional[ResultStepResultFixture] = None

    label_match: Optional[ResultStepResultLabelMatch] = FieldInfo(alias="labelMatch", default=None)

    name: Optional[str] = None

    presence_absence: Optional[ResultStepResultPresenceAbsence] = FieldInfo(alias="presenceAbsence", default=None)

    result: Optional[str] = None

    text_match: Optional[ResultStepResultTextMatch] = FieldInfo(alias="textMatch", default=None)


class Result(BaseModel):
    capture_at_ms: Optional[float] = FieldInfo(alias="captureAtMs", default=None)

    result: Optional[str] = None

    step_results: Optional[List[ResultStepResult]] = FieldInfo(alias="stepResults", default=None)


class RunRetrievebycameraprogramResponse(BaseModel):
    device_id: Optional[int] = FieldInfo(alias="deviceId", default=None)

    ended_at_ms: Optional[int] = FieldInfo(alias="endedAtMs", default=None)

    program_id: Optional[int] = FieldInfo(alias="programId", default=None)

    report_metadata: Optional[ReportMetadata] = FieldInfo(alias="reportMetadata", default=None)

    results: Optional[List[Result]] = None

    started_at_ms: Optional[int] = FieldInfo(alias="startedAtMs", default=None)
