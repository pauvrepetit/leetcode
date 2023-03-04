select Department.name as 'Department', out_table.name as 'Employee', out_table.salary as 'Salary'
from Employee out_table join Department
where out_table.departmentId = Department.id
and out_table.salary in (
    select a.* from (
    select in_table.salary
    from Employee in_table
    where in_table.departmentId = out_table.departmentId
    group by in_table.salary
    order by in_table.salary desc
    limit 3 ) a
);
