-- 595. 大的国家
--
-- 20200811
-- huao

-- Write your MySQL query statement below
select name, population, area from World
where population > 25000000 or area > 3000000;