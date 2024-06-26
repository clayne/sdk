# Generated by ariadne-codegen
# Source: ./src/binaryai/query.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class Sha256(BaseModel):
    file: Optional["Sha256File"]


class Sha256File(BaseModel):
    sha_256: str = Field(alias="sha256")


Sha256.model_rebuild()
