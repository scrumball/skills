#!/usr/bin/env node
// Since 2.0.0 Scrumball runs as a remote MCP server with browser sign-in; the local
// API-key server of 0.x is retired. Anyone still launching the old command gets this guidance.
process.stderr.write(`Scrumball no longer runs as a local MCP server, and API keys are no longer used.

Connect your AI agent to the remote server and sign in with your Scrumball account in the browser:
  https://api.scrumball.ai/mcp/server

Install the skills (they guide the setup):
  npx skills add scrumball/skills -g

Guide: https://github.com/scrumball/skills
`);
process.exit(1);
