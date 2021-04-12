# CSC 315 Project Group 1 Transcript Catalog

This repository contains documents, database design, and code related to Group 1's implementation to house the transcripts from the trentoniana. As we progress
more in the stages, more of these readme sections will be filled out.

In addition to our README, please visit our wiki for more information.

# Technology

The database used will be postgres. The back-end server will be made with Python, Flask, and Psycopg2. The front-end will use HTML, CSS, and JavaScript.

# Installation and Setup

We will put steps to setup the project as it is developed

# Database Design

Please see [this document](https://github.com/TCNJ-degoodj/stage-iv-group-1/blob/main/docs/Database%20Model%20Updated%20-%20Stage%20IV.pdf) for our database design that has an EER diagram and relational schema.

Please see [this document](https://github.com/TCNJ-degoodj/stage-iv-group-1/blob/main/docs/Stage%20IV.pdf) to see our design (Normalization, Views and a set of queries for our transactions).

# Repo structure

* `code` - The code for the project. Contains two folders, `app` for the application code and `queries` for the database interactions and setup. See `queries/README.md` for info about the SQL queries.

* `docs` - All the documents created during the projects for the different stages.

* `data` - All the prepared transcripts we used for the initial database. See `data/README.md` for more information about the data files.

* `terminal_session_files` - Terminal Session Files to show queries running

# Database Setup
NOTE: This assumes that none of the tables or views currently exist or have prepopulated data in it.

1. In terminal, cd to code/queries
2. Update the CSV file paths to match your file system. The COPY command requires an absolute path to the CSVs in order to work.
3. Ensure that the shell file can be executed from the terminal. Run `chmod +x setup.sh`
4. Run `./setup.sh`

Please see `queries/README.md` for more information

# Dependency Installation
1. In terminal, cd to `code/app`
2. Run `pip3 install -r requirements.txt`
3. If you wish to prepare other transcript data csv files, you will also need to do `pip3 install pandas`

# Start Application
1. In terminal, cd to `code/app`
2. Ensure the shell file can be executed by doing `chmod +x start.sh`
3. Run `./start.sh`

# Contributing 

This section is for CSC 315 students who may continue to work on this after the original developers (if this project remains private) 
or for general developers who want to contribute (if this project is open sourced after the Spring 2021 semester).

Once the project is at a stable point, this section will contain that information
