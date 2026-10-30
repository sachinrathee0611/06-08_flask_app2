# CI Demo App

A tiny Flask API for practicing Continuous Integration with GitHub Actions.

## What it does

- `/` returns basic app info
- `/health` returns health status
- `/add`, `/subtract`, `/multiply`, `/divide` perform math operations

## Run locally 

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
flask --app app run
```

Then open `http://127.0.0.1:5000/`.

## Run tests

```bash
pytest
```

## Run lint

```bash
flake8 .
```

## Files for CI labs

- `.github/workflows/simple-ci.yml`
- `.github/workflows/medium-ci.yml`
- `.github/workflows/advanced-ci.yml`

Use the same repo and switch between workflows during the class.
