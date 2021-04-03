-- Filter a full transcript entry by a partial match transcipt's title
-- This file is a demonstrative example. Please update to match your database snapshot in order to run this
-- Query created as a group. File created by Thomas Orth. Reviewed by Matt Van Soelen and Justin Pabon
SELECT * FROM full_transcript_view WHERE title ILIKE '%joel%';