"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mistralai.types import BaseModel
from typing import Literal, Optional
from typing_extensions import NotRequired, TypedDict


TextChunkType = Literal["text"]


class TextChunkTypedDict(TypedDict):
    text: str
    type: NotRequired[TextChunkType]


class TextChunk(BaseModel):
    text: str

    type: Optional[TextChunkType] = "text"
