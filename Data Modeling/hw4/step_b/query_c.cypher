MATCH (p1:Person) - [f:Friend] -> (p2:Person) 
where p1.state = 'Nebraska' and f.year >= 2005 
RETURN p1, COUNT(p2) as count
ORDER BY count DESC
limit 1
;
// MATCH q=(p1:Person) - [f:Friend] -> (p2:Person) 
// where p1.state = 'Nebraska' and f.year >= 2005 
// RETURN q, COUNT(p2) as count
// ORDER BY count DESC
// limit 1
// ;
