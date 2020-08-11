-- 177. 第N高的薪水
--
-- 20200811
-- huao
-- 这mysql就有毒...

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N=N-1;
  RETURN (
      -- Write your MySQL query statement below.
      select max(Salary) from Employee
      where Salary not in 
      (select * from (select * from (select distinct Salary from Employee order by Salary desc) as t limit N) as t2)
  );
END