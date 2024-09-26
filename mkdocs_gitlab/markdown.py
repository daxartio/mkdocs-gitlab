import os
from typing import TYPE_CHECKING, List

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

if TYPE_CHECKING:  # pragma:no cover
    from markdown import core

PREPROCESSOR_PRIORITY = int(os.getenv("MKDOCS_GITLAB_PREPROCESSOR_PRIORITY", "175"))


class TOCPreprocessor(Preprocessor):
    def run(self, lines: List[str]) -> List[str]:
        new_lines = []
        for line in lines:
            if line.strip() in ["[[_TOC_]]", "[TOC]", "[[_toc_]]", "[toc]"]:
                continue
            new_lines.append(line)
        return new_lines


class TOCExtension(Extension):
    def extendMarkdown(self, md: "core.Markdown") -> None:  # noqa:N802
        md.preprocessors.register(TOCPreprocessor(md), "toc", PREPROCESSOR_PRIORITY)
