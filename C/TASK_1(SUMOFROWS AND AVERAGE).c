#include <stdlib.h>
#include <stdio.h>

int main()
{
int rows=0,columns=0,counter=0,counter_2=0,counter_3=0,sum=0;
float average=0;
while(rows<=0 || columns<=0)
{
printf("please enter number of rows : ");
scanf("%d",&rows);
printf("please enter number of columns : ");
scanf("%d",&columns);
}

int *p=malloc(rows*columns*sizeof(int));
int *x=malloc(rows*sizeof(int));

for(counter;counter<rows;++counter)
{
for(counter_2=0;counter_2<columns;counter_2++)
{
if(counter_2==0)
{
*(x+counter)=0;
}
printf("\nElement[%d][%d] = ",counter,counter_2);
scanf("%d",p+counter_3);
///printf("*(p+counter_3)=%d\n",*(p+counter_3));
*(x+counter)+=*(p+counter_3);
///printf("*(x+counter)=%d\n",*(x+counter));
sum+=*(p+counter_3);
counter_3++;
}
}
printf("\n");
for(int i=0;i<rows;++i)
{
    printf("Sum of elements of row No.%d is %d\n",i,*(x+i));
}
printf("Average of all elements = %.2f",sum/(rows*columns*1.0));



}
