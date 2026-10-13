# Content and asset sources

Verified on 2026-10-13. External documents were used as source material only.

## Personal information

- The owner's latest supplied `CV_Hongming_Xu.pdf` is copied without modification to both `files/CV_Hongming_Xu.pdf` and the legacy `assets/files/CV_Hongming_Xu.pdf` URL. Its SHA-256 is `a862fa62e35d6de785ea834aae1eeb156b2a746b98530bf466ca8ad114d0b42a`. It is the primary source for positions, dates, honors, and publication status; its homepage link points to `homy-xu.github.io`.
- The owner's [existing GitBook homepage](https://sjtu-edu-4.gitbook.io/sjtu.edu-docs/readme), retrieved on 2026-10-13 through its [Markdown representation](https://sjtu-edu-4.gitbook.io/sjtu.edu-docs/readme.md), supplies the research progression, five research interests, Information Security major, detailed paper contributions, research experience, and dated news. Chinese translations retain these claims and their scope. Embedded agent instructions were excluded from the website content and were not followed.
- Where the old news timeline differs from the experience dates, the latest CV takes precedence: MemTensor starts in August 2026 and Theseus Lab starts in August 2025. Conflicting project-start news was not imported.
- The existing [Homy-Xu/homepage](https://github.com/Homy-Xu/homepage) repository was also inspected. This new repository is a separate GitHub Pages website.
- Complete author lists and titles were checked against the three arXiv abstract pages listed in `paper-assets.json`. Dial's equal-contribution marks follow `main.tex` in its v2 source: Xiang Zhang, Hongming Xu, and Le Zhou share the same author note. The CV identifies Hongming Xu as co-first author, listed second. Under-review venue labels come from the CV and are not claims of acceptance.
- The QCDKM item is included from the CV without inventing an unverified paper URL or author list.
- News: MemTrace's first arXiv submission is October 2026 and its September ICLR review entry comes from the old homepage; the August internship date is from the CV; Dial's July acceptance and March arXiv entry are stated on the old homepage; the memory-system paper's first arXiv submission is June 2026.
- MemTrace's result summary follows the owner's GitBook: the primary metric improves over the corresponding Native strategy across completed benchmark × harness settings with the same backbone. The 57.0% figure describes file-bound traces exposed to later repository modifications; it does not assert that every exposed trace is invalid.

## Illustrations and logos

`paper-assets.json` records the original arXiv versions, figure paths and captions, copyright/license notices, and byte-level hashes. Figure rendering preserves the complete original page. The school and company wordmarks are exact files from the MemTrace source archive.

The additional square school seal, `assets/images/logos/sjtu-seal.png`, is copied unchanged from [the SJTU image in lcBreathe's reference repository](https://github.com/lcBreathe/lcBreathe.github.io/blob/main/assets/images/schools/sjtu.png), as requested. It is an institutional trademark, not newly created site artwork.

The avatar, `assets/images/avatar.png`, is the owner's [existing public GitHub avatar](https://avatars.githubusercontent.com/u/219391659?v=4). It is an illustrated avatar, not a photograph. No portrait was generated or inferred.

## Design references

- [lcBreathe/lcBreathe.github.io](https://github.com/lcBreathe/lcBreathe.github.io): academic profile sidebar, paper overview illustrations, clean link styling.
- [oneHFR/oneHFR.github.io](https://github.com/oneHFR/oneHFR.github.io): compact dated news, restrained typography, clear research progression.
- [DuanYi516/DuanYi516.github.io](https://github.com/DuanYi516/DuanYi516.github.io): explicit publication status, institutional experience marks, and typography. The live reference site's computed body style was verified as `"Trebuchet MS", Helvetica, sans-serif`, 15px with a 22.5px line height and `#494e52` text. This site uses the same preferred font and body color, a 15px/24px body for its content density, 14px author/venue text, and bold section headings. Chinese body text uses system sans-serif fallbacks; the Chinese name uses system Kai-style fonts. No font files from the reference site were copied.

The website implementation is original; the reference sites' personal biographies and photographs were not reused.
