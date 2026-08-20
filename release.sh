#!/usr/bin/env bash
# release.sh — create and push a new version tag for the Zira fonts.
#
# Usage:
#   ./release.sh v0.0.2      # or without the "v" prefix: ./release.sh 0.0.2
#
# The tag is created at the current HEAD and pushed to origin. jsDelivr
# caches tagged versions permanently, so version numbers must never be
# reused — this script refuses to overwrite an existing tag.

set -euo pipefail

usage() {
  echo "Usage: $0 <version>" >&2
  echo "  version: semver, e.g. v0.0.2 or 0.0.2 (leading 'v' is optional)" >&2
  exit 1
}

[[ $# -eq 1 ]] || usage

version="$1"
case "$version" in
  v*) tag="$version" ;;
  *) tag="v$version" ;;
esac

# Basic semver check: v1.2.3 (optionally with -prerelease or +build metadata)
if [[ ! "$tag" =~ ^v[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z.-]+)?(\+[0-9A-Za-z.-]+)?$ ]]; then
  echo "ERROR: '$tag' is not a valid semver version (expected e.g. v0.0.2)" >&2
  exit 1
fi

# Refuse to tag a dirty working tree (the tag must pin a stable commit)
if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "ERROR: working tree has uncommitted changes; commit or stash them first" >&2
  exit 1
fi

# Refuse to reuse a version number
if git rev-parse -q --verify "refs/tags/$tag" >/dev/null 2>&1; then
  echo "ERROR: tag '$tag' already exists locally" >&2
  exit 1
fi
if git ls-remote --exit-code --tags origin "refs/tags/$tag" >/dev/null 2>&1; then
  echo "ERROR: tag '$tag' already exists on origin" >&2
  exit 1
fi

# Warn if the local HEAD is not the same commit as origin/main (e.g. the CI
# build from the latest push has not been finished or pulled yet), so the
# tag does not accidentally pin stale fonts.
git fetch origin --quiet
if [[ "$(git rev-parse HEAD)" != "$(git rev-parse origin/main)" ]]; then
  echo "WARNING: local HEAD ($(git log -1 --format=%h HEAD)) differs from"
  echo "         origin/main ($(git log -1 --format=%h origin/main))."
  echo "         If the CI build hasn't finished or been pulled yet, this tag"
  echo "         may pin stale fonts."
  read -r -p "Press Enter to continue, or Ctrl-C to abort... "
fi

git tag -a "$tag" -m "Zira fonts $tag"
git push origin "$tag"

echo
echo "Tag $tag created and pushed."
echo "jsDelivr URLs (permanent cache):"
echo "  https://cdn.jsdelivr.net/gh/dangpang/zira-font@$tag/zira/fonts.css"
echo "  https://cdn.jsdelivr.net/gh/dangpang/zira-font@$tag/zira/mono/ZiraMono.css"
echo "  https://cdn.jsdelivr.net/gh/dangpang/zira-font@$tag/zira/sans/ZiraSans.css"
echo "  https://cdn.jsdelivr.net/gh/dangpang/zira-font@$tag/zira/serif/ZiraSerif.css"
echo "  https://cdn.jsdelivr.net/npm/zira-font@${tag#v}/zira/fonts.css"
