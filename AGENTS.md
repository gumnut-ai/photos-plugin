# Agent guide

This repository is public. Keep internal tracker identifiers and links,
private repository names, account details, and reviewer credentials out of
files, commit messages, branch names, and pull request bodies.

## Writing skills

- Skills teach an assistant how to combine Gumnut Photos tools for a job. Do
  not restate what a tool's own description or the server instructions
  already say; add the sequence, the judgment calls, and the pitfalls.
- Name tools by their exact MCP tool names in backticks, and only tools the
  Gumnut Photos MCP server exposes. A REST-only endpoint is invisible to the
  assistant.
- Front matter may contain only `name`, `description`, `license`,
  `compatibility`, and `metadata`; claude.ai rejects other keys. `name`
  matches the folder name. `scripts/check_skills.py` enforces this.
- Refer to "the assistant" rather than a specific product, since the same
  skill runs in Claude and ChatGPT.
- `gumnut-photos/README.md` is the public Claude directory listing, not
  developer documentation.
