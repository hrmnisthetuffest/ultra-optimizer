#!/usr/bin/env bash
# Ultra Optimizer installer (Linux/macOS). Installs the `race` and `optimize` skills.
# Never touches unrelated skills. Never needs admin. Idempotent.
set -u
usage() { cat <<U
Usage: install.sh [--scope project|personal] [--target SKILLS_DIR] [--only race|optimize]
                  [--yes] [--dry-run] [--force-backup]
  --scope project   (default) install into ./.claude/skills
  --scope personal  install into \$HOME/.claude/skills (personal skills take precedence over project skills)
  --target DIR      explicit skills directory (overrides --scope)
  --yes             allow replacing an existing race/optimize directory (a timestamped backup is always made)
  --dry-run         print what would happen, change nothing
  --force-backup    back up and reinstall even identical existing installs
U
}
SCOPE=project; TARGET=""; ONLY=""; YES=0; DRY=0; FB=0
while [ $# -gt 0 ]; do
  case "$1" in
    --scope) SCOPE="${2:-}"; shift 2 ;;
    --target) TARGET="${2:-}"; shift 2 ;;
    --only) ONLY="${2:-}"; shift 2 ;;
    --yes) YES=1; shift ;;
    --dry-run) DRY=1; shift ;;
    --force-backup) FB=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
done
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$HERE/../.claude/skills"
[ -d "$SRC/race" ] && [ -d "$SRC/optimize" ] || { echo "source skills not found at: $SRC" >&2; exit 1; }
if [ -z "$TARGET" ]; then
  case "$SCOPE" in
    project) TARGET="$PWD/.claude/skills" ;;
    personal) [ -n "${HOME:-}" ] || { echo "HOME not set" >&2; exit 1; }; TARGET="$HOME/.claude/skills" ;;
    *) echo "invalid --scope: $SCOPE" >&2; exit 2 ;;
  esac
fi
case "$ONLY" in ""|race|optimize) ;; *) echo "invalid --only: $ONLY" >&2; exit 2 ;; esac
NAMES="race optimize"; [ -n "$ONLY" ] && NAMES="$ONLY"
if command -v sha256sum >/dev/null 2>&1; then H() { sha256sum "$1" | cut -d' ' -f1; }
elif command -v shasum >/dev/null 2>&1; then H() { shasum -a 256 "$1" | cut -d' ' -f1; }
else echo "need sha256sum or shasum" >&2; exit 1; fi
MAN="$TARGET/.ultra-optimizer-manifest.tsv"
TS="$(date +%Y%m%d-%H%M%S)"
BK="$TARGET/.ultra-optimizer-backups/$TS"
INST=(); SKIP=(); BACKED=()
dry() { echo "[dry-run] $*"; }
list_files() { ( cd "$1" && find . -type f ! -name '*.pyc' ! -path '*/__pycache__/*' | sort ); }
same_tree() {
  local a="$1" b="$2" f ta tb
  [ -d "$b" ] || return 1
  ta="$(list_files "$a")"; tb="$(list_files "$b")"
  [ "$ta" = "$tb" ] || return 1
  while IFS= read -r f; do [ -n "$f" ] && { cmp -s "$a/$f" "$b/$f" || return 1; }; done <<< "$ta"
  return 0
}
for n in $NAMES; do
  s="$SRC/$n"; d="$TARGET/$n"
  if [ -e "$d" ]; then
    if [ "$FB" = 0 ] && same_tree "$s" "$d"; then SKIP+=("$n (already up to date)"); continue; fi
    if [ "$YES" = 0 ]; then
      if [ "$DRY" = 1 ]; then dry "would need --yes to replace existing $d"; SKIP+=("$n (needs --yes)"); continue
      elif [ -t 0 ]; then
        printf 'Existing "%s" found at %s. Back it up and replace? [y/N] ' "$n" "$d"; read -r ans
        case "$ans" in y|Y|yes) ;; *) SKIP+=("$n (existing kept; not confirmed)"); continue ;; esac
      else SKIP+=("$n (existing kept; rerun with --yes)"); continue; fi
    fi
    if [ "$DRY" = 1 ]; then dry "backup $d -> $BK/$n"; dry "replace $d"
    else mkdir -p "$BK" && cp -a "$d" "$BK/$n" || { echo "backup failed" >&2; exit 1; }; rm -r "$d"; fi
    BACKED+=("$d -> $BK/$n")
  fi
  if [ "$DRY" = 1 ]; then dry "install $s -> $d"
  else
    mkdir -p "$TARGET" && cp -a "$s" "$d" || { echo "copy failed" >&2; exit 1; }
    find "$d" -name '__pycache__' -type d -prune -exec rm -r {} + 2>/dev/null
    find "$d" -name '*.pyc' -type f -delete 2>/dev/null
  fi
  INST+=("$n")
done
if [ "$DRY" = 0 ] && [ "${#INST[@]}" -gt 0 ]; then
  touch "$MAN"
  for n in "${INST[@]}"; do
    grep -v -F "	$n/" "$MAN" > "$MAN.tmp"; mv "$MAN.tmp" "$MAN"
    ( cd "$TARGET" && find "$n" -type f | sort ) | while IFS= read -r f; do printf '%s\t%s\n' "$(H "$TARGET/$f")" "$f" >> "$MAN"; done
  done
fi
echo "Target: $TARGET"
echo "Installed: ${INST[*]:-none}"
echo "Skipped: ${SKIP[*]:-none}"
echo "Backed up: ${BACKED[*]:-none}"
[ "$DRY" = 1 ] && echo "(dry run: nothing changed)"
exit 0
