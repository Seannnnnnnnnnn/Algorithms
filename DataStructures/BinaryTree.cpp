/*
   Contains Code for Binary Search Tree Data Structure
*/
#include <iostream>
#include <cstdlib>


class BinarySearchTree{
private:
	struct Node{
		int data;
		Node* right;
		Node* left;
		Node* parent;
	};
	int size = 0;
	Node* root = NULL;
	
public:
	void insert(int data){
		// Inserts node into Binary Tree as per Corman Et All (Page 294)
		// Time complexity: Average Case: O(log(n))    Worst Case: O(n)
		Node* n = new Node;
		n->data = data;
		n->left = NULL;
		n->right = NULL;
		n->parent = NULL;
		
		Node* curr = root;
		Node* prev = NULL;
		while (curr != NULL) {
			prev = curr;
			if (data < curr->data){
				curr = curr->left;
			}
			else{
				curr = curr->right;
			}
		}
		n->parent = prev;
		if (prev == NULL){
			root = n;
		}
		else if (data < prev->data){
			prev->left = n;
		}
		else{
			prev->right = n;
		}
		size++;
	}
	
	Node* search(int data, Node* curr){
		// Peforms binary search on the tree for data
		// Time complexity: Average Case: O(log(n))    Worst Case: O(n)
		if (curr == NULL or data == curr->data) {
			return curr;
		}
		else if (data < curr->data){
			return search(data, curr->left);
		}
		else{
			return search(data, curr->right);
		}
	}

	int get_min(){
		// Returns the minimum element in the tree
		// Time complexity: Average Case: O(log(n))    Worst Case: O(n)
		Node* curr = root;
		while (curr->left != NULL) {
			curr = curr->left;
		}
		return curr->data;
	}
	
	int get_max(){
		// Returns the minimum element in the tree
		// Time complexity: Average Case: O(log(n))    Worst Case: O(n)
		Node* curr = root;
		while (curr->right != NULL) {
			curr = curr->right;
		}
		return curr->data;
	}
	
	int get_size(){
		// Returns size of the binary tree
		// Time complexity: O(1)
		return size;
	}
};


int main() {
	int foo[] = {2, 5, 3, -5, 8, 7, -1};
	BinarySearchTree Tester;
	
	std::cout<<"Testing Insertion\n";
	for (int i=0; i<=7; i++){
		Tester.insert(foo[i]);
	}
	std::cout<<"\nTests Passed\n";
	
	std::cout<<"\nGet Minimimum:\n";
	std::cout<<Tester.get_min();
	std::cout<<"\nTests Passed\n";
	
	std::cout<<"\nGet Maximum:\n";
	std::cout<<Tester.get_max();
	std::cout<<"\nTests Passed\n";
	
	std::cout<<"\nTesting Search & :\n";
	std::cout<<Tester.get_max();
	std::cout<<"\nTests Passed\n";
}
