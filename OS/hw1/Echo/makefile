CC      = g++
LDLIBS  = -lpthead
CFLAGS += -MMD -MP
SRC     = $(wildcard *.cpp)
OBJ     = $(SRC:.cpp=.o)
DEP     = $(SRC:.cpp=.d)
TARGET  = echo
-include $(DEP)
${TARGET}: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)
clean:
	rm *.o ${TARGET}