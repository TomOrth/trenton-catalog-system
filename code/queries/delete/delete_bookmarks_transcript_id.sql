-- Deletes a bookmarks relationship by a given transcript_id
-- The id is hardcoded for demonstrative purposes. The ID needs to be updated to match your current database snapshot to see it in action
-- Query designed as a group. File created by Thomas Orth. Reviewd by Matt Van Soelen and Justin Pabon.
DELETE FROM bookmarks where transcript_id = 2;