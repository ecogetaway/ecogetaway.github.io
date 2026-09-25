# ecogetaway.github.io

Personal research hub for **Sanjay C.** — open source contribution infrastructure: localization and language inclusion, accessibility review, AI contribution policy, and machine-operable documentation.

Live: https://ecogetaway.github.io/

## How this site relates to the initiative site

- **This site** is person-forward: publications, background, contact, and essays.
  It carries the `Person` entity (`https://ecogetaway.github.io/#sanjay-c`) that
  other sites reference in their structured data.
- **https://oss-infrastructure-initiative.netlify.app/** is project-forward: one
  page per workstream, research, roadmap, funding, and ways to contribute. Topic
  searches ("open source localization review", "accessibility pull request review",
  "AI contribution policy examples") should land there or on the repositories, not here.

## Projects linked from this hub

- [oss-language-inclusion](https://github.com/ecogetaway/oss-language-inclusion) — localization review evidence and i18n tooling, including i18n-security-lint
- [oss-accessibility-inclusion](https://github.com/ecogetaway/oss-accessibility-inclusion) — a11y review case studies, rubric, and templates
- [oss-ai-contribution-policy](https://github.com/ecogetaway/oss-ai-contribution-policy) — AI contribution policy catalogue + draft schema
- [machine-operable/readme-ci](https://github.com/machine-operable/readme-ci) — tests the code examples in Markdown documentation

## Site structure

- `style.css` — shared stylesheet (tokens, focus, contrast)
- `index.html` — hub
- `accessibility.html` — accessibility statement
- `writing/` — essays (start with `overlays-supply-chain.html`)
- `404.html` — not-found page (noindex; uses root-relative links because it is served at any path)
- `robots.txt`, `sitemap.xml` — crawler rules and the list of indexable URLs
- `favicon.svg`, `apple-touch-icon.png`, `social-card.png` (source: `social-card.svg`)
- `c7cf13d7a648be30c2b5e444592f218f.txt` — IndexNow ownership key. After deploying a new or changed page, submit it: see the initiative site's README for the one-line `curl`.

Deploys run from `.github/workflows/pages.yml`, which copies files **by name**.
A new file must be added in three places: the `.gitignore` allowlist, the
workflow's `cp` lines, and (if indexable) `sitemap.xml`.

To re-render the images after editing the SVG source (macOS):

```bash
sips -s format png social-card.svg --out social-card.png
```

## Checklist for a new page (essay, case study, project, tool)

1. **Title** under ~60 characters, subject first, ending `— Sanjay C.`
2. **Meta description** of 120–160 characters that says what the page contains; no keyword lists.
3. `<link rel="canonical">` with the full `https://ecogetaway.github.io/...` URL.
4. Open Graph and Twitter tags, copied from an existing page (`og:type` is `article` for essays).
5. One `h1`, then `h2`/`h3` in order; skip link to `main id="content"`.
6. JSON-LD: `Article` for essays, with `author` pointing at `https://ecogetaway.github.io/#sanjay-c`
   and a real `datePublished`. Add the same entry to the homepage `@graph`.
7. Link it from the homepage Writing or Current work section, with a one-line summary.
8. Link out to the relevant initiative workstream page and repository, and link back from them where it fits.
9. Add the URL to `sitemap.xml` and bump `lastmod` on any page you changed.
10. Add the file to the `.gitignore` allowlist and the workflow `cp` step.
11. Descriptive alt text on any image; describe what it shows, not "image of".
12. After deploy: check the URL returns 200, run axe or WAVE, add the result to the testing
    log in `accessibility.html`, and request indexing in Search Console.
13. Articles first published elsewhere go here only after the outlet publishes, with an
    "originally published at" link and `rel="canonical"` pointing at the original.
