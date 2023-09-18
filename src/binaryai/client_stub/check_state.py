# Generated by ariadne-codegen on 2023-09-18 11:53
# Source: ./src/binaryai/query.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import Status


class CheckState(BaseModel):
    file: Optional["CheckStateFile"]


class CheckStateFile(BaseModel):
    smart_binary_status: Optional["CheckStateFileSmartBinaryStatus"] = Field(alias="smartBinaryStatus")
    smart_beat_status: Optional["CheckStateFileSmartBeatStatus"] = Field(alias="smartBeatStatus")
    text: Optional["CheckStateFileText"]
    decompile_result: Optional["CheckStateFileDecompileResult"] = Field(alias="decompileResult")


class CheckStateFileSmartBinaryStatus(BaseModel):
    status: Status


class CheckStateFileSmartBeatStatus(BaseModel):
    status: Status


class CheckStateFileText(BaseModel):
    content: Optional[str]


class CheckStateFileDecompileResult(BaseModel):
    basic_info: "CheckStateFileDecompileResultBasicInfo" = Field(alias="basicInfo")


class CheckStateFileDecompileResultBasicInfo(BaseModel):
    file_type: str = Field(alias="fileType")


CheckState.model_rebuild()
CheckStateFile.model_rebuild()
CheckStateFileSmartBinaryStatus.model_rebuild()
CheckStateFileSmartBeatStatus.model_rebuild()
CheckStateFileText.model_rebuild()
CheckStateFileDecompileResult.model_rebuild()
CheckStateFileDecompileResultBasicInfo.model_rebuild()