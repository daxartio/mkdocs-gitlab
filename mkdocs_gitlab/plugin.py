import os
from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from mkdocs.plugins import BasePlugin

if TYPE_CHECKING:  # pragma: no cover
    from mkdocs.config.defaults import MkDocsConfig


CI_PROJECT_TITLE = "CI_PROJECT_TITLE"
CI_PROJECT_DESCRIPTION = "CI_PROJECT_DESCRIPTION"
CI_PROJECT_URL = "CI_PROJECT_URL"
CI_PAGES_URL = "CI_PAGES_URL"
CI_PROJECT_NAME = "CI_PROJECT_NAME"
CI_PROJECT_PATH = "CI_PROJECT_PATH"
CI_DEFAULT_BRANCH = "CI_DEFAULT_BRANCH"


@dataclass
class SiteConfig:
    site_name: str
    site_url: Optional[str]
    repo_url: Optional[str]
    repo_name: Optional[str]
    site_description: str


def get_config_from_gitlab() -> SiteConfig:
    project_title = os.getenv(CI_PROJECT_TITLE, "Documentation")
    project_description = os.getenv(CI_PROJECT_DESCRIPTION, "")
    project_url = os.getenv(CI_PROJECT_URL)
    pages_url = os.getenv(CI_PAGES_URL)
    repo_name = os.getenv(CI_PROJECT_PATH)

    return SiteConfig(
        site_name=project_title,
        site_url=pages_url,
        repo_url=project_url,
        repo_name=repo_name,
        site_description=project_description,
    )


class MkDocsGitlabPlugin(BasePlugin):  # type: ignore
    def on_config(self, config: "MkDocsConfig") -> "MkDocsConfig":
        site_config = get_config_from_gitlab()

        config.site_name = site_config.site_name
        config.site_description = site_config.site_description
        config.site_url = site_config.site_url
        config.repo_url = site_config.repo_url
        config.repo_name = site_config.repo_name

        if "gitlab" not in config.markdown_extensions:
            config.markdown_extensions.append("gitlab")

        return config
