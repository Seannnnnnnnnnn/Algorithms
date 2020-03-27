//  ProjectEuler - Problem 25:
//  find first k digit Fibonacci number: 

#include <iostream>
using namespace std;

int fibonacci(int n){
    // Create an array to store the Fibonacci numbers:
    int f[n+1];
    
    // Define the first members of the sequence;
    f[0] = 0; f[1] = 1;
    
    for (int i=2; i <= n; i++) {
        f[i] = f[i-1] + f[i-2];
    }
    
    return f[n];
}

string k_digit_fibonacci(int k){
    // returns the first fibonacci number that has k digits
    int i =0;
    while (true) {
        string str = to_string(fibonacci(i));
     
        if (str.size() == k){
            return str;
        }else{
            i++;
        }
    }
}


int main() {
    cout << "First 4 digit Fibonacci number is : " << k_digit_fibonacci(4) << endl;
    return 0;
}
