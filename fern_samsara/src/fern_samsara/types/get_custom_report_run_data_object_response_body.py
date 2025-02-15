# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .custom_report_columns_object_response_body import CustomReportColumnsObjectResponseBody
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GetCustomReportRunDataObjectResponseBody(UniversalBaseModel):
    columns: typing.Optional[typing.List[CustomReportColumnsObjectResponseBody]] = pydantic.Field(default=None)
    """
    An array of objects containing data about column definitions
    """

    rows: typing.List[typing.List[typing.Dict[str, typing.Optional[typing.Any]]]] = pydantic.Field()
    """
    An array of arrays that represents each row in a custom report. The first index represents which row the data is for and the second index represents which column the data is for. For example, rows[1][3] accesses the second row's fourth column data. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
