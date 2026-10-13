#!/usr/bin/env python3
"""Build the bilingual static homepage with Python's standard library."""
import argparse
import html
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = json.loads((ROOT / "content/profile.json").read_text(encoding="utf-8"))
ASSETS = json.loads((ROOT / "docs/paper-assets.json").read_text(encoding="utf-8"))
FIGURES = {paper["key"]: paper for paper in ASSETS["papers"]}


def esc(value):
    return html.escape(str(value), quote=True)


def t(value, tag="span", css="", rich=False):
    """Render both languages, keeping the English document usable without JS."""
    render = str if rich else esc
    if isinstance(value, str):
        return render(value)
    if value["en"] == value["zh"]:
        return f'<{tag} class="{css}">{render(value["en"])}</{tag}>'
    return "".join(
        f'<{tag} class="i18n {css}" data-lang="{lang}" lang="{locale}">{render(value[lang])}</{tag}>'
        for lang, locale in (("en", "en"), ("zh", "zh-CN"))
    )


def label(en, zh):
    return t({"en": en, "zh": zh})


def icon(name):
    return f'<svg class="icon" aria-hidden="true"><use href="#icon-{name}"/></svg>'


def section_title(en, zh, extra=""):
    return f'<div class="section-heading"><h2>{label(en, zh)}</h2>{extra}</div>'


def publication(p):
    authors = []
    for name in p["authors"]:
        author = f'<strong>{esc(name)}</strong>' if name == P["name"] else esc(name)
        if name in p["equal_contributors"]:
            author += '<sup title="Equal contribution">*</sup>'
        authors.append(author)
    role = f'<span class="paper-role">{t(p["role"])}</span>' if p["role"]["en"] else ""
    return f'''
    <article class="publication" id="{esc(p['id'])}">
      <figure class="paper-figure">
        <a class="figure-link" href="{esc(p['image'])}" data-preview data-paper="{esc(p['paper'])}"
           data-title="{esc(p['title'])}" data-caption-en="{esc(p['figure_caption']['en'])}"
           data-caption-zh="{esc(p['figure_caption']['zh'])}" aria-haspopup="dialog"
           aria-label="Enlarge figure: {esc(p['title'])}">
          <span class="paper-badge{' accepted' if p['badge'] != 'Preprint' else ''}">{esc(p['badge'])}</span>
          <img src="{esc(p['image'])}" alt="{esc(p['image_alt'])}" width="{FIGURES[p['id']]['width']}" height="{FIGURES[p['id']]['height']}" loading="lazy" decoding="async">
          <span class="zoom-hint">{icon('expand')}{label('Enlarge', '放大')}</span>
        </a>
        <figcaption>{t(p['figure_caption'])}</figcaption>
      </figure>
      <div class="paper-copy">
        <h3><a href="{esc(p['paper'])}">{esc(p['title'])}</a></h3>
        <p class="authors">{', '.join(authors)}</p>
        <p class="paper-meta"><span class="venue">{t(p['venue'])}</span>{role}</p>
        {t(p['summary'], 'p', 'paper-summary', rich=True)}
        <div class="paper-links">
          <a href="{esc(p['paper'])}">{icon('file')}{label('Paper', '论文')}</a>
          <a href="{esc(p['code'])}">{icon('github')}{label('Code', '代码')}</a>
        </div>
        <details class="contribution"><summary>{label('My contribution', '我的贡献')}</summary>{t(p['contribution'], 'p')}</details>
      </div>
    </article>'''


def experience(item):
    return f'''
    <article class="experience-item">
      <div class="organization-logo"><img src="{esc(item['logo'])}" alt="{esc(item['organization'])} logo" loading="lazy"></div>
      <div class="experience-copy">
        <div class="item-heading"><h3><a href="{esc(item['url'])}">{esc(item['organization'])}</a></h3><span class="date">{t(item['dates'])}</span></div>
        <p class="position">{t(item['role'])}</p>
        <p class="mentor">{t(item['mentor'])}</p>
        {t(item['description'], 'p', 'experience-description')}
      </div>
    </article>'''


