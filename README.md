# Manager Mixer Finance:
![MMF Logo](\resources\ManagerMinerFinance_Logo1.ai)
<img src="https://github.com/MaxWayne/ManagerMixerFinance/blob/master/resources/ManagerMinerFinance.ai" />

## The Goal:
To create a Docker image of a fully integrated server with a user interface UI to manage the scrapping and storage of up-to-date financial informations available on the internet.

### Definition:
A python web application to manage the extraction and storage of all Financial data available on the web.
The software is written mainly in Python and uses popular librairies to create a web interface that master a scrapper engine which store the informations.
It scraps from a broad list of sources (data providers, stock exchanges, etc.) in the web, gathers them to be stored in a PostgreSQL database.
The manager shows a live visualisation of the state of the PostgreSQL database.

This project is a mix various Python projects found on Github. We link them to build a web interface that automate the mecanics of importing all captured data related to financial systems available on the web.

### Basic Usage:
Visualise the "Big Picture" by looking at the live aggregation of all financial values stored in the database.
Check is all the channels are opened and their informations up to date.
Manage the sources

----

# Table of Contents:

## Tools:
<ul>
<li>Operating System: Ubuntu</li>
<li>Docker: </li>
<li>Language: Python3.9</li>
<li>UserInterface: Django3.2</li>
<li>Webscraper Library: Scrapy</li>
<li>database: PostgreSQL</li>
</ul>

## Data Structure:
Json file

## Application Structure:
### Frontend:
JavaScrip (TypeScrip)
Django 3.2

### API:

### Backend:
Python 3.9
PostgreSQL
Redis
container (kubernetes)
Tor

## Installation: 

See more options, explanations and Pipenv usage in [INSTALL.md](https://github.com/MaxWayne/ManagerMixerFinance/blob/master/resources/INSTALL.md).

----

## To Do List:
- Establish a full list of financial assets available 
<ol>
<li> Check if the source is available and up-to-date</li>
<li> Scrap the raw data</li>
<li> Clean the data and integrate them in the database</li>
</ol>
### Future works:
<ul>
<li>a web interface</li>
<li>serializers</li>
<li>get Newsletters</li>
</ul>

### RestAPI:
To be implemented.

## Sources:

### GitHub Projects:
  - https://github.com/je-suis-tm/web-scraping
  - https://github.com/bmoscon/cryptofeed
  - https://github.com/JerBouma/FinanceDatabase
  - https://github.com/ckz8780/market-toolkit
  - https://github.com/kootenpv/yagmail
  - https://github.com/mcdallas/wallstreet
  - https://github.com/JerBouma/FundamentalAnalysis
  
## Contributing:
 Do not hesitate, leave a like, a feedback, a star, a follow, some money or even a contribution!
 This work needs contributors, every help will be welcomed. :)

# Contact Us:
For any questions left unaswered, please feel free to contact us:
<ol>
<li> at http://www.hadrian-advisors.com/ </li>
<li> directly through GitHub @MaxWayne</li>
<li> or by sending us an email at: maximilien.pelletier@gmail.com</li>
</ol>
