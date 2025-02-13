# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .ifta_jurisdiction_summary_object_response_body import IftaJurisdictionSummaryObjectResponseBody
from ..core.serialization import FieldMetadata
import pydantic
from .ifta_report_troubleshooting_object_response_body import IftaReportTroubleshootingObjectResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class IftaJurisdictionReportDataObjectResponseBody(UniversalBaseModel):
    """
    Dictionary containing summarized jurisdiction report data.
    """

    jurisdiction_reports: typing_extensions.Annotated[
        typing.List[IftaJurisdictionSummaryObjectResponseBody], FieldMetadata(alias="jurisdictionReports")
    ] = pydantic.Field()
    """
    List of summarized jurisdiction reports.
    """

    month: typing.Optional[str] = pydantic.Field(default=None)
    """
    The specified month duration for this IFTA report.
    """

    quarter: typing.Optional[str] = pydantic.Field(default=None)
    """
    The specified quarter duration for this IFTA report.
    """

    troubleshooting: typing.Optional[IftaReportTroubleshootingObjectResponseBody] = None
    year: int = pydantic.Field()
    """
    The specified year for this IFTA report.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
