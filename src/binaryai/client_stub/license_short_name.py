# Generated by ariadne-codegen
# Source: ./src/binaryai/query.graphql

from typing import List, Optional

from .base_model import BaseModel


class LicenseShortName(BaseModel):
    file: Optional["LicenseShortNameFile"]


class LicenseShortNameFile(BaseModel):
    scainfo: Optional[List["LicenseShortNameFileScainfo"]]


class LicenseShortNameFileScainfo(BaseModel):
    license: Optional[str]


LicenseShortName.model_rebuild()
LicenseShortNameFile.model_rebuild()
