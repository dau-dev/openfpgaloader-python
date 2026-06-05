# openfpgaloader

Python wrapping for openfpgaloader

[![Build Status](https://github.com/dau-dev/openfpgaloader/actions/workflows/build.yaml/badge.svg?branch=main&event=push)](https://github.com/dau-dev/openfpgaloader/actions/workflows/build.yaml)
[![codecov](https://codecov.io/gh/dau-dev/openfpgaloader/branch/main/graph/badge.svg)](https://codecov.io/gh/dau-dev/openfpgaloader)
[![License](https://img.shields.io/github/license/dau-dev/openfpgaloader)](https://github.com/dau-dev/openfpgaloader)
[![PyPI](https://img.shields.io/pypi/v/openfpgaloader.svg)](https://pypi.python.org/pypi/openfpgaloader)

## Overview

Wrapper of [openFPGALoader](https://github.com/trabucayre/openFPGALoader), distributed via PyPI. openFPGALoader is a universal utility for programming FPGAs, supporting a wide range of boards and cables.

```bash
# Pass-through to openFPGALoader
openfpgaloader-cli --help

# Flash a bitstream to a board
openfpgaloader-cli -b board_name bitstream.bit
```

## License

This software is licensed under the Apache 2.0 license. See the [LICENSE](LICENSE) file for details.

openFPGALoader is Copyright (c) Gwenhael Goavec-Merou and contributors, licensed under the Apache 2.0 license.

> [!NOTE]
> This library was generated using [copier](https://copier.readthedocs.io/en/stable/) from the [Base Python Project Template repository](https://github.com/python-project-templates/base).
