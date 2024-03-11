# coding: utf-8

"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from api_video_python_sdk.paths.watermarks.get import ListAllRaw
from api_video_python_sdk.paths.watermarks.post import WatermarkRaw
from api_video_python_sdk.paths.watermarks_watermark_id.delete import Watermark0Raw


class WatermarksApiRaw(
    ListAllRaw,
    WatermarkRaw,
    Watermark0Raw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
