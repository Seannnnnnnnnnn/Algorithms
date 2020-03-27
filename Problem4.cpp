// Project Euler Question #4: 

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
    int largest = 0;
    
    
    for(int i=101; i<1000; i++){
        for(int j=101; j<1000; j++){
            
            int p = i*j;
            
            // Convert p to a string to check if it is a palindrome
            string str = to_string(p);
            
            if (is_palindrome(str) && p>largest) {
                largest = p;
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
