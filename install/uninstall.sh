#!/usr/bin/env bash
# Removes only files listed in the installer manifest whose hash still matches. Modified files are kept.
set -u
SCOPE=project; TARGET=""; DRY=0
while [ $# -gt 0 ]; do
  case "$1" in
    --scope) SCOPE="${2:-}"; shift 2 ;;
    --target) TARGET="${2:-}"; shift 2 ;;
    --dry-run) DRY=1; shift ;;
    -h|--help) echo "Usage: uninstall.sh [--scope project|personal] [--target SKILLS_DIR] [--dry-run]"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done
if [ -z "$TARGET" ]; then
  case "$SCOPE" in
    project) TARGET="$PWD/.claude/skills" ;;
    personal) [ -n "${HOME:-}" ] || { echo "HOME not set" >&2; exit 1; }; TARGET="$HOME/.claude/skills" ;;
    *) echo "invalid --scope" >&2; exit 2 ;;
  esac
fi
if command -v sha256sum >/dev/null 2>&1; then H() { sha256sum "$1" | cut -d' ' -f1; }
else H() { shasum -a 256 "$1" | cut -d' ' -f1; }; fi
MAN="$TARGET/.ultra-optimizer-manifest.tsv"
[ -f "$MAN" ] || { echo "No installer manifest at $MAN; nothing removed."; exit 0; }
REM=0; KEPT=(); MISS=0
while IFS=$'\t' read -r h f; do
  [ -n "$f" ] || continue
  p="$TARGET/$f"
  if [ ! -f "$p" ]; then MISS=$((MISS+1)); continue; fi
  if [ "$(H "$p")" = "$h" ]; then
    if [ "$DRY" = 1 ]; then echo "[dry-run] remove $f"; else rm -f "$p"; fi; REM=$((REM+1))
  else KEPT+=("$f"); fi
done < "$MAN"
if [ "$DRY" = 0 ]; then
  for n in race optimize ping-optimize server-optimize; do [ -d "$TARGET/$n" ] && find "$TARGET/$n" -depth -type d -empty -delete 2>/dev/null; done
  [ "${#KEPT[@]}" -eq 0 ] && rm -f "$MAN"
fi
echo "Removed files: $REM (already missing: $MISS)"
echo "Kept (modified since install): ${KEPT[*]:-none}"
echo "Backups under $TARGET/.ultra-optimizer-backups are left in place."
exit 0
