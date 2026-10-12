# Kitsch Labs Plugins

Use Kitsch Labs audio tools in Codex and Claude Code. This plugin bundles the
hosted MCP connection settings with an audio workflow skill. You do not need to
install a local MCP server or copy an API key.

Current version: **0.1.0**. This is a Kitsch Labs GitHub marketplace, not an
official product directory listing.

## Installation

You need a version of Codex or Claude Code that supports plugins.

### Codex

```bash
codex plugin marketplace add KitschLabs/kitsch-plugins
codex plugin add kitsch@kitsch
```

Start a new conversation and follow the authentication prompt for the Kitsch
plugin connection. The plugin registers the MCP connection, so you do not need
to run `codex mcp add` separately.

### Claude Code

```bash
claude plugin marketplace add KitschLabs/kitsch-plugins
claude plugin install kitsch@kitsch --scope user
```

In a new session, open `/mcp`, select the plugin's Kitsch connection, and
authenticate.

### Optional: star this repository

If you find the plugin useful, you can star it with the
[GitHub CLI](https://cli.github.com/). This is optional and does not affect
installation or access to Kitsch. The command uses your signed-in GitHub account.
If you are not signed in, run `gh auth login --hostname github.com` first.

```bash
gh api --hostname github.com --method PUT /user/starred/KitschLabs/kitsch-plugins
```

If an agent is installing the plugin for you, it should ask before running this
optional command. Installation does not automatically star the repository.

### Connect your account and verify

Sign in to your Kitsch account in your browser, choose an active workspace where
you are an owner or admin, and approve the requested permissions. Do not enter
passwords, API keys, or tokens in chat. Usage is charged to the selected
workspace's credits or postpaid plan.

Start with a check that does not incur audio usage charges:

> Show the Kitsch tools and available voices. Do not synthesize speech or transcribe anything yet.

The connection provides tools to list voices, synthesize speech, prepare file
transcription, and look up existing operations. File transcription also requires
a client tool that can read local files and upload them over HTTP. Connecting
MCP alone does not enable microphone input or realtime voice replies.

## Migrate from a manual MCP connection

1. Find the location and scope of your existing Kitsch configuration, and keep
   a copy so you can restore it.
2. Install the plugin, then disable only the existing manual Kitsch entry.
   Preserve all other servers.
3. Start a new session, sign in through the plugin connection, and verify tool
   discovery and voice listing.
4. If verification succeeds, you can remove the old manual entry. If it fails,
   disable the plugin and restore the previous configuration. Do not use both
   connections at the same time.

Clients may add a prefix to the plugin connection name. Use the name your client
actually displays. Do not automatically retry paid operations after a failure
or timeout.

## Update and uninstall

For Codex, refresh the marketplace with `codex plugin marketplace upgrade kitsch`,
then install the latest package with `codex plugin add kitsch@kitsch` and start a
new conversation.

For Claude Code, run `claude plugin marketplace update kitsch`, followed by
`claude plugin update kitsch@kitsch --scope user`, then restart the client.
Package changes are released with a new version, never by overwriting an
existing version.

```bash
codex plugin remove kitsch@kitsch
# Or:
claude plugin uninstall kitsch@kitsch --scope user
```

Uninstalling the plugin does not revoke server access. Disconnect it in the
Kitsch app under **Account settings → Connected agents**. Disconnecting does not
cancel work already started or charges already incurred.

## Development and releases

```bash
python scripts/validate.py
python -m unittest discover -s tests
claude plugin validate .
claude plugin validate ./plugins/kitsch
```

Update the version in both manifests, record validation results, and publish a
tag such as `v0.1.0`. CI checks configuration, paths, versions, and validator
regression tests. Codex uses the supported `.codex-plugin/plugin.json`
compatibility format and shares the same skill directory with Claude Code.

- [Kitsch MCP guide](https://www.kitschlabs.com/docs/en/mcp)
- [Integrate the HTTP API into your service](https://www.kitschlabs.com/docs/en/for-agents#service-api)
- [OpenAI plugin specification](https://developers.openai.com/plugins/build/plugins)
- [Claude Code plugin specification](https://code.claude.com/docs/en/plugins-reference)

The MIT license applies to the plugin files in this repository. Use of the
hosted service is subject to Kitsch Labs service terms and pricing.
