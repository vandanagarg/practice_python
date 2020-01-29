# Data Engineering Solution Guide

##TECH STACK
* Python IDE - Pycharm
* MySQL Server

## HOW TO RUN
* Attachment includes 3 files namely:  `run.py`, `csv_reader.py` and `database_adapter.py` in folder `src`.
* MySQL configuration can be found under class `DatabaseAdapter` in `database_adapter.py` script.
* Post this we must execute script `run.py` with the input file `cleaned_api_response.tsv`.

## SCOPE OF IMPROVEMENT
* I had to clean up a few anomalies in file manually, since it required a lot of extra efforts to optimize the code further ; which unfortunately I was not able to take care in the code at this stage.
* Due to limited time I was not able to make Unit Test Cases for the script; which are good to include from a testing point of view.
* For now I have just used a simple mysql connector in order to connect with MySQL database. This can be surely optimized using some specific ORM for the ease of development for other developers.

 