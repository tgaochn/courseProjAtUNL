MATCH (p1:Person) - [f:Friend] -> (p2:Person) 
RETURN p1, COUNT(p2) as count
ORDER BY count DESC
limit 1
;
