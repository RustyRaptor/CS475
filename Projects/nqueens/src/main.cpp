#include <iostream>
#include <vector>
#include <algorithm>
#include <experimental/iterator>


using namespace std;

vector<int> generateQueens( int Q1, int Q2, int Q3, int Q4 ) {
        vector<int> queens;
        queens.push_back( Q1 );
        queens.push_back( Q2 );
        queens.push_back( Q3 );
        queens.push_back( Q4 );
        return queens;
}

void printStack( vector<vector<int> > stack ) {
        for ( auto i = stack.begin( ); i != stack.end( ); i++ ) {
                for ( auto j = ( *i ).begin( ); j != ( *i ).end( ); j++ ) {
                        cout << *j << ",";
                }
                cout << endl;
        }
}

vector<vector<int>> generateBranch(vector<int> queens, vector<vector<int>> stack) {
        if (find(queens.begin(), queens.end(), 0) == queens.end()) {
                return stack;
        }
}

int main( int argc, char **argv ) {
        // for ( int i = 0; i < argc; i++ ) {
        //         cout << argv[i] << endl;
        // }

        // First lets get the value of N

        if ( ( argc < 2 ) | ( argc > 2 ) ) {
                cout << "Invalid argument count please pass an integer N"
                     << endl;
        }
        int N = atoi( argv[1] );


        vector<vector<int> > stack;
        for ( int i = 1; i <= N; i++ ) {
                stack.push_back( generateQueens( 0, 0, 0, 0 ) );
                stack.
        }

        cout << N << endl;

        printStack( stack );
}
