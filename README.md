# scrumball-skills

`scrumball-skills` is a set of AI Skills for influencer marketing workflows. It helps you:

- discover creators and build candidate pools
- evaluate creator audience fit against your target segments
- pull fresh creator metrics for account health checks
- monitor campaign execution progress
- analyze commerce performance on channels such as TikTok Shop

You can treat these as callable creator data and analytics services: describe your business task in natural language, and the AI can invoke the right Skill when needed.

---

## Installation and Included Skills

Install all `scrumball` skills:

```bash
npx skills add scrumball/skills
```

This package includes:

- `influencer-lead-discovery`: Search creators by keyword/category/region and build candidate lists.
- `influencer-audience-fit-scoring`: Analyze creator audience profiles and score target-audience fit.
- `influencer-realtime-enrichment`: Refresh creator records with up-to-date profile and performance signals.
- `influencer-campaign-monitoring`: Track campaign task progress and baseline creator performance.
- `influencer-commerce-intel`: Evaluate creator commerce outcomes, especially for TikTok Shop-like funnels.

To install only one Skill:

```bash
npx skills add scrumball/skills --skill <skill-name>
```

Examples:

- `npx skills add scrumball/skills --skill influencer-lead-discovery`
- `npx skills add scrumball/skills --skill influencer-audience-fit-scoring`
- `npx skills add scrumball/skills --skill influencer-realtime-enrichment`
- `npx skills add scrumball/skills --skill influencer-campaign-monitoring`
- `npx skills add scrumball/skills --skill influencer-commerce-intel`

---

## Skill Capability Overview

### influencer-lead-discovery

- Search potential creators by keyword, brand, or category
- Filter by market, language, follower range, and related signals
- Best for sourcing and shortlist creation

### influencer-audience-fit-scoring

- Analyze audience makeup (interests, geography, age, gender, etc.)
- Score alignment with your target audience definition
- Compare multiple creators for selection decisions

### influencer-realtime-enrichment

- Pull fresh follower and engagement indicators
- Refresh existing creator records before outreach or activation
- Support recurring account health checks

### influencer-campaign-monitoring

- View campaign-level execution status across participating creators
- Track publishing progress and baseline performance metrics
- Support campaign tracking dashboards and reporting

### influencer-commerce-intel

- Focus on closed-loop commerce channels such as TikTok Shop
- Inspect sales, GMV, and conversion-related signals
- Prioritize creators with stronger selling capability

---

## Using Skills in AI Conversations

After setup, you can describe requests in natural language inside any AI environment that supports Skills. The AI can call the matching `scrumball` Skill as needed.

Typical prompt examples:

- **Creator discovery (`influencer-lead-discovery`)**
  - "Find 20 sports creators related to `nike`, each with over 100K followers, mainly in the US and UK. Return a table."
  - "Search 30 beauty creators targeting Southeast Asia with 50K-500K followers, sorted by follower count."

- **Audience fit scoring (`influencer-audience-fit-scoring`)**
  - "Analyze TikTok account `nike` and score fit with US users aged 18-24 who are interested in basketball and fitness."
  - "Compare `xxx1`, `xxx2`, and `xxx3` for a European skincare campaign and explain which one fits best."

- **Realtime health checks (`influencer-realtime-enrichment`)**
  - "Check creator IDs `id1, id2, id3` for the last 7 days. Flag sharp follower drops or risk signals."
  - "Pull the latest growth and video performance for TikTok account `nike` and summarize key changes."

- **Campaign monitoring (`influencer-campaign-monitoring`)**
  - "List all active monitoring tasks sorted by start time."
  - "For campaign `summer-sale-2025`, list participating creators, published content links, and current baseline performance."

- **Commerce intelligence (`influencer-commerce-intel`)**
  - "Review TikTok account `nike` for commerce performance, including sales, GMV, and conversion signals."
  - "Compare three creators on TikTok Shop performance and recommend who to prioritize with reasons."

---

## Common Errors and Troubleshooting

- **`SCRUMBALL_BASE_URL is required` / `SCRUMBALL_API_KEY is required`**
  - Required runtime configuration is missing. Ask your platform administrator or DevOps owner to provide the environment variables.

- **`Missing required ...`**
  - A required field was not provided in the call (for example an account ID or query condition). Add the missing details and retry.

- **Network / DNS errors**
  - The gateway may be temporarily unreachable. Retry later or contact your infrastructure owner.

---

## License

MIT. See `LICENSE`.
