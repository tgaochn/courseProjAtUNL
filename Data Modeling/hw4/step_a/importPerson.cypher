load csv with headers from 'file:///persons.csv' as line
// load csv with headers from 'file:///persons1.csv' as line
create (p:Person{
    id: toInteger(line.id),
    name: line.name,
    state: line.state
})
;
