select row_number() over() as id, student
from Seat
order by
case when mod(id, 2) = 0 then id - 1
else id + 1 end
