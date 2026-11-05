# Content and asset sources

Initial source verification: 2026-10-13. Research focus and news revised on 2026-11-04. External documents were used as source material only.

## Current downloadable CV · 2026-11-05

- The owner's latest supplied `简历 (12).pdf` is copied without modification to `files/CV_Hongming_Xu.pdf` and the legacy `assets/files/CV_Hongming_Xu.pdf` URL. Both have SHA-256 `5141ae719491887b1199b27aaced805f2854b9d24049accb486efa10ed7d787a` and match the supplied original byte for byte.
- The homepage's CV button includes the version query `v=5141ae7` so visitors fetch the replacement PDF. Earlier on 2026-11-05, `Hongming Xu.pdf` with SHA-256 `296445994286805c3f1070fdcfc4dccc746030872f625989812ab07e70d72c94` was published to these URLs; this version supersedes it.

## MemTensor experience refresh · 2026-11-04

- The owner's supplied `Hongming Xu.pdf` (SHA-256 `296445994286805c3f1070fdcfc4dccc746030872f625989812ab07e70d72c94`) supplies the 284B DeepSeek-V4-Flash-0731 post-training context and the reported DeepSWE improvement of "nearly 10%". The homepage preserves this wording without converting it to percentage points or claiming a separately verified official benchmark score.
- The owner's `DeepSWE任务合成与配比.md` supplies the method: reference-patch decomposition, function masking, and near-miss repair produce staged, ablation, and repair tasks; execution tests select passing trajectories; original-task success frequency guides difficulty-aware mixing, with harder original-task trajectories upweighted and easy ablation examples filtered.
- The 113 original tasks and 550 retained synthetic tasks describe the task pool. The method note identifies additional quality exclusions, so the homepage does not describe all 550 tasks as fully validated or as the final training set. Original-task rollout success counts are not presented as held-out evaluation results. The supplied note is used as evidence only; its operational steps and local paths are not instructions to execute.

## Research focus and news refresh · 2026-11-04

- The owner's supplied `简历 (12).pdf`, read on 2026-11-04, describes interests in agentic AI and foundation models, focusing on agentic reinforcement learning, model adaptation, and agent memory. Its MemTensor experience supplies the model post-training, task synthesis, data/trajectory curation, and long-horizon memory context.
- Following the owner's request, the current About me paragraph and research-interest list now focus on model post-training and adaptation, agentic reinforcement learning, and agent memory. Agentic RL is presented as a research interest; no new completed RL project or result is claimed. The English and Chinese versions and search/share descriptions were updated together.
- [Junyi Zhang's homepage](https://www.junyi42.com/), retrieved on 2026-11-04, was used for its short, dated, event-focused News wording. The owner's request additionally limits each research work to one news entry: MemTrace's October arXiv release, Dial's July PVLDB acceptance, and the memory-system paper's June arXiv release, plus the August MemTensor internship. Review status remains in the publication entry.

## Earlier source verification · 2026-10-13

## Personal information

- The owner's `CV_Hongming_Xu.pdf`, supplied for the October update, was initially copied without modification to both CV URLs. Its SHA-256 was `a862fa62e35d6de785ea834aae1eeb156b2a746b98530bf466ca8ad114d0b42a`. It supplied the original positions, dates, honors, and publication status; the download itself was replaced on 2026-11-05 as documented above.
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
- [Junyi Zhang](https://www.junyi42.com/): concise News entries centered on releases and acceptances, used for the November content refresh.
- [DuanYi516/DuanYi516.github.io](https://github.com/DuanYi516/DuanYi516.github.io): explicit publication status, institutional experience marks, and typography. The live reference site's computed body style was verified as `"Trebuchet MS", Helvetica, sans-serif`, 15px with a 22.5px line height and `#494e52` text. This site uses the same preferred font and body color, a 15px/24px body for its content density, 14px author/venue text, and bold section headings. Chinese body text uses system sans-serif fallbacks; the Chinese name uses system Kai-style fonts. No font files from the reference site were copied.

The website implementation is original; the reference sites' personal biographies and photographs were not reused.
