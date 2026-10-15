# Gumnut Photos

Gumnut Photos gives your AI assistant an understanding of your photo library:
who is in each photo, what is happening, where and when it was taken, and how
good it is technically. This plugin connects your assistant to the Gumnut
Photos MCP server and adds skills that show it how to combine those signals
for common jobs, such as choosing the best photos from a trip, building an
album, or tidying up the people Gumnut recognizes.

## How to use it

1. Add the plugin, then connect **Gumnut Photos** from the plugin's
   connectors and sign in with your Gumnut account. New to Gumnut? Create an
   account at [gumnut.ai](https://www.gumnut.ai).
2. Ask for what you want in plain language, for example "Make an album of the
   best photos from our Japan trip" or "Who appears most often in last
   summer's photos?" Your assistant picks up the relevant skill automatically.

See the [MCP guide](https://docs.gumnut.ai/guides/mcp/overview) for what the
connection can do.

## Data and privacy

The skills are instructions only; they run no code and send nothing on their
own. Your assistant reaches your library through the Gumnut Photos server at
`https://api.gumnut.ai/mcp`, using the account you sign in with. It reads and
changes only what that account can access, and the changes it makes (such as
albums, people names, or moving photos to trash) are saved in your Gumnut
library. Photo content and metadata that the assistant requests are returned
to the AI app you are using. See the
[Gumnut privacy policy](https://www.gumnut.ai/privacy).

## Support

Report problems or ask questions in
[this repository's issues](https://github.com/gumnut-ai/photos-plugin/issues).
