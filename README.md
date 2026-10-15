# ResearchProjectTemplate

A template for a research project whose `docs/` directory is published as a site on GitHub Pages.
The markdown under `docs/` is the source. It reads the same on GitHub as it does on the site, and
`docs/LANDING_PAGE.md` is the root page.

The site is built by [MkDocs](https://www.mkdocs.org/) with the
[Material](https://squidfunk.github.io/mkdocs-material/) theme and published by the GitHub Action in
`.github/workflows/docs.yml`. Nothing needs running by hand after the one setting described below.

## Using the template

1. On GitHub, open this repository and choose **Use this template**, then **Create a new repository**.
2. In the new repository's settings, under **Pages**, set **Source** to **GitHub Actions**. Until this
   is set the build succeeds and the deploy step fails, which is the failure to expect on the first
   run.
3. In `mkdocs.yml`, change the five values at the top: `site_name`, `site_description`, `site_url`,
   `repo_url` and `repo_name`. Change the link under `extra.social` and the `copyright` line to match.
4. In `docs/CITATIONS.md`, change the author, the title, the year and the URL.
5. Push to `main`. The site lands at the address in `site_url`.

## What is where

| Path | What it is |
| --- | --- |
| `docs/LANDING_PAGE.md` | The root page of the site. The hero, the cards and the links into everything else. |
| `docs/PAPER.md` | The paper. Shows how citations, footnotes, math and tables are written. |
| `docs/BIBLIOGRAPHY.md` | Every work the paper cites, one anchor per entry. |
| `docs/CITATIONS.md` | How to cite this project. |
| `docs/stylesheets/site.css` | The palette, the type and the landing page layout. |
| `docs/javascript/mathjax.js` | MathJax settings, and the re-render after instant navigation. |
| `docs/assets/favicon.svg` | The icon in the browser tab. |
| `hooks/landing_page.py` | Serves `LANDING_PAGE.md` at the site root in place of `index.md`. |
| `mkdocs.yml` | The site configuration and the navigation. |
| `requirements.txt` | The pinned theme version. |
| `.github/workflows/docs.yml` | Builds the site on every push to `main` and publishes it. |

## Adding a document

A document is a markdown file under `docs/`. To put it on the site:

1. Write it as `docs/NAME.md`. The first line is a level-one heading, which becomes the page title.
2. Add it to `nav` in `mkdocs.yml`. The entry's label is what the header shows, and its order in the
   list is its order in the header. A document under a group heading sits in a dropdown:

   ```yaml
   nav:
     - Home: index.md
     - Paper: PAPER.md
     - References:
         - Bibliography: BIBLIOGRAPHY.md
         - Citing this work: CITATIONS.md
     - Appendix: APPENDIX.md
   ```

   `index.md` is the landing page under the name the site serves it as. Leave that entry alone.

3. Link to it from the landing page. A link is a relative path to the markdown file, with the `.md`
   extension kept. The site rewrites it to the page's address and GitHub follows it as is:

   ```markdown
   [The appendix](APPENDIX.md){ .md-button }
   ```

   To link to a section, add the heading's anchor, which is its text in lower case with spaces as
   hyphens: `[Results](PAPER.md#results)`.

A document that is not in `nav` is still built and still reachable by link, but `mkdocs build
--strict` reports it, and the Action builds with `--strict`. A link to a file that does not exist
fails the build the same way, so a broken link never reaches the site.

### Landing page cards

A card is an item in a list inside a `grid cards` block. The icon, the title and the description
are each one line, with a rule between the title and the text. The title is the link, and the whole
card is clickable:

```markdown
<div class="grid cards" markdown>

-   :material-file-document-outline:{ .lg .middle } __[The appendix](APPENDIX.md)__

    ---

    One or two lines on what the reader finds there

</div>
```

Icon names are the Material Design icon set, written as `:material-NAME:`. The theme's
[icon search](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/) finds them by
keyword.

### Citations

A citation in the paper is a link to an anchor in `docs/BIBLIOGRAPHY.md`:

```markdown
A claim made before this work is cited where it is used [Knuth (1997)](BIBLIOGRAPHY.md#knuth1997).
```

An entry in the bibliography is one paragraph followed by its anchor on the next line. The anchor is
the first author's surname and the year, run together in lower case:

```markdown
Knuth, D. E. (1997). *The Art of Computer Programming, Volume 1* (3rd ed.). Addison-Wesley.
{ #knuth1997 }
```

Two works by the same author in the same year take a letter after the year, `knuth1997a` and
`knuth1997b`.

### Footnotes

A footnote is a marker in the text and a line anywhere in the file:

```markdown
A claim that needs a remark beside it.[^remark]

[^remark]: The remark.
```

### Math

Inline math goes between single dollar signs and display math between double dollar signs on their
own lines. The site renders it with MathJax and GitHub renders it natively.

## Building locally

```sh
pip install -r requirements.txt
mkdocs serve          # http://127.0.0.1:8000, rebuilds as you edit
mkdocs build --strict # what the Action runs; writes site/
```

`site/` is the rendered output and is not tracked. The Action rebuilds it on every push.

## Files the site does not publish

Only `docs/` is published. Source, data, scripts and anything else in the repository are reachable
from the site through full GitHub links, which a card or a button can carry the same as a page link:

```markdown
[:octicons-arrow-right-24: The code](https://github.com/dstroy0/ResearchProjectTemplate/tree/main/src)
```
