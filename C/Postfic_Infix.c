
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

typedef struct node
{
    struct node *next;
    double data;
} node ;
typedef struct
{
    node * top;
} stack;

/**------(* ^ *)----------Stack main operations------(* ^ *)----------**/
/*node * newItem(double value);
stack * newStack();
void push(stack *mainStack,float value);
stack * pop(stack *mainStack);
float peek(stack *mainStack);
int isEmpty(stack * mainStack);
void display (stack *mainStack);*/

node * newItem(float value);
stack * initialize();
void push(stack *mainStack,float value);
float pop(stack *mainStack);
float peek(stack *mainStack);
int isEmpty(stack * mainStack);
void display (stack *mainStack);

node * newItem(float value)
{
    node *neww = (node*)malloc(sizeof(node));
    neww->next =  NULL;
    neww->data = value;
    return neww;
}
stack * initialize()
{
    stack* neww = (stack*)malloc(sizeof(stack));

    neww->top = NULL;

    return neww;
}
void push(stack *mainStack,float value)
{
    node * n = newItem(value);
    n->next = mainStack->top;
    mainStack->top = n;
}
float pop(stack *mainStack)
{
    /*if(isEmpty(mainStack))
        return mainStack;
    else
    {*/
    node * temp = mainStack->top;
    float data=temp->data;
    mainStack->top = temp->next;
    free(temp);
    return data;
    // }
}
float peek(stack *mainStack)
{
    if(!isEmpty(mainStack)) return mainStack->top->data;
    // else printf("%s","Stack is Empty\n");

}
int isEmpty(stack * mainStack)
{
    return (mainStack->top == NULL)?1:0;
}
void display (stack *mainStack)
{
    if(isEmpty(mainStack))return;
    node *temp = mainStack->top;
    while(temp!= NULL)
    {
        printf("%f ",temp->data);
        temp = temp->next;
    }
    printf("\n");

}
/**------(* ^ *)---------- Expression Evaluation ------(* ^ *)----------**/
char * tok(char * expression);
char* infixTopostfix(char *infix);
int precedence(char operatorr);
float evaluatePostfix(char * postfix);
char * tok(char * expression)
{
    char updated[1024]= {};
    char n[4]="   ";
    int i=0,j=0;
    while(expression[i]!= '\0')
    {
        if((expression[i] == '-' || expression[i] == '+') && ((i==0) || (!isdigit(expression[i-1])&&isdigit(expression[i+1])&&expression[i-1]!=')')))
        {
            {
                n[0]=expression[i];
                n[1]=expression[i+1];
                n[2] = '\0';
                strcat(updated,n);
                i+=2;
                j+=2;
            }

        }
        else if(isdigit(expression[i]))
        {
            updated[j++] = expression[i++];
        }
        else if ((expression[i]>='(' && expression[i]<='/')||(expression[i] == '%') || (expression[i] == '^'))
        {
            n[0]=' ',n[1]=expression[i];
            n[2] = ' ' ;
            strcat(updated,n);
            j+=3;
            i++;
        }
        else if(expression[i] == ' ')
        {
            printf("gggg-----");
            i++;
        }
    }
    char * new_expression = malloc((strlen(updated)+1)*sizeof(char));
    strcpy(new_expression,updated);
    return new_expression;

}
/// precedence of operators
int precedence(char operatorr)
{
    if(operatorr == '^')return 5;
    else if(operatorr == '*' || operatorr == '/' || operatorr == '%')return 4;
    else if(operatorr == '+'|| operatorr == '-' )return 3;
    else if(operatorr == '(')return 2;


}

