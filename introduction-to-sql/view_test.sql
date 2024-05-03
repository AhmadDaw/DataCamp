-- Create the view
CREATE VIEW library_authors AS
SELECT DISTINCT author AS unique_author
FROM books;

-- Select all columns from library_authors view
--SELECT *
--FROM library_authors;
