-- Sets up all the tabls and views
-- Queries created as a group. File created by Thomas Orth. Reviewed by Matthew Van Soelen and Justin Pabon


-- Creates the transcripts table
-- Text_content is meant to be unique but since the UNIQUE constraint creates an index, it cannot store large amounts of text
CREATE TABLE transcripts (
  transcript_id SERIAL PRIMARY KEY,
  title text UNIQUE,
  summary text UNIQUE,
  audio_file_path text UNIQUE,
  text_file_path text UNIQUE,
  text_content text
);

-- Creates the users table
CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  email text UNIQUE,
  password_hash text UNIQUE,
  lflag int
);

-- Creates the participants table
CREATE TABLE participants (
  p_id SERIAL PRIMARY KEY,
  name text UNIQUE
);

-- Creates the locations table
CREATE TABLE locations (
  location_id SERIAL PRIMARY KEY,
  street_name text UNIQUE
);

-- Creates the keywords table
CREATE TABLE keywords (
  k_id SERIAL PRIMARY KEY,
  keyword text UNIQUE
);

-- Creates the bookmarks table
CREATE TABLE bookmarks (
  user_id int REFERENCES users,
  transcript_id int REFERENCES transcripts,
  PRIMARY KEY (user_id, transcript_id)
);

-- Creates the participates table
CREATE TABLE participates (
  p_id int REFERENCES participants,
  transcript_id int REFERENCES transcripts,
  PRIMARY KEY (p_id, transcript_id)
);

-- Creates the mentions table
CREATE TABLE mentions (
  location_id int REFERENCES locations,
  transcript_id int REFERENCES transcripts,
  PRIMARY KEY (location_id, transcript_id)
);

-- Creates the describes table
CREATE TABLE describes (
  k_id int REFERENCES keywords,
  transcript_id int REFERENCES transcripts,
  PRIMARY KEY (k_id, transcript_id)
);

-- Creates a view that joins participants and transcripts
-- Its a representation of the participates relationship
CREATE VIEW participant_transcript_view AS
   SELECT * FROM (SELECT participants.*, transcripts.* FROM participates
                  LEFT OUTER JOIN participants ON participants.p_id = participates.p_id
                  LEFT OUTER JOIN transcripts ON transcripts.transcript_id = participates.transcript_id) as PTV;
 
-- Creates a view that joins locations and transcripts
-- Its a representation of the mentions relationship
CREATE VIEW location_transcript_view AS
   SELECT * FROM (SELECT locations.*, transcripts.* FROM mentions
                  LEFT OUTER JOIN locations ON locations.location_id = mentions.location_id
                  LEFT OUTER JOIN transcripts ON transcripts.transcript_id = mentions.transcript_id) as LTV;

-- Creates a view that joins users and transcripts
-- Its a representation of the bookmarks relationship                  
CREATE VIEW user_transcript_view AS
   SELECT * FROM (SELECT users.*, transcripts.* FROM bookmarks
                  LEFT OUTER JOIN users ON users.user_id = bookmarks.user_id
                  LEFT OUTER JOIN transcripts ON transcripts.transcript_id = bookmarks.transcript_id) as UTV;

-- Creates a view that joins keywords and transcripts
-- Its a representation of the describes relationship
CREATE VIEW keyword_transcript_view AS
   SELECT * FROM (SELECT keywords.*, transcripts.* FROM describes
                  LEFT OUTER JOIN keywords ON keywords.k_id = describes.k_id
                  LEFT OUTER JOIN transcripts ON transcripts.transcript_id = describes.transcript_id) as UTV;

-- Creates a view that joins the mentions, describes and participates relationships into one view       
 CREATE VIEW full_transcript_view AS
   SELECT * FROM (SELECT keyword_transcript_view.keyword, keyword_transcript_view.k_id, location_transcript_view.location_id, location_transcript_view.street_name, participant_transcript_view.* FROM participant_transcript_view
                  LEFT OUTER JOIN keyword_transcript_view ON keyword_transcript_view.transcript_id = participant_transcript_view.transcript_id
                  LEFT OUTER JOIN location_transcript_view ON location_transcript_view.transcript_id = participant_transcript_view.transcript_id) as FT;