char* infixTopostfix(char *infix)
{

    stack *st = initialize();

    ///  temporary string to be concatenated

    char temp[6]="";

    /// postfix string
    char post[1024]= {};
    /// tokenizer
    char *token;
    char temm;
    token = strtok(infix," ");
    while(token!= NULL)
    {

        /// if the portion is a positive  or a negative number
        if(isdigit(token[0]) || ((token[0] == '+' || token[0] == '-' )&&(isdigit(token[1]))))
        {

            strcat(post,token);
            strcat(post," ");


        }
        else if((token[0]>='(' && token[0] <= '/') || token[0] == '^')
        {

            /// pop the operators until a ')' is found
            if(token[0] == ')')
            {



                while(((char)peek(st))!= '(')
                {
                    temp[0] = (char)(peek(st));
                    pop(st);
                    strcat(post,temp);
                    strcat(post," ");

                }
                pop(st);
            }

            else
            {


                if(isEmpty(st))
                {
                    push(st,token[0]);
                }
                else if(precedence((char)peek(st))>= precedence(token[0]))
                {
                    if(token[0] == '(')
                        push(st,token[0]);
                    else
                    {


                        temp[0] = (char)(peek(st));
                        pop(st);
                        strcat(post,temp);
                        strcat(post," ");
                        ///
                        if(precedence((char)peek(st)) == precedence(token[0]))
                        {
                            temp[0] = (char)(peek(st));
                            pop(st);
                            strcat(post,temp);
                            strcat(post," ");
                        }
                        push(st,token[0]);

                    }

                }

                else if (precedence((char)peek(st))<precedence(token[0]) )
                {
                    push(st,token[0]);
                }
            }

        }

        token = strtok(NULL," ");

    }





    /// pop the remaining operators
    while(!isEmpty(st))
    {

        temp[0] = (char)(peek(st));
        pop(st);
        strcat(post,temp);
        strcat(post," ");
    }


    char * postfix = (char*) malloc(sizeof(char)*(strlen(post)+1));
    strcpy(postfix,post);
   // printf("%d\n",strlen(postfix));
    post[23] = '\0';
    /*int i = 0;
    / while(post[i++] != '\0')
        printf(" %d.hi\n",i);*/
    return postfix;
}
/**--evaluation the postfix expression function--**/
float evaluatePostfix(char * postfix)
{
    stack * s = initialize();

    int i = 0;
    while(postfix[i]!='\0')
    {


        if(isdigit(postfix[i])||(postfix[i]=='-'&&isdigit(postfix[i+1]))||postfix[i]=='.')
        {

            float op1 = 0;
            int sign = 1;
            int decimal = 0;
        // checking negative sign
            if (postfix[i]=='-')
            {
                sign= (-1);
                i++;
            }
            while(isdigit(postfix[i])||postfix[i]=='.')
            {  // checking for a decimal point
                if (postfix[i]=='.')
                {
                    decimal = 1;
                    i++;
                    continue;
                }
                if(decimal)
                {
                    op1 = op1+(postfix[i]-'0')/pow(10,decimal);
                    decimal++;
                    i++;
                }
                else
                {
                    op1 = op1*10+(postfix[i]-'0');
                    /**/          i++;
                }
// i++;
            }

            push(s,sign*op1);
        }
        else if(postfix[i]==' ')
        {
            i++;
        }
        else
        {
            float operand2=pop(s);
            float operand1=pop(s);
            switch(postfix[i])
            {
            case '+':
                push(s,operand1+operand2);
                break;
            case '-':
                push(s,operand1-operand2);
                break;
            case '*':
                push(s,operand1*operand2);
                break;
            case '/':
                push(s,operand1/operand2);
                break;
            case '^':
                push(s,pow(operand1,operand2));
                break;
            default:
                printf(" Invalid operater : %c\n",postfix[i]);

            }
            i++;
        }

    }
    float result = pop(s);

    return result;
    free(s);

}

int main()
{

    stack * st = initialize();

    char *expression/*"2 + ( -2.5 + 3.14 ) * ( -5.4 + 8.1 ) ^ ( -0.5 )"*/;
    printf("Infix : ");
    fgets(expression,100,stdin);
    char *nill;
    char *d = infixTopostfix(expression);
    printf("Postfix : %s\n",d);
    float y=evaluatePostfix(d);
    printf("value : %f\n",y);

    return 0;
}

