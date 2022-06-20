objects = lp.o

lp : $(objects)
	g++ -Wall -std=c++17 -o lp lp.o

lp.o : lp.cpp
	g++ -Wall -std=c++17 -c lp.cpp

.PHONY : clean
clean :
	rm lp $(objects)