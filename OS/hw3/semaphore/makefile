CC      = g++
LDLIBS  = -lpthead
CFLAGS += -MMD -MP -lpthread
SRC     = $(wildcard *.cpp)
OBJ     = $(SRC:.cpp=.o)
DEP     = $(SRC:.cpp=.d)
TARGET  = SemSort
-include $(DEP)
${TARGET}: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)
clean:
	rm -f *.o *.d ${TARGET}
