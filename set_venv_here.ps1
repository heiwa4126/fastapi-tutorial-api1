Set-Location $PSScriptRoot
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install -U pip
pip install -U -r requirements.txt
