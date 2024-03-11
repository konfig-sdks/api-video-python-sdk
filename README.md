<div align="center">

[![Visit Api.video](./header.png)](https://api.video)

# Api.video<a id="apivideo"></a>

api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`apivideo.advanced_authentication.get_bearer_token`](#apivideoadvanced_authenticationget_bearer_token)
  * [`apivideo.advanced_authentication.refresh_bearer_token`](#apivideoadvanced_authenticationrefresh_bearer_token)
  * [`apivideo.analytics.get_live_stream_plays`](#apivideoanalyticsget_live_stream_plays)
  * [`apivideo.analytics.get_video_plays`](#apivideoanalyticsget_video_plays)
  * [`apivideo.captions.delete_by_language`](#apivideocaptionsdelete_by_language)
  * [`apivideo.captions.get_by_language`](#apivideocaptionsget_by_language)
  * [`apivideo.captions.list_by_video_id`](#apivideocaptionslist_by_video_id)
  * [`apivideo.captions.update_settings`](#apivideocaptionsupdate_settings)
  * [`apivideo.captions.upload_vtt_file`](#apivideocaptionsupload_vtt_file)
  * [`apivideo.chapters.delete_chapter_in_language`](#apivideochaptersdelete_chapter_in_language)
  * [`apivideo.chapters.get_chapter_by_language`](#apivideochaptersget_chapter_by_language)
  * [`apivideo.chapters.list_by_video`](#apivideochapterslist_by_video)
  * [`apivideo.chapters.upload_vtt_file`](#apivideochaptersupload_vtt_file)
  * [`apivideo.live_streams.create_livestream_object`](#apivideolive_streamscreate_livestream_object)
  * [`apivideo.live_streams.delete_livestream`](#apivideolive_streamsdelete_livestream)
  * [`apivideo.live_streams.delete_thumbnail`](#apivideolive_streamsdelete_thumbnail)
  * [`apivideo.live_streams.get_livestream_by_id`](#apivideolive_streamsget_livestream_by_id)
  * [`apivideo.live_streams.list_all`](#apivideolive_streamslist_all)
  * [`apivideo.live_streams.update_livestream_object`](#apivideolive_streamsupdate_livestream_object)
  * [`apivideo.live_streams.upload_thumbnail`](#apivideolive_streamsupload_thumbnail)
  * [`apivideo.player_themes.delete_player`](#apivideoplayer_themesdelete_player)
  * [`apivideo.player_themes.get_theme_by_player_id`](#apivideoplayer_themesget_theme_by_player_id)
  * [`apivideo.player_themes.players`](#apivideoplayer_themesplayers)
  * [`apivideo.player_themes.players_0`](#apivideoplayer_themesplayers_0)
  * [`apivideo.player_themes.remove_logo`](#apivideoplayer_themesremove_logo)
  * [`apivideo.player_themes.update_player_details`](#apivideoplayer_themesupdate_player_details)
  * [`apivideo.player_themes.upload_logo`](#apivideoplayer_themesupload_logo)
  * [`apivideo.upload_tokens.delete_token`](#apivideoupload_tokensdelete_token)
  * [`apivideo.upload_tokens.generate_token`](#apivideoupload_tokensgenerate_token)
  * [`apivideo.upload_tokens.get_details`](#apivideoupload_tokensget_details)
  * [`apivideo.upload_tokens.list_active_delegated_tokens`](#apivideoupload_tokenslist_active_delegated_tokens)
  * [`apivideo.videos.create_object`](#apivideovideoscreate_object)
  * [`apivideo.videos.delete_video_object`](#apivideovideosdelete_video_object)
  * [`apivideo.videos.get_video_object`](#apivideovideosget_video_object)
  * [`apivideo.videos.get_video_status_and_details`](#apivideovideosget_video_status_and_details)
  * [`apivideo.videos.ingest_video_from_source`](#apivideovideosingest_video_from_source)
  * [`apivideo.videos.list_all_objects`](#apivideovideoslist_all_objects)
  * [`apivideo.videos.set_thumbnail_from_interval`](#apivideovideosset_thumbnail_from_interval)
  * [`apivideo.videos.update_video_object_parameters`](#apivideovideosupdate_video_object_parameters)
  * [`apivideo.videos.upload`](#apivideovideosupload)
  * [`apivideo.videos.upload_thumbnail`](#apivideovideosupload_thumbnail)
  * [`apivideo.watermarks.list_all`](#apivideowatermarkslist_all)
  * [`apivideo.watermarks.watermark`](#apivideowatermarkswatermark)
  * [`apivideo.watermarks.watermark_0`](#apivideowatermarkswatermark_0)
  * [`apivideo.webhooks.create_webhook_event`](#apivideowebhookscreate_webhook_event)
  * [`apivideo.webhooks.delete_webhook`](#apivideowebhooksdelete_webhook)
  * [`apivideo.webhooks.get_details_by_id`](#apivideowebhooksget_details_by_id)
  * [`apivideo.webhooks.list_all`](#apivideowebhookslist_all)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=api.video&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from api_video_python_sdk import ApiVideo, ApiException

apivideo = ApiVideo()

try:
    # Get Bearer Token
    get_bearer_token_response = apivideo.advanced_authentication.get_bearer_token(
        api_key="9VxMaPgsaFg7EBqmuspSzF7",
    )
    print(get_bearer_token_response)
except ApiException as e:
    print("Exception when calling AdvancedAuthenticationApi.get_bearer_token: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from api_video_python_sdk import ApiVideo, ApiException

apivideo = ApiVideo()


async def main():
    try:
        # Get Bearer Token
        get_bearer_token_response = (
            await apivideo.advanced_authentication.aget_bearer_token(
                api_key="9VxMaPgsaFg7EBqmuspSzF7",
            )
        )
        print(get_bearer_token_response)
    except ApiException as e:
        print(
            "Exception when calling AdvancedAuthenticationApi.get_bearer_token: %s\n"
            % e
        )
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from api_video_python_sdk import ApiVideo, ApiException

apivideo = ApiVideo()

try:
    # Get Bearer Token
    get_bearer_token_response = apivideo.advanced_authentication.raw.get_bearer_token(
        api_key="9VxMaPgsaFg7EBqmuspSzF7",
    )
    pprint(get_bearer_token_response.body)
    pprint(get_bearer_token_response.body["access_token"])
    pprint(get_bearer_token_response.body["token_type"])
    pprint(get_bearer_token_response.body["refresh_token"])
    pprint(get_bearer_token_response.body["expires_in"])
    pprint(get_bearer_token_response.headers)
    pprint(get_bearer_token_response.status)
    pprint(get_bearer_token_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AdvancedAuthenticationApi.get_bearer_token: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `apivideo.advanced_authentication.get_bearer_token`<a id="apivideoadvanced_authenticationget_bearer_token"></a>

Returns a bearer token that can be used to authenticate other endpoint.

You can find the tutorial on using the disposable bearer token [here](https://docs.api.video/reference/disposable-bearer-token-authentication).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_bearer_token_response = apivideo.advanced_authentication.get_bearer_token(
    api_key="9VxMaPgsaFg7EBqmuspSzF7",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### api_key: `str`<a id="api_key-str"></a>

Your account API key. You can use your sandbox API key, or you can use your production API key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthenticatePayload`](./api_video_python_sdk/type/authenticate_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AccessToken`](./api_video_python_sdk/pydantic/access_token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/auth/api-key` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.advanced_authentication.refresh_bearer_token`<a id="apivideoadvanced_authenticationrefresh_bearer_token"></a>

Accepts the old bearer token and returns a new bearer token that can be used to authenticate other endpoint.

You can find the tutorial on using the disposable bearer token [here](https://docs.api.video/reference/disposable-bearer-token-authentication).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
refresh_bearer_token_response = apivideo.advanced_authentication.refresh_bearer_token(
    refresh_token="def502005346d9cc2bd79a7793ab5bdabfefcaabfbb8c253f14733f1262077e1a3f38c4751d6d20f590c3784e531a82adc11f05fc1949aa46d5575aaa99cb84b9334ba66ac773576b5d7a418937ae337de62811d086dd42ad1164b12f87d67be6ffea18f2d50be9b95697b21c4d3c4372849bdb2287259cb80541570e913691a08b2fa33c85885930de15cebea627fc09f0255562ab3d39d87d4ff8fc02b00e252afcd480421dec7de9d1411176bcf669c527762e22294b453bc9ea06e9fa8ba5b873feb2ee14ce0a6a6ddd4b78c580631e210e9b9387265dc2bec9478a66a09dcdce1c40d2f856689e9d81742c9628a0b87b359e0b218ea1f07427eef89f999e47af89792f598e05847bd008fddc32ee63f4a601ffb4cd2ad08977f1c854ec358238322c918f05aa5a41f8a171dee497218408abc8283473f6112aeed7310815416a0fa36c63667e0ed014fa40b8992891bf58bae400d901c01450101c88f4978938ad138adc19cfe5698d60fd82cb27c586f6a8f70f4393c7c9e579df8739d46d249fb76d7",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### refresh_token: `str`<a id="refresh_token-str"></a>

The refresh token is either the first refresh token you received when you authenticated with the auth/api-key endpoint, or it's the refresh token from the last time you used the auth/refresh endpoint. Place this in the body of your request to obtain a new access token (which is valid for an hour) and a new refresh token. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RefreshTokenPayload`](./api_video_python_sdk/type/refresh_token_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AccessToken`](./api_video_python_sdk/pydantic/access_token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/auth/refresh` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.analytics.get_live_stream_plays`<a id="apivideoanalyticsget_live_stream_plays"></a>

Retrieve filtered analytics about the number of plays for your live streams in a project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_live_stream_plays_response = apivideo.analytics.get_live_stream_plays(
    _from="2023-06-01T00:00:00.000Z",
    dimension="browser",
    to="2023-06-10T00:00:00.000Z",
    filter="liveStreamId:li3q7HxhApxRF1c8F8r6VeaI",
    current_page=2,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `date`<a id="_from-date"></a>

Use this query parameter to set the start date for the time period that you want analytics for. - The API returns analytics data including the day you set in `from`. - The date you set must be **within the last 30 days**. - The value you provide must follow the `YYYY-MM-DD` format. 

##### dimension: `str`<a id="dimension-str"></a>

Use this query parameter to define the dimension that you want analytics for. - `liveStreamId`: Returns analytics based on the public live stream identifiers. - `emittedAt`: Returns analytics based on the times of the play events. The API returns data in specific interval groups. When the date period you set in `from` and `to` is less than or equals to 2 days, the response for this dimension is grouped in hourly intervals. Otherwise, it is grouped in daily intervals. - `country`: Returns analytics based on the viewers' country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). - `deviceType`: Returns analytics based on the type of device used by the viewers during the play event. Possible response values are: `computer`, `phone`, `tablet`, `tv`, `console`, `wearable`, `unknown`. - `operatingSystem`: Returns analytics based on the operating system used by the viewers during the play event. Response values include `windows`, `mac osx`, `android`, `ios`, `linux`. - `browser`: Returns analytics based on the browser used by the viewers during the play event. Response values include `chrome`, `firefox`, `edge`, `opera`.

##### to: `date`<a id="to-date"></a>

Use this optional query parameter to set the end date for the time period that you want analytics for. - If you do not specify a `to` date, the API returns analytics data starting from the `from` date up until today, and excluding today. - The date you set must be **within the last 30 days**. - The value you provide must follow the `YYYY-MM-DD` format. 

##### filter: `str`<a id="filter-str"></a>

Use this query parameter to filter your results to a specific live stream in a project that you want analytics for. You must use the `liveStreamId:` prefix when specifying a live stream ID.

##### current_page: `int`<a id="current_page-int"></a>

Choose the number of search results to return per page. Minimum value: 1

##### page_size: `int`<a id="page_size-int"></a>

Results per page. Allowed values 1-100, default is 25.

#### 🔄 Return<a id="🔄-return"></a>

[`AnalyticsPlaysResponse`](./api_video_python_sdk/pydantic/analytics_plays_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/live-streams/plays` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.analytics.get_video_plays`<a id="apivideoanalyticsget_video_plays"></a>

Retrieve filtered analytics about the number of plays for your videos in a project.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_video_plays_response = apivideo.analytics.get_video_plays(
    _from="2023-06-01T00:00:00.000Z",
    dimension="browser",
    to="2023-06-10T00:00:00.000Z",
    filter="videoId:vi3q7HxhApxRF1c8F8r6VeaI",
    current_page=2,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `date`<a id="_from-date"></a>

Use this query parameter to set the start date for the time period that you want analytics for. - The API returns analytics data including the day you set in `from`. - The date you set must be **within the last 30 days**. - The value you provide must follow the `YYYY-MM-DD` format. 

##### dimension: `str`<a id="dimension-str"></a>

Use this query parameter to define the dimension that you want analytics for. - `videoId`: Returns analytics based on the public video identifiers. - `emittedAt`: Returns analytics based on the times of the play events. The API returns data in specific interval groups. When the date period you set in `from` and `to` is less than or equals to 2 days, the response for this dimension is grouped in hourly intervals. Otherwise, it is grouped in daily intervals. - `country`: Returns analytics based on the viewers' country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). - `deviceType`: Returns analytics based on the type of device used by the viewers during the play event. Possible response values are: `computer`, `phone`, `tablet`, `tv`, `console`, `wearable`, `unknown`. - `operatingSystem`: Returns analytics based on the operating system used by the viewers during the play event. Response values include `windows`, `mac osx`, `android`, `ios`, `linux`. - `browser`: Returns analytics based on the browser used by the viewers during the play event. Response values include `chrome`, `firefox`, `edge`, `opera`.

##### to: `date`<a id="to-date"></a>

Use this optional query parameter to set the end date for the time period that you want analytics for. - If you do not specify a `to` date, the API returns analytics data starting from the `from` date up until today, and excluding today. - The date you set must be **within the last 30 days**. - The value you provide must follow the `YYYY-MM-DD` format. 

##### filter: `str`<a id="filter-str"></a>

Use this query parameter to filter your results to a specific video in a project that you want analytics for. You must use the `videoId:` prefix when specifying a video ID.

##### current_page: `int`<a id="current_page-int"></a>

Choose the number of search results to return per page. Minimum value: 1

##### page_size: `int`<a id="page_size-int"></a>

Results per page. Allowed values 1-100, default is 25.

#### 🔄 Return<a id="🔄-return"></a>

[`AnalyticsPlaysResponse`](./api_video_python_sdk/pydantic/analytics_plays_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/analytics/videos/plays` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.captions.delete_by_language`<a id="apivideocaptionsdelete_by_language"></a>

Delete a caption in a specific language by by video id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
apivideo.captions.delete_by_language(
    video_id="vi4k0jvEUuaTdRAEjQ4Prklgc",
    language="en",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

The unique identifier for the video you want to delete a caption from.

##### language: `str`<a id="language-str"></a>

A valid language identifier using IETF language tags. You can use primary subtags like `en` (English), extended subtags like `fr-CA` (French, Canada), or region subtags like `zh-Hans-CN` (Simplified Chinese used in the PRC).  - This parameter **only accepts dashes for separators**, for example `fr-CA`. If you use a different separator in your request, the API returns an error. - When the value in your request does not match any covered language, the API returns an error. - You can find the list of supported tags [here](https://docs.api.video/vod/add-captions#supported-caption-language-tags).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos/{videoId}/captions/{language}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.captions.get_by_language`<a id="apivideocaptionsget_by_language"></a>

Retrieve a caption for a video in a specific language.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_language_response = apivideo.captions.get_by_language(
    video_id="vi4k0jvEUuaTdRAEjQ4Prklg",
    language="en",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

The unique identifier for the video you want captions for.

##### language: `str`<a id="language-str"></a>

A valid language identifier using IETF language tags. You can use primary subtags like `en` (English), extended subtags like `fr-CA` (French, Canada), or region subtags like `zh-Hans-CN` (Simplified Chinese used in the PRC).  - This parameter **only accepts dashes for separators**, for example `fr-CA`. If you use a different separator in your request, the API returns an error. - When the value in your request does not match any covered language, the API returns an error. - You can find the list of supported tags [here](https://docs.api.video/vod/add-captions#supported-caption-language-tags).

#### 🔄 Return<a id="🔄-return"></a>

[`Caption`](./api_video_python_sdk/pydantic/caption.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos/{videoId}/captions/{language}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.captions.list_by_video_id`<a id="apivideocaptionslist_by_video_id"></a>

Retrieve a list of available captions by video id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_video_id_response = apivideo.captions.list_by_video_id(
    video_id="vi4k0jvEUuaTdRAEjQ4Prklg",
    current_page=2,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

The unique identifier for the video you want to retrieve a list of captions for.

##### current_page: `int`<a id="current_page-int"></a>

Choose the number of search results to return per page. Minimum value: 1

##### page_size: `int`<a id="page_size-int"></a>

Results per page. Allowed values 1-100, default is 25.

#### 🔄 Return<a id="🔄-return"></a>

[`CaptionsListResponse`](./api_video_python_sdk/pydantic/captions_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos/{videoId}/captions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.captions.update_settings`<a id="apivideocaptionsupdate_settings"></a>

Update caption settings.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_settings_response = apivideo.captions.update_settings(
    video_id="vi4k0jvEUuaTdRAEjQ4Prklg",
    language="en",
    default=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

The unique identifier for the video you want to have automatic captions for.

##### language: `str`<a id="language-str"></a>

A valid language identifier using IETF language tags. You can use primary subtags like `en` (English), extended subtags like `fr-CA` (French, Canada), or region subtags like `zh-Hans-CN` (Simplified Chinese used in the PRC).  - This parameter **only accepts dashes for separators**, for example `fr-CA`. If you use a different separator in your request, the API returns an error. - When the value in your request does not match any covered language, the API returns an error. - You can find the list of supported tags [here](https://docs.api.video/vod/add-captions#supported-caption-language-tags).

##### default: `bool`<a id="default-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CaptionsUpdatePayload`](./api_video_python_sdk/type/captions_update_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Caption`](./api_video_python_sdk/pydantic/caption.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos/{videoId}/captions/{language}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.captions.upload_vtt_file`<a id="apivideocaptionsupload_vtt_file"></a>

Upload a VTT file to add captions to your video. More information can be found [here](https://docs.api.video/vod/add-captions)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_vtt_file_response = apivideo.captions.upload_vtt_file(
    video_id="vi4k0jvEUuaTdRAEjQ4Prklg",
    language="en",
    file=open("/path/to/file", "rb"),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

The unique identifier for the video you want to add a caption to.

##### language: `str`<a id="language-str"></a>

A valid language identifier using IETF language tags. You can use primary subtags like `en` (English), extended subtags like `fr-CA` (French, Canada), or region subtags like `zh-Hans-CN` (Simplified Chinese used in the PRC).  - This parameter **only accepts dashes for separators**, for example `fr-CA`. If you use a different separator in your request, the API returns an error. - When the value in your request does not match any covered language, the API returns an error. - You can find the list of supported tags [here](https://docs.api.video/vod/add-captions#supported-caption-language-tags).

##### file: `IO`<a id="file-io"></a>

The video text track (VTT) you want to upload.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CaptionsUploadPayload`](./api_video_python_sdk/type/captions_upload_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Caption`](./api_video_python_sdk/pydantic/caption.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos/{videoId}/captions/{language}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.chapters.delete_chapter_in_language`<a id="apivideochaptersdelete_chapter_in_language"></a>

Delete a chapter in a specific language by providing the video ID for the video you want to delete the chapter from and the language the chapter is in.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
apivideo.chapters.delete_chapter_in_language(
    video_id="vi4k0jvEUuaTdRAEjQ4Jfrgz",
    language="en",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

The unique identifier for the video you want to delete a chapter from.

##### language: `str`<a id="language-str"></a>

A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos/{videoId}/chapters/{language}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.chapters.get_chapter_by_language`<a id="apivideochaptersget_chapter_by_language"></a>

Retrieve a chapter for by video id in a specific language. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_chapter_by_language_response = apivideo.chapters.get_chapter_by_language(
    video_id="vi4k0jvEUuaTdRAEjQ4Jfrgz",
    language="en",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

The unique identifier for the video you want to show a chapter for.

##### language: `str`<a id="language-str"></a>

A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.

#### 🔄 Return<a id="🔄-return"></a>

[`Chapter`](./api_video_python_sdk/pydantic/chapter.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos/{videoId}/chapters/{language}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.chapters.list_by_video`<a id="apivideochapterslist_by_video"></a>

Retrieve a list of all chapters for by video id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_video_response = apivideo.chapters.list_by_video(
    video_id="vi4k0jvEUuaTdRAEjQ4Jfrgz",
    current_page=2,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

The unique identifier for the video you want to retrieve a list of chapters for.

##### current_page: `int`<a id="current_page-int"></a>

Choose the number of search results to return per page. Minimum value: 1

##### page_size: `int`<a id="page_size-int"></a>

Results per page. Allowed values 1-100, default is 25.

#### 🔄 Return<a id="🔄-return"></a>

[`ChaptersListResponse`](./api_video_python_sdk/pydantic/chapters_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos/{videoId}/chapters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.chapters.upload_vtt_file`<a id="apivideochaptersupload_vtt_file"></a>

Upload a VTT file to add chapters to your video.
Chapters help break the video into sections. Read our [tutorial](https://api.video/blog/tutorials/adding-chapters-to-your-videos/) for more details.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_vtt_file_response = apivideo.chapters.upload_vtt_file(
    video_id="vi4k0jvEUuaTdRAEjQ4Jfrgz",
    language="en",
    file=open("/path/to/file", "rb"),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

The unique identifier for the video you want to upload a chapter for.

##### language: `str`<a id="language-str"></a>

A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.

##### file: `IO`<a id="file-io"></a>

The VTT file describing the chapters you want to upload.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChaptersUpdatePayload`](./api_video_python_sdk/type/chapters_update_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Chapter`](./api_video_python_sdk/pydantic/chapter.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos/{videoId}/chapters/{language}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.live_streams.create_livestream_object`<a id="apivideolive_streamscreate_livestream_object"></a>

Creates a livestream object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_livestream_object_response = apivideo.live_streams.create_livestream_object(
    name="My Live Stream Video",
    public=True,
    player_id="pl4f4ferf5erfr5zed4fsdd",
    restreams=[
        {
            "name": "My RTMP server",
            "server_url": "rtmp://my.broadcast.example.com/app",
            "stream_key": "dw-dew8-q6w9-k67w-1ws8",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Add a name for your live stream here.

##### public: `bool`<a id="public-bool"></a>

Whether your video can be viewed by everyone, or requires authentication to see it. A setting of false will require a unique token for each view. Learn more about the Private Video feature [here](https://docs.api.video/delivery-analytics/video-privacy-access-management).

##### player_id: `str`<a id="player_id-str"></a>

The unique identifier for the player.

##### restreams: List[`RestreamsRequestObject`]<a id="restreams-listrestreamsrequestobject"></a>

Use this parameter to add, edit, or remove RTMP services where you want to restream a live stream. The list can only contain up to 5 destinations.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LiveStreamCreationPayload`](./api_video_python_sdk/type/live_stream_creation_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LiveStream`](./api_video_python_sdk/pydantic/live_stream.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/live-streams` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.live_streams.delete_livestream`<a id="apivideolive_streamsdelete_livestream"></a>

If you do not need a live stream any longer, you can send a request to delete it. All you need is the liveStreamId.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
apivideo.live_streams.delete_livestream(
    live_stream_id="li400mYKSgQ6xs7taUeSaEKr",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### live_stream_id: `str`<a id="live_stream_id-str"></a>

The unique ID for the live stream that you want to remove.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/live-streams/{liveStreamId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.live_streams.delete_thumbnail`<a id="apivideolive_streamsdelete_thumbnail"></a>

Send the unique identifier for a live stream to delete its thumbnail.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_thumbnail_response = apivideo.live_streams.delete_thumbnail(
    live_stream_id="li400mYKSgQ6xs7taUeSaEKr",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### live_stream_id: `str`<a id="live_stream_id-str"></a>

The unique identifier of the live stream whose thumbnail you want to delete.

#### 🔄 Return<a id="🔄-return"></a>

[`LiveStream`](./api_video_python_sdk/pydantic/live_stream.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/live-streams/{liveStreamId}/thumbnail` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.live_streams.get_livestream_by_id`<a id="apivideolive_streamsget_livestream_by_id"></a>

Get a livestream by id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_livestream_by_id_response = apivideo.live_streams.get_livestream_by_id(
    live_stream_id="li400mYKSgQ6xs7taUeSaEKr",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### live_stream_id: `str`<a id="live_stream_id-str"></a>

The unique ID for the live stream you want to watch.

#### 🔄 Return<a id="🔄-return"></a>

[`LiveStream`](./api_video_python_sdk/pydantic/live_stream.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/live-streams/{liveStreamId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.live_streams.list_all`<a id="apivideolive_streamslist_all"></a>

Get the list of livestreams on the workspace.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = apivideo.live_streams.list_all(
    stream_key="dw-dew8-q6w9-k67w-1ws8",
    name="My Video",
    sort_by="createdAt",
    sort_order="desc",
    current_page=2,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### stream_key: `str`<a id="stream_key-str"></a>

The unique stream key that allows you to stream videos.

##### name: `str`<a id="name-str"></a>

You can filter live streams by their name or a part of their name.

##### sort_by: `str`<a id="sort_by-str"></a>

Enables you to sort live stream results. Allowed attributes: `name`, `createdAt`, `updatedAt`. `name` - the name of the live stream. `createdAt` - the time a live stream was created. `updatedAt` - the time a live stream was last updated.  When using `createdAt` or `updatedAt`, the API sorts the results based on the ISO-8601 time format. 

##### sort_order: `str`<a id="sort_order-str"></a>

Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones. For title, it is 0-9 and A-Z ascending and Z-A, 9-0 descending.

##### current_page: `int`<a id="current_page-int"></a>

Choose the number of search results to return per page. Minimum value: 1

##### page_size: `int`<a id="page_size-int"></a>

Results per page. Allowed values 1-100, default is 25.

#### 🔄 Return<a id="🔄-return"></a>

[`LiveStreamListResponse`](./api_video_python_sdk/pydantic/live_stream_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/live-streams` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.live_streams.update_livestream_object`<a id="apivideolive_streamsupdate_livestream_object"></a>

Updates the livestream object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_livestream_object_response = apivideo.live_streams.update_livestream_object(
    live_stream_id="li400mYKSgQ6xs7taUeSaEKr",
    name="My Live Stream Video",
    public=True,
    player_id="pl45KFKdlddgk654dspkze",
    restreams=[
        {
            "name": "My RTMP server",
            "server_url": "rtmp://my.broadcast.example.com/app",
            "stream_key": "dw-dew8-q6w9-k67w-1ws8",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### live_stream_id: `str`<a id="live_stream_id-str"></a>

The unique ID for the live stream that you want to update information for such as player details.

##### name: `str`<a id="name-str"></a>

The name you want to use for your live stream.

##### public: `bool`<a id="public-bool"></a>

Whether your video can be viewed by everyone, or requires authentication to see it. A setting of false will require a unique token for each view. Learn more about the Private Video feature [here](https://docs.api.video/delivery-analytics/video-privacy-access-management).

##### player_id: `str`<a id="player_id-str"></a>

The unique ID for the player associated with a live stream that you want to update.

##### restreams: List[`RestreamsRequestObject`]<a id="restreams-listrestreamsrequestobject"></a>

Use this parameter to add, edit, or remove RTMP services where you want to restream a live stream. The list can only contain up to 5 destinations. This operation updates all restream destinations in the same request. If you do not want to modify an existing restream destination, you need to include it in your request, otherwise it is removed.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LiveStreamUpdatePayload`](./api_video_python_sdk/type/live_stream_update_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LiveStream`](./api_video_python_sdk/pydantic/live_stream.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/live-streams/{liveStreamId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.live_streams.upload_thumbnail`<a id="apivideolive_streamsupload_thumbnail"></a>

Upload the thumbnail for the livestream.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_thumbnail_response = apivideo.live_streams.upload_thumbnail(
    live_stream_id="vi4k0jvEUuaTdRAEjQ4Jfrgz",
    file=open("/path/to/file", "rb"),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### live_stream_id: `str`<a id="live_stream_id-str"></a>

The unique ID for the live stream you want to upload.

##### file: `IO`<a id="file-io"></a>

The image to be added as a thumbnail. The mime type should be image/jpeg, image/png or image/webp. The max allowed size is 8 MiB.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LiveStreamThumbnailUploadPayload`](./api_video_python_sdk/type/live_stream_thumbnail_upload_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LiveStream`](./api_video_python_sdk/pydantic/live_stream.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/live-streams/{liveStreamId}/thumbnail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.player_themes.delete_player`<a id="apivideoplayer_themesdelete_player"></a>

Delete a player if you no longer need it. You can delete any player that you have the player ID for.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
apivideo.player_themes.delete_player(
    player_id="pl45d5vFFGrfdsdsd156dGhh",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### player_id: `str`<a id="player_id-str"></a>

The unique identifier for the player you want to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/players/{playerId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.player_themes.get_theme_by_player_id`<a id="apivideoplayer_themesget_theme_by_player_id"></a>

Retreive a player theme by player id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_theme_by_player_id_response = apivideo.player_themes.get_theme_by_player_id(
    player_id="pl45d5vFFGrfdsdsd156dGhh",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### player_id: `str`<a id="player_id-str"></a>

The unique identifier for the player you want to retrieve. 

#### 🔄 Return<a id="🔄-return"></a>

[`PlayerTheme`](./api_video_python_sdk/pydantic/player_theme.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/players/{playerId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.player_themes.players`<a id="apivideoplayer_themesplayers"></a>

Retrieve a list of all the player themes you created, as well as details about each one.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
players_response = apivideo.player_themes.players(
    sort_by="createdAt",
    sort_order="asc",
    current_page=2,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort_by: `str`<a id="sort_by-str"></a>

createdAt is the time the player was created. updatedAt is the time the player was last updated. The time is presented in ISO-8601 format.

##### sort_order: `str`<a id="sort_order-str"></a>

Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones.

##### current_page: `int`<a id="current_page-int"></a>

Choose the number of search results to return per page. Minimum value: 1

##### page_size: `int`<a id="page_size-int"></a>

Results per page. Allowed values 1-100, default is 25.

#### 🔄 Return<a id="🔄-return"></a>

[`PlayerThemesListResponse`](./api_video_python_sdk/pydantic/player_themes_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/players` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.player_themes.players_0`<a id="apivideoplayer_themesplayers_0"></a>

Create a player for your video, and customise it.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
players_0_response = apivideo.player_themes.players_0(
    name="My nice theme",
    text="rgba(255, 255, 255, .95)",
    link="rgba(255, 0, 0, .95)",
    link_hover="rgba(255, 255, 255, .75)",
    link_active="rgba(255, 0, 0, .75)",
    track_played="rgba(255, 255, 255, .95)",
    track_unplayed="rgba(255, 255, 255, .1)",
    track_background="rgba(0, 0, 0, 0)",
    background_top="rgba(72, 4, 45, 1)",
    background_bottom="rgba(94, 95, 89, 1)",
    background_text="rgba(255, 255, 255, .95)",
    enable_api=True,
    enable_controls=True,
    force_autoplay=False,
    hide_title=False,
    force_loop=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Add a name for your player theme here.

##### text: `str`<a id="text-str"></a>

RGBA color for timer text. Default: rgba(255, 255, 255, 1)

##### link: `str`<a id="link-str"></a>

RGBA color for all controls. Default: rgba(255, 255, 255, 1)

##### link_hover: `str`<a id="link_hover-str"></a>

RGBA color for all controls when hovered. Default: rgba(255, 255, 255, 1)

##### link_active: `str`<a id="link_active-str"></a>

RGBA color for the play button when hovered.

##### track_played: `str`<a id="track_played-str"></a>

RGBA color playback bar: played content. Default: rgba(88, 131, 255, .95)

##### track_unplayed: `str`<a id="track_unplayed-str"></a>

RGBA color playback bar: downloaded but unplayed (buffered) content. Default: rgba(255, 255, 255, .35)

##### track_background: `str`<a id="track_background-str"></a>

RGBA color playback bar: background. Default: rgba(255, 255, 255, .2)

##### background_top: `str`<a id="background_top-str"></a>

RGBA color: top 50% of background. Default: rgba(0, 0, 0, .7)

##### background_bottom: `str`<a id="background_bottom-str"></a>

RGBA color: bottom 50% of background. Default: rgba(0, 0, 0, .7)

##### background_text: `str`<a id="background_text-str"></a>

RGBA color for title text. Default: rgba(255, 255, 255, 1)

##### enable_api: `bool`<a id="enable_api-bool"></a>

enable/disable player SDK access. Default: true

##### enable_controls: `bool`<a id="enable_controls-bool"></a>

enable/disable player controls. Default: true

##### force_autoplay: `bool`<a id="force_autoplay-bool"></a>

enable/disable player autoplay. Default: false

##### hide_title: `bool`<a id="hide_title-bool"></a>

enable/disable title. Default: false

##### force_loop: `bool`<a id="force_loop-bool"></a>

enable/disable looping. Default: false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PlayerThemeCreationPayload`](./api_video_python_sdk/type/player_theme_creation_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PlayerTheme`](./api_video_python_sdk/pydantic/player_theme.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/players` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.player_themes.remove_logo`<a id="apivideoplayer_themesremove_logo"></a>

Delete the logo associated to a player.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
apivideo.player_themes.remove_logo(
    player_id="pl14Db6oMJRH6SRVoOwORacK",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### player_id: `str`<a id="player_id-str"></a>

The unique identifier for the player.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/players/{playerId}/logo` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.player_themes.update_player_details`<a id="apivideoplayer_themesupdate_player_details"></a>

Use a player ID to update specific details for a player. 
NOTE: It may take up to 10 min before the new player configuration is available from our CDN.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_player_details_response = apivideo.player_themes.update_player_details(
    player_id="pl45d5vFFGrfdsdsd156dGhh",
    name="string_example",
    text="string_example",
    link="string_example",
    link_hover="string_example",
    link_active="string_example",
    track_played="string_example",
    track_unplayed="string_example",
    track_background="string_example",
    background_top="string_example",
    background_bottom="string_example",
    background_text="string_example",
    enable_api=True,
    enable_controls=True,
    force_autoplay=True,
    hide_title=True,
    force_loop=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### player_id: `str`<a id="player_id-str"></a>

The unique identifier for the player.

##### name: `str`<a id="name-str"></a>

Add a name for your player theme here.

##### text: `str`<a id="text-str"></a>

RGBA color for timer text. Default: rgba(255, 255, 255, 1)

##### link: `str`<a id="link-str"></a>

RGBA color for all controls. Default: rgba(255, 255, 255, 1)

##### link_hover: `str`<a id="link_hover-str"></a>

RGBA color for all controls when hovered. Default: rgba(255, 255, 255, 1)

##### link_active: `str`<a id="link_active-str"></a>

RGBA color for the play button when hovered.

##### track_played: `str`<a id="track_played-str"></a>

RGBA color playback bar: played content. Default: rgba(88, 131, 255, .95)

##### track_unplayed: `str`<a id="track_unplayed-str"></a>

RGBA color playback bar: downloaded but unplayed (buffered) content. Default: rgba(255, 255, 255, .35)

##### track_background: `str`<a id="track_background-str"></a>

RGBA color playback bar: background. Default: rgba(255, 255, 255, .2)

##### background_top: `str`<a id="background_top-str"></a>

RGBA color: top 50% of background. Default: rgba(0, 0, 0, .7)

##### background_bottom: `str`<a id="background_bottom-str"></a>

RGBA color: bottom 50% of background. Default: rgba(0, 0, 0, .7)

##### background_text: `str`<a id="background_text-str"></a>

RGBA color for title text. Default: rgba(255, 255, 255, 1)

##### enable_api: `bool`<a id="enable_api-bool"></a>

enable/disable player SDK access. Default: true

##### enable_controls: `bool`<a id="enable_controls-bool"></a>

enable/disable player controls. Default: true

##### force_autoplay: `bool`<a id="force_autoplay-bool"></a>

enable/disable player autoplay. Default: false

##### hide_title: `bool`<a id="hide_title-bool"></a>

enable/disable title. Default: false

##### force_loop: `bool`<a id="force_loop-bool"></a>

enable/disable looping. Default: false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PlayerThemeUpdatePayload`](./api_video_python_sdk/type/player_theme_update_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PlayerTheme`](./api_video_python_sdk/pydantic/player_theme.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/players/{playerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.player_themes.upload_logo`<a id="apivideoplayer_themesupload_logo"></a>

Upload an image file as a logo for your player. The image should fit within these constraints:
- The image mime type must be `image/jpeg` or `image/png`. api.video recommends using `png` images with transparent background.
- The image size should be a maximum of 200px width x 100px.
- The file size should be a maximum of 100 KiB.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_logo_response = apivideo.player_themes.upload_logo(
    player_id="pl14Db6oMJRH6SRVoOwORacK",
    file="mylogo.jpg",
    link="https://my-company.com",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### player_id: `str`<a id="player_id-str"></a>

The unique identifier for the player.

##### file: `IO`<a id="file-io"></a>

The name of the file you want to use for your logo.

##### link: `str`<a id="link-str"></a>

A public link that you want to advertise in your player. For example, you could add a link to your company. When a viewer clicks on your logo, they will be taken to this address.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PlayerThemeUploadLogoPayload`](./api_video_python_sdk/type/player_theme_upload_logo_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PlayerTheme`](./api_video_python_sdk/pydantic/player_theme.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/players/{playerId}/logo` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.upload_tokens.delete_token`<a id="apivideoupload_tokensdelete_token"></a>

Delete an existing upload token. This is especially useful for tokens you may have created that do not expire.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
apivideo.upload_tokens.delete_token(
    upload_token="to1tcmSFHeYY5KzyhOqVKMKb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### upload_token: `str`<a id="upload_token-str"></a>

The unique identifier for the upload token you want to delete. Deleting a token will make it so the token can no longer be used for authentication.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/upload-tokens/{uploadToken}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.upload_tokens.generate_token`<a id="apivideoupload_tokensgenerate_token"></a>

Generates an upload token that can be used to replace the API Key. More information can be found [here](https://docs.api.video/vod/delegated-upload-tokens)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_token_response = apivideo.upload_tokens.generate_token(
    ttl=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ttl: `int`<a id="ttl-int"></a>

Time in seconds that the token will be active. A value of 0 means that the token has no exipration date. The default is to have no expiration.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TokenCreationPayload`](./api_video_python_sdk/type/token_creation_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UploadToken`](./api_video_python_sdk/pydantic/upload_token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/upload-tokens` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.upload_tokens.get_details`<a id="apivideoupload_tokensget_details"></a>

Retrieve details about a specific upload token by id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = apivideo.upload_tokens.get_details(
    upload_token="to1tcmSFHeYY5KzyhOqVKMKb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### upload_token: `str`<a id="upload_token-str"></a>

The unique identifier for the token you want information about.

#### 🔄 Return<a id="🔄-return"></a>

[`UploadToken`](./api_video_python_sdk/pydantic/upload_token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/upload-tokens/{uploadToken}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.upload_tokens.list_active_delegated_tokens`<a id="apivideoupload_tokenslist_active_delegated_tokens"></a>

Retrieve a list of all currently active delegated tokens.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_active_delegated_tokens_response = (
    apivideo.upload_tokens.list_active_delegated_tokens(
        sort_by="ttl",
        sort_order="asc",
        current_page=2,
        page_size=30,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort_by: `str`<a id="sort_by-str"></a>

Allowed: createdAt, ttl. You can use these to sort by when a token was created, or how much longer the token will be active (ttl - time to live). Date and time is presented in ISO-8601 format.

##### sort_order: `str`<a id="sort_order-str"></a>

Allowed: asc, desc. Ascending is 0-9 or A-Z. Descending is 9-0 or Z-A.

##### current_page: `int`<a id="current_page-int"></a>

Choose the number of search results to return per page. Minimum value: 1

##### page_size: `int`<a id="page_size-int"></a>

Results per page. Allowed values 1-100, default is 25.

#### 🔄 Return<a id="🔄-return"></a>

[`TokenListResponse`](./api_video_python_sdk/pydantic/token_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/upload-tokens` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.videos.create_object`<a id="apivideovideoscreate_object"></a>

Creates a video object. More information on video objects can be found [here](https://docs.api.video/reference/api/Videos).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_object_response = apivideo.videos.create_object(
    title="Maths video",
    tags=['["maths", "string theory", "video"]'],
    description="A video about string theory.",
    source="https://www.myvideo.url.com/video.mp4 OR vi4k0jvEUuaTdRAEjQ4JfOyl",
    public=True,
    panoramic=False,
    mp4_support=True,
    player_id="pl45KFKdlddgk654dspkze",
    metadata=[
        {
            "key": "Color",
            "value": "Green",
        }
    ],
    clip={
        "start_timecode": "00:01:15",
        "end_timecode": "00:02:33",
    },
    watermark={
        "id": "watermark_1BWr2L5MTQwxGkuxKjzh6i",
        "top": "10px",
        "left": "10px",
        "bottom": "10px",
        "right": "10px",
        "width": "initial",
        "height": "initial",
        "opacity": "70%",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

The title of your new video.

##### tags: [`VideoCreationPayloadTags`](./api_video_python_sdk/type/video_creation_payload_tags.py)<a id="tags-videocreationpayloadtagsapi_video_python_sdktypevideo_creation_payload_tagspy"></a>

##### description: `str`<a id="description-str"></a>

A brief description of your video.

##### source: `str`<a id="source-str"></a>

You can either add a video already on the web, by entering the URL of the video, or you can also enter the `videoId` of one of the videos you already have on your api.video acccount, and this will generate a copy of your video. Creating a copy of a video can be especially useful if you want to keep your original video and trim or apply a watermark onto the copy you would create.

##### public: `bool`<a id="public-bool"></a>

Default: True. If set to `false` the video will become private. More information on private videos can be found [here](https://docs.api.video/delivery-analytics/video-privacy-access-management)

##### panoramic: `bool`<a id="panoramic-bool"></a>

Indicates if your video is a 360/immersive video.

##### mp4_support: `bool`<a id="mp4_support-bool"></a>

Enables mp4 version in addition to streamed version.

##### player_id: `str`<a id="player_id-str"></a>

The unique identification number for your video player.

##### metadata: List[`Metadata`]<a id="metadata-listmetadata"></a>

A list of key value pairs that you use to provide metadata for your video. These pairs can be made dynamic, allowing you to segment your audience. Read more on [dynamic metadata](https://api.video/blog/endpoints/dynamic-metadata/).

##### clip: [`VideoClip`](./api_video_python_sdk/type/video_clip.py)<a id="clip-videoclipapi_video_python_sdktypevideo_clippy"></a>


##### watermark: [`VideoWatermark`](./api_video_python_sdk/type/video_watermark.py)<a id="watermark-videowatermarkapi_video_python_sdktypevideo_watermarkpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VideoCreationPayload`](./api_video_python_sdk/type/video_creation_payload.py)
video to create

#### 🔄 Return<a id="🔄-return"></a>

[`Video`](./api_video_python_sdk/pydantic/video.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.videos.delete_video_object`<a id="apivideovideosdelete_video_object"></a>

Delete a video object by video ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
apivideo.videos.delete_video_object(
    video_id="vi4k0jvEUuaTdRAEjQ4Jfrgz",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

The video ID for the video you want to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos/{videoId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.videos.get_video_object`<a id="apivideovideosget_video_object"></a>

Retrieve the video details by video id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_video_object_response = apivideo.videos.get_video_object(
    video_id="videoId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

The unique identifier for the video you want details about.

#### 🔄 Return<a id="🔄-return"></a>

[`Video`](./api_video_python_sdk/pydantic/video.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos/{videoId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.videos.get_video_status_and_details`<a id="apivideovideosget_video_status_and_details"></a>

Retrieve upload status and encoding status to determine when the video is uploaded or ready to playback. Once encoding is completed, the response also lists the available stream qualities.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_video_status_and_details_response = apivideo.videos.get_video_status_and_details(
    video_id="vi4k0jvEUuaTdRAEjQ4Jfrgz",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

The unique identifier for the video you want the status for.

#### 🔄 Return<a id="🔄-return"></a>

[`VideoStatus`](./api_video_python_sdk/pydantic/video_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos/{videoId}/status` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.videos.ingest_video_from_source`<a id="apivideovideosingest_video_from_source"></a>

Ingest a video from a source or file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ingest_video_from_source_response = apivideo.videos.ingest_video_from_source(
    video_id="vi4k0jvEUuaTdRAEjQ4Jfrgz",
    file="@/path/to/video.mp4",
    content_range="bytes 209715200-419430399/524288000 OR part 2/3",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

Enter the videoId you want to use to upload your video.

##### file: `IO`<a id="file-io"></a>

The path to the video you would like to upload. The path must be local. If you want to use a video from an online source, you must use the \\\"/videos\\\" endpoint and add the \\\"source\\\" parameter when you create a new video.

##### content_range: `str`<a id="content_range-str"></a>

`part <part>/<total_parts>` ; `bytes <from_byte>-<to_byte>/<total_bytes>`

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VideoUploadPayload`](./api_video_python_sdk/type/video_upload_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Video`](./api_video_python_sdk/pydantic/video.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos/{videoId}/source` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.videos.list_all_objects`<a id="apivideovideoslist_all_objects"></a>

List all the video objects that are associated with the current workspace.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_objects_response = apivideo.videos.list_all_objects(
    title="My Video.mp4",
    tags_=['["captions", "dialogue"]'],
    metadata={
        "key": "string_example",
    },
    description="New Zealand",
    live_stream_id="li400mYKSgQ6xs7taUeSaEKr",
    sort_by="publishedAt",
    sort_order="asc",
    current_page=2,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

The title of a specific video you want to find. The search will match exactly to what term you provide and return any videos that contain the same term as part of their titles.

##### tags_: List[`str`]<a id="tags_-liststr"></a>

A tag is a category you create and apply to videos. You can search for videos with particular tags by listing one or more here. Only videos that have all the tags you list will be returned.

##### metadata: [`Dict[str, str]`](./api_video_python_sdk/type/.py)<a id="metadata-dictstr-strapi_video_python_sdktypepy"></a>

Videos can be tagged with metadata tags in key:value pairs. You can search for videos with specific key value pairs using this parameter. [Dynamic Metadata](https://api.video/blog/endpoints/dynamic-metadata/) allows you to define a key that allows any value pair.

##### description: `str`<a id="description-str"></a>

Retrieve video objects by `description`.

##### live_stream_id: `str`<a id="live_stream_id-str"></a>

Retrieve video objects that were recorded from a live stream by `liveStreamId`.

##### sort_by: `str`<a id="sort_by-str"></a>

Use this parameter to sort videos by the their created time, published time, updated time, or by title.

##### sort_order: `str`<a id="sort_order-str"></a>

Use this parameter to sort results. `asc` is ascending and sorts from A to Z. `desc` is descending and sorts from Z to A.

##### current_page: `int`<a id="current_page-int"></a>

Choose the number of search results to return per page. Minimum value: 1

##### page_size: `int`<a id="page_size-int"></a>

Results per page. Allowed values 1-100, default is 25.

#### 🔄 Return<a id="🔄-return"></a>

[`VideosListResponse`](./api_video_python_sdk/pydantic/videos_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.videos.set_thumbnail_from_interval`<a id="apivideovideosset_thumbnail_from_interval"></a>

Set a thumbnail from a specific time interval within a video.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_thumbnail_from_interval_response = apivideo.videos.set_thumbnail_from_interval(
    timecode="0.0",
    video_id="vi4k0jvEUuaTdRAEjQ4Jfrgz",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### timecode: `str`<a id="timecode-str"></a>

Frame in video to be used as a placeholder before the video plays.  Example: '\\\"00:01:00.000\\\" for 1 minute into the video.' Valid Patterns:  \\\"hh:mm:ss.ms\\\" \\\"hh:mm:ss:frameNumber\\\" \\\"124\\\" (integer value is reported as seconds)  If selection is out of range, \\\"00:00:00.00\\\" will be chosen.

##### video_id: `str`<a id="video_id-str"></a>

Unique identifier of the video you want to add a thumbnail to, where you use a section of your video as the thumbnail.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VideoThumbnailPickPayload`](./api_video_python_sdk/type/video_thumbnail_pick_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Video`](./api_video_python_sdk/pydantic/video.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos/{videoId}/thumbnail` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.videos.update_video_object_parameters`<a id="apivideovideosupdate_video_object_parameters"></a>

Update the parameters associated with a video ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_video_object_parameters_response = (
    apivideo.videos.update_video_object_parameters(
        video_id="vi4k0jvEUuaTdRAEjQ4Jfrgz",
        tags=['["maths", "string theory", "video"]'],
        title="String theory",
        description="A film about good books.",
        player_id="pl4k0jvEUuaTdRAEjQ4Jfrgz",
        public=True,
        panoramic=False,
        mp4_support=True,
        metadata=[
            {
                "key": "Color",
                "value": "Green",
            }
        ],
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

The video ID for the video you want to update.

##### tags: [`VideoUpdatePayloadTags`](./api_video_python_sdk/type/video_update_payload_tags.py)<a id="tags-videoupdatepayloadtagsapi_video_python_sdktypevideo_update_payload_tagspy"></a>

##### title: `str`<a id="title-str"></a>

The title you want to use for your video.

##### description: `str`<a id="description-str"></a>

A brief description of the video.

##### player_id: `str`<a id="player_id-str"></a>

The unique ID for the player you want to associate with your video.

##### public: `bool`<a id="public-bool"></a>

Whether the video is publicly available or not. False means it is set to private. Default is true. Tutorials on [private videos](https://api.video/blog/endpoints/private-videos/).

##### panoramic: `bool`<a id="panoramic-bool"></a>

Whether the video is a 360 degree or immersive video.

##### mp4_support: `bool`<a id="mp4_support-bool"></a>

Whether the player supports the mp4 format.

##### metadata: List[`Metadata`]<a id="metadata-listmetadata"></a>

A list (array) of dictionaries where each dictionary contains a key value pair that describes the video. As with tags, you must send the complete list of metadata you want as whatever you send here will overwrite the existing metadata for the video. [Dynamic Metadata](https://api.video/blog/endpoints/dynamic-metadata/) allows you to define a key that allows any value pair.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VideoUpdatePayload`](./api_video_python_sdk/type/video_update_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Video`](./api_video_python_sdk/pydantic/video.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos/{videoId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.videos.upload`<a id="apivideovideosupload"></a>

Uploading a video with the delegated upload token.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_response = apivideo.videos.upload(
    token="to1tcmSFHeYY5KzyhOqVKMKb",
    file="path/to/video/video.mp4",
    content_range="Content-Range: bytes 200-100/5000",
    video_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### token: `str`<a id="token-str"></a>

The unique identifier for the token you want to use to upload a video.

##### file: `IO`<a id="file-io"></a>

The path to the video you want to upload.

##### content_range: `str`<a id="content_range-str"></a>

Content-Range represents the range of bytes that will be returned as a result of the request. Byte ranges are inclusive, meaning that bytes 0-999 represents the first 1000 bytes in a file or object.

##### video_id: `str`<a id="video_id-str"></a>

The video id returned by the first call to this endpoint in a large video upload scenario.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TokenUploadPayload`](./api_video_python_sdk/type/token_upload_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Video`](./api_video_python_sdk/pydantic/video.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/upload` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.videos.upload_thumbnail`<a id="apivideovideosupload_thumbnail"></a>

Upload a thumbnail for a certain video.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_thumbnail_response = apivideo.videos.upload_thumbnail(
    video_id="videoId_example",
    file=open("/path/to/file", "rb"),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_id: `str`<a id="video_id-str"></a>

Unique identifier of the chosen video 

##### file: `IO`<a id="file-io"></a>

The image to be added as a thumbnail. The mime type should be image/jpeg, image/png or image/webp. The max allowed size is 8 MiB.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VideoThumbnailUploadPayload`](./api_video_python_sdk/type/video_thumbnail_upload_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Video`](./api_video_python_sdk/pydantic/video.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/videos/{videoId}/thumbnail` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.watermarks.list_all`<a id="apivideowatermarkslist_all"></a>

List all watermarks associated with your workspace.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = apivideo.watermarks.list_all(
    sort_by="createdAt",
    sort_order="asc",
    current_page=2,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sort_by: `str`<a id="sort_by-str"></a>

Allowed: createdAt. You can search by the time watermark were created at.

##### sort_order: `str`<a id="sort_order-str"></a>

Allowed: asc, desc. asc is ascending and sorts from A to Z. desc is descending and sorts from Z to A.

##### current_page: `int`<a id="current_page-int"></a>

Choose the number of search results to return per page. Minimum value: 1

##### page_size: `int`<a id="page_size-int"></a>

Results per page. Allowed values 1-100, default is 25.

#### 🔄 Return<a id="🔄-return"></a>

[`WatermarksListResponse`](./api_video_python_sdk/pydantic/watermarks_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/watermarks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.watermarks.watermark`<a id="apivideowatermarkswatermark"></a>

Create a new watermark by uploading a `JPG` or a `PNG` image.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
watermark_response = apivideo.watermarks.watermark(
    file=open("/path/to/file", "rb"),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file: `IO`<a id="file-io"></a>

The `.jpg` or `.png` image to be added as a watermark.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WatermarkUploadPayload`](./api_video_python_sdk/type/watermark_upload_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Watermark`](./api_video_python_sdk/pydantic/watermark.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/watermarks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.watermarks.watermark_0`<a id="apivideowatermarkswatermark_0"></a>

Delete a watermark.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
apivideo.watermarks.watermark_0(
    watermark_id="watermark_1BWr2L5MTQwxGkuxKjzh6i",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### watermark_id: `str`<a id="watermark_id-str"></a>

The watermark ID for the watermark you want to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/watermarks/{watermarkId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.webhooks.create_webhook_event`<a id="apivideowebhookscreate_webhook_event"></a>

Webhooks can push notifications to your server, rather than polling api.video for changes. We currently offer four events: 
* ```video.encoding.quality.completed``` Occurs when a new video is uploaded into your account, it will be encoded into several different HLS and mp4 qualities. When each version is encoded, your webhook will get a notification.  It will look like ```{ "type": "video.encoding.quality.completed", "emittedAt": "2021-01-29T16:46:25.217+01:00", "videoId": "viXXXXXXXX", "encoding": "hls", "quality": "720p"} ```. This request says that the 720p HLS encoding was completed.
* ```live-stream.broadcast.started```  When a live stream begins broadcasting, the broadcasting parameter changes from false to true, and this webhook fires.
* ```live-stream.broadcast.ended```  This event fires when a live stream has finished broadcasting.
* ```video.source.recorded```  This event occurs when a live stream is recorded and submitted for encoding.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_webhook_event_response = apivideo.webhooks.create_webhook_event(
    events=["video.encoding.quality.completed"],
    url="https://example.com/webhooks",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### events: [`WebhooksCreationPayloadEvents`](./api_video_python_sdk/type/webhooks_creation_payload_events.py)<a id="events-webhookscreationpayloadeventsapi_video_python_sdktypewebhooks_creation_payload_eventspy"></a>

##### url: `str`<a id="url-str"></a>

The the url to which HTTP notifications are sent. It could be any http or https URL.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksCreationPayload`](./api_video_python_sdk/type/webhooks_creation_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Webhook`](./api_video_python_sdk/pydantic/webhook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.webhooks.delete_webhook`<a id="apivideowebhooksdelete_webhook"></a>

This endpoint will delete the indicated webhook.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
apivideo.webhooks.delete_webhook(
    webhook_id="webhookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: `str`<a id="webhook_id-str"></a>

The webhook you wish to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{webhookId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.webhooks.get_details_by_id`<a id="apivideowebhooksget_details_by_id"></a>

Retrieve webhook details by id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_by_id_response = apivideo.webhooks.get_details_by_id(
    webhook_id="webhookId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webhook_id: `str`<a id="webhook_id-str"></a>

The unique webhook you wish to retreive details on.

#### 🔄 Return<a id="🔄-return"></a>

[`Webhook`](./api_video_python_sdk/pydantic/webhook.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{webhookId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `apivideo.webhooks.list_all`<a id="apivideowebhookslist_all"></a>

Retrieve a list of all webhooks configured for the current workspace.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = apivideo.webhooks.list_all(
    events="video.encoding.quality.completed",
    current_page=2,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### events: `str`<a id="events-str"></a>

The webhook event that you wish to filter on.

##### current_page: `int`<a id="current_page-int"></a>

Choose the number of search results to return per page. Minimum value: 1

##### page_size: `int`<a id="page_size-int"></a>

Results per page. Allowed values 1-100, default is 25.

#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksListResponse`](./api_video_python_sdk/pydantic/webhooks_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
