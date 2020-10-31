// MATCH (p1:Person) - [f:Friend] -> (p2:Person) 
// where p1.state = 'Nebraska' and f.year >= 2005 
// RETURN p2
// ;
MATCH q=(p1:Person) - [f:Friend] -> (p2:Person) 
where p1.state = 'Nebraska' and f.year >= 2005 
RETURN q
;
