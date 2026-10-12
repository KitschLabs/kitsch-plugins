import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate import ROOT, validate


class ValidateTests(unittest.TestCase):
    def test_release(self):
        self.assertRegex(validate(), r"^\d+\.\d+\.\d+$")

    def test_rejects_drift_and_unsafe_configuration(self):
        cases = [
            (".claude-plugin/plugin.json", "version", "0.2.0"),
            (".codex-plugin/plugin.json", "mcpServers",
             {"kitsch": {"type": "http", "url": "http://unexpected.invalid/mcp"}}),
        ]
        for manifest, key, value in cases:
            with self.subTest(key=key), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                for name in ("plugins", ".agents", ".claude-plugin"):
                    shutil.copytree(ROOT / name, root / name)
                path = root / "plugins/kitsch" / manifest
                data = json.loads(path.read_text())
                data[key] = value
                path.write_text(json.dumps(data))
                with self.assertRaises(AssertionError):
                    validate(root)

    def test_rejects_marketplace_path_escape(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in ("plugins", ".agents", ".claude-plugin"):
                shutil.copytree(ROOT / name, root / name)
            path = root / ".agents/plugins/marketplace.json"
            data = json.loads(path.read_text())
            data["plugins"][0]["source"]["path"] = "../elsewhere"
            path.write_text(json.dumps(data))
            with self.assertRaises(AssertionError):
                validate(root)
