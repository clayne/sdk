# Generated by ariadne-codegen
# Source: ./src/binaryai/query.graphql

from typing import List

from pydantic import Field

from .base_model import BaseModel


class CreateFile(BaseModel):
    create_file: "CreateFileCreateFile" = Field(alias="createFile")


class CreateFileCreateFile(BaseModel):
    sha_256: str = Field(alias="sha256")
    md_5: str = Field(alias="md5")
    name: List[str]
    size: int
    mime_type: str = Field(alias="mimeType")


CreateFile.model_rebuild()
