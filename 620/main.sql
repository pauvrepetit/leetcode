-- 620. 有趣的电影
--
-- 20200726
-- huao
-- 一个简单的select语句

select id, movie, description, rating from cinema
where id % 2 = 1 and description <> 'boring'
order by rating desc;