-- Day 17: Task 1 - The Database Architect
-- 1. Create the table
CREATE TABLE interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
);

-- 2. Insert sample data
INSERT INTO interns VALUES 
(1, 'Anas', 'Data Science', 10000),
(2, 'Sarah', 'Web Dev', 8000),
(3, 'Rahul', 'Data Science', 10000),
(4, 'Emily', 'Cybersecurity', 9000),
(5, 'John', 'App Dev', 8500);

-- 3. Retrieve specific columns
SELECT name, track FROM interns;