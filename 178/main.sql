select os.score AS score, (select count(distinct(ins.score))+1 from Scores ins where ins.score > os.score) AS 'rank'
from Scores os
order by os.score desc;