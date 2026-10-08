# Python API Autotests

A learning project: automated API tests in Python, written during a QA training course (2024). The tests run against the public training API `https://api.pokemonbattle.me/v2`.

## What's inside

- `py_test_pokemon/test_pokemon.py` — a script that exercises the API end to end: creates a pokemon, updates it, and adds it to a pokeball
- `tests/test_pokemon.py` — two `pytest` test cases:
  - `test_staus_code` — checks that `GET /trainers` returns HTTP 200
  - `test_of_response` — checks the trainer name in the response body

## Requirements

- Python 3.x
- `requests`, `pytest`

```bash
pip install requests pytest
```

## How to run

```bash
# run the demo script
python py_test_pokemon/test_pokemon.py

# run the pytest suite
pytest tests/
```

> Note: the scripts use a placeholder trainer token (`youre_token`). Replace it with your own token from the training API to run them for real.

## Status

Course exercise (2024). Written while learning API test automation with Python.
