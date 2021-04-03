# Data instructions

The general format is each folder is for one transcript.

Each folder will have:
* A .txt file that is the raw text for the transcript
* A .pdf file that is the original transcript file
* A .mp3 file that is the audio of the transcripted interview
* A `csv` filder that holds the prepared csv files for insertion via the COPY command

Since the transcripts are big, there is a need to format the data.

Each transcript will be prepared using the `prepare.py` file. The transcripts will be moved into the `csv` folder for that respective transcript. The `copy` sql files will then be executed in order to insert the data into the tables.

The catch is that since the IDs are SERIAL (auto incrementing), we cannot just use any old id for the initial database insertion. It was noted that inserting an explicit ID causes issues in [this stackoverflow post](https://stackoverflow.com/questions/9108833/postgres-autoincrement-not-updated-on-explicit-id-inserts). Therefore, you have to inspect the table rows to find the ids and then manually insert the proper relationships into their respective tables.

The current plan is to populate the database with 3 transcripts. 2 will be inserted during initial setup. The 3rd will be inserted using the application system. If an issue arises with creating the upload page, the 3rd will be added via the `copy` sql files.