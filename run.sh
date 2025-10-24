set -euo pipefail

HEREDIR="$(dirname "$(realpath "$0")")"
VDIR="$HEREDIR/py3.venv"

activate() {
. "$VDIR/bin/activate"
}

if [[ ! -f "$VDIR/bin/activate" ]]; then
    python3 -m venv "$VDIR"
    (
        activate
        pip install -r requirements.txt
    )
fi

activate

python3 "$HEREDIR/tm-reader.py" "$@"
