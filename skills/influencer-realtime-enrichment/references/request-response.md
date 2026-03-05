# Request and Response Guide

## `GET /api/v1/instagram/realtime/media/detail`
- operationId: `instagram_realtime_media_detail`
- summary: 实时采集-贴文详情
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `media_code` | `query` | `true` | `string` | media code |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_RealTimeInstagramMediaInfoRes_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/instagram/realtime/user/info`
- operationId: `instagram_realtime_user_info`
- summary: 实时采集-用户信息
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `false` | `string` | username |
| `user_id` | `query` | `false` | `string` | user_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_RealTimeInstagramUserInfoRes_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/instagram/realtime/user/medias`
- operationId: `instagram_realtime_user_medias`
- summary: 实时采集-用户贴文
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `user_id` | `query` | `true` | `string` | user_id |
| `offset` | `query` | `false` | `string` | offset |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_RealTimeInstagramUserMediasRes_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/instagram/realtime/user/stories`
- operationId: `instagram_realtime_user_stories`
- summary: 实时采集-用户故事
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `user_id` | `query` | `true` | `string` | user_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_RealTimeInstagramUserStoriesRes_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/tiktok/realtime/user/info`
- operationId: `tiktok_realtime_user_info`
- summary: 实时采集-用户信息
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `false` | `string` | unique_id |
| `user_id` | `query` | `false` | `string` | user_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_RealTimeTiktokUserInfoRes_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/tiktok/realtime/user/videos`
- operationId: `tiktok_realtime_user_videos`
- summary: 实时采集-用户视频
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `uid` | `query` | `true` | `string` | uid or sec_uid |
| `region` | `query` | `false` | `string` | country code:US,VN... |
| `offset` | `query` | `false` | `string` | offset |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_RealTimeTiktokUserVideosRes_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/tiktok/realtime/video/detail`
- operationId: `tiktok_realtime_video_detail`
- summary: 实时采集-视频详情
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `video_id` | `query` | `true` | `string` | 视频ID |
| `region` | `query` | `true` | `string` | country code:US,VN... |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_RealTimeTiktokVideoInfoRes_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/youtube/realtime/user/info`
- operationId: `youtube_realtime_user_info`
- summary: 实时采集-用户信息
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `false` | `string` | channel_id |
| `username` | `query` | `false` | `string` | username |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_RealTimeYoutubeUserInfoRes_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/youtube/realtime/user/videos`
- operationId: `youtube_realtime_user_videos`
- summary: 实时采集-用户视频
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `true` | `string` | channel_id |
| `offset` | `query` | `false` | `string` | offset |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_RealTimeYoutubeUserVideosRes_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/youtube/realtime/video/detail`
- operationId: `youtube_realtime_video_detail`
- summary: 实时采集-视频详情
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `video_id` | `query` | `true` | `string` | video_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_RealTimeYoutubeVideoInfoRes_ |
| `422` | application/json: HTTPValidationError |
