#include<bits/stdc++.h>

//global structure

struct node {

    int data;
    struct node *next;
};
int main()
{
    struct node *head, *middle, *last;

   // head   =  malloc(sizeof(struct node));
  //  middle =  malloc(sizeof(struct node));
   // last   =  malloc(sizeof(struct node));

    head->data   = 10;
    middle->data = 20;
    last->data   = 30;

    head->next   = middle;
    middle->next = last;
    last->next   = NULL;

    struct node *temp = head;
    while(temp->next != NULL) {
        printf("%d\n", temp->data);
        temp = temp->next;

    }


    printf("%d", sizeof(struct node));


    return 0;
}
