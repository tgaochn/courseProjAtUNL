load csv with headers from 'file:///init.csv' as line
// load csv with headers from 'file:///init1.csv' as line

match (f1:PointCloud{plantId: line.plantId})
match (f2:PointCloud{plantId: line.plantId}) where f1.date = line.curDate and f2.date = line.nextDate
create (f1) - [:NextDate {plantId: line.plantId}] -> (f2)

