# Request and Response Guide

## `GET /api/v1/instagram/task/video/download`
- operationId: `instagram_task_video_download`
- summary: 任务-视频下载
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `video_code` | `query` | `true` | `string` | 视频code |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_InstagramTaskVideoDownloadRes_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/instagram/user/monitor/metrics`
- operationId: `instagram_user_monitor_metrics`
- summary: 用户监控指标
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
| `period` | `query` | `false` | `string` | 周期(last_31_days,monthly) |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_InstagramUserMonitorMetricsRes__ |
| `422` | application/json: HTTPValidationError |

## `POST /api/v1/monitor/video/tasks/create`
- operationId: `create_monitor_task`
- summary: 创建视频监测任务
- parameters: none
- requestBody:
| content-type | schema |
|---|---|
| `application/json` | `VideoMonitorTaskCreateReq` |
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_VideoMonitorTaskRep_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/monitor/video/tasks/detail`
- operationId: `get_monitor_task_detail`
- summary: 获取视频监测任务详情
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `monitor_id` | `query` | `true` | `string` | 监测ID |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_VideoMonitorTaskDetailRep_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/monitor/video/tasks/list`
- operationId: `list_monitor_tasks`
- summary: 获取视频监测任务列表
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `platform` | `query` | `false` | `object` | 平台筛选：tiktok、youtube、instagram |
| `monitor_status` | `query` | `false` | `object` | 状态筛选：0-监测中 10-已完成 20-已停止 |
| `page` | `query` | `false` | `integer` | 页码 |
| `page_size` | `query` | `false` | `integer` | 每页数量 |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_BasePage_VideoMonitorTaskRep__ |
| `422` | application/json: HTTPValidationError |

## `POST /api/v1/monitor/video/tasks/refresh`
- operationId: `refresh_monitor_task`
- summary: 手动刷新视频监测数据
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `monitor_id` | `query` | `true` | `string` | 监测ID |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_VideoMonitorSnapshotRep_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/monitor/video/tasks/stop`
- operationId: `stop_monitor_task`
- summary: 停止视频监测任务
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `monitor_id` | `query` | `true` | `string` | 监测ID |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/tiktok/task/video/download`
- operationId: `tiktok_task_video_download`
- summary: 任务-视频下载
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `video_id` | `query` | `true` | `string` | 视频ID |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_TiktokTaskVideoDownloadRes_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/tiktok/user/monitor/metrics`
- operationId: `tiktok_user_monitor_metrics`
- summary: 用户监控指标
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
| `period` | `query` | `false` | `string` | 周期(last_31_days,monthly) |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_TiktokUserMonitorMetricsRes__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/youtube/task/video/download`
- operationId: `youtube_task_video_download`
- summary: 任务-视频下载
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `video_id` | `query` | `true` | `string` | 视频ID |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_YoutubeTaskVideoDownloadRes_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/youtube/user/monitor/metrics`
- operationId: `youtube_user_monitor_metrics`
- summary: 用户监控指标
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `true` | `string` | 频道ID |
| `period` | `query` | `false` | `string` | 周期(last_31_days,monthly) |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_YoutubeUserMonitorMetricsRes__ |
| `422` | application/json: HTTPValidationError |
