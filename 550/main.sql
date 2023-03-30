SELECT ROUND((
SELECT COUNT(DISTINCT t1.player_id) as fraction
FROM Activity t1 JOIN Activity t2
WHERE t1.player_id = t2.player_id
AND ADDDATE(t1.event_date ,INTERVAL 1 day) = t2.event_date
AND t1.event_date = (SELECT MIN(event_date) FROM Activity t3 WHERE t3.player_id = t1.player_id)
) / (
SELECT COUNT(DISTINCT Activity.player_id) FROM Activity
), 2) as fraction;