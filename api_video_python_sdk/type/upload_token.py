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


class RequiredUploadToken(TypedDict):
    pass

class OptionalUploadToken(TypedDict, total=False):
    # The unique identifier for the token you will use to authenticate an upload.
    token: str

    # Time-to-live - how long the upload token is valid for.
    ttl: int

    # When the token was created, displayed in ISO-8601 format.
    createdAt: datetime

    # When the token expires, displayed in ISO-8601 format.
    expiresAt: typing.Optional[datetime]

class UploadToken(RequiredUploadToken, OptionalUploadToken):
    pass
