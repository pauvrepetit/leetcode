UPDATE Salary
SET sex = 
CASE
    WHEN sex = 'f' THEN 'm'
    ELSE 'f'
END

-- CASE的用法，MySQL好像还有if的用法
