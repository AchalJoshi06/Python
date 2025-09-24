#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
    struct Node *prev;
};

// Function to traverse the doubly linked list
void linkedListTraversal(struct Node *head) {
    struct Node *ptr = head;
    while (ptr != NULL) {
        printf("Element is %d\n", ptr->data);
        ptr = ptr->next;
    }
}

// Function to insert a new node at the beginning of the doubly linked list
struct Node *insertAtFirst(struct Node *head, int data) {
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    ptr->data = data;
    ptr->next = head;
    ptr->prev = NULL;

    if (head != NULL) {
        head->prev = ptr;
    }

    head = ptr;
    return head;
}

// Function to insert a new node at the end of the doubly linked list
struct Node *insertAtLast(struct Node *head, int data) {
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    ptr->data = data;
    ptr->next = NULL;

    if (head == NULL) {
        ptr->prev = NULL;
        return ptr;
    }

    struct Node *temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    
    temp->next = ptr;
    ptr->prev = temp;

    return head;
}

// Function to insert a new node at a specific position in the doubly linked list
struct Node *insertInBetween(struct Node *head, int data, int position) {
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    ptr->data = data;

    if (position == 1) {
        return insertAtFirst(head, data);
    }

    struct Node *temp = head;
    for (int i = 1; i < position - 1; i++) {
        if (temp == NULL) {
            printf("Position out of bounds\n");
            return head;
        }
        temp = temp->next;
    }

    if (temp->next == NULL) {
        return insertAtLast(head, data);
    }

    ptr->next = temp->next;
    ptr->prev = temp;
    temp->next->prev = ptr;
    temp->next = ptr;

    return head;
}

int main() {
    struct Node *head = NULL;

    head = insertAtFirst(head, 10);
    head = insertAtFirst(head, 20);
    head = insertAtLast(head, 30);
    head = insertInBetween(head, 25, 3);  // Insert 25 at position 3

    printf("Doubly Linked List after various insertions:\n");
    linkedListTraversal(head);

    return 0;
}
