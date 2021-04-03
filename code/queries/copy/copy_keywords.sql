-- Copies keyword data in bulk from CSV. Delimiter is  | since it is uncommonly used by users
-- Requires to be a SUPERUSER in order to use the COPY query
-- Please update the path to where you have the file stored
-- By Thomas Orth. Reviewed by Matthew Van Soelen and Justin Pabon
COPY keywords(keyword)
FROM '/home/lion/stage-v-group-1/data/joel/csv/insert_data_keywords.csv' DELIMITER '|' CSV HEADER;