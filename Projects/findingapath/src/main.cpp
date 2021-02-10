#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <fstream>


using namespace std;

// Will print a 2D vector (for debugging)
void printStack2D( vector<vector<int> > stack ) {
        for ( auto i = stack.begin( ); i != stack.end( ); i++ ) {
                for ( auto j = ( *i ).begin( ); j != ( *i ).end( ); j++ ) {
                        cout << *j << " ";
                }
                cout << endl;
        }
}

// Will print a vector
void printStack( vector<int> stack ) {
        for ( auto i = stack.begin( ); i != stack.end( ); i++ ) {
                cout << *i << " ";
        }
        cout << endl;
}


bool vecContains( int x, vector<int> v ) {
        if ( std::find( v.begin( ), v.end( ), x ) != v.end( ) ) {
                return true;
        } else {
                return false;
        }
}

int main( int argc, char **argv ) {
        vector<int> explored;

        // for ( int i = 0; i < argc; i++ ) {
        //         cout << argv[i] << endl;
        //         cout << argc << endl;
        // }

        if ( argc > 1 ) {
                cout << "Please pass one argument the name of the test file"
                     << endl;
        }

        int N, A, B;
        ifstream infile( argv[1] );
        infile >> N >> A >> B;

        // cout << N << " " << A << " " << B << endl;
        vector<int> vec;
        vec.push_back( A );

        vector<vector<int> > possible_paths;
        possible_paths.push_back( vec );


        vector<vector<int> > graph;


        int src, dst;

        while ( infile >> src >> dst ) {
                // cout << src << " " << dst << " " << endl;
                vector<int> vect;
                vect.push_back( src );
                vect.push_back( dst );
                graph.push_back( vect );
        }

        while ( !possible_paths.empty( ) ) {
                vector<int> temp = possible_paths.back( );
                possible_paths.pop_back( );
                // cout << "TEMP BACK IS: " << temp.back();
                if ( temp.back( ) == B ) {
                        cout << "FOUND SOLUTION" << endl;
                        printStack( temp );
                        return 0;
                }
                vector<int> connections;
                for ( auto i = graph.begin( ); i != graph.end( ); i++ ) {
                        if ( ( *i )[0] == temp.back( ) ) {
                                // cout << "i: " << ( *i )[0]
                                //      << "tempback: " << temp.back( ) << endl;
                                connections.push_back( ( *i )[1] );
                        } else if ( ( *i )[1] == temp.back( ) ) {
                                // cout << "i: " << ( *i )[1]
                                //      << "tempback: " << temp.back( ) << endl;
                                connections.push_back( ( *i )[0] );
                        }
                }

                while ( !connections.empty( ) ) {
                        // printStack(temp);
                        if ( !vecContains( temp.back( ), explored ) ) {
                                vector<int> temp2 = temp;
                                temp2.push_back( connections.back( ) );
                                // cout << "THIS IS TEMP2: ";
                                // printStack( temp2 );
                                possible_paths.push_back( temp2 );
                        }
                        connections.pop_back( );
                        // cout << "CONNECTIONS:" << endl;
                        // printStack( connections );
                }
                // printStack2D( possible_paths );
                explored.push_back( temp.back( ) );
        }

        cout << "NO SOLUTION" << endl;


        // cout << graph[0][0] << " " << graph[0][1] << endl;

        // printStack2D( graph );
}
