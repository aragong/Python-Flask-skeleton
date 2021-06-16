
# PACKAGE_NAME
Package short description.

![GitHub top language](https://img.shields.io/github/languages/top/aragong/Python-skeleton?style=plastic)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/aragong/Python-skeleton?label=latest%20tag&style=plastic)
![GitHub repo size](https://img.shields.io/github/repo-size/aragong/Python-skeleton?style=plastic)
![GitHub](https://img.shields.io/github/license/aragong/Python-skeleton?style=plastic)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/aragong/Python-skeleton/main.svg)](https://results.pre-commit.ci/latest/github/aragong/Python-skeleton/main)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/aragong/Python-skeleton/CI?label=CI%20build&style=plastic)
[![codecov](https://codecov.io/gh/aragong/Python-skeleton/branch/main/graph/badge.svg)](https://codecov.io/gh/aragong/Python-skeleton)

---
## :zap: Main methods
All main methods are located in the file main.py:
* `main_method_1(arguments)` - [Short description]:

```python
# Execute whit a-arguments whatever it makes
main_method_1_a(arg_1=1, arg_2='aaa')

# Execute whit b-arguments whatever it makes
main_method_1_b(arg_1=2, arg_2='bbb')
```
* `main_method_2(arguments)` - [Short description]:
```python
# Delete jobs older than 2 days
clean_old_jobs(days=2)
```

## :package: Package structure
````
(tree /f)
SICMA.Process.OperationalController
│   .gitignore
│   authentifications.key
│   CHANGELOG.md
│   DEPLOY_REQUIREMENTS.md
│   environment.yml
│   main.py
│   README.md
│   requirements.txt
|
├───logs
|
├───operational_controller
│   │   config.py
│   │   controller.py
│   │   __init__.py
│   │
│   └───utils
│           data_repository.py
│           logger.py
│           __init__.py
|
└───tests
    │   __init__.py
    │
    ├───integration
    │       test_cases.py
    │       test_data_repository.py
    │       __init__.py
    |
    └───unit
            test_config.py
            test_controller.py
            __init__.py

````
## :house: Local installation

* Using venv + pip:
```bash
# Create virtual env
python -m venv env --clear

# Activate virtual env
source 'venv_path'

# Install dependencies
python -m pip install -r requirements.txt

# Install datahubclient github package with --no-deps option
python -m pip install git+git://github.com/IHCantabria/datahub.client.git@v0.8.6#egg=datahubClient --no-deps
```

* Using conda + pip:
```bash
# Create conda env and install python libreries
conda env create --file environment.yml --name env

# Activate virtual env
conda activate env

# Install package from github with --no-deps option
pip install git+git://github.com/IHCantabria/datahub.client.git@v0.8.6#egg=datahubClient --no-deps

```
---
## :recycle: Testing
* To run tests:
```bash
# Unzip tests/fake_results/fake_results.zip in the same directory (fake_inputs/) and run pytest
unzip -j tests/fake_results/fake_test.zip -d tests/fake_results/

# Run pytests from console
pytest
```
---

## :rocket: Package deployment
Check [DEPLOY_REQUIREMENTS.md](https://github.com/IHCantabria/SICMA.Process.OperationalController/blob/main/DEPLOY_REQUIREMENTS.md) for a full detailed explanation.

## :incoming_envelope: Contact us

:snake: For code-development issues contact :man_technologist: [German Aragon](https://ihcantabria.com/en/directorio-personal/investigador/german-aragon/) @ :office: [IHCantabria](https://github.com/IHCantabria)


## :copyright: Credits

*  Developed by [IHCantabria](https://github.com/IHCantabria) in the Framework of [SICMA](https://sicma.ihcantabria.es/en/).

* This development is part of the project *[SICMA - "Development of a system for the prevention and response to marine and air pollution by Hazardous Noxious Substances" [RTC-2017-6642-2, 2019-2021]](https://sicma.ihcantabria.es/en/).*

* A project in parthnership with [CEPSA](https://www.cepsa.com/en) and supported by [Spanish Ministry of Science and Innovation](https://www.ciencia.gob.es/portal/site/MICINN?lang_choosen=en) and cofinanced by [European Regional Development Fund](https://ec.europa.eu/regional_policy/en/funding/erdf/).
