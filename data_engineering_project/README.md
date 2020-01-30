# Data Engineering Test

This directory contains an example for data engineering field.

The inspiration comes from real-world experience working on originator data sets. 
The task is to extract data from a poorly formatted TSV file (api-response.tsv) and load it into a database table.

### Instructions

We have to write a simple script using Python to get the values from (api-response.tsv) and load them into a MySQL database.
The resulting database should have the following properties:

* A primary index exists
* Each database row contains as much data from the TSV as possible.
* TSV reserved characters (e.g. `\t`, `\r`, `\n`) should be removed.
* All fields are UTF-8 encoded (`api-response.tsv` is UTF-16LE encoded).
* Fields do have a reasonable data-type .


###### At the end we must have following:

1. A python script to extract, transform and load the data from api-response.tsv into a MySQL database, adhering the guidelines in the previous section.
2. A SQL script to create and insert the data into a MySQL database (Dump after the script was run).
3. A brief documentation about limitations/constraints of the ETL script .

