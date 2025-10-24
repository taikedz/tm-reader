set -euo pipefail

HEREDIR="$(dirname "$(realpath "$0")")"

. "$HEREDIR/py3.venv/bin/activate"

python3 "$HEREDIR/tm-reader.py" "$@"
