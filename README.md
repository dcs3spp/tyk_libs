# README

This repository contains python CLI and functions to support tyk-docs. Example
usages are CLIs for use in GitHub actions.

## Prerequisites

- [poetry](https://python-poetry.org/): Python package and dependency manager

## Setup

1. `make install`
2. `make pytest`
3. `make behave`

## CLI Utilities

| CLI                | Description                                               | Usage                                  |
| :----------------- | :-------------------------------------------------------- | :------------------------------------- |
| find_missing_links | Check menu.yaml for missing content paths                 | `make find_missing_links`              |
| map_branch         | Map Tyk Gateway release branch to Tyk-docs release branch | `make map_branch branch=release-4.2.3` |
