#include <stdio.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

double compute(char symbol, double op1, double op2) {
    switch(symbol) {
        case '+': return op1 + op2;
        case '-': return op1 - op2;
        case '*': return op1 * op2;
        case '/': 
            if (op2 == 0) {
                fprintf(stderr, "Error: Division by zero\n");
                exit(EXIT_FAILURE);
            }
            return op1 / op2;
        case '^': 
        case '$': return pow(op1, op2);
        default:
            fprintf(stderr, "Error: Invalid operator '%c'\n", symbol);
            exit(EXIT_FAILURE);
    }
}

int main(void) {
    double s[20];
    int top = -1;
    char postfix[100];  // bigger buffer
    char symbol;
    double op1, op2, res;

    printf("Enter the postfix expression: ");
    if (scanf("%99s", postfix) != 1) {
        fprintf(stderr, "Error reading input\n");
        return EXIT_FAILURE;
    }

    for (int i = 0; i < strlen(postfix); i++) {
        symbol = postfix[i];
        if (isdigit(symbol)) {
            s[++top] = symbol - '0';  // still single-digit
        } else {
            if (top < 1) {
                fprintf(stderr, "Error: Not enough operands\n");
                return EXIT_FAILURE;
            }
            op2 = s[top--];
            op1 = s[top--];
            res = compute(symbol, op1, op2);
            s[++top] = res;
        }
    }

    if (top != 0) {
        fprintf(stderr, "Error: Invalid postfix expression\n");
        return EXIT_FAILURE;
    }

    printf("The result is %.2f\n", s[top]);
    return 0;
}