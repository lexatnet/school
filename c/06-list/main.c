#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define MAXINPUT 100

typedef struct node {
    int val;
    struct node * next;
} node_t;

int is_number(char* str) {
    int result = 1;
    int length;
    length = strlen(str);
    for (int i = 0; i < length; i++)
        if (!isdigit(str[i])) {
            result = 0;
            break;
        }
    return result;
}

int print_list(node_t * head ) {
    node_t * current = NULL;

    current = head;
    
    while(1) {
        printf("%d\n", current->val);
        if(current->next != NULL) {
        current = current->next;
        } else {
            break;
        }
    }
}

node_t * fill_list() {
    node_t * head = NULL;
    node_t * tmp = NULL;
    node_t * last = NULL;
    int x;
    char input[MAXINPUT] = "";
    
    while(1) {
        printf("enter next numder: ");
        scanf("%s", input);
        if (!is_number(input)) {
            printf("error: not a number!\n");
            break;
        }
        
        x = atoi(input);
        
        if (x <= 0) {
            printf("close input!\n");
            break;
        }
            
        tmp = malloc(sizeof(node_t));
        if (tmp == NULL) {
            return 1;
        }
        if(head == NULL) {
            head = tmp;
        }
        tmp->val = x;
        tmp->next = NULL;
        if(last != NULL){
            last->next = tmp;
        }
        last = tmp;
    }
    return head;
}

int main() {
    node_t * head = NULL;
    
    head = fill_list();
    
    if(head != NULL) {
        printf("list contains:\n");
        print_list(head);
    }
    
    return 0;
}
