-- Filter a bookmarked transcript for a partial match of the title
-- The given search query is meant to be demonstrative. Please update based on your database snapshot
-- Query designed as a group. File created by Thomas Orth. Reviewed by Matt Van Soelen and Justin Pabon 
SELECT * FROM user_transcript_view WHERE user_id=2 AND title ILIKE '%joel%';