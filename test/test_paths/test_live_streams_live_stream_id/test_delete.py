# coding: utf-8

"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import api_video_python_sdk
from api_video_python_sdk.paths.live_streams_live_stream_id import delete
from api_video_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestLiveStreamsLiveStreamId(ApiTestMixin, unittest.TestCase):
    """
    LiveStreamsLiveStreamId unit test stubs
        Delete a live stream
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