-- Insert users

-- Dummy Password for the users are "password", "admin", and "lib"
INSERT INTO users(email, password_hash, lflag) VALUES ('test@gmail.com', '$2b$12$B0ChMc2GW9RSKShJTqQnLOwemKAfQZPCPOG/pfQip8h6iTXGngQ9m', 0), ('test2@gmail.com', '$2b$12$Ddna1VJdMgIjpcylmbsMjuhUDZb.c/oujD8S9gEOUuHaz9Z9Gm/92', 0), ('lib@gmail.com', '$2b$12$bnWrAP.siJ.RNl1V5D66c.GZMXEu4rZGuWsuSpU8hmw/Ucm7L/uJ6', 1);

-- UPDATE WITH YOUR PATH ON YOUR SYSTEM FOR THE COPY COMMANDS

-- Insert first transcript and relevant information
COPY transcripts(title, text_file_path, audio_file_path, summary, text_content)
FROM '/Users/matthewvansoelen/Desktop/stage-v-group-1/data/joel/csv/insert_data_transcript.csv' DELIMITER '|' CSV HEADER;

COPY participants(name)
FROM '/Users/matthewvansoelen/Desktop/stage-v-group-1/data/joel/csv/insert_data_participants.csv' DELIMITER '|' CSV HEADER;

COPY locations(street_name)
FROM '/Users/matthewvansoelen/Desktop/stage-v-group-1/data/joel/csv/insert_data_locations.csv' DELIMITER '|' CSV HEADER;

COPY keywords(keyword)
FROM '/Users/matthewvansoelen/Desktop/stage-v-group-1/data/joel/csv/insert_data_keywords.csv' DELIMITER '|' CSV HEADER;

INSERT INTO participates VALUES (1,1);
INSERT INTO describes VALUES (1,1), (2,1);
INSERT INTO mentions VALUES (1,1), (2,1);
INSERT INTO bookmarks VALUES (1,1), (2,1);

-- Insert second transcript with relevant information
COPY transcripts(title, text_file_path, audio_file_path, summary, text_content)
FROM '/Users/matthewvansoelen/Desktop/stage-v-group-1/data/brenda/csv/insert_data_transcript.csv' DELIMITER '|' CSV HEADER;

COPY participants(name)
FROM '/Users/matthewvansoelen/Desktop/stage-v-group-1/data/brenda/csv/insert_data_participants.csv' DELIMITER '|' CSV HEADER;

COPY locations(street_name)
FROM '/Users/matthewvansoelen/Desktop/stage-v-group-1/data/brenda/csv/insert_data_locations.csv' DELIMITER '|' CSV HEADER;

COPY keywords(keyword)
FROM '/Users/matthewvansoelen/Desktop/stage-v-group-1/data/brenda/csv/insert_data_keywords.csv' DELIMITER '|' CSV HEADER;

INSERT INTO participates VALUES (2,2);
INSERT INTO describes VALUES (3,2), (4,2);
INSERT INTO mentions VALUES (3,2), (4,2);
INSERT INTO bookmarks VALUES (1,2);

-- Insert third transcript with relevant information
COPY transcripts(title, text_file_path, audio_file_path, summary, text_content)
FROM '/Users/matthewvansoelen/Desktop/stage-v-group-1/data/charles/csv/insert_data_transcript.csv' DELIMITER '|' CSV HEADER;

COPY participants(name)
FROM '/Users/matthewvansoelen/Desktop/stage-v-group-1/data/charles/csv/insert_data_participants.csv' DELIMITER '|' CSV HEADER;

COPY locations(street_name)
FROM '/Users/matthewvansoelen/Desktop/stage-v-group-1/data/charles/csv/insert_data_locations.csv' DELIMITER '|' CSV HEADER;

COPY keywords(keyword)
FROM '/Users/matthewvansoelen/Desktop/stage-v-group-1/data/charles/csv/insert_data_keywords.csv' DELIMITER '|' CSV HEADER;

INSERT INTO participates VALUES (3,3);
INSERT INTO describes VALUES (5,3), (6,3);
INSERT INTO mentions VALUES (4,3), (5,3);
