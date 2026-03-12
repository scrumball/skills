# Task Map
Use this file when you want to start from a business task instead of memorizing raw `operationId` values.
## How to use it
1. Pick the task that matches the user's goal.
2. Ask only for the minimum identifier listed in the table.
3. Run the mapped task with `python3 scripts/scrumball_cli.py demo --task <task-id> --param key=value`.
4. If a required input is missing, stop and ask the stored follow-up question instead of guessing.
5. Use `--use-example` only when you intentionally want the documented sample payload.

## Coverage
- `docs/task-map.json` now covers `86` practical tasks across discovery, audience fit, realtime enrichment, monitoring, and commerce.
- Examples in `docs/task-map.json` are documentation and opt-in demo seeds, not automatic defaults.
- Aggregate audience-fit tasks stay available, and the platform/dimension tasks below expose the fuller capability surface.
- Contributors can run `python3 scripts/scrumball_cli.py check-task-map` to catch task-map drift after adding operations.

## Lead discovery
| Task phrase | Task ID | Platform | Skill | Starts with | Minimum input |
|---|---|---|---|---|---|
| Generate platform search suggestions | `lead.suggest-search-terms` | `cross-platform` | `influencer-lead-discovery` | `search_instagram_suggest` | `platform, query` |
| Check Instagram hashtag engagement | `lead.check-instagram-hashtag-engagement` | `instagram` | `influencer-lead-discovery` | `instagram_user_hashtag_engagement` | `username` |
| Find Instagram creators by keyword | `lead.find-instagram-creators` | `instagram` | `influencer-lead-discovery` | `search_instagram_user` | `query` |
| Find Instagram media by keyword | `lead.find-instagram-media` | `instagram` | `influencer-lead-discovery` | `search_instagram_media` | `query` |
| Find creators similar to an Instagram handle | `lead.find-similar-instagram-creators` | `instagram` | `influencer-lead-discovery` | `instagram_user_similar` | `username` |
| List Instagram creator brand affinities | `lead.list-instagram-brand-affinities` | `instagram` | `influencer-lead-discovery` | `instagram_user_brands` | `username` |
| List Instagram creator media | `lead.list-instagram-media` | `instagram` | `influencer-lead-discovery` | `instagram_db_user_medias` | `username` |
| Look up an Instagram creator profile | `lead.lookup-instagram-profile` | `instagram` | `influencer-lead-discovery` | `instagram_db_user_info` | `username` |
| Check TikTok hashtag engagement | `lead.check-tiktok-hashtag-engagement` | `tiktok` | `influencer-lead-discovery` | `tiktok_user_hashtag_engagement` | `unique_id` |
| Find creators similar to a TikTok handle | `lead.find-similar-tiktok-creators` | `tiktok` | `influencer-lead-discovery` | `tiktok_user_similar` | `unique_id` |
| Find TikTok creators by keyword | `lead.find-tiktok-creators` | `tiktok` | `influencer-lead-discovery` | `search_tiktok_user` | `query` |
| Find TikTok videos by keyword | `lead.find-tiktok-videos` | `tiktok` | `influencer-lead-discovery` | `search_tiktok_video` | `query` |
| List TikTok creator brand affinities | `lead.list-tiktok-brand-affinities` | `tiktok` | `influencer-lead-discovery` | `tiktok_user_brands` | `unique_id` |
| List TikTok creator videos | `lead.list-tiktok-videos` | `tiktok` | `influencer-lead-discovery` | `tiktok_db_user_videos` | `unique_id` |
| Look up a TikTok creator profile | `lead.lookup-tiktok-profile` | `tiktok` | `influencer-lead-discovery` | `tiktok_db_user_info` | `unique_id` |
| Check YouTube hashtag engagement | `lead.check-youtube-hashtag-engagement` | `youtube` | `influencer-lead-discovery` | `youtube_user_hashtag_engagement` | `channel_id` |
| Find creators similar to a YouTube channel | `lead.find-similar-youtube-creators` | `youtube` | `influencer-lead-discovery` | `youtube_user_similar` | `channel_id, channel_handle` |
| Find YouTube creators by keyword | `lead.find-youtube-creators` | `youtube` | `influencer-lead-discovery` | `search_youtube_user` | `query` |
| Find YouTube videos by keyword | `lead.find-youtube-videos` | `youtube` | `influencer-lead-discovery` | `search_youtube_video` | `query` |
| List YouTube creator brand affinities | `lead.list-youtube-brand-affinities` | `youtube` | `influencer-lead-discovery` | `youtube_user_brands` | `channel_id` |
| List YouTube creator videos | `lead.list-youtube-videos` | `youtube` | `influencer-lead-discovery` | `youtube_db_user_videos` | `channel_id` |
| Look up a YouTube creator profile | `lead.lookup-youtube-profile` | `youtube` | `influencer-lead-discovery` | `youtube_db_user_info` | `channel_id, username` |

