objects = test.o

test : $(objects)
	g++ -Wall -std=c++17 -o test test.o

test.o : test.cpp
	g++ -Wall -std=c++17 -c test.cpp

.PHONY : clean
clean :
	rm test $(objects)