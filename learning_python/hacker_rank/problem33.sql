/*
print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.
*/
select c.company_code, c.founder, 
    count(distinct l.lead_manager_code), count(distinct s.senior_manager_code), 
    count(distinct m.manager_code),count(distinct e.employee_code) 
from Company c, Lead_Manager l, Senior_Manager s, Manager m, Employee e 
where c.company_code = l.company_code 
    and l.lead_manager_code=s.lead_manager_code 
    and s.senior_manager_code=m.senior_manager_code 
    and m.manager_code=e.manager_code 
group by c.company_code order by c.company_code;


select company_code, founder,
(select count(distinct lead_manager_code) from Lead_Manager where company_code=c.company_code),
(select count(distinct senior_manager_code) from Senior_Manager where company_code=c.company_code),
(select count(distinct manager_code) from Manager where company_code=c.company_code),
(select count(distinct employee_code) from Employee where company_code=c.company_code)
from Company c
order by company_code;
