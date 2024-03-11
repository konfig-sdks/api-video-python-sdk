# coding: utf-8

"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from api_video_python_sdk.paths.videos_video_id_chapters_language.delete import DeleteChapterInLanguage
from api_video_python_sdk.paths.videos_video_id_chapters_language.get import GetChapterByLanguage
from api_video_python_sdk.paths.videos_video_id_chapters.get import ListByVideo
from api_video_python_sdk.paths.videos_video_id_chapters_language.post import UploadVttFile
from api_video_python_sdk.apis.tags.chapters_api_raw import ChaptersApiRaw


class ChaptersApi(
    DeleteChapterInLanguage,
    GetChapterByLanguage,
    ListByVideo,
    UploadVttFile,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ChaptersApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ChaptersApiRaw(api_client)