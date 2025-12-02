from flask import Flask, jsonify, abort
from pathlib import Path
import os
import yaml

app = Flask(__name__)

# Base directory inside the container where YAML files are stored
BASE_DIR = Path(os.getenv('BASE_DIR', '/'))


def _safe_resolve_yaml(path_fragment: str) -> Path:
    """
    Resolves the YAML path safely within BASE_DIR in order to avoid directory traversal.
    """
    candidate = (BASE_DIR / path_fragment).resolve()

    try:
        candidate.relative_to(BASE_DIR)
    except ValueError:
        abort(400, description='Invalid path')

    if not candidate.exists() or not candidate.is_file():
        abort(404, description='YAML file not found')

    return candidate


@app.route('/parse/<path:yaml_path>', methods=['GET'])
def parse_yaml(yaml_path: str):
    """
    Parses a YAML file and returns its contents as JSON.
    """
    yaml_file = _safe_resolve_yaml(yaml_path)

    try:
        with yaml_file.open(encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        abort(400, description=f'Invalid YAML: {exc}')

    return jsonify(data)


if __name__ == '__main__':
    port = int(os.getenv('PORT', '8080'))
    app.run(host='0.0.0.0', port=port)