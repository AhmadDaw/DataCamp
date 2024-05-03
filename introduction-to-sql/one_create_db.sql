-- Create the database
CREATE DATABASE library;

-- Use the database
USE library;

-- Create the "patrons" table
CREATE TABLE patrons (
    card_num INT(5),
    name VARCHAR(255),
    member_year INT(4),
    total_fine FLOAT
);

-- Insert 4 records into the "patrons" table
INSERT INTO patrons (card_num, name, member_year, total_fine) VALUES
(12345, 'John Doe', 2018, 5.50),
(67890, 'Jane Smith', 2015, 0.00),
(54321, 'Bob Johnson', 2020, 12.75),
(98765, 'Sarah Lee', 2019, 3.25);

-- Create the "books" table
CREATE TABLE books (
    id INT(3),
    title VARCHAR(255),
    author VARCHAR(255),
    genre VARCHAR(255),
    pub_year INT(4)
);

-- Insert 4 records into the "books" table
INSERT INTO books (id, title, author, genre, pub_year) VALUES
(123, 'The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 1925),
(456, 'To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1960),
(789, 'The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 1951),
(321, 'Brave New World', 'Aldous Huxley', 'Science Fiction', 1932);

-- Create the "checkouts" table
CREATE TABLE checkouts (
    id INT(3),
    start_date DATE,
    due_date DATE,
    card_num INT(5),
    book_id INT(3)
);

-- Insert 4 records into the "checkouts" table
INSERT INTO checkouts (id, start_date, due_date, card_num, book_id) VALUES
(101, '2023-04-01', '2023-04-15', 12345, 123),
(102, '2023-03-15', '2023-03-29', 67890, 456),
(103, '2023-05-01', '2023-05-15', 54321, 789),
(104, '2023-02-20', '2023-03-06', 98765, 321);

-- Select unique authors and genre combinations from the books table
SELECT DISTINCT author , genre
FROM books;

-- Alias author so that it becomes unique_author
SELECT DISTINCT author AS unique_author
FROM books;


