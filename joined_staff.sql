CREATE TABLE joined_staff (
	staff_id int PRIMARY KEY,
    birth_date date,
    f_name varchar(14),
    l_name varchar(16),
    gender enum('M','F'),
    hire_date date,
    location_id INT
    );
    
SELECT * FROM wez6fg.dept_emp;
ALTER TABLE dept_emp ALTER dept_no SET DEFAULT 1;
ALTER TABLE dept_emp DROP COLUMN from_date;
ALTER TABLE dept_emp DROP COLUMN to_date; 
INSERT INTO `dept_emp` (`emp_no`) SELECT `staff_id` FROM `employees`;

UPDATE dept_emp
SET dept_no = CASE 
                        WHEN emp_no BETWEEN 1 AND 19  THEN '1'
                        WHEN emp_no BETWEEN 20 AND 39 THEN '2'
                        WHEN emp_no BETWEEN 40 AND 59 THEN '3'
                        WHEN emp_no BETWEEN 60 AND 79 THEN '4'
                        ELSE '5'
                END;
INSERT INTO joined_staff (staff_id, birth_date, f_name, l_name, gender, hire_date, location_id)
SELECT e.staff_id, e.birth_date, e.first_name, e.last_name, e.gender, e.hire_date, de.dept_no
FROM employees e
JOIN dept_emp de ON e.staff_id = de.emp_no;

SELECT * FROM joined_staff;


