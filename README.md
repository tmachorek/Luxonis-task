# Luxonis-task

A interview task for the company Luxonis. The task comprises of creating scrapping tool that fetches titles and property images urls of first 500 listed items on the webpage 'http://sreality.cz',
saves them to PostgreSQL database and shows those scrapped ads on 'localhost:8080'.

The project is partioned into invidual Docker containers, one for Postgre db, one for Scrapy framework and last one for Flask web application but there is also an option to run the project natively.

## How to run 

### Docker container
1. Install the latest Docker distribution for your operating system
2. Clone the repositary and navigate to the repositaries folder
   ```sh
   $ git clone git@github.com:tmachorek/Luxonis-task.git && cd Luxonis-task
   ```
3. Run the following command (optionally use Docker desktop):
  ```sh
  $ docker-compose up
  ```
4. Navigate to http://127.0.0.1:8080 to see the scrapped ads.

### Natively
1. Install Python, ver. >= 3.11.4
2. Clone the repositary and navigate to the repositaries folder
   ```sh
   $ git clone git@github.com:tmachorek/Luxonis-task.git && cd Luxonis-task
   ```
4. Run the following command:
   ```sh
   $ python -m pip install --upgrade pip
   ```
5. Run the following command:
   ```sh
   $ cd Scrapping && pip install -r requirements.txt && cd .. && cd Web && pip install -r requirements.txt
   ```
6. Install PostgreSQL, ver. >= 15.3
7. On your prefred PostgreSQL db run the script `Db/create_tables.sql`
8. In `Scrapping/Sreality_scrapper/Sreality_scrapper/pipelines.py:create_connection` change your PostgreSQL access details to fit your database
9. In `Web/Initialize_web.py:index` change your PostgreSQL access details to fit your database
10. Run `main.py`
11. Navigate to http://127.0.0.1:8080 to see the scrapped ads.

## Possible improvements

By the nature of the tasks' description this task was fulfilled as functional developer demo via the easiest working means and could be improved by the following changes:
- **SQL query sanitation** - The INSERT queries that populate PostgreSQL database are not completely sanitised and hence could be security risk.
- **Documentation** - The code is missing any sort of comments, in dev env they should be included.
- **Docker compose vars** - Inclusion of enviromental variables for choice of Postgre db, password, ...
- **Docker volumes/containers cleanup** - As of this moment this implementation does not have automatic prunning of containers and or volumes.
- **Continuous Scrapy usage** - In current versio the Scrapy container is ran only once upon `docker-compose up` command so the feed of the newest listings on scrapped website is not continuos
  but as `robots.txt` do not allow Scrapy framework it could result in breach of it's company policies hence this may be the best approach for demo showing. 
