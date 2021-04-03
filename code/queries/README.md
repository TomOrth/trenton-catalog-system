# Queries

In order to setup the tables and views, please checkout and run `setup.sql`.

General query structure:

* copy - All queries using COPY
* delete - All queries for deletion
* filtering - All queries for filtering. Two subfolders:
    * bookmarks_filtering: Queries for filtering bookmarked transcripts
    * transcript_filtering: Queries for filtering general transcripts
* insert - All queries for inserting into the tables
* select - All queries for selecting entries. A decent number of these are for debugging
* update - All queries for updating entries

NOTE: Alot of these queries are demonstrative. If you want them to work properly within your database setup and snapshot, you will need to update the ids that are being referenced.
