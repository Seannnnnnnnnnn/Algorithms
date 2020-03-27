//
//  Notes:
//  C++ is gay
//  array syntax: dtype _name_ [] = {x_1, x_2, ..., x_n}

#include <iostream>
using namespace std;


string reverse_string(string s){
    int n = s.length();
    for(int i=0; i<n/2; i++){
        swap(s[i], s[n-i-1]);
    }
    return s;
}


bool is_palindrome(string s){
    
    return s == reverse_string(s);
}


int largest_palindrome(){
    int largest, int1, int2, = 0, 0, 0;
    
    
    for(int i=101; i<1000; i++){
        for(int j=101; j<1000; j++){
            
            int p = i*j;
            
            // Convert p to a string to check if it is a palindrome
            string str = to_string(p);
            
            if (is_palindrome(str) && p>largest) {
                largest = p;
                int1 = i;
                int2 = j;
            }
            
        }
    }
    
    return largest;
}


int main()
{
    
    cout << "Largest palindrome that is product of 3 digit integers: " << largest_palindrome() << endl;
    

    return 0;
}
