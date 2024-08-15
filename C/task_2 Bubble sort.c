#include <stdio.h>
#include <stdlib.h>

void Sort (int *a, int n);

int main()
{
int size=0, counter;
while(size<=0)
{
printf("Size of the array :");
scanf("%d",&size);
}
int *p=malloc(sizeof(int)*size);
printf("Please enter the array:\n");
for(counter=0;counter<size;++counter)
{
scanf("%d",(p+counter));
}
printf("Unsorted Array\n");
for(counter=0;counter<size;++counter)
{
printf("%d ",*(p+counter));
}

Sort (p,size);
printf("\nSorted Array\n");
for(counter=0;counter<size;++counter)
{
printf("%d ",*(p+counter));
}

}
void Sort (int *a, int n)
{
int counter=0,counter_2=0,temp;

for(counter;counter<n-1;++counter)
{
for(counter_2=0;counter_2<n-counter-1;++counter_2)
{
if(*(a+counter_2+1)>*(a+counter_2))
{
temp=*(a+counter_2);
*(a+counter_2)=*(a+counter_2+1);
*(a+counter_2+1)=temp;
}
}
}
}
