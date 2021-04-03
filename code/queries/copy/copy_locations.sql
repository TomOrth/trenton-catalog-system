-- Copies location data in bulk from CSV. Delimiter is  | since it is uncomoonly used by users
-- Requires to be a SUPERUSER in order to use the COPY query
-- Please update the path to where you have the file stored
-- By Thomas Orth. Reviewed by Matthew Van Soelen and Justin Pabon
COPY locations(street_name)
FROM '/home/lion/stage-v-group-1/data/joel/csv/insert_data_locations.csv' DELIMITER '|' CSV HEADER;