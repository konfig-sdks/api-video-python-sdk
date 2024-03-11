# coding: utf-8

"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from api_video_python_sdk.type.pagination import Pagination
from api_video_python_sdk.type.upload_token import UploadToken

class RequiredTokenListResponse(TypedDict):
    data: typing.List[UploadToken]

    pagination: Pagination

class OptionalTokenListResponse(TypedDict, total=False):
    pass

class TokenListResponse(RequiredTokenListResponse, OptionalTokenListResponse):
    pass