def build():
    news = "".join(f'<li><time datetime="{n["date"].replace(".", "-")}">{esc(n["date"])}</time><div>{t(n["text"], rich=True)}</div></li>' for n in P["news"])
    interests = "".join(f'<li>{t(i)}</li>' for i in P["interests"])
    intro = "".join(t(p, "p", rich=True) for p in P["intro"])
    papers = "".join(publication(p) for p in P["publications"])
    experiences = "".join(experience(x) for x in P["experience"])
    extra = P["additional_publication"]
    education = P["education"]
    structured = json.dumps({
        "@context": "https://schema.org", "@type": "Person", "name": P["name"],
        "alternateName": [P["chinese_name"], "Homy Xu"], "url": P["url"],
        "image": P["url"] + P["avatar"], "sameAs": [P["github"]],
        "affiliation": {"@type": "CollegeOrUniversity", "name": P["school"]["en"]},
        "knowsAbout": [i["en"] for i in P["interests"]]
    }, ensure_ascii=False)
    document = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <title>Hongming Xu · 许鸿铭</title>
  <meta name="description" content="Hongming Xu, undergraduate at Shanghai Jiao Tong University and research intern at MemTensor. Research in coding foundation models, long-horizon agents, and self-improving AI.">
  <link rel="canonical" href="{esc(P['url'])}">
  <meta property="og:type" content="profile">
  <meta property="og:title" content="Hongming Xu · 许鸿铭">
  <meta property="og:description" content="Coding foundation models · Long-horizon agents · Self-improving AI. Shanghai Jiao Tong University / MemTensor.">
  <meta property="og:url" content="{esc(P['url'])}">
  <meta property="og:image" content="{esc(P['url'] + P['avatar'])}">
  <meta name="twitter:card" content="summary">
  <link rel="icon" href="assets/images/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/css/site.css">
  <script src="assets/js/site.js" defer></script>
  <script type="application/ld+json">{structured}</script>
