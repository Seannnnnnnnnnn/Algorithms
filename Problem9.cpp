//  Project Euler - Problem 9
//  Explanation: https://radiusofcircle.blogspot.com/2016/04/problem-9-project-euler-solution-with-python.html


#include <iostream>
using namespace std;


int square(int n){
    return n*n;
}

void solve(){
    for(int m=0; m<= 100; m++){
        for(int n =0; n<=100; n++){
            
            int a = square(n) - square(m);
            int b = 2*n*m;
            int c = square(n) + square(m);
            
            if (a+b+c == 1000){
                cout << a << " " << b << " " << c << endl;
                return;
            }
        }
    }
}
    


int main() {
    solve();
    return 0;
}
