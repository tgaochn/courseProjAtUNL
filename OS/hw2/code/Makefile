CC      = gcc
LDLIBS  = -lpthead
CFLAGS += -MMD -MP
SRC     = $(wildcard *.c)
OBJ     = $(SRC:.c=.o)
DEP     = $(SRC:.c=.d)
TARGET  = q5
-include $(DEP)
${TARGET}: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)
clean:
	rm *.d *.o ${TARGET}    