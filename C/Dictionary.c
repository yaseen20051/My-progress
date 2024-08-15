#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    char * word;
    struct node * right;
    struct node * left;

} node;


/**  Tree  functions **/
node * new_leaf(char* new_word);
node * search_parent(node *head, char*word);
node *getMaxx(node *root);
node *getMin(node *root);
node * successor(node*head,char *word);
node * predccesor(node*head,char *word);
void * search_iter(node *head, char*word);
node * insert (node * head,char * new_word);
node * load_dictonary(node * root,FILE * file2);
void inorderTraverse(node * n);
void breadthFirstTraversal(node* root);
int countNodes(node *head);
int max(int a, int b);
int treeHeight(node* head);


/***   main ***/

int main()
{
    FILE*file2=fopen("Dictionary.txt","r");

    if(file2==NULL)printf("the file is empty.\n");

    node * root = load_dictonary(root,file2);

    fclose(file2);
    printf("Size = %d\n --------------------------------\n",countNodes(root));

    printf("Height = %d\n --------------------------------\n",treeHeight(root));
    char sentence[1000];
    printf("Enter a sentence : \n");
    fgets(sentence,sizeof(sentence),stdin);
    char *token=strtok(sentence," ");
    while(token!=NULL)
    {
        token[strcspn(token,"\n")]=0;
        search_iter(root,token);
        token=strtok(NULL," ");
    }

}

/**     functions    **/

int countNodes(node *head)
{
    if(head==NULL)return 0;
    return 1+countNodes(head->left)+countNodes(head->right);
}
int max(int a, int b)
{
    return a>b?a:b;
}
int treeHeight(node* head)
{
    if(head==NULL)
        return -1;

    return 1+max(treeHeight(head->left),treeHeight(head->right));
}


void breadthFirstTraversal(node* root)
{
    if (root == NULL)
    {
        return;
    }

    node* queue[100];
    int front = 0, rear = 0;

    queue[rear++] = root;

    while (front < rear)
    {
        node* current = queue[front++];
        printf("%s ", current->word);

        if (current->left!= NULL)
        {
            queue[rear++] = current->left;
        }

        if (current->right!= NULL)
        {
            queue[rear++] = current->right;
        }
    }
    printf("\n");
}
node * new_leaf(char* new_word)
{

    node* newNode = (node*)malloc(sizeof(node));
    newNode->word = (char*)malloc(sizeof(char)*(strlen(new_word)+1));
    strcpy(newNode->word,new_word);
    newNode->left = newNode->right = NULL;

    return newNode;
}
node * insert (node * head,char * new_word)
{

    if(head == NULL)

    {
        return new_leaf(new_word);
    }

    if (strcasecmp(head->word,new_word) < 0 )
    {

        head->right = insert(head->right,new_word);

    }
    else if (strcasecmp(head->word,new_word) > 0)
    {

        head->left = insert(head->left,new_word);

    }


    return head;

}

void inorderTraverse(node * n)
{
    if(n == NULL);
    else
    {
        printf("%s\n",n->word);
        inorderTraverse(n->left);
        inorderTraverse(n->right);
    }
}

void * search_iter(node *head, char*word)
{
    node *root = head;



    while(root != NULL && strcasecmp(word,root->word)!=0)
    {



        if (strcasecmp(root->word,word) >0 )
        {
            root = root->left;
        }
        else if (strcasecmp(root->word,word) < 0)
        {
            root = root->right;
        }


    }
    if(root!= NULL) printf("%s %s",root->word," - correct!!\n");
    else if (root == NULL)
    {

        node * parent = search_parent(head,word);
        node * ancestor = successor(head,parent->word);
        node * second_ancestor= predccesor(head,parent->word);


        // if(ancestor == NULL)

        if (parent == NULL)
            printf("%s %s",word," - Incorrect!!, No suggestions");
        else
        {
            if(ancestor == NULL && second_ancestor == NULL)
            {
                printf("%s %s",word," - Incorrect!!, suggestions : ");
                printf("%s \n",parent->word);
            }
            else if(ancestor == NULL )
            {

                printf("%s %s",word," - Incorrect!!, suggestions : ");
                printf("%s %s \n",parent->word,second_ancestor->word);
            }
            else if(second_ancestor == NULL )
            {

                printf("%s %s",word," - Incorrect!!, suggestions : ");
                printf("%s %s \n",parent->word,ancestor->word);
            }
            else
            {
                printf("%s %s",word," - Incorrect!!, suggestions : ");
                printf("%s %s %s \n",parent->word,ancestor->word,second_ancestor->word);
            }



        }



    }
}
node * search_parent(node *head, char*word)
{

    node *root = head;
    if(root == NULL) return NULL;
    node*parent = NULL;


    while(root != NULL && strcasecmp(word,root->word)!=0)
    {



        if (strcasecmp(root->word,word) > 0)
        {
            parent = root;
            root = root->left;
        }
        else if (strcmp(root->word,word) < 0)
        {
            parent = root;
            root = root->right;
        }


    }

    return parent;
}

node * load_dictonary(node * root,FILE * file2)
{

    char buf[100];
    fgets (buf, 100, file2);
    node *n = new_leaf(buf);

    while( fscanf(file2,"%s",buf) == 1 )
    {

        insert(n,buf);

    }
    printf("Dictionary Loaded Successfully !\n --------------------------------\n");

    return n;

}
node *getMin(node *root)
{
    if(root == NULL) return root;
    else if(root->left == NULL) return root;
    else  return getMin(root->left);
}
node *getMaxx(node *root)
{
    if(root == NULL) return root;
    else if(root->right == NULL) return root;
    else  return getMaxx(root->right);
}

node * successor (node*head,char *word)
{
    node *root = head;



    node*success = NULL;
    while (root != NULL && strcasecmp(word,root->word)!=0)
    {

        if (strcasecmp(word,root->word) > 0 )
        {
            root = root->right;
        }
        else if (strcasecmp(word,root->word) < 0)
        {

            success = root;
            root = root->left;
        }

    }
    if (root!= NULL && root->right!= NULL)
    {
        success = getMin (root->right);
    }

    return success;





}

node * predccesor(node*head,char *word)
{
    node *root = head;

    node*predecess = NULL;
    while(root != NULL && strcasecmp(word,root->word)!=0)
    {

        if(strcasecmp(word,root->word) > 0)
        {
            predecess = root;
            root = root->right;
        }
        else if (strcasecmp(word,root->word) < 0 )
        {

            root = root->left;
        }

    }
    if(root!= NULL && root->left!= NULL)
    {
        predecess = getMaxx(root->left);
    }

    return predecess;





}

