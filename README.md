# ZSXQ's crawler

## 0. Table of Contents

- [ZSXQ's crawler](#zsxqs-crawler)
    - [0. Table of Contents](#0-table-of-contents)
    - [1. Background](#1-background)
        - [1.0 Install](#10-install)
        - [1.1 Name Convention](#11-name-convention)
    - [2. Architecture](#2-architecture)
        - [2.0 Overview](#20-overview)
        - [2.1 Class](#21-class)
    - [7. License](#7-license)
    - [8. External Link](#8-external-link)
    - [9. ChangeLog](#9-changelog)

## 1. Background

- 定期监控知识星球，并导出 Markdown 与图片；
- 导出知识星球所有内容；
- 将知识星球转换为 RSS 订阅；

### 1.0 Install

- Clone GitHub Repository `git clone https://github.com/Spehhhhh/crawler-zsxq.git`
- Switch to the directory `cd crawler-zsxq`

```bash
# This project uses pipenv to manage the virtual environment.

# Install Poetry
$ curl -sSL https://install.python-poetry.org | python3 -

# Set environment variables
$ echo 'export PATH="$HOME/.poetry/bin:$PATH"' >> ~/.zshrc

# Install package
$ poetry install

# Activate the virtual environment for the current project
$ poetry shell

# Generate lockfile
$ poetry lock --no-update

# Run the main program
$ poetry run python <files>
```

### 1.1 Name Convention

- Class Naming Convention: `CapWords`
- Class Member Convention: `lower_with_under_`
- Function Naming Convention: `lower_with_under()`
- Variables Naming Convention: `lower_with_under`

## 2. Architecture

### 2.0 Overview

[[TODO]]

### 2.1 Class

[[TODO]]

## 7. License

[Apache-2.0](LICENSE)

## 8. External Link

[[TODO]]

## 9. ChangeLog

- 2022-05-11 init
