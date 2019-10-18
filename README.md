# Scraping website

The aim of this repository is to get an email each time there is a new project on 'TheFouleFactory' website.
Therefore, each day:
* we connect to the website. 
* we scrap the website, more especially the projects index of the website.
* we analyse the content of the projects index.
* we send an email if there is a new project available in the projects index.

The source code can be updated to scrap other websites. The source code has been configured to write logs inside a file `logs\file.log`

## Getting Started

### Prerequisites

* Python 3.6 (with Anaconda to get project environment).
* OS Windows if using the bat script.
* Gmail account if the project is used in 'production' mode.

### Installing

* Create the environment for the project and install the requirements: 
```
conda create --name py36_scraping_env python=3.6
conda activate py36_scraping_env
pip install -r requirements.txt
```
* Copy file `config.example.ini` and name it `config.ini`. Update every information between `<info>`.

* You can skip this part if the file `config.ini` is placed next to `config.example.ini`. Otherwise, you need to define the environment variable `WEBSITE_SCRAPING_CONFIG=<relative_path_to_config.ini>\config.ini`.

#### Mode debug
* In `config.ini`, put `MODE = debug`.

* In the anaconda terminal, tap:
```
python -m smtpd -c DebuggingServer -n localhost:1025
```

* You can now execute `src/app.py`.

#### Mode production
* In `config.ini`, put `MODE = production`.

* You will need to download the file `credentials.json` (put it next to `config.ini`).
Then, when the program `src/app.py` will be executed, it will create automatically the file `token.pickle`.

To do that, configure a gmail account as it is described here: 
> https://developers.google.com/gmail/api/quickstart/python

* You can now execute `src/app.py`.

#### Scheduler managament
To execute daily and automatically this script, we can use Windows Task Scheduler. In order to do that, we need:

* Copy file `src\web_scraping.example.bat` and name it `src\web_scraping.bat`. Update every information between `<info>`.

* Follow the instructions to configure the Windows Task Scheduler:
> https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279

## Running the tests

* You can run the tests via pytest. Configure pytest to point the `tests` folder out. 

## Acknowledgments

* Python Web Scraping, Second Edition from Katharine Jarmul, Richard Lawson
* https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279
* https://developers.google.com/gmail/api/quickstart/python
* https://realpython.com/python-send-email/

