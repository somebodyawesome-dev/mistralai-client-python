"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .functioncall import FunctionCall, FunctionCallTypedDict
from .tooltypes import ToolTypes
from mistralai_gcp.types import BaseModel
from mistralai_gcp.utils import validate_open_enum
from pydantic.functional_validators import PlainValidator
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ToolCallTypedDict(TypedDict):
    function: FunctionCallTypedDict
    id: NotRequired[str]
    type: NotRequired[ToolTypes]


class ToolCall(BaseModel):
    function: FunctionCall

    id: Optional[str] = "null"

    type: Annotated[Optional[ToolTypes], PlainValidator(validate_open_enum(False))] = (
        None
    )