## Audience fit
| Task phrase | Task ID | Platform | Skill | Starts with | Minimum input |
|---|---|---|---|---|---|
| Check Instagram audience fit | `audience.check-instagram-fit` | `instagram` | `influencer-audience-fit-scoring` | `audience_instagram_geography` | `username` |
| Check Instagram audience age split | `audience.instagram-age` | `instagram` | `influencer-audience-fit-scoring` | `audience_instagram_age` | `username` |
| Check Instagram brand opportunity fit | `audience.instagram-brand-opportunities` | `instagram` | `influencer-audience-fit-scoring` | `audience_instagram_brand_opportunities` | `username` |
| Check Instagram content style | `audience.instagram-content-style` | `instagram` | `influencer-audience-fit-scoring` | `audience_instagram_content_style` | `username` |
| Check Instagram audience devices | `audience.instagram-devices` | `instagram` | `influencer-audience-fit-scoring` | `audience_instagram_device` | `username` |
| Check Instagram audience engagement behavior | `audience.instagram-engagement-behavior` | `instagram` | `influencer-audience-fit-scoring` | `audience_instagram_interactive_behavior` | `username` |
| Check Instagram follower authenticity | `audience.instagram-follower-authenticity` | `instagram` | `influencer-audience-fit-scoring` | `audience_instagram_follower_authenticity` | `username` |
| Check Instagram audience gender split | `audience.instagram-gender` | `instagram` | `influencer-audience-fit-scoring` | `audience_instagram_gender` | `username` |
| Check Instagram overall audience gender split | `audience.instagram-gender-overall` | `instagram` | `influencer-audience-fit-scoring` | `audience_instagram_gender_overall` | `username` |
| Check Instagram audience geography | `audience.instagram-geography` | `instagram` | `influencer-audience-fit-scoring` | `audience_instagram_geography` | `username` |
| Check Instagram audience interests | `audience.instagram-interests` | `instagram` | `influencer-audience-fit-scoring` | `audience_instagram_interest` | `username` |
| Check Instagram audience language | `audience.instagram-language` | `instagram` | `influencer-audience-fit-scoring` | `audience_instagram_language` | `username` |
| Check Instagram rating tier | `audience.instagram-rating-tier` | `instagram` | `influencer-audience-fit-scoring` | `audience_instagram_rating_tier` | `username` |
| Check TikTok audience fit | `audience.check-tiktok-fit` | `tiktok` | `influencer-audience-fit-scoring` | `audience_tiktok_geography` | `unique_id` |
| Check TikTok audience age split | `audience.tiktok-age` | `tiktok` | `influencer-audience-fit-scoring` | `audience_tiktok_age` | `unique_id` |
| Check TikTok brand opportunity fit | `audience.tiktok-brand-opportunities` | `tiktok` | `influencer-audience-fit-scoring` | `audience_tiktok_brand_opportunities` | `unique_id` |
| Check TikTok content style | `audience.tiktok-content-style` | `tiktok` | `influencer-audience-fit-scoring` | `audience_tiktok_content_style` | `unique_id` |
| Check TikTok audience devices | `audience.tiktok-devices` | `tiktok` | `influencer-audience-fit-scoring` | `audience_tiktok_device` | `unique_id` |
| Check TikTok audience engagement behavior | `audience.tiktok-engagement-behavior` | `tiktok` | `influencer-audience-fit-scoring` | `audience_tiktok_interactive_behavior` | `unique_id` |
| Check TikTok follower authenticity | `audience.tiktok-follower-authenticity` | `tiktok` | `influencer-audience-fit-scoring` | `audience_tiktok_follower_authenticity` | `unique_id` |
| Check TikTok audience gender split | `audience.tiktok-gender` | `tiktok` | `influencer-audience-fit-scoring` | `audience_tiktok_gender` | `unique_id` |
| Check TikTok overall audience gender split | `audience.tiktok-gender-overall` | `tiktok` | `influencer-audience-fit-scoring` | `audience_tiktok_gender_overall` | `unique_id` |
| Check TikTok audience geography | `audience.tiktok-geography` | `tiktok` | `influencer-audience-fit-scoring` | `audience_tiktok_geography` | `unique_id` |
| Check TikTok audience interests | `audience.tiktok-interests` | `tiktok` | `influencer-audience-fit-scoring` | `audience_tiktok_interest` | `unique_id` |
| Check TikTok audience language | `audience.tiktok-language` | `tiktok` | `influencer-audience-fit-scoring` | `audience_tiktok_language` | `unique_id` |
| Check TikTok rating tier | `audience.tiktok-rating-tier` | `tiktok` | `influencer-audience-fit-scoring` | `audience_tiktok_rating_tier` | `unique_id` |
| Check YouTube audience fit | `audience.check-youtube-fit` | `youtube` | `influencer-audience-fit-scoring` | `audience_youtube_geography` | `channel_id` |
| Check YouTube audience age split | `audience.youtube-age` | `youtube` | `influencer-audience-fit-scoring` | `audience_youtube_age` | `channel_id` |
| Check YouTube brand opportunity fit | `audience.youtube-brand-opportunities` | `youtube` | `influencer-audience-fit-scoring` | `audience_youtube_brand_opportunities` | `channel_id` |
| Check YouTube content style | `audience.youtube-content-style` | `youtube` | `influencer-audience-fit-scoring` | `audience_youtube_content_style` | `channel_id` |
| Check YouTube audience engagement behavior | `audience.youtube-engagement-behavior` | `youtube` | `influencer-audience-fit-scoring` | `audience_youtube_interactive_behavior` | `channel_id` |
| Check YouTube follower authenticity | `audience.youtube-follower-authenticity` | `youtube` | `influencer-audience-fit-scoring` | `audience_youtube_follower_authenticity` | `channel_id` |
| Check YouTube audience gender split | `audience.youtube-gender` | `youtube` | `influencer-audience-fit-scoring` | `audience_youtube_gender` | `channel_id` |
| Check YouTube overall audience gender split | `audience.youtube-gender-overall` | `youtube` | `influencer-audience-fit-scoring` | `audience_youtube_gender_overall` | `channel_id` |
| Check YouTube audience geography | `audience.youtube-geography` | `youtube` | `influencer-audience-fit-scoring` | `audience_youtube_geography` | `channel_id` |
| Check YouTube audience interests | `audience.youtube-interests` | `youtube` | `influencer-audience-fit-scoring` | `audience_youtube_interest` | `channel_id` |
| Check YouTube audience language | `audience.youtube-language` | `youtube` | `influencer-audience-fit-scoring` | `audience_youtube_language` | `channel_id` |
| Check YouTube rating tier | `audience.youtube-rating-tier` | `youtube` | `influencer-audience-fit-scoring` | `audience_youtube_rating_tier` | `channel_id` |

