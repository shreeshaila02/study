#include <stdio.h>
#include <stdlib.h>
#define SIZE 4

int top = -1, s[SIZE];

void push() {
    int ele;
    if (top == SIZE - 1) {
        printf("Stack overflow\n");
        return;
    }
    printf("Enter the element to insert: ");
    scanf("%d", &ele);
    s[++top] = ele;
}

void pop() {
    if (top == -1) {
        printf("Stack underflow\n");
        return;
    }
    printf("Popped element is: %d\n", s[top]);
    top--;
}

void display() {
    if (top == -1) {
        printf("Stack is empty\n");
        return;
    }
    printf("Stack elements:\n");
    for (int i = top; i >= 0; i--) {
        printf("%d\n", s[i]);
    }
}

int main() {
    int ch;
    while (1) {
        printf("\n1. Push\n2. Pop\n3. Display\n4. Exit\n");
        scanf("%d", &ch);
        switch (ch) {
            case 1: push(); break;
            case 2: pop(); break;
            case 3: display(); break;
            case 4: exit(0);
            default: printf("Invalid choice\n");
        }
    }
    return 0;
}