SELECT DISTINCT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3

-- GROUP BY 可以针对多列做聚合
