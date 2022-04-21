-- Showing all data
SELECT *
from teachers;

-- Showing teachers whose salary is above 50000
select *
from teachers
where salary > 50000;

-- Counting the number of teachers whose salary is above 50000
SELECT COUNT(*)
from teachers
where salary > 50000;

-- Showing teachers whose first_name is 'samuel'
SELECT *
from teachers
WHERE BINARY first_name = 'samuel';

-- Showing teachers whose first_name starts with 'Sam'
SELECT *
from teachers
where first_name like 'Sam%';

-- Showing teachers whose first_name ends with 'sam'
SELECT *
from teachers
WHERE first_name like '%sam';

-- Showing teachers whose first_name contains 'sam'
SELECT *
from teachers
where first_name like '%sam%';

-- Showing teacher with the highest salary
SELECT first_name,
	last_name
FROM teachers
where salary = (
	SELECT MAX(salary)
	FROM teachers
);

-- Showing average salary in Cambridge University
SELECT AVG(salary),
	FLOOR(AVG(salary)),
	CEILING(AVG(salary))
FROM teachers
WHERE school = 'Cambridge University';

-- Showing the highest salary in each university
SELECT school,
	MAX(salary)
FROM teachers
GROUP by school;

-- Showing teachers with the highest salary in each university
SELECT first_name,
	last_name,
    salary
FROM teachers
WHERE (school, salary) in (
	SELECT school,
		MAX(salary)
	FROM teachers
	GROUP by school
);

-- Joining table 'teachers' with table 'courses'
SELECT *
FROM teachers
JOIN courses ON teachers.id = courses.teachers_id;

-- Showing all teachers who teach Calculus
SELECT *
from teachers
JOIN courses on teachers.id = courses.teachers_id
WHERE courses.name = 'Calculus';

-- Showing the total number of courses in each university
SELECT teachers.school,
	COUNT(courses.id) AS total_courses
from teachers
JOIN courses on teachers.id = courses.teachers_id
GROUP by teachers.school;

-- Showing universities which have more than 5 courses
SELECT teachers.school,
	COUNT(courses.id) AS total_courses
from teachers
JOIN courses on teachers.id = courses.teachers_id
GROUP BY teachers.school
HAVING total_courses > 5;

-- Showing teacher's first_name and the number of courses taught
SELECT teachers.first_name,
	COUNT(courses.id) as total_courses
FROM teachers
JOIN courses on teachers.id = courses.teachers_id
GROUP by teachers.id
ORDER by total_courses DESC, teachers.first_name ASC;