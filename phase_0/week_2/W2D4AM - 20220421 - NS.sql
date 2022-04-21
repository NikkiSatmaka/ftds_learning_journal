-- Creating table 'teachers'
CREATE TABLE teachers (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  first_name varchar(25) not NULL,
  last_name varchar(50),
  school varchar(50) not NULL,
  hire_date date,
  salary numeric
);

-- Adding column 'age'
alter table teachers add age int;

-- Deleting column 'age'
ALTER table teachers DROP COLUMN age;

-- Changing data type of column 'salary'
alter table teachers MODIFY COLUMN salary int;

-- Changing table name from 'teachers' to 'guru'
ALTER TABLE teachers rename to guru;

-- Changing table name from 'guru' to 'teachers'
alter table guru rename to teachers;

-- Inputting data to table 'teachers'
INSERT into teachers (id, first_name, last_name, school, hire_date, salary)
    VALUES (1,'Janet', 'Smith', 'MIT', '2011-10-30', 36200),
           (2,'Lee', 'Reynolds', 'MIT', '1993-05-22', 65000),
           (3,'Samuel', 'Cole', 'Cambridge University', '2005-08-01', 43500),
           (4,'Samantha', 'Bush', 'Cambridge University', '2011-10-30', 36200),
           (5,'Betty', 'Diaz', 'Cambridge University', '2005-08-30', 43500),
           (6,'Kathleen', 'Roush', 'MIT', '2010-10-22', 38500),
           (7,'James', 'Diaz', 'Harvard University', '2003-07-18', 61000),
           (8,'Zack', 'Smith', 'Harvard University', '2000-12-29', 55500),
           (9,'Luis', 'Gonzales', 'Standford University', '2002-12-01', 50000),
           (10,'Frank', 'Abbers', 'Standford University', '1999-01-30', 66000);

-- Looking inside the table 'teachers'
SELECT * from teachers;

-- Deleting all records of the table 'teachers'
TRUNCATE TABLE teachers;

-- Deleting the table 'teachers'
drop table teachers;

-- Changing salary from id=3
update teachers
SET salary = 50000
WHERE id = 3;

-- Looking at column first_name, last_name, and school
SELECT first_name, last_name, school
FROM teachers;

-- Sorting last_name from Z-A
SELECT *
from teachers
ORDER by last_name DESC;

-- Sorting last_name from Z-A and school from A-Z
SELECT *
from teachers
ORDER by last_name DESC, school ASC;

-- Deleting data with id=6
DELETE FROM teachers
WHERE id = 6;

SELECT * from teachers;

-- Adding new data
INSERT into teachers (first_name, last_name, school, hire_date, salary)
    VALUES ('Samuel', 'Abbers', 'Standford University', '2006-01-30', 32000),
           ('Jessica', 'Abbers', 'Standford University', '2005-01-30', 33000),
           ('Tom', 'Massi', 'Harvard University', '1999-09-09', 39500),
           ('Esteban', 'Brown', 'MIT', '2007-01-30', 36000),
           ('Carlos', 'Alonso', 'Standford University', '2001-01-30', 44000);
           
-- Looking for teachers who teach in Harvard University with salary over 50000
SELECT *
from teachers
WHERE school = 'harvard university'
and salary > 50000;

-- Looking for teachers whose last_name is abbers or smith
-- First method using OR
SELECT *
from teachers
WHERE last_name = 'abbers'
or last_name = 'smith';

-- Second method using IN
SELECT *
FROM teachers
WHERE last_name in ('abbers', 'smith');

-- Looking at the total salary from MIT
SELECT sum(salary) as total_salary
from teachers
WHERE school = 'mit';

SELECT school,
	SUM(salary) as total_salary,
	avg(salary) as avg_salary,
    MIN(salary) as min_salary,
    max(salary) as max_salary
from teachers
WHERE school = 'mit';

-- Looking at unique value from column school
SELECT DISTINCT(school)
from teachers;

SELECT COUNT(DISTINCT(school))
from teachers;