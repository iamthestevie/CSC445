#include <iostream>
#include <string>
#include <vector>
#include <sstream>

void print_lp_types(std::vector< std::vector<float> > &lp);

int main() {

    // vector of vectors to hold our linear program
    std::vector< std::vector<float>  > lp {};

    // Read in an LP from standard input.
    std::string line {};
    while( std::getline( std::cin, line ) )
    {
        // skip empty lines
        if( line.size() == 0 )
            continue;

        std::istringstream is( line );
        lp.push_back( std::vector<float>( std::istream_iterator<float>(is),
                                          std::istream_iterator<float>() ) );
    }

    print_lp_types(lp);
    

    return 0;
}

void print_lp_types(std::vector< std::vector<float> > &lp)
{
    for (int i {0}; i < lp.size(); i++)
    {
        for (int j {0}; j < lp.at(i).size(); j++)
        {
            std::cout << lp.at(i).at(j) << "-" << typeid(lp.at(i).at(j)).name() << " ";
        }

        std::cout << std::endl;
    }
}