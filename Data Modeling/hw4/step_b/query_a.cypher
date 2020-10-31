// MATCH (p1:Person) - [:Friend] -> (p2:Person) 
// where p1.state = 'Nebraska' 
// RETURN p2
// ;

MATCH q=(p1:Person) - [:Friend] -> (p2:Person) 
where p1.state = 'Nebraska' 
RETURN q
;
