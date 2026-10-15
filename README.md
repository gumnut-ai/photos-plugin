# Gumnut Photos plugin

Source for the Gumnut Photos plugin, which adds skills on top of the
[Gumnut Photos MCP server](https://docs.gumnut.ai/guides/mcp/overview)
(`https://api.gumnut.ai/mcp`). The same skills ship to Claude and to ChatGPT.

## Layout

| Path | Purpose |
|------|---------|
| `gumnut-photos/` | The plugin folder: manifest, MCP server reference, skills, and the README shown as the Claude directory listing |
| `gumnut-photos/skills/<name>/SKILL.md` | One skill per folder, shared by both hosts |
| `.claude-plugin/marketplace.json` | Lets Claude Code and claude.ai install the plugin straight from this repository |
| `scripts/check_skills.py` | Checks skills against the front-matter rules both hosts accept |

## Try it before release

- **Claude Code:** `claude --plugin-dir ./gumnut-photos`, or
  `claude plugin marketplace add gumnut-ai/photos-plugin` followed by
  `claude plugin install gumnut-photos@gumnut`.
- **claude.ai and Cowork:** **Customize > Plugins > Add > Add marketplace**
  with this repository's URL.

## Checks

```sh
claude plugin validate gumnut-photos
claude plugin validate .
uv run scripts/check_skills.py
```

CI runs the same checks on every pull request.

## Releasing

Raise `version` in `gumnut-photos/.claude-plugin/plugin.json` with every
release.

- **Claude:** the Claude directory follows this repository's `main` branch
  and picks up each merged version after its automated checks.
- **ChatGPT:** upload a new package to the existing Gumnut Photos plugin in
  the OpenAI Platform. Build it from the plugin's current release package so
  that its listing and review metadata carry over, with this repository's
  `gumnut-photos/skills/` as its `skills/` folder.

## License

[Apache-2.0](LICENSE)
