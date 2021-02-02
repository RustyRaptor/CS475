#include <iostream>
#include <vector>

using namespace std;
int main( ) {

        // 0 is unknown
        int N = 4;
        vector<int> board;
        for ( int i = 1; i <= N; i++ ) {
                board.push_back( 0 );
        }

        cout << "Hello world!" << endl;
        cout << N << endl;

        for (auto i = board.begin(); i != board.end(); i++) {
                cout << *i << ", ";
        }

        
}

// (1,1) (2,2) (3,3) (4,4)