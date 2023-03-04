select l.name as 'Employee'
from Employee l join Employee r
where l.managerId = r.id
and l.salary > r.salary
;
