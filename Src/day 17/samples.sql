-- ==========================================================
-- TOPIC 1: Introduction to SQL & SELECT Queries
-- ==========================================================
-- 1. Create the students table
CREATE TABLE students (
    id INTEGER,
    name TEXT,
    marks INTEGER
);

-- 2. Insert sample data
INSERT INTO students VALUES (1, 'Amit', 85);
INSERT INTO students VALUES (2, 'Riya', 92);
INSERT INTO students VALUES (3, 'John', 78);

-- 3. Run basic queries
SELECT * FROM students;
SELECT name, marks FROM students;


-- ==========================================================
-- TOPIC 2: Filtering Data with WHERE Clause
-- ==========================================================
-- 1. Query students with marks above 80
SELECT * FROM students WHERE marks > 80;

-- 2. Combine conditions
SELECT * FROM students WHERE marks > 80 AND name != 'John';

-- 3. Another code example
SELECT name FROM students WHERE marks >= 90;


-- ==========================================================
-- TOPIC 3: Aggregation with GROUP BY
-- ==========================================================
-- 1. Create a new table
CREATE TABLE scores (
    subject TEXT,
    marks INTEGER
);

-- 2. Insert data
INSERT INTO scores VALUES ('Math', 80);
INSERT INTO scores VALUES ('Math', 90);
INSERT INTO scores VALUES ('Science', 85);

-- 3. Aggregate functions
SELECT subject, AVG(marks) FROM scores GROUP BY subject;
SELECT subject, COUNT(*) FROM scores GROUP BY subject;


-- ==========================================================
-- TOPIC 4: SQL JOINS
-- ==========================================================
-- 1. Create another table
CREATE TABLE departments (
    id INTEGER,
    dept TEXT
);

-- (Adding dummy data here so the JOIN actually shows results when you test it!)
INSERT INTO departments VALUES (1, 'Computer Science');
INSERT INTO departments VALUES (2, 'Physics');
INSERT INTO departments VALUES (3, 'Mathematics');

-- 2. Join tables together
SELECT students.name, departments.dept
FROM students
INNER JOIN departments
ON students.id = departments.id;
