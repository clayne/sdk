# Generated by ariadne-codegen
# Source: ./src/binaryai/query.graphql

from typing import Any, Dict, List, Optional, Union

from .ascii_string import ASCIIString
from .base_client import BaseClient
from .base_model import UNSET, UnsetType
from .check_or_upload import CheckOrUpload
from .check_state import CheckState
from .compressed_file import CompressedFile
from .create_file import CreateFile
from .cve_name import CVEName
from .download_link import DownloadLink
from .file_k_hash import FileKHash
from .file_malware_probability import FileMalwareProbability
from .file_size import FileSize
from .filename import Filename
from .function_info import FunctionInfo
from .function_list import FunctionList
from .function_match import FunctionMatch
from .functions_info import FunctionsInfo
from .input_types import CreateFileInput, CreateUploadTicketInput, ReanalyzeInput
from .license import License
from .license_short_name import LicenseShortName
from .mime_type import MIMEType
from .overview import Overview
from .reanalyze import Reanalyze
from .sca import SCA
from .sha_256 import Sha256


def gql(q: str) -> str:
    return q


class Client(BaseClient):
    def sha_256(self, md_5: str, **kwargs: Any) -> Sha256:
        query = gql(
            """
            query Sha256($md5: String!) {
              file: fileByHash(input: {md5: $md5}) {
                sha256
              }
            }
            """
        )
        variables: Dict[str, object] = {"md5": md_5}
        response = self.execute(
            query=query, operation_name="Sha256", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return Sha256.model_validate(data)

    def filename(self, sha_256: str, **kwargs: Any) -> Filename:
        query = gql(
            """
            query Filename($sha256: String!) {
              file: fileByHash(input: {sha256: $sha256}) {
                name
              }
            }
            """
        )
        variables: Dict[str, object] = {"sha256": sha_256}
        response = self.execute(
            query=query, operation_name="Filename", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return Filename.model_validate(data)

    def mime_type(self, sha_256: str, **kwargs: Any) -> MIMEType:
        query = gql(
            """
            query MIMEType($sha256: String!) {
              file: fileByHash(input: {sha256: $sha256}) {
                mimeType
              }
            }
            """
        )
        variables: Dict[str, object] = {"sha256": sha_256}
        response = self.execute(
            query=query, operation_name="MIMEType", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return MIMEType.model_validate(data)

    def file_size(self, sha_256: str, **kwargs: Any) -> FileSize:
        query = gql(
            """
            query FileSize($sha256: String!) {
              file: fileByHash(input: {sha256: $sha256}) {
                size
              }
            }
            """
        )
        variables: Dict[str, object] = {"sha256": sha_256}
        response = self.execute(
            query=query, operation_name="FileSize", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return FileSize.model_validate(data)

    def cve_name(self, sha_256: str, **kwargs: Any) -> CVEName:
        query = gql(
            """
            query CVEName($sha256: String!) {
              file: fileByHash(input: {sha256: $sha256}) {
                scainfo {
                  cves {
                    name
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"sha256": sha_256}
        response = self.execute(
            query=query, operation_name="CVEName", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return CVEName.model_validate(data)

    def license_short_name(self, sha_256: str, **kwargs: Any) -> LicenseShortName:
        query = gql(
            """
            query LicenseShortName($sha256: String!) {
              file: fileByHash(input: {sha256: $sha256}) {
                scainfo {
                  license
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"sha256": sha_256}
        response = self.execute(
            query=query,
            operation_name="LicenseShortName",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return LicenseShortName.model_validate(data)

    def license(self, sha_256: str, **kwargs: Any) -> License:
        query = gql(
            """
            query License($sha256: String!) {
              file: fileByHash(input: {sha256: $sha256}) {
                scainfo {
                  licenselist {
                    checkreason
                    content
                    extra
                    fullName
                    pass
                    risk
                    shortName
                    source
                    url
                    tags {
                      permission {
                        tagName
                        description
                      }
                      condition {
                        tagName
                        description
                      }
                      forbidden {
                        tagName
                        description
                      }
                    }
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"sha256": sha_256}
        response = self.execute(
            query=query, operation_name="License", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return License.model_validate(data)

    def ascii_string(self, sha_256: str, **kwargs: Any) -> ASCIIString:
        query = gql(
            """
            query ASCIIString($sha256: String!) {
              file: fileByHash(input: {sha256: $sha256}) {
                executable {
                  __typename
                  ... on COFFInfo {
                    asciiStrings
                  }
                  ... on ELFInfo {
                    asciiStrings
                  }
                  ... on MachoInfo {
                    asciiStrings
                  }
                  ... on PEInfo {
                    asciiStrings
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"sha256": sha_256}
        response = self.execute(
            query=query, operation_name="ASCIIString", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return ASCIIString.model_validate(data)

    def sca(self, sha_256: str, **kwargs: Any) -> SCA:
        query = gql(
            """
            query SCA($sha256: String!) {
              file: fileByHash(input: {sha256: $sha256}) {
                scainfo {
                  name
                  version
                  description
                  sourceCodeURL
                  summary
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"sha256": sha_256}
        response = self.execute(
            query=query, operation_name="SCA", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return SCA.model_validate(data)

    def overview(self, sha_256: str, **kwargs: Any) -> Overview:
        query = gql(
            """
            query Overview($sha256: String!) {
              file: fileByHash(input: {sha256: $sha256}) {
                decompileResult {
                  basicInfo {
                    fileType
                    machine
                    platform
                    endian
                    loader
                    entryPoint
                    baseAddress
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"sha256": sha_256}
        response = self.execute(
            query=query, operation_name="Overview", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return Overview.model_validate(data)

    def download_link(self, sha_256: str, **kwargs: Any) -> DownloadLink:
        query = gql(
            """
            query DownloadLink($sha256: String!) {
              file: fileByHash(input: {sha256: $sha256}) {
                downloadLink
              }
            }
            """
        )
        variables: Dict[str, object] = {"sha256": sha_256}
        response = self.execute(
            query=query, operation_name="DownloadLink", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return DownloadLink.model_validate(data)

    def check_state(self, sha_256: str, **kwargs: Any) -> CheckState:
        query = gql(
            """
            query CheckState($sha256: String!) {
              file: fileByHash(input: {sha256: $sha256}) {
                smartBinaryStatus: analyzeStatus(analyzer: SmartBinary) {
                  status
                }
                smartBeatStatus: analyzeStatus(analyzer: SmartBeat) {
                  status
                }
                text {
                  content
                }
                decompileResult {
                  basicInfo {
                    fileType
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"sha256": sha_256}
        response = self.execute(
            query=query, operation_name="CheckState", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return CheckState.model_validate(data)

    def function_list(self, sha_256: str, **kwargs: Any) -> FunctionList:
        query = gql(
            """
            query FunctionList($sha256: String!) {
              file: fileByHash(input: {sha256: $sha256}) {
                decompileResult {
                  functions {
                    offset
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"sha256": sha_256}
        response = self.execute(
            query=query, operation_name="FunctionList", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return FunctionList.model_validate(data)

    def function_info(
        self, sha_256: str, offset: Any, with_embedding: bool, **kwargs: Any
    ) -> FunctionInfo:
        query = gql(
            """
            query FunctionInfo($sha256: String!, $offset: BigInt!, $withEmbedding: Boolean!) {
              file: fileByHash(input: {sha256: $sha256}) {
                decompileResult {
                  function(offset: $offset) {
                    offset
                    name
                    embedding @include(if: $withEmbedding) {
                      vector
                      version
                    }
                    pseudoCode {
                      code
                    }
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "sha256": sha_256,
            "offset": offset,
            "withEmbedding": with_embedding,
        }
        response = self.execute(
            query=query, operation_name="FunctionInfo", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return FunctionInfo.model_validate(data)

    def functions_info(
        self,
        sha_256: str,
        with_embedding: bool,
        offset: Union[Optional[List[Any]], UnsetType] = UNSET,
        **kwargs: Any
    ) -> FunctionsInfo:
        query = gql(
            """
            query FunctionsInfo($sha256: String!, $offset: [BigInt!], $withEmbedding: Boolean!) {
              file: fileByHash(input: {sha256: $sha256}) {
                decompileResult {
                  functions(offset: $offset) {
                    offset
                    name
                    embedding @include(if: $withEmbedding) {
                      vector
                      version
                    }
                    pseudoCode {
                      code
                    }
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "sha256": sha_256,
            "offset": offset,
            "withEmbedding": with_embedding,
        }
        response = self.execute(
            query=query, operation_name="FunctionsInfo", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return FunctionsInfo.model_validate(data)

    def function_match(self, sha_256: str, offset: Any, **kwargs: Any) -> FunctionMatch:
        query = gql(
            """
            query FunctionMatch($sha256: String!, $offset: BigInt!) {
              file: fileByHash(input: {sha256: $sha256}) {
                decompileResult {
                  function(offset: $offset) {
                    match(topK: 10) {
                      score
                      function {
                        code
                      }
                    }
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"sha256": sha_256, "offset": offset}
        response = self.execute(
            query=query, operation_name="FunctionMatch", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return FunctionMatch.model_validate(data)

    def file_k_hash(self, sha_256: str, **kwargs: Any) -> FileKHash:
        query = gql(
            """
            query FileKHash($sha256: String!) {
              file: fileByHash(input: {sha256: $sha256}) {
                decompileResult {
                  kHashInfo {
                    hash {
                      hash
                      version
                    }
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"sha256": sha_256}
        response = self.execute(
            query=query, operation_name="FileKHash", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return FileKHash.model_validate(data)

    def file_malware_probability(
        self, sha_256: str, **kwargs: Any
    ) -> FileMalwareProbability:
        query = gql(
            """
            query FileMalwareProbability($sha256: String!) {
              file: fileByHash(input: {sha256: $sha256}) {
                decompileResult {
                  malwareProbability
                }
                analyzeStatus(analyzer: SmartBeat) {
                  status
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"sha256": sha_256}
        response = self.execute(
            query=query,
            operation_name="FileMalwareProbability",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return FileMalwareProbability.model_validate(data)

    def compressed_file(self, sha_256: str, **kwargs: Any) -> CompressedFile:
        query = gql(
            """
            query CompressedFile($sha256: String!) {
              file: fileByHash(input: {sha256: $sha256}) {
                decompressed {
                  __typename
                  ... on CompressedFile {
                    path
                    sha256
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"sha256": sha_256}
        response = self.execute(
            query=query, operation_name="CompressedFile", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return CompressedFile.model_validate(data)

    def reanalyze(self, input: ReanalyzeInput, **kwargs: Any) -> Reanalyze:
        query = gql(
            """
            mutation Reanalyze($input: ReanalyzeInput!) {
              reanalyze(input: $input) {
                noopReason
                file {
                  analyzeStatus {
                    status
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = self.execute(
            query=query, operation_name="Reanalyze", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return Reanalyze.model_validate(data)

    def check_or_upload(
        self, input: CreateUploadTicketInput, **kwargs: Any
    ) -> CheckOrUpload:
        query = gql(
            """
            mutation CheckOrUpload($input: CreateUploadTicketInput!) {
              createUploadTicket(input: $input) {
                __typename
                ... on File {
                  sha256
                }
                ... on UploadTicket {
                  ticketID
                  url
                  requestHeaders {
                    key
                    value
                  }
                }
                ... on OwnershipTicket {
                  ticketID
                  secretPrepend
                  secretAppend
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = self.execute(
            query=query, operation_name="CheckOrUpload", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return CheckOrUpload.model_validate(data)

    def create_file(self, input: CreateFileInput, **kwargs: Any) -> CreateFile:
        query = gql(
            """
            mutation CreateFile($input: CreateFileInput!) {
              createFile(input: $input) {
                sha256
                md5
                name
                size
                mimeType
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = self.execute(
            query=query, operation_name="CreateFile", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return CreateFile.model_validate(data)
