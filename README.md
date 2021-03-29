# SICMA.Process.OperationalController
Python package designed by [IHCantabria](https://ihcantabria.com/en/) to trigger spill simulations in operational mode.

## :zap: Main methods
All main methods are located in the file main.py:
* `run_operational_job()` - Launch simulation in the refenery selected:
```python
# Run job in Algeciras refinery
run_operational_job(refinery_id=1)

# Run job in Huelva refinery
run_operational_job(refinery_id=2)

# Run job in Tenerife refinery
run_operational_job(refinery_id=3)
```
* `clean_old_jobs(days)` - Delete all the jobs simulated before a selected number of days.
```python
# Delete jobs older than 2 days 
clean_old_jobs(days=2)
```

## :package: Package structure
````
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

## :rocket: Package deployment
Check [DEPLOY_REQUIREMENTS.md](https://github.com/IHCantabria/SICMA.Process.OperationalController/blob/main/DEPLOY_REQUIREMENTS.md) for a full detailed explanation.

## :incoming_envelope: Contact us

:snake: For code-development issues contact :man_technologist: [German Aragon](https://ihcantabria.com/en/directorio-personal/investigador/german-aragon/) @ :office: [IHCantabria](https://github.com/IHCantabria)

:key: For system administration issues contact :man_technologist: [David del Prado](https://ihcantabria.com/en/directorio-personal/tecnologo/david-del-prado-secadas/) and :woman_technologist: [Gloria Zamora](https://ihcantabria.com/en/directorio-personal/tecnologo/gloria-zamora/) @ :office: [IHCantabria](https://github.com/IHCantabria)

## :copyright: Credits

*  Developed by [IHCantabria](https://github.com/IHCantabria) in the Framework of [SICMA](https://sicma.ihcantabria.es/en/).

* This development is part of the project *[SICMA - "Development of a system for the prevention and response to marine and air pollution by Hazardous Noxious Substances" [RTC-2017-6642-2, 2019-2021]](https://sicma.ihcantabria.es/en/).*

* A project in parthnership with [CEPSA](https://www.cepsa.com/en) and supported by [Spanish Ministry of Science and Innovation](https://www.ciencia.gob.es/portal/site/MICINN?lang_choosen=en) and cofinanced by [European Regional Development Fund](https://ec.europa.eu/regional_policy/en/funding/erdf/).

