-- 1. Rebuild the database for the new Day 18 folder
CREATE TABLE
IF NOT EXISTS interns
(
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
);

INSERT OR
IGNORE INTO interns
VALUES
    (1, 'Anas', 'Data Science', 10000),
    (2, 'Sarah', 'Web Dev', 8000),
    (3, 'Rahul', 'Data Science', 10000),
    (4, 'Emily', 'Cybersecurity', 9000),
    (5, 'John', 'App Dev', 8500);

.mode column
.header on

-- 2. Task 1: Filter
SELECT '--- FILTER: Data Science > 5000 ---' AS Task;
SELECT *
FROM interns
WHERE track = 'Data Science' AND stipend > 5000;

-- 3. Task 1: Aggregate
SELECT '--- AGGREGATE: Average Stipend ---' AS Task;
SELECT track, AVG(stipend) AS average_stipend
FROM interns
GROUP BY track;

-- 4. Task 1: Count
SELECT '--- COUNT: Total Interns ---' AS Task;
SELECT track, COUNT(*) AS total_interns
FROM interns
GROUP BY track;