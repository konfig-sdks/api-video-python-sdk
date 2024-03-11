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


class RequiredChaptersUpdatePayload(TypedDict):
    # The VTT file describing the chapters you want to upload.
    file: typing.IO

class OptionalChaptersUpdatePayload(TypedDict, total=False):
    pass

class ChaptersUpdatePayload(RequiredChaptersUpdatePayload, OptionalChaptersUpdatePayload):
    pass
