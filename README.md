# CSC 315 Project Group 1 Transcript Catalog

This repository contains documents, database design, and code related to Group 1's implementation to house the transcripts from the trentoniana. Documents are listed on this repository's wiki page under the wiki tab.

In addition to our README, please visit our wiki for more information.

Our group proposal is [here](https://github.com/TomOrth/trenton-catalog-system/blob/main/docs/Proposal_stage3.pdf)

# Technology

The database used will be postgres. The back-end server will be made with Python, Flask, and Psycopg2. The front-end will use HTML, CSS, and JavaScript.

# Installation and Setup

Two main technologies need:

* Postgres - https://www.postgresql.org/docs/9.3/tutorial-install.html
* Python 3.8 - https://realpython.com/installing-python/

Please see other sections of this README for further setup

# Database Design

Please see [this document](https://github.com/TomOrth/trenton-catalog-system/blob/main/docs/Database%20Model%20Updated%20-%20Stage%20IV.pdf) for our database design that has an EER diagram and relational schema.

Please see [this document](https://github.com/TomOrth/trenton-catalog-system/blob/main/docs/Stage%20Va%20-%20Updated%20Design%20Doc.pdf) to see our design (Normalization, Views and a set of queries for our transactions).

# Repo structure

* `code` - The code for the project. Contains two folders, `app` for the application code and `queries` for the database interactions and setup. See `queries/README.md` for info about the SQL queries.

* `docs` - All the documents created during the projects for the different stages.

* `data` - All the prepared transcripts we used for the initial database. See `data/README.md` for more information about the data files.

* `terminal_session_files` - Terminal Session Files to show queries running

# Database Setup
NOTE: This assumes that none of the tables or views currently exist or have prepopulated data in it.

A few more notes: This setup script assumes you are running it on the TCNJ CSC 315 VM and have a database called lion setup with a lion database user. If these aren't made, set these up using the appropriate Postgres commands (`createdb lion` and `createuser -P lion` and enter the password lion). You will be prompted for the VMs or computer's password as the lion user is temporarily given superuser priviliges to allow for the copy command to work. This requires using sudo and accessing the postgres user.


1. In terminal (assuming your terminal current directory is the repository's folder), cd to `code/queries`
2. Update the CSV file paths in `setup.sql` to match your file system. The COPY command requires an absolute path to the CSVs in order to work.
3. Ensure that the shell file can be executed from the terminal. Run `chmod +x setup.sh`
4. Run `./setup.sh`


Please see `queries/README.md` for more information

# Dependency Installation
1. In terminal, cd to `code/app`
2. Run `pip3 install -r requirements.txt`
3. Next run `pip3 install -U Werkzeug==0.16.0`
4. If you wish to prepare other transcript data csv files, you will also need to do `pip3 install pandas`
5. If you have an issue starting the application by following the `Start Application` guidelines, run `sudo apt install python3-flask`. This issue happened on one group members VM but not on another so that is why this is not an earlier step.

# Start Application
NOTE: Before running. If you are not on the TCNJ VM for CSC 315, you must update/create a config.yaml that has `db`, `user`, `password` all set in it for the database user that reflects your database setup (Otherwise, use the file currently in this repository).
1. In terminal (assuming your terminal current directory is the repository's folder), cd to `code/app`
2. Ensure the shell file can be executed by doing `chmod +x start.sh`
3. Run `./start.sh`
4. If you have an issue starting the application and receive an error about the `flask` command not being found on line 1 of the shell script, run `sudo apt install python3-flask` and re-run the shell script. This issue happened on one group members VM but not on another so that is why this is not an earlier step.
5. Assuming steps 3 and 4 go well, then navigate in a web browser (we recommend using Google Chrome or Firefox), to localhost:5000 to view our web application. You will be greeted with a page that looks like this: ![image](https://user-images.githubusercontent.com/8887487/117052026-387aeb00-ace5-11eb-9cbd-ade072b2b1de.png)

# Contributing 

To contribute:
* Find an open issue
* Make a new branch for your Pull Request that branches off of `main`
* Push your code as you work
* Create the Pull Request then assign and tag a reviewer
