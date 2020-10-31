hadoop jar $STREAM  \
-files ./mapper1.py,./reducer1.py \
-mapper ./mapper1.py \
-reducer ./reducer1.py \
-input /input/tian/full_wordcount_text.txt \
-output /output/tian/7 


hadoop jar $STREAM  \
-files ./mapper2.py,./reducer2.py \
-mapper ./mapper2.py \
-reducer ./reducer2.py \
-input /output/tian/7 \
-output /output/tian/8 
