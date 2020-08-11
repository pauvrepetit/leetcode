-- 175. 组合两个表
--
-- 20200811
-- huao

-- Write your MySQL query statement below
select FirstName, LastName, City, State
from Person p LEFT JOIN Address a on p.PersonId = a.PersonId;