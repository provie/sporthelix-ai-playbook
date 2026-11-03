"""Offline tests for bilingual documentation and relative Markdown links."""
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAIRS = [
    ("README.md", "README.de.md"),
    ("prompts/event-extraction.md", "prompts/event-extraction.de.md"),
    ("prompts/source-validation.md", "prompts/source-validation.de.md"),
    ("agents/codex-implementation.md", "agents/codex-implementation.de.md"),
    ("examples/walkthrough.md", "examples/walkthrough.de.md"),
    ("references.md", "references.de.md"),
]
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


class BilingualDocsTest(unittest.TestCase):
    def test_all_language_versions_exist_and_crosslink(self):
        for english, german in PAIRS:
            with self.subTest(english=english):
                en_path, de_path = ROOT / english, ROOT / german
                self.assertTrue(en_path.is_file())
                self.assertTrue(de_path.is_file())
                self.assertIn(de_path.name, en_path.read_text(encoding="utf-8"))
                self.assertIn(en_path.name, de_path.read_text(encoding="utf-8"))

    def test_relative_markdown_links_resolve(self):
        for document in ROOT.rglob("*.md"):
            text = document.read_text(encoding="utf-8")
            for match in LINK_PATTERN.finditer(text):
                link = match.group(1).split(maxsplit=1)[0].strip("<>")
                if not link or link.startswith("#"):
                    continue
                parsed = urlsplit(link)
                if parsed.scheme or parsed.netloc:
                    continue
                target = (document.parent / unquote(parsed.path)).resolve()
                with self.subTest(document=str(document.relative_to(ROOT)), target=link):
                    self.assertTrue(target.is_file(), f"Invalid relative link: {link}")


if __name__ == "__main__":
    unittest.main()