</head>
<body>
  <a class="skip-link" href="#main">{label('Skip to content', '跳转到正文')}</a>
  <svg xmlns="http://www.w3.org/2000/svg" class="svg-sprite" aria-hidden="true">
    <symbol id="icon-mail" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/></symbol>
    <symbol id="icon-pin" viewBox="0 0 24 24"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/></symbol>
    <symbol id="icon-file" viewBox="0 0 24 24"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9Z"/><path d="M14 3v6h6M8 13h8M8 17h6"/></symbol>
    <symbol id="icon-expand" viewBox="0 0 24 24"><path d="M8 3H3v5m13-5h5v5M3 16v5h5m13-5v5h-5"/></symbol>
    <symbol id="icon-arrow" viewBox="0 0 24 24"><path d="M7 17 17 7M7 7h10v10"/></symbol>
    <symbol id="icon-language" viewBox="0 0 24 24"><path d="M3 5h12M9 3v2m4 0c-1 6-4 9-9 12m1-9c2 4 4 6 8 8m1 5 5-12 5 12m-8-4h6"/></symbol>
    <symbol id="icon-github" viewBox="0 0 24 24"><path d="M9 19c-4 1-4-2-6-2m12 5v-4a3.5 3.5 0 0 0-1-2.7c3.3-.4 6.7-1.6 6.7-7.3a5.7 5.7 0 0 0-1.5-4 5.3 5.3 0 0 0-.1-4s-1.2-.4-4.1 1.5a14 14 0 0 0-7 0C5.1-.4 3.9 0 3.9 0a5.3 5.3 0 0 0-.1 4 5.7 5.7 0 0 0-1.5 4c0 5.7 3.4 6.9 6.7 7.3A3.5 3.5 0 0 0 8 18v4" transform="translate(1 1) scale(.9)"/></symbol>
  </svg>
  <div class="page">
    <header class="masthead">
      <a class="brand" href="#about"><span class="brand-mark" aria-hidden="true">HX</span><span>Hongming Xu</span></a>
      <nav class="navigation" aria-label="Main navigation">
        <a href="#about">{label('About', '关于')}</a>
        <a href="#publications">{label('Publications', '论文')}</a>
        <a href="#experience">{label('Experience', '经历')}</a>
        <a href="#education">{label('Education', '教育')}</a>
      </nav>
      <button class="language-button" type="button" aria-label="Switch to Chinese" hidden>{icon('language')}<span>中文</span></button>
    </header>

    <div class="site-grid">
      <aside class="profile" aria-label="Profile and contact information">
        <img class="avatar" src="{esc(P['avatar'])}" width="460" height="460" alt="Hongming Xu's GitHub avatar" fetchpriority="high">
        <div class="profile-info">
          <p class="profile-eyebrow">{t(P['role'])}</p>
          <h1>{esc(P['name'])}</h1>
          <p class="other-name"><span lang="zh-CN">{esc(P['chinese_name'])}</span><span class="name-divider">/</span>{esc(P['nickname'])}</p>
          <p class="profile-school"><a href="{esc(P['school_url'])}">{t(P['school'])}</a></p>
          <p class="profile-program">{t(P['program'], rich=True)}</p>
          <ul class="contact-links">
            <li class="location">{icon('pin')}{label('Shanghai, China', '中国 · 上海')}</li>
            <li><a href="mailto:{esc(P['email'])}">{icon('mail')}{esc(P['email'])}</a></li>
            <li><a href="mailto:{esc(P['secondary_email'])}">{icon('mail')}{esc(P['secondary_email'])}</a></li>
            <li><a href="{esc(P['github'])}">{icon('github')}GitHub {icon('arrow')}</a></li>
          </ul>
          <a class="cv-link" href="{esc(P['cv'])}">{icon('file')}{label('Curriculum vitae', '个人简历')}{icon('arrow')}</a>
          <p class="profile-note">{label('Building agents that learn<br>from experience.', '让智能体从经验中学习。') .replace('&lt;br&gt;', '<br>')}</p>
        </div>
      </aside>

      <main id="main">
        <section id="about" class="section about">
          {section_title('About me', '关于我')}
          <div class="intro">{intro}</div>
          <ul class="research-interests" aria-label="Research interests">{interests}</ul>
        </section>

        <section id="news" class="section news-section">
          {section_title('News', '近况')}
          <ul class="news-list">{news}</ul>
        </section>

        <section id="publications" class="section">
          {section_title('Selected publications', '代表性论文', '<span class="section-note">' + label('* Equal contribution', '* 共同贡献') + '</span>')}
          <div class="publications">{papers}</div>
          <article class="additional-publication">
            <p class="additional-label">{label('Also in data systems', '其他数据系统工作')}</p>
            <h3>{esc(extra['title'])}</h3>
            <p class="paper-meta"><span class="venue">{esc(extra['venue'])}</span></p>
            {t(extra['summary'], 'p', 'paper-summary', rich=True)}
          </article>
        </section>

        <section id="experience" class="section">
          {section_title('Research experience', '研究经历')}
          {experiences}
        </section>

        <section id="education" class="section">
          {section_title('Education', '教育背景')}
          <article class="experience-item education-item">
            <div class="organization-logo"><img src="assets/images/logos/sjtu-seal.png" alt="Shanghai Jiao Tong University logo" width="2805" height="2806" loading="lazy"></div>
            <div class="experience-copy">
              <div class="item-heading"><h3><a href="{esc(P['school_url'])}">{t(P['school'])}</a></h3><span class="date">{t(education['dates'])}</span></div>
              <p class="position">{t(education['degree'])}</p>
              <p class="mentor">{t(education['note'])}</p>
              <p class="honor">{t(P['honor'])}</p>
            </div>
          </article>
        </section>

        <section id="beyond" class="section beyond">
          {section_title('Beyond research', '科研之外')}
          <p>{t(P['personal'])}</p>
        </section>
      </main>
    </div>

    <footer class="footer">
      <span>© 2026 Hongming Xu</span>
      <div><span>{label('Updated October 2026', '更新于 2026 年 10 月')}</span><a href="https://github.com/Homy-Xu/Homy-Xu.github.io">{label('Source', '源码')}{icon('arrow')}</a><a href="#about">{label('Back to top', '回到顶部')} ↑</a></div>
    </footer>
  </div>

  <dialog class="figure-dialog" aria-labelledby="figure-dialog-title">
    <div class="dialog-header"><div><p class="dialog-eyebrow">{label('Research overview', '研究概览')}</p><h2 id="figure-dialog-title"></h2></div><button class="dialog-close" type="button" aria-label="Close figure">×</button></div>
    <div class="dialog-image-wrap"><img class="dialog-image" alt=""></div>
    <div class="dialog-footer"><span class="dialog-caption"></span><a class="dialog-paper-link" href="https://arxiv.org/">{label('View paper on arXiv', '在 arXiv 查看论文')}{icon('arrow')}</a></div>
  </dialog>
</body>
</html>
'''
    return "\n".join(line.rstrip() for line in document.splitlines()) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Also stage the deployable website here")
    args = parser.parse_args()
    document = build()
    (ROOT / "index.html").write_text(document, encoding="utf-8")
    if args.output:
        output = args.output.resolve()
        if output == ROOT or ROOT in output.parents and output.name in {"assets", "content", "scripts", "files", "docs"}:
            raise SystemExit("Choose a separate build directory such as _site.")
        output.mkdir(parents=True, exist_ok=True)
        (output / "index.html").write_text(document, encoding="utf-8")
        for folder in ("assets", "files"):
            shutil.copytree(ROOT / folder, output / folder, dirs_exist_ok=True)
        for name in (".nojekyll", "robots.txt", "sitemap.xml", "404.html"):
            shutil.copy2(ROOT / name, output / name)
        print(f"Staged website: {output}")
    print("Built index.html from content/profile.json")


if __name__ == "__main__":
    main()
