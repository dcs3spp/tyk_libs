# Summary

A CLI to convert a release branch name with patch semver to a branch name
containing minor semver string. contains a major and minor version number, e.g.
`major.minor`.

The conceptual idea is that this CLI can be used from GitHub action(s). It is
intended to serve as the mechanism by which we can convert from `release-x.y.z`
to `release-x.y`. This document outlines why.

## Overview

The tyk-docs repository uses a GitHub action, [Tyk OAS API definition fields sync](https://github.com/TykTechnologies/tyk-docs/blob/master/.github/workflows/update-oas-docs.yaml),
to respond to a `repository_dispatch` event for synchronising changes to Tyk OAS
definition fields.

The event payload contains the following fields:

- _sha_: SHA commit from the repository that raised the repository dispatch
  event.
- _ref_: The name of the branch that raised the event. The branch name is
  prefixed with `release-` with a semantic version appended, e.g. `release-x.y.z`.

An example payload is listed below:

```json
{
  "sha": "SHA commit from the TykTechnologies/Tyk repository",
  "ref": "release-x.y.z"
}
```

## The Current Workflow

Tyk-docs repository contains a GitHub action, named [Tyk OAS API definition
fields
sync](https://github.com/TykTechnologies/tyk-docs/blob/master/.github/workflows/update-oas-docs.yaml),
that listens for a `tyk-oas-docs` repository dispatch event and performs the
following sequence of actions:

1. Checkout the branch in tyk-docs that corresponding to the ref payload field.
2. Checkout the SHA commit on TykTechnologies/Tyk repository.
3. Copies `./tyk/apidef/oas/schema/x-tyk-gateway.md`to
   `./tyk-docs/tyk-docs/content/shared/x-tyk-gateway.md`
4. Raises a pull request from the tyk-docs branch with the same name as `ref`

## The Problem

The tyk-docs repository only uses a release branch name of `release-x.y`, i.e.
at the time of writing only a major and minor release cadence is used.
Conversely, other Tyk products use full semantic versioning, e.g. x.y.z.

Subsequently, an error is raised by the tyk-docs GitHub action when it tries to
checkout the branch `release-x.y.z` that is received in the event payload.

This is blocking us from synchronising OAS definition updates.
