# coding: utf-8

"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from api_video_python_sdk.paths.videos_video_id_captions_language.delete import DeleteByLanguage
from api_video_python_sdk.paths.videos_video_id_captions_language.get import GetByLanguage
from api_video_python_sdk.paths.videos_video_id_captions.get import ListByVideoId
from api_video_python_sdk.paths.videos_video_id_captions_language.patch import UpdateSettings
from api_video_python_sdk.paths.videos_video_id_captions_language.post import UploadVttFile
from api_video_python_sdk.apis.tags.captions_api_raw import CaptionsApiRaw


class CaptionsApi(
    DeleteByLanguage,
    GetByLanguage,
    ListByVideoId,
    UpdateSettings,
    UploadVttFile,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CaptionsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CaptionsApiRaw(api_client)
