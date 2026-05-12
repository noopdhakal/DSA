
-- # Find the employees with salary more than their managers salary

create table emp(emp_id int,emp_name varchar(10),salary int ,manager_id int);

insert into emp values(1,'Ankit',10000,4);
insert into emp values(2,'Mohit',15000,5);
insert into emp values(3,'Vikas',10000,4);
insert into emp values(4,'Rohit',5000,2);
insert into emp values(5,'Mudit',12000,6);
insert into emp values(6,'Agam',12000,2);
insert into emp values(7,'Sanjay',9000,2);
insert into emp values(8,'Ashish',5000,2);

select * from emp;

select a.emp_id, a.emp_name, b.emp_name as manager_name, b.salary, b.salary as manager_salary from emp a 
inner  join emp b
on a.MANAGER_ID = b.EMP_ID 
;

-- ## questions like get managers only

select e.emp_id, e.emp_name, m.emp_name, e.SALARY, m.SALARY as manager_salary  from emp e 
inner join emp m on e.manager_id = m.emp_id
where e.SALARY > m.SALARY
;

-- Display Employee Name with Manager Name

select e.EMP_NAME as empoyee_name, m.EMP_NAME as manager_name from  emp e
inner join emp m
on e.manager_id = m.EMP_ID;

-- Managers are employees who appear as manager_id.

select distinct m.EMP_ID, m.EMP_NAME as manager_name from  emp e
inner join emp m
on e.manager_id = m.EMP_ID;

-- 4. Find Employees Who Do Not Have a Manager (Top-Level Managers)

select emp_id, emp_name from emp where MANAGER_ID is null;

-- 5. Count Number of Employees Reporting to Each Manager
SELECT m.emp_id,
       m.emp_name AS manager_name,
       COUNT(*) AS total_reports
FROM emp e
INNER JOIN emp m
    ON e.manager_id = m.emp_id
GROUP BY m.emp_id, m.emp_name;

-- 6. Find Managers with More Than 2 Direct Reports
SELECT m.emp_id,
       m.emp_name AS manager_name,
       COUNT(*) AS total_reports
FROM emp e
INNER JOIN emp m
    ON e.manager_id = m.emp_id
GROUP BY m.emp_id, m.emp_name having  count(*) > 2;

-- 7. Find the Manager with the Highest Number of Direct Reports

SELECT m.emp_id,
       m.emp_name AS manager_name,
       COUNT(*) AS total_reports
FROM emp e
INNER JOIN emp m
    ON e.manager_id = m.emp_id
GROUP BY m.emp_id, m.emp_name
order by total_reports desc
fetch first 1 row only;


-- 8. Find Employees Having the Same Salary as Their Manager

select distinct e.EMP_NAME from emp e inner join emp m 
on m.MANAGER_ID = e.EMP_ID
where m.SALARY = e.SALARY;

-- 10. Find Highest Paid Employee Under Each Manager
select distinct m.EMP_NAME as manager_name, max(e.SALARY) as highest_employee_salary from emp e inner join emp m 
on m.MANAGER_ID = e.EMP_ID
group by m.EMP_NAME;
