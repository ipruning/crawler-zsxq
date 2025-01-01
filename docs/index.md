# `crawler_zsxq` User Guide

!!! info

    For more information on how this was built and deployed, as well as other Python best
    practices, see [`python-blueprint`](https://github.com/johnthagen/python-blueprint).

!!! info

    This user guide is purely an illustrative example that shows off several features of MkDocs
    and included Markdown extensions.

## Installation

First, create and activate a Python virtual environment:

=== "Linux/macOS"

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

=== "Windows"

    ```powershell
    py -m venv venv
    venv\Scripts\activate
    ```

Then install the `crawler_zsxq` package:

```bash
pip install .
```

## Quick Start

To use `crawler_zsxq` within your project, import the `demo_function` function and execute it like:

```python
from crawler_zsxq.lib import demo_function

# (1)
assert demo_function(3) == 6
```

1. This assertion will be `True`

!!! tip

    Within PyCharm, use ++tab++ to auto-complete suggested imports while typing.

### Expected Results

<div class="center-table" markdown>

| Input | Output |
|:-----:|:------:|
|   1   |   1    |
|   2   |   2    |
|   3   |   6    |
|   4   |   24   | 

</div>