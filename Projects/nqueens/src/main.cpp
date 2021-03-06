#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>


using namespace std;

// Will print a 2D vector (for debugging)
void printStack2D( vector<vector<int> > stack ) {
        for ( auto i = stack.begin( ); i != stack.end( ); i++ ) {
                for ( auto j = ( *i ).begin( ); j != ( *i ).end( ); j++ ) {
                        cout << *j << ",";
                }
                cout << endl;
        }
}

// Will print a vector
void printStack( vector<int> stack ) {
        for ( auto i = stack.begin( ); i != stack.end( ); i++ ) {
                cout << *i;
        }
        cout << endl;
}

// Will insert a number into a position in the queens vector. 
// I'm not sure how this got so complicated. I need to get better at C++
vector<int> generatePosition( int num, vector<int> queens, int n ) {
        vector<int> newQueens = queens;

        // if ( int pos = find( newQueens.begin( ), newQueens.end( ), 0 ) !=
        //                newQueens.end( ) ) {
        //         newQueens[pos] = num;
        // }

        for ( int i = 0; i < n; i++ ) {
                if ( newQueens[i] == 0 ) {
                        newQueens[i] = num;
                        break;
                }
        }
        // printStack( newQueens );

        return newQueens;
}


// Checks if the queens can attack each other using absolute value for their slope.
// WIsh it wasn't so over nested but it works. 
bool isValid( vector<int> queens, int n ) {
        for ( int i = 0; i < n; i++ ) {
                for ( int j = 0; j < n; j++ ) {
                        if ( i != j ) {
                                if ( ( queens[i] != 0 ) &&
                                     ( queens[j] != 0 ) ) {
                                        if ( queens[i] == queens[j] ) {
                                                return true;
                                        }
                                        if ( abs( i - j ) ==
                                             abs( queens[i] - queens[j] ) ) {
                                                return true;
                                        }
                                }
                        }
                }
        }
        return false;
}

// Main code to solve the nqueens problem. 
vector<int> nqueenSolv( int N ) {
        vector<vector<int> > all_positions;
        for ( int i = 0; i < N; i++ ) {
                vector<int> queens;
                for ( int i = 0; i < N; i++ ) {
                        queens.push_back( 0 );
                }
                queens[0] = i + 1;
                all_positions.push_back( queens );
        }

        // // uncomment for debugging. 
        // for ( auto i : all_positions ) {
        //         for ( auto j : i ) {
        //                 cout << j;
        //         }
        //         cout << endl;
        // }

        while ( !all_positions.empty( ) ) {
                vector<int> queens = all_positions.back( );
                all_positions.pop_back( );
                if ( !isValid( queens, N ) ) {
                        if ( queens.back( ) != 0 ) {
                                return queens;
                        }
                        for ( int i = 0; i < N; i++ ) {
                                all_positions.push_back(
                                        generatePosition( i + 1, queens, N ) );
                        }
                }
        }
        vector<int> nope;
        return nope;
}

int main( int argc, char **argv ) {
        for ( int i = 0; i < argc; i++ ) {
                cout << argv[i] << endl;
        }

        // I initially was going to use command line args but figured it's easier
        // to just get user input for the time being. 

        if ( ( argc < 2 ) | ( argc > 2 ) ) {
                cout << "Invalid argument count please pass an integer N"
                     << endl;
        }

        cout << "Enter the value of N pls";
        int N = 0;
        cin >> N;

        vector<int> result = nqueenSolv(N);
        if (result.empty()) {
                cout << "THERE IS NO SOLUTION" << endl;
        } else {
                printStack(result);
        }
}
