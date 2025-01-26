set -xe

uv pip install -r dev_reqs.txt

uv run -m pytest