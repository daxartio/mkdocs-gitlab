import os

import pytest
from mkdocs.config.defaults import MkDocsConfig

from mkdocs_gitlab.plugin import MkDocsGitlabPlugin


@pytest.fixture()
def plugin():
    return MkDocsGitlabPlugin()


def test_on_config_by_default(plugin, mocker):
    config = mocker.Mock(spec=MkDocsConfig)
    config.markdown_extensions = []

    plugin.on_config(config)

    assert config.site_name == "Documentation"
    assert config.site_description == ""
    assert config.markdown_extensions == ["gitlab"]


def test_on_config(plugin, mocker):
    os.environ["CI_PROJECT_TITLE"] = "Test"
    os.environ["CI_PROJECT_DESCRIPTION"] = "Test description"
    os.environ["CI_PROJECT_URL"] = "http://example.com"
    os.environ["CI_PAGES_URL"] = "http://pages.example.com"
    os.environ["CI_PROJECT_PATH"] = "group/test"
    config = mocker.Mock(spec=MkDocsConfig)
    config.markdown_extensions = ["gitlab"]

    plugin.on_config(config)

    assert config.site_name == "Test"
    assert config.site_description == "Test description"
    assert config.site_url == "http://pages.example.com"
    assert config.repo_url == "http://example.com"
    assert config.repo_name == "group/test"
    assert config.markdown_extensions == ["gitlab"]
