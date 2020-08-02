/*
   Contains Code for Coin Change problem 
*/
#include <iostream>
#include <vector>


void coin_change(int coins[], int target, int n){
	// performs the coin change problem bottom-up: returns min number of coins to make target
	// coins: denominations in array
	// target: value to reach
	// n: size of coins array
	
	std::vector<int> min_coins;
	for (int i=0; i<=target; i++){
		min_coins.push_back(1000);
	}
	min_coins[0]=0;

	for (int v=1; v<=target; v++) {
		for (int i=0; i<n; i++){
			if (coins[i]<=v) {
				min_coins[v] = std::min(min_coins[v], 1+min_coins[v-coins[i]]);
			}
		}
	}
	std::cout<<"Mininimum no. of Coins for "<< target<<": "<<min_coins[target]<<"\nDenominations:\t";
	
	// backtrack to retrieve solution
	while (target>0) {
		for (int i=0; i<n; i++) {
			if (coins[i]<=target && min_coins[target] == 1+min_coins[target-coins[i]]){
				std::cout<<coins[i]<<'\t';
				target -= coins[i];
			}
		}
	}
	std::cout<<'\n';
}


int main() {
	int coins [] = {1, 5, 6, 9};
	coin_change(coins, 13, 4);
}
