# :rocket: DEPLOY REQUIREMENTS

**Deploy requirements for IH-IT software**

---
## :bust_in_silhouette: Process Name

    - SICMA_Operational (sicmaPOC)

---
## :page_facing_up: App Template

    - Python-task (Cron triggered)

---
## :green_book: Playbook name

    - Deploy SICMA_Operational (sicmaPOC)

---
## :computer: System

    - Linux

---
## :earth_americas: Environment

    - Dev
    - Prod

---
## :octocat: Github url

    - git@github.com:IHCantabria/SICMA.Process.OperationalController

---
## :floppy_disk: Distribution

    - Main
    - Tag

---
## :snake: Python set-up

* Create virtual env
  * :warning: Python version `3.6.12`
```bash
python -m venv env --clear
source /var/www/sicmaPOC/env/bin/activate
```

* Install python requirements
```bash
python -m pip install --upgrade pip
pip install pytest
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
```
* Set-up config file `operational_controller/config.py`
  * Set-up environment `dev` or `prod` 
  * Set-up log path

```python 
# file-example: operational_controller/config.py
ENV = "dev"
LOG_PATH = "/dat/log/sicmaPOC/"
```

* Run tests (if you want!)
```bash
pytest
```

---
## :hourglass: Cron set-up (5 tasks)
* Trigger operational jobs for each refinery `hourly`
```bash
PYTHON_PATH=/var/www/sicmaPOC/env/bin/python
CODE_CURRENT=/var/www/sicmaPOC

# python-binary python-file python-fuction refineryId
# Cron task 1 (Run Algeciras)
cd $CODE_CURRENT/ &&  $PYTHON_PATH main.py run_operational_job 1

# Cron task 2 (Run Huelva)
cd $CODE_CURRENT/ &&  $PYTHON_PATH main.py run_operational_job 2

# Cron task 3 (Run Tenerife)
cd $CODE_CURRENT/ &&  $PYTHON_PATH main.py run_operational_job 3
```

* Trigger operational clean-up of old jobs
```bash
# python-binary python-file python-fuction numberOfDays
# Cron task 4 (clean old operational jobs)
cd $CODE_CURRENT/ &&  $PYTHON_PATH main.py clean_old_jobs 1

# python-binary python-file python-fuction
# Cron task 4 (clean unreg operational jobs)
cd $CODE_CURRENT/ &&  $PYTHON_PATH main.py clean_unregistered_jobs
```

---
## :calling: Other services, apis or external packages called
  * :package: SICMA.Api
  * :package: SICMA.Apiprocess
  * :package: datahub.client

---
## :incoming_envelope: Contact us
* :snake: For code-development issues contact :man_technologist: [German Aragon](https://ihcantabria.com/en/directorio-personal/investigador/german-aragon/) @ :office: [IHCantabria](https://github.com/IHCantabria)

* :key: For system administration issues contact :man_technologist: [David del Prado](https://ihcantabria.com/en/directorio-personal/tecnologo/david-del-prado-secadas/) and :woman_technologist: [Gloria Zamora](https://ihcantabria.com/en/directorio-personal/tecnologo/gloria-zamora/) @ :office: [IHCantabria](https://github.com/IHCantabria)

---
## :copyright: Credits
*  Developed by [IHCantabria](https://github.com/IHCantabria) in the Framework of [SICMA](https://sicma.ihcantabria.es/en/).

* This development is part of the project *[SICMA - "Development of a system for the prevention and response to marine and air pollution by Hazardous Noxious Substances" [RTC-2017-6642-2, 2019-2021]](https://sicma.ihcantabria.es/en/).*

* A project in parthnership with [CEPSA](https://www.cepsa.com/en) and supported by [Spanish Ministry of Science and Innovation](https://www.ciencia.gob.es/portal/site/MICINN?lang_choosen=en) and cofinanced by [European Regional Development Fund](https://ec.europa.eu/regional_policy/en/funding/erdf/).


