-- Copies transcript data from CSV. Delimiter is  | since it is uncomoonly used by users
-- CSV is needed because transcript text is rather large
-- Requires to be a SUPERUSER in order to use the COPY query
-- Please update the path to where you have the file stored
-- By Thomas Orth. Reviewed by Matthew Van Soelen and Justin Pabon
COPY transcripts(title, text_file_path, audio_file_path, summary, text_content)
FROM '/home/lion/stage-v-group-1/data/joel/csv/insert_data_transcript.csv' DELIMITER '|' CSV HEADER;