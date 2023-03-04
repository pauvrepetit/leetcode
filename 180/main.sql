select distinct(num) as ConsecutiveNums
from Logs out_table
where out_table.num IN (
    select num from Logs in_table
    where in_table.id = out_table.id - 1)
and out_table.num IN (
    select num from Logs in_table
    where in_table.id = out_table.id - 2)
;
