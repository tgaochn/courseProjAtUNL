CC      = g++
LDLIBS  = -lpthead
CFLAGS += -MMD -MP
SRC     = $(wildcard *.cpp)
OBJ     = $(SRC:.cpp=.o)
DEP     = $(SRC:.cpp=.d)
TARGET  = Hello_world
-include $(DEP)
${TARGET}: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)
clean:
	rm *.o ${TARGET}