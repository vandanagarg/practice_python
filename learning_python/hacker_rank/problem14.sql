/* ''' 1. Professor Names and Salaries
A university maintains data on professors and departments in two tables:
PROFESSOR and DEPARTMENT.
Write a query to print the NAME and SALARY for each professor
who satisfies the following two requirements:
• The professor does not work In the Arts and Humanities department.
• The professor's salary is greater than the smallest salary of any
professor In the Arts and Humanties department.
The name must be printed before the salary, but row Order does not matter.

Schema
DEPARTMENT
Name    Type       Description
ID      Integer    A dept ID in inclusive range [1, 1000], primary key
NAME    String     Dept name.This field contains between 1 and 100 characters

PROFESSOR
Name                Type       Description
ID                  Integer    A professor's ID in inclusive range [1, 1000], primary key
NAME                String     professor's name.field contains between 1 and 100 characters
DEPARTMENT_ID       Integer    A professors department ID. TN, Is a foreign key to DEPARTMENT.ID
SALARY              Integer    professor's salary In the inclusive range [5000, 40000]
''' */

select p.name, p.salary
from professor p
join DEPARTMENT d
on p.DEPARTMENT_ID = d.ID
where p.DEPARTMENT_ID not in (select id from department where name = "Arts and Humanities")
and p.salary > (select min(p2.salary) from professor p2
join department d2
on p2.DEPARTMENT_ID = d2.ID
where p2.DEPARTMENT_ID = (select id from department where name = "Arts and Humanities")
);


select PROFESSOR.NAME, PROFESSOR.SALARY from PROFESSOR
join DEPARTMENT
on PROFESSOR.DEPARTMENT_ID DEPARTMENT.ID
where DEPARTMENT.NAME != "Arts and Humanities"
and PROFESSOR.SALARY >
(select (PROFESSOR.SALARY) from PROFESSOR
join DEPARTMENT
on PROFESSOR.DEPARTMENT_ID DEPARTMENT.ID
where DEPARTMENT.NAME = "Arts and Humanities");
