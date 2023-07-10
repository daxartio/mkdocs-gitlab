import os

import pytest
from mkdocs.config.defaults import MkDocsConfig

from mkdocs_gitlab.plugin import MkDocsGitlabPlugin


@pytest.fixture()
def plugin():
    return MkDocsGitlabPlugin()


def test_on_config_by_default(plugin, mocker):
    config = mocker.Mock(spec=MkDocsConfig)

    plugin.on_config(config)

    assert config.site_name == "Documentation"
    assert config.site_description == ""


def test_on_config(plugin, mocker):
    os.environ["CI_PROJECT_TITLE"] = "Test"
    os.environ["CI_PROJECT_DESCRIPTION"] = "Test description"
    os.environ["CI_PROJECT_URL"] = "http://example.com"
    config = mocker.Mock(spec=MkDocsConfig)

    plugin.on_config(config)

    assert config.site_name == "Test"
    assert config.site_description == "Test description"
    assert config.site_url == "http://example.com"
