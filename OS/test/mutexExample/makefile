CC      = g++-7
LDLIBS  = -lpthead
CFLAGS += -MMD -MP -lpthread
SRC     = $(wildcard *.cpp)
OBJ     = $(SRC:.cpp=.o)
DEP     = $(SRC:.cpp=.d)
TARGET  = main
-include $(DEP)
${TARGET}: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)
clean:
	rm -f *.o *.d ${TARGET}
