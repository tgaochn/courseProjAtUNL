load csv with headers from 'file:///init.csv' as line
// load csv with headers from 'file:///init1.csv' as line

create (f:PointCloud{
    plantId: line.plantId,
    date: line.curDate,
    filePath: line.plyPath
})
;