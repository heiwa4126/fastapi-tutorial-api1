#!/bin/sh
cd $(dirname $0)
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
pip install -U -r requirements.txt

echo "Run the command below:"
echo ". .venv/bin/activate"
