# my-arithmetic-llamoity

[![pipeline](https://gitlab.univ-lr.fr/llamoity/my-arithmetic-llamoity/badges/main/pipeline.svg)](https://gitlab.univ-lr.fr/llamoity/my-arithmetic-llamoity/-/pipelines)
[![coverage](https://gitlab.univ-lr.fr/llamoity/my-arithmetic-llamoity/badges/main/coverage.svg)](https://gitlab.univ-lr.fr/llamoity/my-arithmetic-llamoity/-/commits/main)
[![CI](https://github.com/llamoity/my-arithmetic-llamoity/actions/workflows/ci.yml/badge.svg)](https://github.com/llamoity/my-arithmetic-llamoity/actions/workflows/ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/llamoity/my-arithmetic-llamoity/badge.svg?branch=main)](https://coveralls.io/github/llamoity/my-arithmetic-llamoity?branch=main)
[![Documentation](https://readthedocs.org/projects/my-arithmetic-llamoity/badge/?version=latest)](https://my-arithmetic-llamoity.readthedocs.io/)

Petite bibliothèque d'arithmétique (TP CI/CD, M1 La Rochelle).

```console
$ hatch test --cover      # tests + couverture
$ hatch build             # dist/*.whl, version calculée depuis les tags git
$ hatch run docs:build    # documentation Sphinx
```
