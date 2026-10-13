# Hongming Xu · 许鸿铭

Personal academic homepage: **[homy-xu.github.io](https://homy-xu.github.io/)**.

A responsive, bilingual academic website with publication figures, research experience, education, and a downloadable CV. English is the default; the language switch remembers the visitor's choice. All text is present in the static HTML, including when JavaScript is disabled.

## Update the homepage

1. Edit `content/profile.json` for biography, research interests, publications, news, and experience. Each translated field has `en` and `zh` values. Introductory paragraphs, news, and summaries allow inline HTML links and emphasis; the remaining fields are plain text. Research interests have a title and description; paper contributions and experience details are lists.
2. Replace both `files/CV_Hongming_Xu.pdf` and `assets/files/CV_Hongming_Xu.pdf` with the same current PDF. The checker verifies that the current and legacy CV URLs stay in sync.
3. Replace `assets/images/avatar.png` to change the profile image. The initial image is the owner's existing GitHub avatar.
4. Run:

   ```sh
   python3 scripts/build.py
   python3 scripts/check.py
   ```

5. Commit and push to `main`. GitHub Actions builds and deploys the site to GitHub Pages.

The website needs no npm packages, external fonts, analytics, or third-party runtime scripts. Python 3.9+ is enough to build. Layout and interactions live in `assets/css/site.css` and `assets/js/site.js`.

The original site's `assets/img/`, `assets/files/`, and `assets/css/style.css` paths are retained so previously published asset links remain usable. The current page uses `assets/images/`, `files/`, and `assets/css/site.css`.

## Local preview

```sh
python3 scripts/build.py
python3 -m http.server 8000
```

Open [localhost:8000](http://localhost:8000/). A deployment artifact can be staged with `python3 scripts/build.py --output _site`.

## Paper illustrations and sources

The three featured figures were rendered from the original figure PDFs in the papers' arXiv TeX source archives. They preserve the complete original illustrations. Click a thumbnail to enlarge it; ordinary image links still work without JavaScript.

- MemTrace: Figure 2, `2610.04838v2`.
- Dial: Figure 2, `2603.07449v2`.
- Are We Ready For An Agent-Native Memory System?: Figure 1, `2606.24775v1`.

See [asset provenance](docs/paper-assets.json) for source paths, versions, authors, captions, license notices, and SHA-256 checksums, and [content sources](docs/content-sources.md) for factual sources and design references. Publication status is maintained from the owner's CV; under-review work is explicitly labeled.

## Design acknowledgments

The composition draws inspiration from [Xiang Zhang](https://lcbreathe.github.io/), [Hongrui Wu](https://onehfr.github.io/), and [Yi Duan](https://duanyi516.github.io/): a compact profile, clear academic typography, figure-led publication entries, and institutional logos. The text uses Trebuchet MS with Helvetica and system fallbacks, following Yi Duan's academic typography. Biography, research interests, and contributions were expanded from [the owner's previous GitBook homepage](https://sjtu-edu-4.gitbook.io/sjtu.edu-docs), with dates and status checked against the latest CV. This repository has its own standalone HTML/CSS/JavaScript implementation.

## License

Original site code is available under the [MIT license](LICENSE). Personal content, the CV, paper illustrations, logos, and the GitHub avatar are excluded from that code license. Paper figures retain the rights and licenses documented in the provenance file; institutional and company marks belong to their respective owners.
