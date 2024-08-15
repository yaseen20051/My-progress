#include<stdio.h>
#include<stdio.h>

int main()
{

int size=0,counter=0,temp;
while(size<=0)
{
printf("size:");
scanf("%d",&size);
}
int *p=malloc(sizeof(int)*size);
printf("Please enter the element of the array :\n");
for(counter=0;counter<size;counter++)
{
scanf("%d",(p+counter));
}
printf("\nArray before reversing \n");
for(counter=0;counter<size;counter++)
{
printf("%d ",*(p+counter));
}
for(counter=0;counter<size/2;++counter)
{
temp=*(p+counter);

*(p+counter)=*(p+size-counter-1);
*(p+size-counter-1)=temp;

}
printf("\nArray after reversing \n");
for(counter=0;counter<size;counter++)
{
printf("%d ",*(p+counter));
}
}
