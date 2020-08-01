#include <iostream>


void swap_pos(int* i, int* j){
	// Auxiliary function that swaps indicies i and j in array. We use pointers as these are array elements
	int tmp = *i;
	*i = *j;
	*j = tmp;
}


int partition(int array[], int lo, int hi){
	// Partition subroutine used for quicksort algorithm. Uses high as pivot element
	// Time Complexity: O(n)
	int pivot = array[hi];
	int i = lo-1;
	for (int j=lo; j<=hi; j++){
		if (array[j] < pivot){
			i++;
			swap_pos(&array[i], &array[j]);
		}
	}
	swap_pos(&array[i+1], &array[hi]);
	return i+1;
}


void quick_sort(int array[], int lo, int hi){
	// Performs quick sort algorithm
	// Time Complexity:  O(nlogn)
	// Space Complexity: O(logn)
	if (lo<hi){
		int p = partition(array, lo, hi);
		quick_sort(array, lo, p-1);
		quick_sort(array, p+1, hi);
	}
}


int main() {
    int foo [] = {43, 5, -23, 66, 80, -12, 4, 5, 6, 100, 12};
	int n = sizeof(foo)/sizeof(foo[0]);
	quick_sort(foo, 0, n);
	
	for (int i =0; i<=n; i++){
		std::cout<<foo[i]<<'\t';
	}
	std::cout<<'\n';
	return 0;
}
