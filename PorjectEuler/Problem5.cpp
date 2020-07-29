//  ProjectEuler
//

#include <iostream>
using namespace std;

bool perfect_divisable(int n){
    // returns true; iff n is prefectly divisible from 1-20
    for(int j=1; j<=20; j++)
        if (n%j > 0) {
            return false;
        }
    return true;
}

void smallest_multiple(){
    /*
     2520 is the smallest number that can be divided by each of the numbers from 1 to
     without any remainder.

     What is the smallest positive number that is evenly divisible by all of the numbers
     from 1 to 20?
     */
    
    int i = 100;
    bool flag = false;
    
    while (flag == false) {
        if (perfect_divisable(i) == true) {
            break;
        }
        i ++;
    }
    
    cout << "Smallest integer perfectly divisible by all integers over the range [1, 20] is : " << i << endl;
    
}


int main() {
    smallest_multiple();
    return 0;
}
