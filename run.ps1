cls
Write-Host "Executing"
# mamba env create -f environment.yml --prefix .venv
ruff check src/*.py