"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .referencechunk import ReferenceChunk, ReferenceChunkTypedDict
from .textchunk import TextChunk, TextChunkTypedDict
from mistralai_azure.utils import get_discriminator
from pydantic import Discriminator, Tag
from typing import Union
from typing_extensions import Annotated, TypeAliasType


ContentChunkTypedDict = TypeAliasType(
    "ContentChunkTypedDict", Union[TextChunkTypedDict, ReferenceChunkTypedDict]
)


ContentChunk = Annotated[
    Union[
        Annotated[TextChunk, Tag("text")], Annotated[ReferenceChunk, Tag("reference")]
    ],
    Discriminator(lambda m: get_discriminator(m, "type", "type")),
]
