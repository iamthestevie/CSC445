#include <iostream>
#include <string>

int main() {

    // Read in an LP from standard input.
    std::string line;
    while( std::getline( std::cin, line ) )
    {
        std::cout << line << std::endl;
    }

    return 0;
}