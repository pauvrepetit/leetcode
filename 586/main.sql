
WITH count_table AS (
SELECT count(customer_number) as c, customer_number
FROM Orders
GROUP BY customer_number
)
SELECT customer_number
FROM count_table
WHERE c = (
SELECT max(c) FROM count_table
)

-- with 真好用
