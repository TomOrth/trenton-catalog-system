# Queries

In order to setup the tables and views along with prepopulated data do the following:

1. cd into this folder
2. Update the CSV file paths to match your file system. The COPY command requires an absolute path to the CSVs in order to work.
3. Ensure that the shell file can be executed from the terminal. Run `chmod +x setup.sh`
4. Run `./setup.sh`

A few notes: This setup script assumes you are running it on the TCNJ CSC 315 VM and have a database called lion setup with a lion database user. If these aren't made, set these up using the appropriate Postgres commands. You will be prompted for the VMs password as the lion user temporarily will have superuser priviliges to allow for the copy command to work. This requires using sudo and accessing the postgres user.

The following queries are demonstrative. They will be incorporated into the application. Change the IDs and data in these files to match your intended action and database snapshot.
 
General query structure:

* copy - All queries using COPY
* delete - All queries for deletion
* filtering - All queries for filtering. Two subfolders:
    * bookmarks_filtering: Queries for filtering bookmarked transcripts
    * transcript_filtering: Queries for filtering general transcripts
* insert - All queries for inserting into the tables
* select - All queries for selecting entries. A decent number of these are for debugging
* update - All queries for updating entries
