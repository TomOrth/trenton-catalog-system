SELECT * FROM keywords;
SELECT * FROM users;
SELECT * FROM locations;
SELECT * FROM participants;
SELECT transcript_id, audio_file_path, text_file_path, summary, title FROM transcripts;

SELECT * FROM participates;
SELECT * FROM mentions;
SELECT * FROM describes;
SELECT user_id, title FROM user_transcript_view;
SELECT title, keyword FROM keyword_transcript_view;
SELECT title, name FROM participant_transcript_view;
SELECT title, street_name FROM location_transcript_view;
SELECT title, keyword, street_name, name FROM full_transcript_view;