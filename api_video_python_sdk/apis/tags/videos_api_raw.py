# coding: utf-8

"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from api_video_python_sdk.paths.videos.post import CreateObjectRaw
from api_video_python_sdk.paths.videos_video_id.delete import DeleteVideoObjectRaw
from api_video_python_sdk.paths.videos_video_id.get import GetVideoObjectRaw
from api_video_python_sdk.paths.videos_video_id_status.get import GetVideoStatusAndDetailsRaw
from api_video_python_sdk.paths.videos_video_id_source.post import IngestVideoFromSourceRaw
from api_video_python_sdk.paths.videos.get import ListAllObjectsRaw
from api_video_python_sdk.paths.videos_video_id_thumbnail.patch import SetThumbnailFromIntervalRaw
from api_video_python_sdk.paths.videos_video_id.patch import UpdateVideoObjectParametersRaw
from api_video_python_sdk.paths.upload.post import UploadRaw
from api_video_python_sdk.paths.videos_video_id_thumbnail.post import UploadThumbnailRaw


class VideosApiRaw(
    CreateObjectRaw,
    DeleteVideoObjectRaw,
    GetVideoObjectRaw,
    GetVideoStatusAndDetailsRaw,
    IngestVideoFromSourceRaw,
    ListAllObjectsRaw,
    SetThumbnailFromIntervalRaw,
    UpdateVideoObjectParametersRaw,
    UploadRaw,
    UploadThumbnailRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass