# DataProject django rest framework

Django Rest Framework version of the data project

## Technology used

* Backend:  Django

* Frontend: Html, CSS

* Database: PostgreSQL

## Prerequisites

1. Download dataset from [*here*](https://data.gov.in/resources/company-master-data-maharashtra-upto-28th-february-2019)

2. Download all the files in your local computer

3. Cd to the directory where the downloaded files are located

4. Install all the dependencies from requirements.txt file

## Get Started

1. Create role and database in postgres from create_db.sql

2. Run below command in terminal to create tables.

    ```python3
        python manage.py migrate
    ```

3. Run below command in terminal to load data from csv file.

    ```python3
        python manage.py dataloader data_gov_maharashtra.csv
    ```

4. Open any browser and go to (http://127.0.0.1:8000/)

5. Delete database and role in postgres using drop_db.sql.
