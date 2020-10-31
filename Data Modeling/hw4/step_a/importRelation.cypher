load csv with headers from 'file:///friends.csv' as line
// load csv with headers from 'file:///friends1.csv' as line
match (p1:Person{id: toInteger(line.personId)})
match (p2:Person{id: toInteger(line.friendId)})
create (p1) - [:Friend {year: toInteger(line.year)}] -> (p2)
create (p2) - [:Friend {year: toInteger(line.year)}] -> (p1)
;
