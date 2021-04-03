-- Filter a full transcript entry by a partial match of a location in trenton mentioned in the transcript
-- This file is a demonstrative example. Please update to match your database snapshot in order to run this
-- Query created as a group. File created by Thomas Orth. Reviewed by Matt Van Soelen and Justin Pabon
SELECT * FROM full_transcript_view WHERE street_name ILIKE '%broad street%';