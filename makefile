test : test.o
	g++ -Wall -std=c++20 -o test test.o

test.o : test.cpp
	g++ -Wall -std=c++20 -c test.cpp

clean :
	rm test test.o