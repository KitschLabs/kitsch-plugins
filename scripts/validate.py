"""Validate the single public plugin without third-party dependencies."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(root, path):
    return json.loads((root / path).read_text(encoding="utf-8"))


def validate(root=ROOT):
    plugin = root / "plugins/kitsch"
    codex = read_json(plugin, ".codex-plugin/plugin.json")
    claude = read_json(plugin, ".claude-plugin/plugin.json")
    for key in ("name", "version", "description", "author", "license", "mcpServers"):
        assert codex[key] == claude[key], f"Manifest mismatch: {key}"
    assert codex["name"] == "kitsch"
    assert re.fullmatch(r"\d+\.\d+\.\d+", codex["version"]), "Invalid version"
    expected = {"kitsch": {"type": "http", "url": "https://mcp.kitschlabs.com/mcp"}}
    assert codex["mcpServers"] == expected, "Unexpected MCP configuration"
    assert codex["skills"] == "./skills/"
    for path in (".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json"):
        market = read_json(root, path)
        assert market["name"] == "kitsch"
        assert len(market["plugins"]) == 1
        entry = market["plugins"][0]
        assert entry["name"] == codex["name"]
        source = entry["source"]
        if isinstance(source, dict):
            assert source["source"] == "local"
            assert entry["policy"] == {
                "installation": "AVAILABLE", "authentication": "ON_INSTALL"
            }
            source = source["path"]
        assert source == "./plugins/kitsch", "Unexpected plugin path"
        assert (root / source).resolve() == plugin.resolve()
    skill = (plugin / "skills/audio/SKILL.md").read_text(encoding="utf-8")
    assert skill.startswith("---\nname: audio\ndescription: ")
    assert skill.count("\n---\n") == 1
    for tool in ("list_voices", "synthesize_speech", "prepare_transcription", "get_audio_operation",
                 "create_audio_stream", "get_audio_stream", "close_audio_stream"):
        assert tool in skill, f"Missing tool: {tool}"
    assert not list(plugin.rglob("*.env")), "Environment files must not ship"
    assert not (plugin / "hooks").exists(), "No runtime hooks in this release"
    return codex["version"]


if __name__ == "__main__":
    print(f"Validated kitsch {validate()}")
