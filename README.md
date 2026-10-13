# homy-xu.github.io

Personal academic homepage of **Hongming (Homy) Xu** — undergraduate student at the School of
Computer Science, Shanghai Jiao Tong University (Zhiyuan Honors Program).

Research interests: coding foundation models, long-horizon agents, agent & parametric memory,
coding-model post-training, and self-improving AI.

Live site: **https://homy-xu.github.io/**

---

## Structure

```
.
├── index.html                      # single page, all content
├── assets/
│   ├── css/style.css               # styling (light + dark, responsive, print)
│   ├── img/
│   │   ├── memtrace-overview.png   # MemTrace, Fig. (system overview)
│   │   ├── dial-overview.png       # Dial, "System Overview of Dial"
│   │   ├── agent-memory-workflows.png
│   │   ├── sjtu-logo.png
│   │   ├── theseus-logo.png
│   │   ├── memtensor-logo.png
│   │   └── favicon.svg
│   └── files/CV_Hongming_Xu.pdf
├── .nojekyll                       # serve assets as-is, skip Jekyll processing
└── README.md
```

## Design notes

- **Static HTML + CSS only.** No build step, no dependencies, no Jekyll — the repository is served
  directly by GitHub Pages from the branch root.
- **Single column, research-first.** Publications lead; contact details and institution logos are
  deliberately understated.
- **Light / dark mode** follow the reader's system preference automatically.
- **Responsive** at a 620 px breakpoint; a print stylesheet is included.

## Updating

Everything lives in `index.html` — edit it directly and push to `main`; GitHub Pages redeploys
automatically in about a minute.

Publication entries follow this shape:

```html
<article class="pub">
  <figure class="pub__fig">
    <img src="assets/img/FILE.png" alt="DESCRIPTION" loading="lazy">
    <figcaption><strong>Caption lead.</strong> Caption body.</figcaption>
  </figure>
  <h3 class="pub__title">Paper Title</h3>
  <p class="pub__authors">A, <span class="me">Hongming Xu</span>, C</p>
  <p class="pub__venue"><span class="badge badge--review">Under review · VENUE</span></p>
  <p class="pub__desc">One-paragraph summary.</p>
  <p class="pub__links"><a href="…">arXiv</a><a href="…">Code</a></p>
</article>
```

Use `badge--accept` for accepted papers and `badge--review` for those under review. Wrap your own
name in `<span class="me">` so it is highlighted in every author list.

## Figure sources

Each overview figure was extracted from the paper's own LaTeX source on arXiv and rasterized at
2200 px from the vector PDF, so it stays sharp on HiDPI displays:

| Figure | Source |
| --- | --- |
| `memtrace-overview.png` | [`arXiv:2610.04838`](https://arxiv.org/abs/2610.04838) — `figures/overview.pdf` |
| `dial-overview.png` | [`arXiv:2603.07449`](https://arxiv.org/abs/2603.07449) — `fig/Framework.pdf` |
| `agent-memory-workflows.png` | [`arXiv:2606.24775`](https://arxiv.org/abs/2606.24775) — `figures/intro_example_workflows_v6.pdf` |

The SJTU, Theseus Lab, and MemTensor logos come from the MemTrace arXiv source bundle
(`assets/arxiv/`), whose title page already uses this institutional logo row.

## Deployment

GitHub Pages, branch `main`, folder `/` (root). The `.nojekyll` file disables Jekyll so the
`assets/` directory is served verbatim.
