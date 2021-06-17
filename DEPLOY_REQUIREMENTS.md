# :rocket: DEPLOY REQUIREMENTS

**Deploy requirements for IH-IT software**

---
## :bust_in_silhouette: Process Name

    - TESEO.Apiprocess

---
## :page_facing_up: App Template

    - Python-Flask API

---
## :green_book: Playbook name

    - TESEO.Apiprocess

---
## :computer: System

    - Linux

---
## :earth_americas: Environment

    - Dev
    - Prod

---
## :octocat: Github url

    - git@github.com:IHCantabria/TESEO.Apiprocess

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
## :calling: Other services, apis or external packages called
  * :package: TESEO binary (numerical model)

---
## :incoming_envelope: Contact us
* :snake: For code-development issues contact :man_technologist: [German Aragon](https://ihcantabria.com/en/directorio-personal/investigador/german-aragon/) @ :office: [IHCantabria](https://github.com/IHCantabria)

* :key: For system administration issues contact :man_technologist: [David del Prado](https://ihcantabria.com/en/directorio-personal/tecnologo/david-del-prado-secadas/) and :woman_technologist: [Gloria Zamora](https://ihcantabria.com/en/directorio-personal/tecnologo/gloria-zamora/) @ :office: [IHCantabria](https://github.com/IHCantabria)

---
## :copyright: Credits
Developed by :man_technologist: [German Aragon](https://ihcantabria.com/en/directorio-personal/investigador/german-aragon/) @ :office: [IHCantabria](https://github.com/IHCantabria).


