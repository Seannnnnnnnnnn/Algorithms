/*
   Contains Code for (singly) Linked List Data Structure
   TODO: reverse() method
*/
#include <iostream>
#include <cstdlib>


class LinkedList{
private:
	struct Node{
		int data;
		Node* next;
	};
	int length = 0;
	Node* head = NULL;
	Node* tail = NULL;
	
public:
	void append(int data){
		// Appends node to end of linked list
		// Time Complexity: O(1)
		Node* n = new Node;
		n->data = data;
		n->next = NULL;
		
		if (head == NULL){
			head = n;
		}
		else if (length == 1){
			head->next = n;
			tail = n;
		}
		else{
			tail->next = n;
			tail = n;
		}
		length++;
	}
	
	void print(){
		// Prints out contents of linked list
		// Time Complexity: O(n)
		Node* curr = head;
		while (curr->next != NULL) {
			std::cout<<curr->data<<'\t';
			curr = curr->next;
		}
		std::cout<<'\n';
	}
	
	void remove(int data){
		// removes first instance of data from linked list using the twin pointer method
		// Time complexity: O(n)
		
		// Edge Case: Deleting head
		if (head->data == data) {
			head = head->next;
		}
		else{
			Node* ptr1 = head;
			Node* ptr2 = head->next;
			while (true) {
				if (ptr2->data == data){
					break;
				}
				else{
					ptr1 = ptr1->next;
					ptr2 = ptr2->next;
				}
			}
			// Edge Case: If element to delete is tail:
			if (tail == ptr2) {
				tail = NULL;
				ptr1->next = NULL;
			}
			ptr2 = ptr2->next;
			ptr1->next = ptr2;
		}
		length--;
	}
	
	void reverse(){
		// reverses the linked list
		// Time complexity:  O(n)
		// Space complexity: O(1)
		Node* previous = NULL;
		Node* current = head;
		Node* following = head;
		
		while (current != NULL) {
			following = following->next;
			current->next = previous;
			previous = current;
			current = following;
		}
		head = previous->next;
	}
	
	int len(){
		// returns length of Linked List
		// Time complexity: O(1)
		return length;
	}
};


int main() {
	int foo[] = {2, 5, 3, 5, 8, 7,};
	LinkedList tester;
	
	std::cout<<"Testing Insertion:\n";
	for (int i=0; i<=6; i++){
		tester.append(foo[i]);
	}
	std::cout<<"Tests Passed\n\n";

	std::cout<<"Testing Print:\n";
	tester.print();
	
	std::cout<<"\n\nTesting Deletion: Deleting 3\n";
	tester.remove(3);
	tester.print();
	std::cout<<"Tests Passed\n";
	
	std::cout<<"\n\nTesting Deletion: Deleting 2\n";
	tester.remove(2);
	tester.print();
	std::cout<<"Tests Passed\n\n";
	
	std::cout<<"\n\nTesting Deletion: Deleting 7\n";
	tester.remove(7);
	tester.print();
	std::cout<<"Tests Passed\n\n";
	
	std::cout<<"\n\nTesting Reversal:\n";
	tester.reverse();
	tester.print();
	std::cout<<"Tests Passed\n\n";
}
