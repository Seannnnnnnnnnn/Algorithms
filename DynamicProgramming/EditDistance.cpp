#include <iostream>
#include <vector>

void edit_distance(std::string s1, std::string s2, int n, int m){
	// Computes the edit distance between s1 and s2
	// Time complexity: O(nm)
	// Space complexity: O(nm)
	
	// Define and instanciate the Dist table
	std::vector<std::vector<int>> Dist(n, std::vector<int>(m, 0));
	for (int i=0; i<n; i++){
		Dist[i][0] = i;
	}
	for (int i=0; i<m; i++){
		Dist[0][i] = i;
	}
	
	// Edit Distance Algorithm:
	for (int i=1; i<n; i++){
		for (int j=1; j<m; j++){
			if (s1[i]==s2[j]) {
				Dist[i][j] = Dist[i-1][j-1];
			}
			else{
				Dist[i][j] = std::min(std::min(Dist[i-1][j-1], Dist[i-1][j]), Dist[i][j-1])+1;
			}
		}
	}
	std::cout<<"Edit Distance: "<<Dist[n-1][m-1]<<'\n';
}


int main(){
	std::string s1 = "computer";
	std::string s2 = "commuter";
	edit_distance(s1, s2, 8, 8);
}
