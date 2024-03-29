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
from pydantic import BaseModel, Field, RootModel

from api_video_python_sdk.pydantic.bytes_range import BytesRange
from api_video_python_sdk.pydantic.video_status_ingest_received_parts import VideoStatusIngestReceivedParts

class VideoStatusIngest(BaseModel):
    # There are four possible statuses depending on how you provide a video file: - `uploading` - the API is gathering the video source file from an upload. - `uploaded` - the video file is fully uploaded. - `ingesting` - the API is gathering the video source file from either a URL, or from cloning. - `ingested` - the video file is fully stored. 
    status: typing.Optional[Literal["uploading", "uploaded", "ingesting", "ingested"]] = Field(None, alias='status')

    # The size of your file in bytes.
    filesize: typing.Optional[typing.Optional[int]] = Field(None, alias='filesize')

    # The total number of bytes received, listed for each chunk of the upload.
    received_bytes: typing.Optional[typing.List[BytesRange]] = Field(None, alias='receivedBytes')

    received_parts: typing.Optional[VideoStatusIngestReceivedParts] = Field(None, alias='receivedParts')
    class Config:
        arbitrary_types_allowed = True