## Realtime enrichment
| Task phrase | Task ID | Platform | Skill | Starts with | Minimum input |
|---|---|---|---|---|---|
| Pull fresh Instagram media | `realtime.list-instagram-media` | `instagram` | `influencer-realtime-enrichment` | `instagram_realtime_user_medias` | `user_id` |
| Pull fresh Instagram stories | `realtime.list-instagram-stories` | `instagram` | `influencer-realtime-enrichment` | `instagram_realtime_user_stories` | `user_id` |
| Pull fresh Instagram media detail | `realtime.lookup-instagram-media` | `instagram` | `influencer-realtime-enrichment` | `instagram_realtime_media_detail` | `media_code` |
| Pull fresh Instagram profile info | `realtime.lookup-instagram-profile` | `instagram` | `influencer-realtime-enrichment` | `instagram_realtime_user_info` | `username, user_id` |
| Pull fresh TikTok videos | `realtime.list-tiktok-videos` | `tiktok` | `influencer-realtime-enrichment` | `tiktok_realtime_user_videos` | `uid` |
| Pull fresh TikTok profile info | `realtime.lookup-tiktok-profile` | `tiktok` | `influencer-realtime-enrichment` | `tiktok_realtime_user_info` | `unique_id, user_id` |
| Pull fresh TikTok video info | `realtime.lookup-tiktok-video` | `tiktok` | `influencer-realtime-enrichment` | `tiktok_realtime_video_detail` | `video_id, region` |
| Pull fresh YouTube videos | `realtime.list-youtube-videos` | `youtube` | `influencer-realtime-enrichment` | `youtube_realtime_user_videos` | `channel_id` |
| Pull fresh YouTube channel info | `realtime.lookup-youtube-profile` | `youtube` | `influencer-realtime-enrichment` | `youtube_realtime_user_info` | `channel_id, username` |
| Pull fresh YouTube video info | `realtime.lookup-youtube-video` | `youtube` | `influencer-realtime-enrichment` | `youtube_realtime_video_detail` | `video_id` |

