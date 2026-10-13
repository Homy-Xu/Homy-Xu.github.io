#!/usr/bin/env python3
"""Check publishable assets, local links, and generated-page consistency."""
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build import build

ROOT = Path(__file__).resolve().parents[1]


class PageLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.images = []

    def handle_starttag(self, tag, attributes):
        attr = dict(attributes)
        if "id" in attr:
            assert attr["id"] not in self.ids, f"Duplicate id: {attr['id']}"
            self.ids.add(attr["id"])
        for key in ("src", "href"):
            if attr.get(key):
                self.links.append(attr[key])
        if tag == "img":
            self.images.append(attr)
            assert "alt" in attr, "Image without alt text"


def main():
    document = (ROOT / "index.html").read_text(encoding="utf-8")
    assert document == build(), "index.html is stale; run python3 scripts/build.py"
    page = PageLinks()
    page.feed(document)
    for link in page.links:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc:
            continue
        if parsed.path:
            target = ROOT / unquote(parsed.path).lstrip("/")
            assert target.is_file(), f"Missing local file: {link}"
        elif parsed.fragment:
            assert parsed.fragment in page.ids, f"Broken fragment: {link}"
    sources = json.loads((ROOT / "docs/paper-assets.json").read_text(encoding="utf-8"))
    for figure in sources["papers"]:
        path = ROOT / figure["output_path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == figure["output_sha256"], f"Figure differs from its provenance: {path}"
    cv = (ROOT / "files/CV_Hongming_Xu.pdf").read_bytes()
    assert cv.startswith(b"%PDF-"), "Invalid CV"
    assert cv == (ROOT / "assets/files/CV_Hongming_Xu.pdf").read_bytes(), "Legacy CV URL is out of date"
    print(f"OK: {len(page.links)} links, {len(page.images)} image elements, 3 original paper figures, and current generated HTML.")


if __name__ == "__main__":
    main()
