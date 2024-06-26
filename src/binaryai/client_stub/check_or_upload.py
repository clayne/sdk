# Generated by ariadne-codegen
# Source: ./src/binaryai/query.graphql

from typing import List, Literal, Union

from pydantic import Field

from .base_model import BaseModel


class CheckOrUpload(BaseModel):
    create_upload_ticket: Union[
        "CheckOrUploadCreateUploadTicketUploadTicket",
        "CheckOrUploadCreateUploadTicketOwnershipTicket",
        "CheckOrUploadCreateUploadTicketFile",
    ] = Field(alias="createUploadTicket", discriminator="typename__")


class CheckOrUploadCreateUploadTicketUploadTicket(BaseModel):
    typename__: Literal["UploadTicket"] = Field(alias="__typename")
    ticket_id: str = Field(alias="ticketID")
    url: str
    request_headers: List[
        "CheckOrUploadCreateUploadTicketUploadTicketRequestHeaders"
    ] = Field(alias="requestHeaders")


class CheckOrUploadCreateUploadTicketUploadTicketRequestHeaders(BaseModel):
    key: str
    value: str


class CheckOrUploadCreateUploadTicketOwnershipTicket(BaseModel):
    typename__: Literal["OwnershipTicket"] = Field(alias="__typename")
    ticket_id: str = Field(alias="ticketID")
    secret_prepend: str = Field(alias="secretPrepend")
    secret_append: str = Field(alias="secretAppend")


class CheckOrUploadCreateUploadTicketFile(BaseModel):
    typename__: Literal["File"] = Field(alias="__typename")
    sha_256: str = Field(alias="sha256")


CheckOrUpload.model_rebuild()
CheckOrUploadCreateUploadTicketUploadTicket.model_rebuild()
