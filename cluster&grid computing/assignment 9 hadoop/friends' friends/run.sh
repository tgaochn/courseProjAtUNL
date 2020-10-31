hadoop jar $STREAM  \
-files ./mapper1.py,./reducer1.py \
-mapper ./mapper1.py \
-reducer ./reducer1.py \
-input /input/tian/uids_of_friends.txt \
-output /output/tian/103


hadoop jar $STREAM  \
-files ./mapper2.py,./reducer2.py \
-mapper ./mapper2.py \
-reducer ./reducer2.py \
-input /output/tian/103 \
-output /output/tian/104
