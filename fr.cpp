#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main( int argc, char const *argv[])
{
    string line {};
    ifstream fs {};
    fs.open( argv[1], ios::in );

    if( fs.is_open() )
    {
        while( getline( fs, line ))
        {
            cout << line << endl;
        }
    }

    fs.close();

    return 0;
}