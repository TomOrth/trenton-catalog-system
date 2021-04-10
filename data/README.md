# Data instructions

The general format is each folder is for one transcript.

Each folder will have:
* 2 .txt files - `raw.txt` that holds the raw text file data, second is `data.txt` that contains the meta data related to the transcripts
* A .pdf file that is the original transcript file
* A `csv` folder that holds the prepared csv files for insertion via the COPY command

Since the transcripts are big, there is a need to format the data into the CSV files. The CSV header columns match the SQL schema columns. Each are separated by a pipe (|) since it not commonly used in the english language.

# Creating new transcript copy files
1. Prepare a new folder using the Folder structure specified above.
2. In prepare.py, replace all the variables with the correct information
3. For locations, keywords, and participants, update the lists in the dataframe calls
4. Execute the script, doing `python3 prepare.py <path to raw.txt file>`
5. Move the CSV into the appropriate directory under the transcript folder