## Campaign monitoring
| Task phrase | Task ID | Platform | Skill | Starts with | Minimum input |
|---|---|---|---|---|---|
| Create a video monitor task | `monitor.create-video-task` | `cross-platform` | `influencer-campaign-monitoring` | `create_monitor_task` | `platform, video_id` |
| List active video monitor tasks | `monitor.list-active-video-tasks` | `cross-platform` | `influencer-campaign-monitoring` | `list_monitor_tasks` | `none` |
| Look up one monitor task | `monitor.lookup-video-task` | `cross-platform` | `influencer-campaign-monitoring` | `get_monitor_task_detail` | `monitor_id` |
| Refresh one monitor task | `monitor.refresh-video-task` | `cross-platform` | `influencer-campaign-monitoring` | `refresh_monitor_task` | `monitor_id` |
| Stop a video monitor task | `monitor.stop-video-task` | `cross-platform` | `influencer-campaign-monitoring` | `stop_monitor_task` | `monitor_id` |
| Download an Instagram monitored video | `monitor.download-instagram-task-video` | `instagram` | `influencer-campaign-monitoring` | `instagram_task_video_download` | `video_code` |
| Check Instagram monitored user metrics | `monitor.lookup-instagram-user-metrics` | `instagram` | `influencer-campaign-monitoring` | `instagram_user_monitor_metrics` | `username` |
| Download a TikTok monitored video | `monitor.download-tiktok-task-video` | `tiktok` | `influencer-campaign-monitoring` | `tiktok_task_video_download` | `video_id` |
| Check TikTok monitored user metrics | `monitor.lookup-tiktok-user-metrics` | `tiktok` | `influencer-campaign-monitoring` | `tiktok_user_monitor_metrics` | `unique_id` |
| Download a YouTube monitored video | `monitor.download-youtube-task-video` | `youtube` | `influencer-campaign-monitoring` | `youtube_task_video_download` | `video_id` |
| Check YouTube monitored user metrics | `monitor.lookup-youtube-user-metrics` | `youtube` | `influencer-campaign-monitoring` | `youtube_user_monitor_metrics` | `channel_id` |

## Commerce intelligence
| Task phrase | Task ID | Platform | Skill | Starts with | Minimum input |
|---|---|---|---|---|---|
| List TikTok shop goods for a creator | `commerce.list-tiktok-shop-goods` | `tiktok` | `influencer-commerce-intel` | `tiktok_user_shop_goods_list` | `unique_id` |
| List TikTok shop live sessions | `commerce.list-tiktok-shop-lives` | `tiktok` | `influencer-commerce-intel` | `tiktok_user_shop_live_list` | `unique_id` |
| List TikTok shop video ads | `commerce.list-tiktok-shop-video-ads` | `tiktok` | `influencer-commerce-intel` | `tiktok_user_shop_video_ad_list` | `unique_id` |
| Check TikTok product detail | `commerce.lookup-product-detail` | `tiktok` | `influencer-commerce-intel` | `tiktok_realtime_product_detail` | `product_id, region` |
| Check TikTok shop sales | `commerce.lookup-tiktok-shop-sales` | `tiktok` | `influencer-commerce-intel` | `tiktok_user_shop_sale` | `unique_id` |

## AI-agent rules of thumb
- Prefer task IDs first in planning and prompting; use raw `operationId` only when executing.
- Treat `example` payloads as optional demo fixtures. Real execution should ask for missing identifiers unless `--use-example` is passed.
- If an identifier is missing, use the exact follow-up question stored in `docs/task-map.json` or the templates in `docs/follow-up-templates.md`.
- Keep follow-ups minimal: ask for one handle, ID, region, or platform choice at a time.
