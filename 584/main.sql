SELECT name
FROM customer
where referee_id IS NULL OR referee_id != 2

-- SQL中的NULL值不能用=/!=做比较，只能用IS