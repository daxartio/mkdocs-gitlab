from markdown import markdown

from mkdocs_gitlab.markdown import TOCExtension


def test_toc():
    md = "\n".join(
        [
            "# Gitlab",
            "[[_TOC_]]",
            "[TOC]",
            "[[_toc_]]",
            "[toc]",
        ]
    )
    html = markdown(
        md,
        extensions=[
            TOCExtension(),
        ],
    )

    assert html == "<h1>Gitlab</h1>"
