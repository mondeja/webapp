# Django + React webapp scaffold

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This basic webapp scaffold includes:

- Separation of backend and frontend code in two obvious folders: `backend` and `frontend`.
- Backend configuration by environment (`development`, `staging` and `production`) through YAML files.
- A backend folder to store all global functions separated by modules (`backend/lib`) added to system PATH at runtime.
- Basic Django configuration: `backend/main` for project configuration and an example app (`backend/app01`).
- Compilation with [Webpack](https://webpack.js.org/) from `frontend/src/js/` to `frontend/dist/js/`.
- Basic Webpack configuration for ES6 with Babel and React support.
- Versioning using [bump2version](https://github.com/c4urself/bump2version/) major, minor and patch increments.
- Linting using `black`, `flake8` and other hooks provided by [pre-commit](https://pre-commit.com/).

## Setup (Linux)

> Python3 with `virtualenv` installed and NodeJS with `npm` are required.

1. `python3 -m virtualenv venv`
2. `source venv/bin/activate`
3. `python3 -m pip install -r requirements.txt`
4. `pre-commit install`
5. `npm install`
6. `python manage.py migrate`

## Commands

- `npm run build`: Build frontend packages using Webpack.
- `npm run lint`: Lint all files using `pre-commit`.
- `npm run server`: Run server.
- `npm run version`: Increase patch version.
- `npm run watch`: Watch for changes in frontend files using Webpack.
