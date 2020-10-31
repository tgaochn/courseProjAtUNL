MATCH (n) DETACH DELETE n

MATCH (n) - [r:SamePlant] -> () DELETE r

match (n:PointCloud) where n.plantId = '329_6' and n.date = '2018-08-03' return n.filePath