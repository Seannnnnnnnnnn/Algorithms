//  ProjectEuler - Problem 7:
//  What is the 10001st prime number?

#include <iostream>
using namespace std;

bool is_prime(int n){
    // primality testing algorithm found at: https://en.wikipedia.org/wiki/Primality_test
    if (n==1 or n==2 or n==3){
        return true;
    }
    
    if (n%2 == 0 or n%3 == 0) {
        return false;
    }
    
    int i = 5;
    while (i*i <= n) {
        if (n%i == 0 or n%(i+2)==0) {
            return false;
        }
        i += 6;
    }
    
    return true;
}


int find_kth_prime(int k){
    // we do one better - finds the 'k'th prime number
    int count = 0, j = 1;
    while (count <= k) {
        if (is_prime(j) == true) {
            count ++;
        }
        
        j ++; // we iterate by 2 - no point to check the primality of even integers
    }
    
    return j-1;
}

int main() {
    cout << find_kth_prime(10001) << "\n";
    return 0;
}
