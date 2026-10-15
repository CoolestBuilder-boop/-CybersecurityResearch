"""Serves docs/LANDING_PAGE.md as the root page of the site.

mkdocs takes docs/index.md as the root page and nothing else. This hook registers LANDING_PAGE.md
under the name index.md, so the root of the site is the landing page and the source file keeps
its own name on GitHub. The edit and view links on the page point at the real file.
"""

import os

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files

LANDING_PAGE = "LANDING_PAGE.md"
ROOT_PAGE = "index.md"


def on_files(files: Files, config: MkDocsConfig) -> Files:
    landing = files.get_file_from_path(LANDING_PAGE)
    if landing is None:
        raise FileNotFoundError(f"docs/{LANDING_PAGE} is the root page of the site and is missing")
    if files.get_file_from_path(ROOT_PAGE) is not None:
        raise FileExistsError(f"docs/{ROOT_PAGE} and docs/{LANDING_PAGE} both claim the root page")
    root = File.generated(config, ROOT_PAGE, abs_src_path=os.path.abspath(landing.abs_src_path))
    root.edit_uri = LANDING_PAGE
    files.remove(landing)
    files.append(root)
    return files
