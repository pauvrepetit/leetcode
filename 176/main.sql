-- 176. 第二高的薪水
--
-- 20200811
-- huao

-- Write your MySQL query statement below
select max(Salary) SecondHighestSalary from Employee
where Salary not in (select max(Salary) from Employee);
