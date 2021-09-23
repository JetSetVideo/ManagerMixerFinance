### Manager Scraper 4 Finance


A python web application to manage the extraction and storage of all Financial data available.
The software is written mainly in Python and uses popular librairies to create a web interface that master a scrapper engine which store the informations.
It scraps from a broad list of sources (data providers, stock exchanges, etc.) in the web, gathers them to be stored in a PostgreSQL database.
The manager shows a live visualisation of the state of the PostgreSQL database.

This project is a mix various Python projects found on Github. We link them to build a web interface that automate the mecanics of importing all captured data related to financial systems available on the web.

## Basic Usage
Visualise the "Big Picture" by looking at the live aggregation of all financial values stored in the database.
Check is all the channels are opened and their informations up to date.
Manage the sources


# Table of Contents:



## Structure:
Language: Python3.9
UserInterface: Django
Webscraper: Beautifulsoup
database: PostgreSQL

## Installation: 
**Note:** MS4F requires Python 3.9+

Cryptofeed can be installed from PyPi. (It's recommended that you install in a virtual environment of your choosing).

    pip install cryptofeed

Cryptofeed has optional dependencies, depending on the backends used. You can install them individually, or all at once. To install Cryptofeed along with all its optional dependencies in one bundle:

    pip install cryptofeed[all]

If you wish to clone the repository and install from source, run this command from the root of the cloned repository

    python setup.py install

Alternatively, you can install in 'edit' mode (also called development mode):

    python setup.py develop

See more options, explanations and Pipenv usage in [INSTALL.md](https://github.com/MaxWayne/ScraperWeb/blob/master/INSTALL.md).

## To Do List:
- Establish a full list of financial assets available 

## Future works:
Get Newsletters

### RestAPI:
To be implemented.

### Sources:

## GitHub Projects:
  - https://github.com/je-suis-tm/web-scraping
  - https://github.com/bmoscon/cryptofeed
  - https://github.com/JerBouma/FinanceDatabase
  - https://github.com/ckz8780/market-toolkit
  - https://github.com/kootenpv/yagmail
  
 # Contributing:
 Do not hesitate, leave a like, a feedback, a star, a follow, some money or even a contribution!
 This work needs contributors, every help will be welcomed. :)
