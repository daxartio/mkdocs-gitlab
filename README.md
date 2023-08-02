# MkDocs Gitlab

[![PyPI](https://img.shields.io/pypi/v/mkdocs-gitlab)](https://pypi.org/project/mkdocs-gitlab/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mkdocs-gitlab)](https://www.python.org/downloads/)
[![GitHub last commit](https://img.shields.io/github/last-commit/daxartio/mkdocs-gitlab)](https://github.com/daxartio/mkdocs-gitlab)
[![GitHub stars](https://img.shields.io/github/stars/daxartio/mkdocs-gitlab?style=social)](https://github.com/daxartio/mkdocs-gitlab)

The plugin updates mkdocs config with Gitlab CI/CD variables.

- CI_PROJECT_TITLE
- CI_PROJECT_DESCRIPTION
- CI_PAGES_URL
- CI_PROJECT_URL
- CI_PROJECT_PATH

Also the pugin deletes the `[[_TOC_]]` or `[TOC]` tag.

## Installation

### pip

```
pip install mkdocs-gitlab
```

## Usage

```yaml
site_name: Title

plugins:
- mkdocs-gitlab

```

## License

* [MIT LICENSE](LICENSE)

## Contribution

[Contribution guidelines for this project](CONTRIBUTING.md)
