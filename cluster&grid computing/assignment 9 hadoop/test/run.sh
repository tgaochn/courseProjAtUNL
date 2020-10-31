hadoop jar $STREAM  \
-files ./mapper.py,./reducer.py \
-mapper ./mapper.py \
-reducer ./reducer.py \
-input /input/tian/test.txt \
-output /output/tian/2 \
