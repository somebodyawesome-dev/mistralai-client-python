"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .imageurl import ImageURL, ImageURLTypedDict
from mistralai.types import BaseModel
from mistralai.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional, Union
from typing_extensions import Annotated, TypedDict


ImageURLChunkType = Literal["image_url"]

ImageURLChunkImageURLTypedDict = Union[ImageURLTypedDict, str]


ImageURLChunkImageURL = Union[ImageURL, str]


class ImageURLChunkTypedDict(TypedDict):
    r"""{\"type\":\"image_url\",\"image_url\":{\"url\":\"data:image/png;base64,iVBORw0"""

    image_url: ImageURLChunkImageURLTypedDict
    type: ImageURLChunkType


class ImageURLChunk(BaseModel):
    r"""{\"type\":\"image_url\",\"image_url\":{\"url\":\"data:image/png;base64,iVBORw0"""

    image_url: ImageURLChunkImageURL

    TYPE: Annotated[
        Annotated[
            Optional[ImageURLChunkType], AfterValidator(validate_const("image_url"))
        ],
        pydantic.Field(alias="type"),
    ] = "image_url"
