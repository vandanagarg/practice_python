# Data Engineering Test

This directory contains a test for data engineering candidates at [xyz](https://www.xyz..com).

The inspiration for this test comes from real-world experience working on originator data sets. 
The task is to extract data from a a poorly formatted TSV file (api-response.tsv) and load it into a database table.

### Instructions

Your task is to write a simple script to get the values from (api-response.tsv) and load them into a MySQL database.
The resulting database should have the following properties:

* A primary index exists
* Each database row contains as much data from the TSV as possible
* TSV reserved characters (e.g. `\t`, `\r`, `\n`) should be removed
* All fields are UTF-8 encoded (`api-response.tsv` is UTF-16LE encoded)
* Fields do have a reasonable data-type 

The script should be written in Python and with any tools the candidate is familiar with. The solution does *not*
need to be generic enough to apply to similar issues in other files; your algorithm can be designed specifically for this
data set. Extra points are awarded for resource-efficient and scalable solutions.

To take the test, please complete the following steps:

1. Write a python script to extract, transform and load the data from api-response.tsv into a MySQL database, adhering the guidelines in the previous section.
2. Provide a SQL script to create and insert the data into a MySQL database (Dump after the script was run)
3. Provide a brief documentation about limitations/constraints of the ETL script 
4. Email an archive to [abc@xyz.com](mailto:abc@xyz.com)
