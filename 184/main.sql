-- 184. 部门工资最高的员工
--
-- 20200812
-- huao

-- Write your MySQL query statement below
select d2.DepartmentName Department, e1.Name Employee, e1.Salary Salary
from Employee e1 join
(select e2.DepartmentId, max(Salary), d1.Name
from Employee e2 join Department d1 on e2.DepartmentId = d1.Id
group by e2.DepartmentId) as d2(DepartmentId, maxSalary, DepartmentName)
on e1.DepartmentId = d2.DepartmentId where e1.Salary = d2.maxSalary;
