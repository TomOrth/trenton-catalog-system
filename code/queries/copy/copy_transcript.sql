COPY transcripts(title, text_file_path, audio_file_path, summary, text_content)
FROM '/home/lion/stage-v-group-1/data/joel/csv/insert_data_transcript.csv' DELIMITER '|' CSV HEADER;