SELECT product_id, product_name
FROM Product
WHERE product_id IN (
SELECT DISTINCT product_id
FROM Sales
WHERE sale_date >= '2019-01-01' AND sale_date <= '2019-03-31'
AND product_id NOT IN (
SELECT DISTINCT product_id
FROM Sales
WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31'
))
