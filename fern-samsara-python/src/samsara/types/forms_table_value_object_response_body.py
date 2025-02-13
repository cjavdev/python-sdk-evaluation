# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .forms_table_column_object_response_body import FormsTableColumnObjectResponseBody
import pydantic
from .forms_table_row_object_response_body import FormsTableRowObjectResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FormsTableValueObjectResponseBody(UniversalBaseModel):
    """
    The value of a table form input field.
    """

    columns: typing.List[FormsTableColumnObjectResponseBody] = pydantic.Field()
    """
    List of table columns.
    """

    rows: typing.List[FormsTableRowObjectResponseBody] = pydantic.Field()
    """
    List of table rows.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
